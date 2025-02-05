[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/</get-started-installation>)
  * [Starter projects](https://docs.langflow.org/</starter-projects-basic-prompting>)
  * [Tutorials](https://docs.langflow.org/</tutorials-blog-writer>)
  * [Concepts](https://docs.langflow.org/</concepts-overview>)
  * [Components](https://docs.langflow.org/</components-agents>)
  * [Agents](https://docs.langflow.org/</agents-overview>)
  * [Configuration](https://docs.langflow.org/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
    * [Docker](https://docs.langflow.org/</Deployment/deployment-docker>)
    * [GCP](https://docs.langflow.org/</deployment-gcp>)
    * [HuggingFace Spaces](https://docs.langflow.org/</deployment-hugging-face-spaces>)
    * [Kubernetes](https://docs.langflow.org/</deployment-kubernetes>)
    * [Railway](https://docs.langflow.org/</deployment-railway>)
    * [Render](https://docs.langflow.org/</deployment-render>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Deployment
  * GCP


On this page
# Deploy on Google Cloud Platform
To deploy Langflow on Google Cloud Platform using Cloud Shell, use the below script. The script will guide you through setting up a Debian-based VM with the Langflow package, Nginx, and the necessary configurations to run the Langflow dev environment in GCP.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * A GCP account with the necessary permissions to create resources
  * A project on GCP where you want to deploy Langflow


## Deploy Langflow in GCP[​](https://docs.langflow.org/<#deploy-langflow-in-gcp> "Direct link to Deploy Langflow in GCP")
  1. Click below to launch Cloud Shell.


[![GCP Deploy](https://docs.langflow.org/deployment-gcp) Deploy to Google Cloud](https://docs.langflow.org/<https:/console.cloud.google.com/cloudshell/open?git_repo=https://github.com/langflow-ai/langflow&working_dir=scripts/gcp&shellonly=true&tutorial=walkthroughtutorial.md>)
  1. Click **Trust repo**. Some gcloud commands may not run in an ephemeral Cloud Shell environment.
  2. Click **Start** and follow the tutorial to deploy Langflow.


## Spot/Preemptible Instance[​](https://docs.langflow.org/<#spotpreemptible-instance> "Direct link to Spot/Preemptible Instance")
When running a [spot (preemptible) instance](https://docs.langflow.org/<https:/cloud.google.com/compute/docs/instances/preemptible>), the code and VM will behave the same way as in a regular instance, executing the startup script to configure the environment, install necessary dependencies, and run the Langflow application. However, **due to the nature of spot instances, the VM may be terminated at any time if Google Cloud needs to reclaim the resources**. This makes spot instances suitable for fault-tolerant, stateless, or interruptible workloads that can handle unexpected terminations and restarts.
## Pricing[​](https://docs.langflow.org/<#pricing> "Direct link to Pricing")
For more information, see the [GCP pricing calculator](https://docs.langflow.org/<https:/cloud.google.com/products/calculator?hl=en>).
[PreviousDocker](https://docs.langflow.org/</Deployment/deployment-docker>)[NextHuggingFace Spaces](https://docs.langflow.org/</deployment-hugging-face-spaces>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Deploy Langflow in GCP](https://docs.langflow.org/<#deploy-langflow-in-gcp>)
  * [Spot/Preemptible Instance](https://docs.langflow.org/<#spotpreemptible-instance>)
  * [Pricing](https://docs.langflow.org/<#pricing>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
