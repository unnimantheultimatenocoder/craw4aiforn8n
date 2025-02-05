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
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
    * [AssemblyAI](https://docs.langflow.org/</integrations-assemblyai>)
    * [Integrate Composio with Langflow](https://docs.langflow.org/</integrations-composio>)
    * [Langfuse](https://docs.langflow.org/</integrations-langfuse>)
    * [LangSmith](https://docs.langflow.org/</integrations-langsmith>)
    * [LangWatch](https://docs.langflow.org/</integrations-langwatch>)
    * [Google](https://docs.langflow.org/</integrations-setup-google-oauth-langflow>)
    * [Notion](https://docs.langflow.org/</integrations/notion/setup>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Integrations
  * Langfuse


On this page
# Integrate Langfuse with Langflow
[Langfuse](https://docs.langflow.org/<https:/langfuse.com/>) is an observability and analytics platform specifically designed for language models and AI applications.
This guide walks you through how to configure Langflow to collect [tracing](https://docs.langflow.org/<https:/langfuse.com/docs/tracing>) data about your flow executions and automatically send the data to Langfuse.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * A project in Langflow with a runnable flow
  * A Langfuse Cloud account in any [data region](https://docs.langflow.org/<https:/langfuse.com/faq/all/cloud-data-regions>)
  * A Langfuse organization and project


## Create Langfuse project credentials[​](https://docs.langflow.org/<#create-langfuse-project-credentials> "Direct link to Create Langfuse project credentials")
  1. In Langfuse, go to your project settings, and then create a new set of API keys.
  2. Copy the following API key information:
     * Secret Key
     * Public Key
     * Host URL


## Set your Langfuse credentials as environment variables[​](https://docs.langflow.org/<#set-your-langfuse-credentials-as-environment-variables> "Direct link to Set your Langfuse credentials as environment variables")
Set your Langfuse project credentials as environment variables in the same environment where you run Langflow.
You can use any method you prefer to set environment variables. The following examples show how to set environment variables in a terminal session (Linux or macOS) and in a command prompt session (Windows):
  * Linux or macOS
  * Windows


`
_10
export LANGFUSE_SECRET_KEY=SECRET_KEY
_10
export LANGFUSE_PUBLIC_KEY=PUBLIC_KEY
_10
export LANGFUSE_HOST=HOST_URL
`
`
_10
set LANGFUSE_SECRET_KEY=SECRET_KEY
_10
set LANGFUSE_PUBLIC_KEY=PUBLIC_KEY
_10
set LANGFUSE_HOST=HOST_URL
`
Replace `SECRET_KEY`, `PUBLIC_KEY`, and `HOST_URL` with the API key information you copied from Langfuse.
## Start Langflow and run a flow[​](https://docs.langflow.org/<#start-langflow-and-run-a-flow> "Direct link to Start Langflow and run a flow")
  1. Start Langflow in the same terminal or environment where you set the environment variables:
`
_10
python -m langflow run
`
  2. In Langflow, open and existing project, and then run a flow.


## View tracing data in Langfuse[​](https://docs.langflow.org/<#view-tracing-data-in-langfuse> "Direct link to View tracing data in Langfuse")
Langflow automatically collects and sends tracing data about the flow execution to Langfuse. You can view the collected data in your Langfuse project dashboard.
## Disable the Langfuse integration[​](https://docs.langflow.org/<#disable-the-langfuse-integration> "Direct link to Disable the Langfuse integration")
To disable the Langfuse integration, remove the environment variables you set in the previous steps and restart Langflow.
[PreviousIntegrate Composio with Langflow](https://docs.langflow.org/</integrations-composio>)[NextLangSmith](https://docs.langflow.org/</integrations-langsmith>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Create Langfuse project credentials](https://docs.langflow.org/<#create-langfuse-project-credentials>)
  * [Set your Langfuse credentials as environment variables](https://docs.langflow.org/<#set-your-langfuse-credentials-as-environment-variables>)
  * [Start Langflow and run a flow](https://docs.langflow.org/<#start-langflow-and-run-a-flow>)
  * [View tracing data in Langfuse](https://docs.langflow.org/<#view-tracing-data-in-langfuse>)
  * [Disable the Langfuse integration](https://docs.langflow.org/<#disable-the-langfuse-integration>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
