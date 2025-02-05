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
    * [Agents](https://docs.langflow.org/</components-agents>)
    * [Create custom Python components](https://docs.langflow.org/</components-custom-components>)
    * [Data](https://docs.langflow.org/</components-data>)
    * [Embeddings](https://docs.langflow.org/</components-embedding-models>)
    * [Helpers](https://docs.langflow.org/</components-helpers>)
    * [Inputs and outputs](https://docs.langflow.org/</components-io>)
    * [Loaders](https://docs.langflow.org/</components-loaders>)
    * [Logic](https://docs.langflow.org/</components-logic>)
    * [Memories](https://docs.langflow.org/</components-memories>)
    * [Models](https://docs.langflow.org/</components-models>)
    * [Processing](https://docs.langflow.org/</components-processing>)
    * [Prompts](https://docs.langflow.org/</components-prompts>)
    * [Tools](https://docs.langflow.org/</components-tools>)
    * [Vector stores](https://docs.langflow.org/</components-vector-stores>)
  * [Agents](https://docs.langflow.org/</agents-overview>)
  * [Configuration](https://docs.langflow.org/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Components
  * Prompts


On this page
# Prompt components in Langflow
A prompt is a structured input to a language model that instructs the model how to handle user inputs and variables.
Prompt components create prompt templates with custom fields and dynamic variables for providing your model structured, repeatable prompts.
Prompts are a combination of natural language and variables created with curly braces.
## Use a prompt component in a flow[​](https://docs.langflow.org/<#use-a-prompt-component-in-a-flow> "Direct link to Use a prompt component in a flow")
An example of modifying a prompt can be found in the [Quickstart](https://docs.langflow.org/</get-started-quickstart#run-the-chatbot-with-retrieved-context>), where a basic chatbot flow is extended to include a full vector RAG pipeline.
![](https://docs.langflow.org/assets/images/quickstart-add-document-ingestion-5f9756b0a4b7e232b1507e12f335b15e.png)
The default prompt in the **Prompt** component is `Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.`
This prompt creates a "personality" for your LLM's chat interactions, but it doesn't include variables that you may find useful when templating prompts.
To modify the prompt template, in the **Prompt** component, click the **Template** field. For example, the `{context}` variable gives the LLM model access to embedded vector data to return better answers.
`
_10
Given the context
_10
{context}
_10
Answer the question
_10
{user_question}
`
When variables are added to a prompt template, new fields are automatically created in the component. These fields can be connected to receive text input from other components to automate prompting, or to output instructions to other components. An example of prompts controlling agents behavior is available in the [sequential tasks agent starter flow](https://docs.langflow.org/</tutorials-sequential-agent>).
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
template| Template| Create a prompt template with dynamic variables.  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
prompt| Prompt Message| The built prompt message returned by the `build_prompt` method.  
## Langchain Hub Prompt Template[​](https://docs.langflow.org/<#langchain-hub-prompt-template> "Direct link to Langchain Hub Prompt Template")
This component fetches prompts from the [Langchain Hub](https://docs.langflow.org/<https:/docs.smith.langchain.com/old/category/prompt-hub>).
When a prompt is loaded, the component generates input fields for custom variables. For example, the default prompt "efriis/my-first-prompt" generates fields for `profession` and `question`.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
langchain_api_key| Your LangChain API Key| The LangChain API Key to use.  
langchain_hub_prompt| LangChain Hub Prompt| The LangChain Hub prompt to use.  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
prompt| Build Prompt| The built prompt message returned by the `build_prompt` method.  
[PreviousProcessing](https://docs.langflow.org/</components-processing>)[NextTools](https://docs.langflow.org/</components-tools>)
  * [Use a prompt component in a flow](https://docs.langflow.org/<#use-a-prompt-component-in-a-flow>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [Langchain Hub Prompt Template](https://docs.langflow.org/<#langchain-hub-prompt-template>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
