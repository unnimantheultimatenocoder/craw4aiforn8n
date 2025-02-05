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
  * Embeddings


On this page
# Embeddings models in Langflow
Embeddings models convert text into numerical vectors. These embeddings capture semantic meaning of the input text, and allow LLMs to understand context.
Refer to your specific component's documentation for more information on parameters.
## Use an embeddings model component in a flow[​](https://docs.langflow.org/<#use-an-embeddings-model-component-in-a-flow> "Direct link to Use an embeddings model component in a flow")
In this example of a document ingestion pipeline, the **OpenAI** embeddings model is connected to a vector database. The component converts the text chunks into vectors and stores them in the vector database. The vectorized data can be used to inform AI workloads like chatbots, similarity searches, and agents.
This embeddings component uses an OpenAI API key for authentication. Refer to your specific embeddings component's documentation for more information on authentication.
![URL component in a data ingestion pipeline](https://docs.langflow.org/assets/images/url-component-0ced1fa00ee3b97582421254b6d5be78.png)
## AI/ML[​](https://docs.langflow.org/<#aiml> "Direct link to AI/ML")
This component generates embeddings using the [AI/ML API](https://docs.langflow.org/<https:/docs.aimlapi.com/api-overview/embeddings>).
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
model_name| String| The name of the AI/ML embedding model to use  
aiml_api_key| SecretString| API key for authenticating with the AI/ML service  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance of AIMLEmbeddingsImpl for generating embeddings  
## Amazon Bedrock Embeddings[​](https://docs.langflow.org/<#amazon-bedrock-embeddings> "Direct link to Amazon Bedrock Embeddings")
This component is used to load embedding models from [Amazon Bedrock](https://docs.langflow.org/<https:/aws.amazon.com/bedrock/>).
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
credentials_profile_name| String| Name of the AWS credentials profile in ~/.aws/credentials or ~/.aws/config, which has access keys or role information  
model_id| String| ID of the model to call, e.g., `amazon.titan-embed-text-v1`. This is equivalent to the `modelId` property in the `list-foundation-models` API  
endpoint_url| String| URL to set a specific service endpoint other than the default AWS endpoint  
region_name| String| AWS region to use, e.g., `us-west-2`. Falls back to `AWS_DEFAULT_REGION` environment variable or region specified in ~/.aws/config if not provided  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance for generating embeddings using Amazon Bedrock  
## Astra DB vectorize[​](https://docs.langflow.org/<#astra-db-vectorize> "Direct link to Astra DB vectorize")
Connect this component to the **Embeddings** port of the [Astra DB vector store component](https://docs.langflow.org/</components-vector-stores#astra-db-vector-store>) to generate embeddings.
This component requires that your Astra DB database has a collection that uses a vectorize embedding provider integration. For more information and instructions, see [Embedding Generation](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/embedding-generation.html>).
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
provider| Embedding Provider| The embedding provider to use  
model_name| Model Name| The embedding model to use  
authentication| Authentication| The name of the API key in Astra that stores your [vectorize embedding provider credentials](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/embedding-generation.html#embedding-provider-authentication>). (Not required if using an [Astra-hosted embedding provider](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/embedding-generation.html#supported-embedding-providers>).)  
provider_api_key| Provider API Key| As an alternative to `authentication`, directly provide your embedding provider credentials.  
model_parameters| Model Parameters| Additional model parameters  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance for generating embeddings using Astra vectorize  
## Azure OpenAI Embeddings[​](https://docs.langflow.org/<#azure-openai-embeddings> "Direct link to Azure OpenAI Embeddings")
This component generates embeddings using Azure OpenAI models.
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
Model| String| Name of the model to use (default: `text-embedding-3-small`)  
Azure Endpoint| String| Your Azure endpoint, including the resource. Example: `https://example-resource.azure.openai.com/`  
Deployment Name| String| The name of the deployment  
API Version| String| The API version to use, options include various dates  
API Key| String| The API key to access the Azure OpenAI service  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance for generating embeddings using Azure OpenAI  
## Cohere Embeddings[​](https://docs.langflow.org/<#cohere-embeddings> "Direct link to Cohere Embeddings")
This component is used to load embedding models from [Cohere](https://docs.langflow.org/<https:/cohere.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs-4> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
cohere_api_key| String| API key required to authenticate with the Cohere service  
model| String| Language model used for embedding text documents and performing queries (default: `embed-english-v2.0`)  
truncate| Boolean| Whether to truncate the input text to fit within the model's constraints (default: `False`)  
### Outputs[​](https://docs.langflow.org/<#outputs-4> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance for generating embeddings using Cohere  
## Embedding similarity[​](https://docs.langflow.org/<#embedding-similarity> "Direct link to Embedding similarity")
This component computes selected forms of similarity between two embedding vectors.
### Inputs[​](https://docs.langflow.org/<#inputs-5> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
embedding_vectors| Embedding Vectors| A list containing exactly two data objects with embedding vectors to compare.  
similarity_metric| Similarity Metric| Select the similarity metric to use. Options: "Cosine Similarity", "Euclidean Distance", "Manhattan Distance".  
### Outputs[​](https://docs.langflow.org/<#outputs-5> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
similarity_data| Similarity Data| Data object containing the computed similarity score and additional information.  
## Google generative AI embeddings[​](https://docs.langflow.org/<#google-generative-ai-embeddings> "Direct link to Google generative AI embeddings")
This component connects to Google's generative AI embedding service using the GoogleGenerativeAIEmbeddings class from the `langchain-google-genai` package.
### Inputs[​](https://docs.langflow.org/<#inputs-6> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
api_key| API Key| Secret API key for accessing Google's generative AI service (required)  
model_name| Model Name| Name of the embedding model to use (default: "models/text-embedding-004")  
### Outputs[​](https://docs.langflow.org/<#outputs-6> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
embeddings| Embeddings| Built GoogleGenerativeAIEmbeddings object  
## Hugging Face Embeddings[​](https://docs.langflow.org/<#hugging-face-embeddings> "Direct link to Hugging Face Embeddings")
note
This component is deprecated as of Langflow version 1.0.18. Instead, use the [Hugging Face API Embeddings component](https://docs.langflow.org/<#hugging-face-embeddings-inference-api>).
This component loads embedding models from HuggingFace.
Use this component to generate embeddings using locally downloaded Hugging Face models. Ensure you have sufficient computational resources to run the models.
### Inputs[​](https://docs.langflow.org/<#inputs-7> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
Cache Folder| Cache Folder| Folder path to cache HuggingFace models  
Encode Kwargs| Encoding Arguments| Additional arguments for the encoding process  
Model Kwargs| Model Arguments| Additional arguments for the model  
Model Name| Model Name| Name of the HuggingFace model to use  
Multi Process| Multi-Process| Whether to use multiple processes  
## Hugging Face embeddings Inference API[​](https://docs.langflow.org/<#hugging-face-embeddings-inference-api> "Direct link to Hugging Face embeddings Inference API")
This component generates embeddings using Hugging Face Inference API models.
Use this component to create embeddings with Hugging Face's hosted models. Ensure you have a valid Hugging Face API key.
### Inputs[​](https://docs.langflow.org/<#inputs-8> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
API Key| API Key| API key for accessing the Hugging Face Inference API  
API URL| API URL| URL of the Hugging Face Inference API  
Model Name| Model Name| Name of the model to use for embeddings  
Cache Folder| Cache Folder| Folder path to cache Hugging Face models  
Encode Kwargs| Encoding Arguments| Additional arguments for the encoding process  
Model Kwargs| Model Arguments| Additional arguments for the model  
Multi Process| Multi-Process| Whether to use multiple processes  
## MistralAI[​](https://docs.langflow.org/<#mistralai> "Direct link to MistralAI")
This component generates embeddings using MistralAI models.
### Inputs[​](https://docs.langflow.org/<#inputs-9> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
model| String| The MistralAI model to use (default: "mistral-embed")  
mistral_api_key| SecretString| API key for authenticating with MistralAI  
max_concurrent_requests| Integer| Maximum number of concurrent API requests (default: 64)  
max_retries| Integer| Maximum number of retry attempts for failed requests (default: 5)  
timeout| Integer| Request timeout in seconds (default: 120)  
endpoint| String| Custom API endpoint URL (default: `https://api.mistral.ai/v1/`)  
### Outputs[​](https://docs.langflow.org/<#outputs-7> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| MistralAIEmbeddings instance for generating embeddings  
## NVIDIA[​](https://docs.langflow.org/<#nvidia> "Direct link to NVIDIA")
This component generates embeddings using NVIDIA models.
### Inputs[​](https://docs.langflow.org/<#inputs-10> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
model| String| The NVIDIA model to use for embeddings (e.g., `nvidia/nv-embed-v1`)  
base_url| String| Base URL for the NVIDIA API (default: `https://integrate.api.nvidia.com/v1`)  
nvidia_api_key| SecretString| API key for authenticating with NVIDIA's service  
temperature| Float| Model temperature for embedding generation (default: `0.1`)  
### Outputs[​](https://docs.langflow.org/<#outputs-8> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| NVIDIAEmbeddings instance for generating embeddings  
## Ollama Embeddings[​](https://docs.langflow.org/<#ollama-embeddings> "Direct link to Ollama Embeddings")
This component generates embeddings using Ollama models.
### Inputs[​](https://docs.langflow.org/<#inputs-11> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
Ollama Model| String| Name of the Ollama model to use (default: `llama2`)  
Ollama Base URL| String| Base URL of the Ollama API (default: `http://localhost:11434`)  
Model Temperature| Float| Temperature parameter for the model. Adjusts the randomness in the generated embeddings  
### Outputs[​](https://docs.langflow.org/<#outputs-9> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance for generating embeddings using Ollama  
## OpenAI Embeddings[​](https://docs.langflow.org/<#openai-embeddings> "Direct link to OpenAI Embeddings")
This component is used to load embedding models from [OpenAI](https://docs.langflow.org/<https:/openai.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs-12> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
OpenAI API Key| String| The API key to use for accessing the OpenAI API  
Default Headers| Dict| Default headers for the HTTP requests  
Default Query| NestedDict| Default query parameters for the HTTP requests  
Allowed Special| List| Special tokens allowed for processing (default: `[]`)  
Disallowed Special| List| Special tokens disallowed for processing (default: `["all"]`)  
Chunk Size| Integer| Chunk size for processing (default: `1000`)  
Client| Any| HTTP client for making requests  
Deployment| String| Deployment name for the model (default: `text-embedding-3-small`)  
Embedding Context Length| Integer| Length of embedding context (default: `8191`)  
Max Retries| Integer| Maximum number of retries for failed requests (default: `6`)  
Model| String| Name of the model to use (default: `text-embedding-3-small`)  
Model Kwargs| NestedDict| Additional keyword arguments for the model  
OpenAI API Base| String| Base URL of the OpenAI API  
OpenAI API Type| String| Type of the OpenAI API  
OpenAI API Version| String| Version of the OpenAI API  
OpenAI Organization| String| Organization associated with the API key  
OpenAI Proxy| String| Proxy server for the requests  
Request Timeout| Float| Timeout for the HTTP requests  
Show Progress Bar| Boolean| Whether to show a progress bar for processing (default: `False`)  
Skip Empty| Boolean| Whether to skip empty inputs (default: `False`)  
TikToken Enable| Boolean| Whether to enable TikToken (default: `True`)  
TikToken Model Name| String| Name of the TikToken model  
### Outputs[​](https://docs.langflow.org/<#outputs-10> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance for generating embeddings using OpenAI  
## Text embedder[​](https://docs.langflow.org/<#text-embedder> "Direct link to Text embedder")
This component generates embeddings for a given message using a specified embedding model.
### Inputs[​](https://docs.langflow.org/<#inputs-13> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
embedding_model| Embedding Model| The embedding model to use for generating embeddings.  
message| Message| The message for which to generate embeddings.  
### Outputs[​](https://docs.langflow.org/<#outputs-11> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
embeddings| Embedding Data| Data object containing the original text and its embedding vector.  
## VertexAI Embeddings[​](https://docs.langflow.org/<#vertexai-embeddings> "Direct link to VertexAI Embeddings")
This component is a wrapper around [Google Vertex AI](https://docs.langflow.org/<https:/cloud.google.com/vertex-ai>) [Embeddings API](https://docs.langflow.org/<https:/cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings>).
### Inputs[​](https://docs.langflow.org/<#inputs-14> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
credentials| Credentials| The default custom credentials to use  
location| String| The default location to use when making API calls (default: `us-central1`)  
max_output_tokens| Integer| Token limit determines the maximum amount of text output from one prompt (default: `128`)  
model_name| String| The name of the Vertex AI large language model (default: `text-bison`)  
project| String| The default GCP project to use when making Vertex API calls  
request_parallelism| Integer| The amount of parallelism allowed for requests issued to VertexAI models (default: `5`)  
temperature| Float| Tunes the degree of randomness in text generations. Should be a non-negative value (default: `0`)  
top_k| Integer| How the model selects tokens for output, the next token is selected from the top `k` tokens (default: `40`)  
top_p| Float| Tokens are selected from the most probable to least until the sum of their probabilities exceeds the top `p` value (default: `0.95`)  
tuned_model_name| String| The name of a tuned model. If provided, `model_name` is ignored  
verbose| Boolean| This parameter controls the level of detail in the output. When set to `True`, it prints internal states of the chain to help debug (default: `False`)  
### Outputs[​](https://docs.langflow.org/<#outputs-12> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
embeddings| Embeddings| An instance for generating embeddings using VertexAI  
[PreviousData](https://docs.langflow.org/</components-data>)[NextHelpers](https://docs.langflow.org/</components-helpers>)
  * [Use an embeddings model component in a flow](https://docs.langflow.org/<#use-an-embeddings-model-component-in-a-flow>)
  * [AI/ML](https://docs.langflow.org/<#aiml>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [Amazon Bedrock Embeddings](https://docs.langflow.org/<#amazon-bedrock-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Astra DB vectorize](https://docs.langflow.org/<#astra-db-vectorize>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Azure OpenAI Embeddings](https://docs.langflow.org/<#azure-openai-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [Cohere Embeddings](https://docs.langflow.org/<#cohere-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-4>)
    * [Outputs](https://docs.langflow.org/<#outputs-4>)
  * [Embedding similarity](https://docs.langflow.org/<#embedding-similarity>)
    * [Inputs](https://docs.langflow.org/<#inputs-5>)
    * [Outputs](https://docs.langflow.org/<#outputs-5>)
  * [Google generative AI embeddings](https://docs.langflow.org/<#google-generative-ai-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-6>)
    * [Outputs](https://docs.langflow.org/<#outputs-6>)
  * [Hugging Face Embeddings](https://docs.langflow.org/<#hugging-face-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-7>)
  * [Hugging Face embeddings Inference API](https://docs.langflow.org/<#hugging-face-embeddings-inference-api>)
    * [Inputs](https://docs.langflow.org/<#inputs-8>)
  * [MistralAI](https://docs.langflow.org/<#mistralai>)
    * [Inputs](https://docs.langflow.org/<#inputs-9>)
    * [Outputs](https://docs.langflow.org/<#outputs-7>)
  * [NVIDIA](https://docs.langflow.org/<#nvidia>)
    * [Inputs](https://docs.langflow.org/<#inputs-10>)
    * [Outputs](https://docs.langflow.org/<#outputs-8>)
  * [Ollama Embeddings](https://docs.langflow.org/<#ollama-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-11>)
    * [Outputs](https://docs.langflow.org/<#outputs-9>)
  * [OpenAI Embeddings](https://docs.langflow.org/<#openai-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-12>)
    * [Outputs](https://docs.langflow.org/<#outputs-10>)
  * [Text embedder](https://docs.langflow.org/<#text-embedder>)
    * [Inputs](https://docs.langflow.org/<#inputs-13>)
    * [Outputs](https://docs.langflow.org/<#outputs-11>)
  * [VertexAI Embeddings](https://docs.langflow.org/<#vertexai-embeddings>)
    * [Inputs](https://docs.langflow.org/<#inputs-14>)
    * [Outputs](https://docs.langflow.org/<#outputs-12>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e06d4315-ec7f-4221-8f56-c940bf27fbb1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8d12488f-a770-4ea7-91c3-dc8e17a46530&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-embedding-models&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e06d4315-ec7f-4221-8f56-c940bf27fbb1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8d12488f-a770-4ea7-91c3-dc8e17a46530&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-embedding-models&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
