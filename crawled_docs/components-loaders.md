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
  * Loaders


On this page
# Loader components in Langflow
info
As of Langflow 1.1, loader components are now found in the **Components** menu under **Bundles**.
Loaders fetch data into Langflow from various sources, such as databases, websites, and local files.
## Use a loader component in a flow[​](https://docs.langflow.org/<#use-a-loader-component-in-a-flow> "Direct link to Use a loader component in a flow")
This flow creates a question-and-answer chatbot for documents that are loaded into the flow. The [Unstructured.io](https://docs.langflow.org/<https:/unstructured.io/>) loader component loads files from your local machine, and then parses them into a list of structured [Data](https://docs.langflow.org/</concepts-objects>) objects. This loaded data informs the **Open AI** component's responses to your questions.
![Sample Flow retrieving data with unstructured](https://docs.langflow.org/assets/images/starter-flow-unstructured-qa-c029fa3529d7098a59549e3dfc1517a8.png)
## Confluence[​](https://docs.langflow.org/<#confluence> "Direct link to Confluence")
The Confluence component integrates with the Confluence wiki collaboration platform to load and process documents. It utilizes the ConfluenceLoader from LangChain to fetch content from a specified Confluence space.
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
url| Site URL| The base URL of the Confluence Space (e.g., `https://company.atlassian.net/wiki`)  
username| Username| Atlassian User E-mail (e.g., `email@example.com`)  
api_key| API Key| Atlassian API Key (Create an API key at: [Atlassian](https://docs.langflow.org/<https:/id.atlassian.com/manage-profile/security/api-tokens>))  
space_key| Space Key| The key of the Confluence space to access  
cloud| Use Cloud?| Whether to use Confluence Cloud (default: true)  
content_format| Content Format| Specify content format (default: STORAGE)  
max_pages| Max Pages| Maximum number of pages to retrieve (default: 1000)  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
data| Data| List of Data objects containing the loaded Confluence documents  
## GitLoader[​](https://docs.langflow.org/<#gitloader> "Direct link to GitLoader")
The GitLoader component uses the GitLoader from LangChain to fetch and load documents from a specified Git repository.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
repo_path| Repository Path| The local path to the Git repository  
clone_url| Clone URL| The URL to clone the Git repository from (optional)  
branch| Branch| The branch to load files from (default: 'main')  
file_filter| File Filter| Patterns to filter files (e.g., '.py' to include only .py files, '!.py' to exclude .py files)  
content_filter| Content Filter| A regex pattern to filter files based on their content  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
data| Data| List of Data objects containing the loaded Git repository documents  
## Unstructured[​](https://docs.langflow.org/<#unstructured> "Direct link to Unstructured")
This component uses the [Unstructured.io](https://docs.langflow.org/<https:/unstructured.io/>) Serverless API to load and parse files into a list of structured [Data](https://docs.langflow.org/</concepts-objects>) objects.
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
file| File| The path to the file to be parsed (supported types are listed [here](https://docs.langflow.org/<https:/docs.unstructured.io/api-reference/api-services/overview#supported-file-types>))  
api_key| API Key| Unstructured.io Serverless API Key  
api_url| Unstructured.io API URL| Optional URL for the Unstructured API  
chunking_strategy| Chunking Strategy| Strategy for chunking the document (options: "", "basic", "by_title", "by_page", "by_similarity")  
unstructured_args| Additional Arguments| Optional dictionary of additional arguments for the Unstructured.io API  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
data| Data| List of Data objects containing the parsed content from the input file  
[PreviousInputs and outputs](https://docs.langflow.org/</components-io>)[NextLogic](https://docs.langflow.org/</components-logic>)
  * [Use a loader component in a flow](https://docs.langflow.org/<#use-a-loader-component-in-a-flow>)
  * [Confluence](https://docs.langflow.org/<#confluence>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [GitLoader](https://docs.langflow.org/<#gitloader>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Unstructured](https://docs.langflow.org/<#unstructured>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
