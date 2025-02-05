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
  * Data


On this page
# Data components in Langflow
Data components load data from a source into your flow.
They may perform some processing or type checking, like converting raw HTML data into text, or ensuring your loaded file is of an acceptable type.
## Use a data component in a flow[​](https://docs.langflow.org/<#use-a-data-component-in-a-flow> "Direct link to Use a data component in a flow")
The **URL** data component loads content from a list of URLs.
In the component's **URLs** field, enter a comma-separated list of URLs you want to load. Alternatively, connect a component that outputs the `Message` type, like the **Chat Input** component, to supply your URLs with a component.
To output a `Data` type, in the **Output Format** dropdown, select **Raw HTML**. To output a `Message` type, in the **Output Format** dropdown, select **Text**. This option applies postprocessing with the `data_to_text` helper function.
In this example of a document ingestion pipeline, the URL component outputs raw HTML to a text splitter, which splits the raw content into chunks for a vector database to ingest.
![URL component in a data ingestion pipeline](https://docs.langflow.org/assets/images/url-component-0ced1fa00ee3b97582421254b6d5be78.png)
## API Request[​](https://docs.langflow.org/<#api-request> "Direct link to API Request")
This component sends HTTP requests to the specified URLs.
Use this component to interact with external APIs or services and retrieve data. Ensure that the URLs are valid and that you configure the method, headers, body, and timeout correctly.
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
URLs| URLs| The URLs to target  
curl| curl| Paste a curl command to fill in the dictionary fields for headers and body  
Method| HTTP Method| The HTTP method to use, such as GET or POST  
Headers| Headers| The headers to include with the request  
Body| Request Body| The data to send with the request (for methods like POST, PATCH, PUT)  
Timeout| Timeout| The maximum time to wait for a response  
## Directory[​](https://docs.langflow.org/<#directory> "Direct link to Directory")
This component recursively loads files from a directory, with options for file types, depth, and concurrency.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Input| Type| Description  
---|---|---  
path| MessageTextInput| Path to the directory to load files from  
types| MessageTextInput| File types to load (leave empty to load all types)  
depth| IntInput| Depth to search for files  
max_concurrency| IntInput| Maximum concurrency for loading files  
load_hidden| BoolInput| If true, hidden files will be loaded  
recursive| BoolInput| If true, the search will be recursive  
silent_errors| BoolInput| If true, errors will not raise an exception  
use_multithreading| BoolInput| If true, multithreading will be used  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Output| Type| Description  
---|---|---  
data| List[Data]| Loaded file data from the directory  
## File[​](https://docs.langflow.org/<#file> "Direct link to File")
The FileComponent is a class that loads and parses text files of various supported formats, converting the content into a Data object. It supports multiple file types and provides an option for silent error handling.
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
path| Path| File path to load.  
silent_errors| Silent Errors| If true, errors will not raise an exception.  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
data| Data| Parsed content of the file as a Data object.  
## URL[​](https://docs.langflow.org/<#url> "Direct link to URL")
The URLComponent is a class that fetches content from one or more URLs, processes the content, and returns it as a list of Data objects. It ensures that the provided URLs are valid and uses WebBaseLoader to fetch the content.
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
urls| URLs| Enter one or more URLs  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
data| Data| List of Data objects containing fetched content and metadata  
## Gmail Loader[​](https://docs.langflow.org/<#gmail-loader> "Direct link to Gmail Loader")
This component loads emails from Gmail using provided credentials and filters.
For more on creating a service account JSON, see [Service Account JSON](https://docs.langflow.org/<https:/developers.google.com/identity/protocols/oauth2/service-account>).
### Inputs[​](https://docs.langflow.org/<#inputs-4> "Direct link to Inputs")
Input| Type| Description  
---|---|---  
json_string| SecretStrInput| JSON string containing OAuth 2.0 access token information for service account access  
label_ids| MessageTextInput| Comma-separated list of label IDs to filter emails  
max_results| MessageTextInput| Maximum number of emails to load  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Output| Type| Description  
---|---|---  
data| Data| Loaded email data  
## Google Drive Loader[​](https://docs.langflow.org/<#google-drive-loader> "Direct link to Google Drive Loader")
This component loads documents from Google Drive using provided credentials and a single document ID.
For more on creating a service account JSON, see [Service Account JSON](https://docs.langflow.org/<https:/developers.google.com/identity/protocols/oauth2/service-account>).
### Inputs[​](https://docs.langflow.org/<#inputs-5> "Direct link to Inputs")
Input| Type| Description  
---|---|---  
json_string| SecretStrInput| JSON string containing OAuth 2.0 access token information for service account access  
document_id| MessageTextInput| Single Google Drive document ID  
### Outputs[​](https://docs.langflow.org/<#outputs-4> "Direct link to Outputs")
Output| Type| Description  
---|---|---  
docs| Data| Loaded document data  
## Google Drive Search[​](https://docs.langflow.org/<#google-drive-search> "Direct link to Google Drive Search")
This component searches Google Drive files using provided credentials and query parameters.
For more on creating a service account JSON, see [Service Account JSON](https://docs.langflow.org/<https:/developers.google.com/identity/protocols/oauth2/service-account>).
### Inputs[​](https://docs.langflow.org/<#inputs-6> "Direct link to Inputs")
Input| Type| Description  
---|---|---  
token_string| SecretStrInput| JSON string containing OAuth 2.0 access token information for service account access  
query_item| DropdownInput| The field to query  
valid_operator| DropdownInput| Operator to use in the query  
search_term| MessageTextInput| The value to search for in the specified query item  
query_string| MessageTextInput| The query string used for searching (can be edited manually)  
### Outputs[​](https://docs.langflow.org/<#outputs-5> "Direct link to Outputs")
Output| Type| Description  
---|---|---  
doc_urls| List[str]| URLs of the found documents  
doc_ids| List[str]| IDs of the found documents  
doc_titles| List[str]| Titles of the found documents  
Data| Data| Document titles and URLs in a structured format  
## Webhook[​](https://docs.langflow.org/<#webhook> "Direct link to Webhook")
This component defines a webhook input for the flow. The flow can be triggered by an external HTTP POST request (webhook) sending a JSON payload.
If the input is not valid JSON, the component will wrap it in a "payload" field. The component's status will reflect any errors or the processed data.
### Inputs[​](https://docs.langflow.org/<#inputs-7> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
data| String| JSON payload for testing the webhook component  
### Outputs[​](https://docs.langflow.org/<#outputs-6> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
output_data| Data| Processed data from the webhook input  
[PreviousCreate custom Python components](https://docs.langflow.org/</components-custom-components>)[NextEmbeddings](https://docs.langflow.org/</components-embedding-models>)
  * [Use a data component in a flow](https://docs.langflow.org/<#use-a-data-component-in-a-flow>)
  * [API Request](https://docs.langflow.org/<#api-request>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
  * [Directory](https://docs.langflow.org/<#directory>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [File](https://docs.langflow.org/<#file>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [URL](https://docs.langflow.org/<#url>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Gmail Loader](https://docs.langflow.org/<#gmail-loader>)
    * [Inputs](https://docs.langflow.org/<#inputs-4>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [Google Drive Loader](https://docs.langflow.org/<#google-drive-loader>)
    * [Inputs](https://docs.langflow.org/<#inputs-5>)
    * [Outputs](https://docs.langflow.org/<#outputs-4>)
  * [Google Drive Search](https://docs.langflow.org/<#google-drive-search>)
    * [Inputs](https://docs.langflow.org/<#inputs-6>)
    * [Outputs](https://docs.langflow.org/<#outputs-5>)
  * [Webhook](https://docs.langflow.org/<#webhook>)
    * [Inputs](https://docs.langflow.org/<#inputs-7>)
    * [Outputs](https://docs.langflow.org/<#outputs-6>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ef6e4948-b294-47b0-b3c7-1fc40b8ab0df&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=2a57132a-e83f-4805-91bc-89347db9eceb&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-data&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ef6e4948-b294-47b0-b3c7-1fc40b8ab0df&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=2a57132a-e83f-4805-91bc-89347db9eceb&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-data&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
