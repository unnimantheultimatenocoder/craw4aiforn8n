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
  * Render


On this page
# Render
## Deploy on Render[​](https://docs.langflow.org/<#20a959b7047e44e490cc129fd21895c0> "Direct link to Deploy on Render")
[Render.com](https://docs.langflow.org/<http:/render.com/>) is a unified cloud platform designed to make deploying web applications, APIs, and static sites easy. It provides a streamlined experience with powerful features like automatic SSL, managed databases, and auto-deploy from Git, making it a popular choice for developers looking to simplify their deployment workflows.
Deploying Langflow to Render is a straightforward process that can be completed in just a few steps:
  1. **Click the Button Below** : Start by clicking the deployment button provided below. This will redirect you to the Render platform.
[![Deploy to Render](https://docs.langflow.org/deployment-render)](https://docs.langflow.org/<https:/render.com/deploy?repo=https%3A%2F%2Fgithub.com%2Flangflow-ai%2Flangflow%2Ftree%2Fdev>)
  2. **Select the Blueprint Configuration** : Once on the Render platform, you will be prompted to provide a blueprint name and to select the branch for your `render.yaml` file in Langflow. This configuration file includes all the necessary settings and resources to deploy Langflow in Render. The default is `main`.
  3. The `render.yaml` file specifies a `standard` Render instance, because Langflow requires at least 2 GB of RAM to run. This may require a credit card to sign up. Review the pricing details on the Render platform to understand any costs involved before proceeding. If you need to change your plan later, from the Render dashboard, go to **Settings** > **Instance Type**.
  4. Click **Deploy Blueprint** to deploy Langflow. Render will handle the rest, including setting up the database, deploying the Langflow instance, and starting the application.


By following these steps, your Langflow instance will be successfully deployed on Render.
[PreviousRailway](https://docs.langflow.org/</deployment-railway>)[NextAssemblyAI](https://docs.langflow.org/</integrations-assemblyai>)
  * [Deploy on Render](https://docs.langflow.org/<#20a959b7047e44e490cc129fd21895c0>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
