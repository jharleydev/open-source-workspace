# Open Source Workspace
[![Kubesec](https://github.com/jharleydev/open-source-workspace/actions/workflows/kubesec-analysis.yml/badge.svg)](https://github.com/jharleydev/open-source-workspace/actions/workflows/kubesec-analysis.yml)

[![CodeQL](https://github.com/jharleydev/open-source-workspace/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/jharleydev/open-source-workspace/actions/workflows/codeql-analysis.yml)## Deploy Secure Hybrid Network to Azure 

[![Secure Hybrid Network](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fmspnp%2Fsamples%2Fmaster%2Fsolutions%2Fsecure-hybrid-network%2Fazuredeploy.json)

## Deploy with Pulumi 
[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new)


The default is to use the cloud hosted platforms as is but you can choose to install the software on your own servers if there are specifc compliance requirements for your project.  

[`Azure-CLI`](https://docs.microsoft.com/en-us/cli/azure/) 
 Available from the command line. The CLI is for working with azure cloud. 

[`Pulumi`](https://www.pulumi.com/)
Available from the command line. This is a infrastructure as code platform that leverages general purpose programing lanaguages like C#, TypeScript, Python, & Go preinstalled. For this project we have chosen to support python primarily. Typescript is also available because Pulumi and has alot of samples.  

[`GitHub Actions`](https://docs.github.com/en/actions)
Helps you deploy apps and infrastructure to your cloud of choice, using nothing but code in your favorite language and GitHub.

[`GitPod`](https://www.gitpod.io/)
Spin up fresh, automated dev environments in the cloud, in seconds. [Enable Gitpod.](https://www.gitpod.io/docs/getting-started)

[`Kubernetes`](https://kubernetes.io/)
Available from the cmd line. Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications.

[`Java`](https://www.microsoft.com/openjdk)
Openjdk 11.0.13. 

[`Jupyter`](https://jupyter.org/) Popular notebooking tool similar to databricks.

## Connect to your data - Available Integration Sources 

* Azure Services 
* Snowflake 
* Microsoft SQL Server 
* PostgreSQL
* MonogoDB 
* SQLite
* REST 
* GraphQL 

## Build a sharable data web app
* Streamlit 
* Appsmith
* Juypter 
* Tableau

## Orchestration 
* Prefect

## Security 
* Validation 
* Audit Logs 
* Multi-Factor Authentication 

## Start Managed Kubernetes Cluster
* Azure AKS 

## Define a Network Policy 
* Pulumi
* Terraform
* ARM
* YAML 
* BICEP



## Recommendations 

This repo is designed with a microservice approach in regards to Pulumi. Below are the general rules of thumb being followed.
Visit [here](https://www.pulumi.com/docs/guides/organizing-projects-stacks/) to learn more about how to orgainze projects and stacks with Pulumi.


* Each micro-service in your architecture  get its own project.
* Application container images may be rebuilt and published independent of infrastructure projects.
* Application concepts like containers and serverless functions may be deployed independently.
* Core, low-level infrastructure – like networks and cluster orchestrators are independent from other infrastructure and applications resources.
* You may have one or more data tiers that are deployed and independently backed up.
* [Prevent your secrets from being leaked](https://blog.gitguardian.com/leaking-secrets-on-github-what-to-do/) 
* Review the [CNCF](https://www.cncf.io/)
* Understand how [Self Hosted Agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/v2-windows?view=azure-devops) work at a high level. 

Please check out the [void](https://www.thevoid.community/) and keep up to date on post mortems, incidents, outages from major companies. These reports are driven by objective metadata from companies. 

## Setup

The github actions preconfigured are triggered with push and pull requests. Both yaml files need the appropriate secrets to actually run. Below is the list of secrets you need to configure or update the yaml files with. Update the authorization flow per your use case. The approach follows what Pulumi reccommends for a [CI/CD workflow with Github Actions](https://www.pulumi.com/docs/guides/continuous-delivery/github-actions/). 


`CONFIFURE_CREDENTIALS_ACTION`
Use the appropriate github actions to login into the cloud provider of your choice. 

`ACCESS_KEY_ID` 
Neccessary for authentication. 

`ACCESS_KEY`
Neccessary for authentication. 

`REGION`
Region where the resources should be created at.  

`PULUMI_STACK_NAME`
The pulumi stack name you want to target. 

`PULUMI_ACCESS_TOKEN`
Access token so Pulumi can set up the projects from Github actions. 

`PULUMI_PERFORM_UPSERT_ON_PULL`
Option to tell Pulumi to create a stack if one does not exists. 

# GitOps Explained by Kelsey Hightower
[Serializing the Practice](https://www.youtube.com/watch?v=yIAa5wHsfw4)

![image](https://user-images.githubusercontent.com/91840749/140296158-4212da27-af6c-448a-a489-b09da8f14fda.png)


# Blog Posts 
[Containerized Applications in Healthcare ?](https://comport.com/resources/data-center/how-do-containerized-applications-fit-in-healthcare/)


# Whitepapers

[Data Driven Healthcare with Snowflake](https://resources.snowflake.com/white-paper/data-driven-healthcare)

[Cloud Transformation Research](https://tdwi.org/Research/List/All-Research.aspx)


# Recent Keynotes 
[Pulumi Opening Key Note](https://www.pulumi.com/resources/kelsey-hightower-joe-duffy-fireside-chat/)

# Podcasts 
[What Github can give to Microsoft with Jason Warner](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/what-github-can-give-to-microsoft-with-jason-warner/)

[Making Multi-Cloud Waves with Betty Junod](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/making-multi-cloud-waves-with-betty-junod/)

# Books 

[Site Reliability Engineering](https://learning.oreilly.com/library/view/site-reliability-engineering/9781491929117/)

[Designing Data Intensive Applications](https://learning.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/) 

[Fundamentals of Software Engineering](https://learning.oreilly.com/library/view/fundamentals-of-software/9781492043447/) 

[Building Microservices](https://learning.oreilly.com/library/view/building-microservices/9781491950340/)




