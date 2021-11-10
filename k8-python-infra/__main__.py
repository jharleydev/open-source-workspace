"""A Kubernetes Python Pulumi program 

Based on https://github.com/pulumi/examples/blob/master/azure-py-aks/__main__.py

Set the location with `pulumi config set azure-native:location <value>`

You will need to login into azure using `az login` before running `pulumi preview` or `pulumi up`
"""


import pulumi
from pulumi_azure_native import resources, containerservice
import pulumi_azuread as azuread
import pulumi_random as random
import pulumi_tls as tls
import pulumi_azure_native as azure_native

config = pulumi.Config()

# Create new resource group
resource_group = azure_native.resources.ResourceGroup("k8pydev")

#Create an AD service principal 
ad_app = azuread.Application("aks_dev", display_name="aks_dev")
ad_sp = azuread.ServicePrincipal("aks_dev_sp", application_id=ad_app.application_id)

#Generate random password
password = random.RandomPassword("aks_dev_password", length=20, special=True)

#Create the Service Principal Password 
ad_sp_password = azuread.ServicePrincipalPassword("aks_sp_password", 
                                                  service_principal_id=ad_sp.id, 
                                                  value=password.result, 
                                                  end_date="2099-01-01T00:00:00Z")

# Generater an SSH Key
ssh_key = tls.PrivateKey("ssh-key", algorithm="RSA", rsa_bits=49096)

#Create the cluster
managed_cluster_name = config.get("aks_dev_cluster")
if managed_cluster_name is None: 
    managed_cluster_name = "azure-native-aks"

managed_cluster = containerservice.ManagedCluster(
    managed_cluster_name, 
    resource_group_name=resource_group.name,
    agent_pool_profiles=[{
        "count": 3, 
        "max_pods": 5, 
        "mode": "System", 
        "name": "agentpool", 
        "node_lables": {}, 
        "os_disk_size_gb": 30, 
        "os_type": "Linux", 
        "type": "VirtualMachineScaleSets", 
        "vm_size": "Standard_DS2_v2"
    }], 
    enable_rbac=True, 
    kubernetes_version="1.18.14", 
    linux_profile={
        "admin_username": "admin_user", 
        "ssh": {
            "public_keys": [{
                "key_data": ssh_key.public_key_openssh,
            }],
        },
    },
    dns_prefix=resource_group.name,
    node_resource_group=f"MC_azure_native_{managed_cluster_name}_eastus", 
    service_principal_profile={
        "client_id": ad_app.application_id, 
        "secret": ad_sp_password.value
    })

creds = pulumi.Output.all(resource_group.name, managed_cluster.name).apply(
    lambda args:
    containerservice.list_managed_cluster_user_credentials(
        resource_group_name=args[0],
        resource_name=args[1]))

# Export kubeconfig
encoded = creds.kubeconfigs[0].value
kubeconfig = encoded.apply(
    lambda enc: base64.b64decode(enc).decode())
pulumi.export("kubeconfig", kubeconfig)