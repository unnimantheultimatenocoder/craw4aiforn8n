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
  * LangWatch


On this page
# LangWatch
LangWatch is an all-in-one LLMOps platform for monitoring, observability, analytics, evaluations and alerting for getting user insights and improve your LLM workflows.
To integrate with Langflow, just add your LangWatch API as a Langflow environment variable and you are good to go!
## Step-by-step Configuration[​](https://docs.langflow.org/<#6f1d56ff6063417491d100d522dfcf1a> "Direct link to Step-by-step Configuration")
  1. Obtain your LangWatch API key from <https://app.langwatch.ai/>
  2. Add the following key to Langflow .env file:


`
_10
LANGWATCH_API_KEY="your-api-key"
`
or export it in your terminal:
`
_10
export LANGWATCH_API_KEY="your-api-key"
`
  1. Restart Langflow using `langflow run --env-file .env`
  2. Run a project in Langflow.
  3. View the LangWatch dashboard for monitoring and observability.


![](https://docs.langflow.org/assets/images/langwatch-dashboard-5f33bb25bb4d9022e08a4dab2592ca86.png)
[PreviousLangSmith](https://docs.langflow.org/</integrations-langsmith>)[NextIntegrate Google OAuth with Langflow](https://docs.langflow.org/</integrations-setup-google-oauth-langflow>)
  * [Step-by-step Configuration](https://docs.langflow.org/<#6f1d56ff6063417491d100d522dfcf1a>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
