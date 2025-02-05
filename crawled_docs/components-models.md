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
  * Models


On this page
# Model components in Langflow
Model components generate text using large language models.
Refer to your specific component's documentation for more information on parameters.
## Use a model component in a flow[​](https://docs.langflow.org/<#use-a-model-component-in-a-flow> "Direct link to Use a model component in a flow")
Model components receive inputs and prompts for generating text, and the generated text is sent to an output component.
The model output can also be sent to the **Language Model** port and on to a **Parse Data** component, where the output can be parsed into structured [Data](https://docs.langflow.org/</concepts-objects>) objects.
This example has the OpenAI model in a chatbot flow. For more information, see the [Basic prompting flow](https://docs.langflow.org/</starter-projects-basic-prompting>).
![](https://docs.langflow.org/assets/images/starter-flow-basic-prompting-09331815d7282bd6a3feedf84838ba20.png)
## AI/ML API[​](https://docs.langflow.org/<#aiml-api> "Direct link to AI/ML API")
This component creates a ChatOpenAI model instance using the AIML API.
For more information, see [AIML documentation](https://docs.langflow.org/<https:/docs.aimlapi.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
max_tokens| Integer| The maximum number of tokens to generate. Set to 0 for unlimited tokens. Range: 0-128000.  
model_kwargs| Dictionary| Additional keyword arguments for the model.  
model_name| String| The name of the AIML model to use. Options are predefined in `AIML_CHAT_MODELS`.  
aiml_api_base| String| The base URL of the AIML API. Defaults to `https://api.aimlapi.com`.  
api_key| SecretString| The AIML API Key to use for the model.  
temperature| Float| Controls randomness in the output. Default: `0.1`.  
seed| Integer| Controls reproducibility of the job.  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatOpenAI configured with the specified parameters.  
## Amazon Bedrock[​](https://docs.langflow.org/<#amazon-bedrock> "Direct link to Amazon Bedrock")
This component generates text using Amazon Bedrock LLMs.
For more information, see [Amazon Bedrock documentation](https://docs.langflow.org/<https:/docs.aws.amazon.com/bedrock>).
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
model_id| String| The ID of the Amazon Bedrock model to use. Options include various models.  
aws_access_key| SecretString| AWS Access Key for authentication.  
aws_secret_key| SecretString| AWS Secret Key for authentication.  
credentials_profile_name| String| Name of the AWS credentials profile to use (advanced).  
region_name| String| AWS region name. Default: `us-east-1`.  
model_kwargs| Dictionary| Additional keyword arguments for the model (advanced).  
endpoint_url| String| Custom endpoint URL for the Bedrock service (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatBedrock configured with the specified parameters.  
## Anthropic[​](https://docs.langflow.org/<#anthropic> "Direct link to Anthropic")
This component allows the generation of text using Anthropic Chat and Language models.
For more information, see the [Anthropic documentation](https://docs.langflow.org/<https:/docs.anthropic.com/en/docs/welcome>).
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
max_tokens| Integer| The maximum number of tokens to generate. Set to 0 for unlimited tokens. Default: `4096`.  
model| String| The name of the Anthropic model to use. Options include various Claude 3 models.  
anthropic_api_key| SecretString| Your Anthropic API key for authentication.  
temperature| Float| Controls randomness in the output. Default: `0.1`.  
anthropic_api_url| String| Endpoint of the Anthropic API. Defaults to `https://api.anthropic.com` if not specified (advanced).  
prefill| String| Prefill text to guide the model's response (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatAnthropic configured with the specified parameters.  
## Azure OpenAI[​](https://docs.langflow.org/<#azure-openai> "Direct link to Azure OpenAI")
This component generates text using Azure OpenAI LLM.
For more information, see the [Azure OpenAI documentation](https://docs.langflow.org/<https:/learn.microsoft.com/en-us/azure/ai-services/openai/>).
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
Model Name| Model Name| Specifies the name of the Azure OpenAI model to be used for text generation.  
Azure Endpoint| Azure Endpoint| Your Azure endpoint, including the resource.  
Deployment Name| Deployment Name| Specifies the name of the deployment.  
API Version| API Version| Specifies the version of the Azure OpenAI API to be used.  
API Key| API Key| Your Azure OpenAI API key.  
Temperature| Temperature| Specifies the sampling temperature. Defaults to `0.7`.  
Max Tokens| Max Tokens| Specifies the maximum number of tokens to generate. Defaults to `1000`.  
Input Value| Input Value| Specifies the input text for text generation.  
Stream| Stream| Specifies whether to stream the response from the model. Defaults to `False`.  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of AzureOpenAI configured with the specified parameters.  
## Cohere[​](https://docs.langflow.org/<#cohere> "Direct link to Cohere")
This component generates text using Cohere's language models.
For more information, see the [Cohere documentation](https://docs.langflow.org/<https:/cohere.ai/>).
### Inputs[​](https://docs.langflow.org/<#inputs-4> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
Cohere API Key| Cohere API Key| Your Cohere API key.  
Max Tokens| Max Tokens| Specifies the maximum number of tokens to generate. Defaults to `256`.  
Temperature| Temperature| Specifies the sampling temperature. Defaults to `0.75`.  
Input Value| Input Value| Specifies the input text for text generation.  
### Outputs[​](https://docs.langflow.org/<#outputs-4> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of the Cohere model configured with the specified parameters.  
## DeepSeek[​](https://docs.langflow.org/<#deepseek> "Direct link to DeepSeek")
This component generates text using DeepSeek's language models.
For more information, see the [DeepSeek documentation](https://docs.langflow.org/<https:/api-docs.deepseek.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs-5> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
max_tokens| Integer| Maximum number of tokens to generate. Set to `0` for unlimited. Range: `0-128000`.  
model_kwargs| Dictionary| Additional keyword arguments for the model.  
json_mode| Boolean| If `True`, outputs JSON regardless of passing a schema.  
model_name| String| The DeepSeek model to use. Default: `deepseek-chat`.  
api_base| String| Base URL for API requests. Default: `https://api.deepseek.com`.  
api_key| SecretString| Your DeepSeek API key for authentication.  
temperature| Float| Controls randomness in responses. Range: `[0.0, 2.0]`. Default: `1.0`.  
seed| Integer| Number initialized for random number generation. Use the same seed integer for more reproducible results, and use a different seed number for more random results.  
### Outputs[​](https://docs.langflow.org/<#outputs-5> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatOpenAI configured with the specified parameters.  
## Google Generative AI[​](https://docs.langflow.org/<#google-generative-ai> "Direct link to Google Generative AI")
This component generates text using Google's Generative AI models.
For more information, see the [Google Generative AI documentation](https://docs.langflow.org/<https:/cloud.google.com/vertex-ai/docs/>).
### Inputs[​](https://docs.langflow.org/<#inputs-6> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
Google API Key| Google API Key| Your Google API key to use for the Google Generative AI.  
Model| Model| The name of the model to use, such as `"gemini-pro"`.  
Max Output Tokens| Max Output Tokens| The maximum number of tokens to generate.  
Temperature| Temperature| Run inference with this temperature.  
Top K| Top K| Consider the set of top K most probable tokens.  
Top P| Top P| The maximum cumulative probability of tokens to consider when sampling.  
N| N| Number of chat completions to generate for each prompt.  
### Outputs[​](https://docs.langflow.org/<#outputs-6> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatGoogleGenerativeAI configured with the specified parameters.  
## Groq[​](https://docs.langflow.org/<#groq> "Direct link to Groq")
This component generates text using Groq's language models.
For more information, see the [Groq documentation](https://docs.langflow.org/<https:/groq.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs-7> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
groq_api_key| SecretString| API key for the Groq API.  
groq_api_base| String| Base URL path for API requests. Default: `https://api.groq.com` (advanced).  
max_tokens| Integer| The maximum number of tokens to generate (advanced).  
temperature| Float| Controls randomness in the output. Range: `[0.0, 1.0]`. Default: `0.1`.  
n| Integer| Number of chat completions to generate for each prompt (advanced).  
model_name| String| The name of the Groq model to use. Options are dynamically fetched from the Groq API.  
### Outputs[​](https://docs.langflow.org/<#outputs-7> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatGroq configured with the specified parameters.  
## Hugging Face API[​](https://docs.langflow.org/<#hugging-face-api> "Direct link to Hugging Face API")
This component generates text using Hugging Face's language models.
For more information, see the [Hugging Face documentation](https://docs.langflow.org/<https:/huggingface.co/>).
### Inputs[​](https://docs.langflow.org/<#inputs-8> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
Endpoint URL| Endpoint URL| The URL of the Hugging Face Inference API endpoint.  
Task| Task| Specifies the task for text generation.  
API Token| API Token| The API token required for authentication.  
Model Kwargs| Model Kwargs| Additional keyword arguments for the model.  
Input Value| Input Value| The input text for text generation.  
## LMStudio[​](https://docs.langflow.org/<#lmstudio> "Direct link to LMStudio")
This component generates text using LM Studio's local language models.
For more information, see [LM Studio documentation](https://docs.langflow.org/<https:/lmstudio.ai/>).
### Inputs[​](https://docs.langflow.org/<#inputs-9> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
base_url| String| The URL where LM Studio is running. Default: `"http://localhost:1234"`.  
max_tokens| Integer| Maximum number of tokens to generate in the response. Default: `512`.  
temperature| Float| Controls randomness in the output. Range: `[0.0, 2.0]`. Default: `0.7`.  
top_p| Float| Controls diversity via nucleus sampling. Range: `[0.0, 1.0]`. Default: `1.0`.  
stop| List[String]| List of strings that will stop generation when encountered (advanced).  
stream| Boolean| Whether to stream the response. Default: `False`.  
presence_penalty| Float| Penalizes repeated tokens. Range: `[-2.0, 2.0]`. Default: `0.0`.  
frequency_penalty| Float| Penalizes frequent tokens. Range: `[-2.0, 2.0]`. Default: `0.0`.  
### Outputs[​](https://docs.langflow.org/<#outputs-8> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of LMStudio configured with the specified parameters.  
## Maritalk[​](https://docs.langflow.org/<#maritalk> "Direct link to Maritalk")
This component generates text using Maritalk LLMs.
For more information, see [Maritalk documentation](https://docs.langflow.org/<https:/www.maritalk.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs-10> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
max_tokens| Integer| The maximum number of tokens to generate. Set to `0` for unlimited tokens. Default: `512`.  
model_name| String| The name of the Maritalk model to use. Options: `sabia-2-small`, `sabia-2-medium`. Default: `sabia-2-small`.  
api_key| SecretString| The Maritalk API Key to use for authentication.  
temperature| Float| Controls randomness in the output. Range: `[0.0, 1.0]`. Default: `0.5`.  
endpoint_url| String| The Maritalk API endpoint. Default: `https://api.maritalk.com`.  
### Outputs[​](https://docs.langflow.org/<#outputs-9> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatMaritalk configured with the specified parameters.  
## Mistral[​](https://docs.langflow.org/<#mistral> "Direct link to Mistral")
This component generates text using MistralAI LLMs.
For more information, see [Mistral AI documentation](https://docs.langflow.org/<https:/docs.mistral.ai/>).
### Inputs[​](https://docs.langflow.org/<#inputs-11> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
max_tokens| Integer| The maximum number of tokens to generate. Set to 0 for unlimited tokens (advanced).  
model_name| String| The name of the Mistral AI model to use. Options include `open-mixtral-8x7b`, `open-mixtral-8x22b`, `mistral-small-latest`, `mistral-medium-latest`, `mistral-large-latest`, and `codestral-latest`. Default: `codestral-latest`.  
mistral_api_base| String| The base URL of the Mistral API. Defaults to `https://api.mistral.ai/v1` (advanced).  
api_key| SecretString| The Mistral API Key to use for authentication.  
temperature| Float| Controls randomness in the output. Default: 0.5.  
max_retries| Integer| Maximum number of retries for API calls. Default: 5 (advanced).  
timeout| Integer| Timeout for API calls in seconds. Default: 60 (advanced).  
max_concurrent_requests| Integer| Maximum number of concurrent API requests. Default: 3 (advanced).  
top_p| Float| Nucleus sampling parameter. Default: 1 (advanced).  
random_seed| Integer| Seed for random number generation. Default: 1 (advanced).  
safe_mode| Boolean| Enables safe mode for content generation (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-10> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatMistralAI configured with the specified parameters.  
## Novita AI[​](https://docs.langflow.org/<#novita-ai> "Direct link to Novita AI")
This component generates text using Novita AI's language models.
For more information, see [Novita AI documentation](https://docs.langflow.org/<https:/novita.ai/docs/model-api/reference/llm/llm.html?utm_source=github_langflow&utm_medium=github_readme&utm_campaign=link>).
### Inputs[​](https://docs.langflow.org/<#inputs-12> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
api_key| SecretString| Your Novita AI API Key.  
model| String| The id of the Novita AI model to use.  
max_tokens| Integer| The maximum number of tokens to generate. Set to 0 for unlimited tokens.  
temperature| Float| Controls randomness in the output. Range: [0.0, 1.0]. Default: 0.7.  
top_p| Float| Controls the nucleus sampling. Range: [0.0, 1.0]. Default: 1.0.  
frequency_penalty| Float| Controls the frequency penalty. Range: [0.0, 2.0]. Default: 0.0.  
presence_penalty| Float| Controls the presence penalty. Range: [0.0, 2.0]. Default: 0.0.  
### Outputs[​](https://docs.langflow.org/<#outputs-11> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of Novita AI model configured with the specified parameters.  
## NVIDIA[​](https://docs.langflow.org/<#nvidia> "Direct link to NVIDIA")
This component generates text using NVIDIA LLMs.
For more information, see [NVIDIA AI documentation](https://docs.langflow.org/<https:/developer.nvidia.com/generative-ai>).
### Inputs[​](https://docs.langflow.org/<#inputs-13> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
max_tokens| Integer| The maximum number of tokens to generate. Set to `0` for unlimited tokens (advanced).  
model_name| String| The name of the NVIDIA model to use. Default: `mistralai/mixtral-8x7b-instruct-v0.1`.  
base_url| String| The base URL of the NVIDIA API. Default: `https://integrate.api.nvidia.com/v1`.  
nvidia_api_key| SecretString| The NVIDIA API Key for authentication.  
temperature| Float| Controls randomness in the output. Default: `0.1`.  
seed| Integer| The seed controls the reproducibility of the job (advanced). Default: `1`.  
### Outputs[​](https://docs.langflow.org/<#outputs-12> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatNVIDIA configured with the specified parameters.  
## Ollama[​](https://docs.langflow.org/<#ollama> "Direct link to Ollama")
This component generates text using Ollama's language models.
For more information, see [Ollama documentation](https://docs.langflow.org/<https:/ollama.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs-14> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
Base URL| Base URL| Endpoint of the Ollama API.  
Model Name| Model Name| The model name to use.  
Temperature| Temperature| Controls the creativity of model responses.  
### Outputs[​](https://docs.langflow.org/<#outputs-13> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of an Ollama model configured with the specified parameters.  
## OpenAI[​](https://docs.langflow.org/<#openai> "Direct link to OpenAI")
This component generates text using OpenAI's language models.
For more information, see [OpenAI documentation](https://docs.langflow.org/<https:/beta.openai.com/docs/>).
### Inputs[​](https://docs.langflow.org/<#inputs-15> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
api_key| SecretString| Your OpenAI API Key.  
model| String| The name of the OpenAI model to use. Options include "gpt-3.5-turbo" and "gpt-4".  
max_tokens| Integer| The maximum number of tokens to generate. Set to 0 for unlimited tokens.  
temperature| Float| Controls randomness in the output. Range: [0.0, 1.0]. Default: 0.7.  
top_p| Float| Controls the nucleus sampling. Range: [0.0, 1.0]. Default: 1.0.  
frequency_penalty| Float| Controls the frequency penalty. Range: [0.0, 2.0]. Default: 0.0.  
presence_penalty| Float| Controls the presence penalty. Range: [0.0, 2.0]. Default: 0.0.  
### Outputs[​](https://docs.langflow.org/<#outputs-14> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of OpenAI model configured with the specified parameters.  
## OpenRouter[​](https://docs.langflow.org/<#openrouter> "Direct link to OpenRouter")
This component generates text using OpenRouter's unified API for multiple AI models from different providers.
For more information, see [OpenRouter documentation](https://docs.langflow.org/<https:/openrouter.ai/docs>).
### Inputs[​](https://docs.langflow.org/<#inputs-16> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
api_key| SecretString| Your OpenRouter API key for authentication.  
site_url| String| Your site URL for OpenRouter rankings (advanced).  
app_name| String| Your app name for OpenRouter rankings (advanced).  
provider| String| The AI model provider to use.  
model_name| String| The specific model to use for chat completion.  
temperature| Float| Controls randomness in the output. Range: [0.0, 2.0]. Default: 0.7.  
max_tokens| Integer| The maximum number of tokens to generate (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-15> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatOpenAI configured with the specified parameters.  
## Perplexity[​](https://docs.langflow.org/<#perplexity> "Direct link to Perplexity")
This component generates text using Perplexity's language models.
For more information, see [Perplexity documentation](https://docs.langflow.org/<https:/perplexity.ai/>).
### Inputs[​](https://docs.langflow.org/<#inputs-17> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
model_name| String| The name of the Perplexity model to use. Options include various Llama 3.1 models.  
max_output_tokens| Integer| The maximum number of tokens to generate.  
api_key| SecretString| The Perplexity API Key for authentication.  
temperature| Float| Controls randomness in the output. Default: 0.75.  
top_p| Float| The maximum cumulative probability of tokens to consider when sampling (advanced).  
n| Integer| Number of chat completions to generate for each prompt (advanced).  
top_k| Integer| Number of top tokens to consider for top-k sampling. Must be positive (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-16> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatPerplexity configured with the specified parameters.  
## Qianfan[​](https://docs.langflow.org/<#qianfan> "Direct link to Qianfan")
This component generates text using Qianfan's language models.
For more information, see [Qianfan documentation](https://docs.langflow.org/<https:/github.com/baidubce/bce-qianfan-sdk>).
## SambaNova[​](https://docs.langflow.org/<#sambanova> "Direct link to SambaNova")
This component generates text using SambaNova LLMs.
For more information, see [Sambanova Cloud documentation](https://docs.langflow.org/<https:/cloud.sambanova.ai/>).
### Inputs[​](https://docs.langflow.org/<#inputs-18> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
sambanova_url| String| Base URL path for API requests. Default: `https://api.sambanova.ai/v1/chat/completions`.  
sambanova_api_key| SecretString| Your SambaNova API Key.  
model_name| String| The name of the Sambanova model to use. Options include various Llama models.  
max_tokens| Integer| The maximum number of tokens to generate. Set to 0 for unlimited tokens.  
temperature| Float| Controls randomness in the output. Range: [0.0, 1.0]. Default: 0.07.  
### Outputs[​](https://docs.langflow.org/<#outputs-17> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of SambaNova model configured with the specified parameters.  
## VertexAI[​](https://docs.langflow.org/<#vertexai> "Direct link to VertexAI")
This component generates text using Vertex AI LLMs.
For more information, see [Google Vertex AI documentation](https://docs.langflow.org/<https:/cloud.google.com/vertex-ai>).
### Inputs[​](https://docs.langflow.org/<#inputs-19> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
credentials| File| JSON credentials file. Leave empty to fallback to environment variables. File type: JSON.  
model_name| String| The name of the Vertex AI model to use. Default: "gemini-1.5-pro".  
project| String| The project ID (advanced).  
location| String| The location for the Vertex AI API. Default: "us-central1" (advanced).  
max_output_tokens| Integer| The maximum number of tokens to generate (advanced).  
max_retries| Integer| Maximum number of retries for API calls. Default: 1 (advanced).  
temperature| Float| Controls randomness in the output. Default: 0.0.  
top_k| Integer| The number of highest probability vocabulary tokens to keep for top-k-filtering (advanced).  
top_p| Float| The cumulative probability of parameter highest probability vocabulary tokens to keep for nucleus sampling. Default: 0.95 (advanced).  
verbose| Boolean| Whether to print verbose output. Default: False (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-18> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
model| LanguageModel| An instance of ChatVertexAI configured with the specified parameters.  
[PreviousMemories](https://docs.langflow.org/</components-memories>)[NextProcessing](https://docs.langflow.org/</components-processing>)
  * [Use a model component in a flow](https://docs.langflow.org/<#use-a-model-component-in-a-flow>)
  * [AI/ML API](https://docs.langflow.org/<#aiml-api>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [Amazon Bedrock](https://docs.langflow.org/<#amazon-bedrock>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Anthropic](https://docs.langflow.org/<#anthropic>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Azure OpenAI](https://docs.langflow.org/<#azure-openai>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [Cohere](https://docs.langflow.org/<#cohere>)
    * [Inputs](https://docs.langflow.org/<#inputs-4>)
    * [Outputs](https://docs.langflow.org/<#outputs-4>)
  * [DeepSeek](https://docs.langflow.org/<#deepseek>)
    * [Inputs](https://docs.langflow.org/<#inputs-5>)
    * [Outputs](https://docs.langflow.org/<#outputs-5>)
  * [Google Generative AI](https://docs.langflow.org/<#google-generative-ai>)
    * [Inputs](https://docs.langflow.org/<#inputs-6>)
    * [Outputs](https://docs.langflow.org/<#outputs-6>)
  * [Groq](https://docs.langflow.org/<#groq>)
    * [Inputs](https://docs.langflow.org/<#inputs-7>)
    * [Outputs](https://docs.langflow.org/<#outputs-7>)
  * [Hugging Face API](https://docs.langflow.org/<#hugging-face-api>)
    * [Inputs](https://docs.langflow.org/<#inputs-8>)
  * [LMStudio](https://docs.langflow.org/<#lmstudio>)
    * [Inputs](https://docs.langflow.org/<#inputs-9>)
    * [Outputs](https://docs.langflow.org/<#outputs-8>)
  * [Maritalk](https://docs.langflow.org/<#maritalk>)
    * [Inputs](https://docs.langflow.org/<#inputs-10>)
    * [Outputs](https://docs.langflow.org/<#outputs-9>)
  * [Mistral](https://docs.langflow.org/<#mistral>)
    * [Inputs](https://docs.langflow.org/<#inputs-11>)
    * [Outputs](https://docs.langflow.org/<#outputs-10>)
  * [Novita AI](https://docs.langflow.org/<#novita-ai>)
    * [Inputs](https://docs.langflow.org/<#inputs-12>)
    * [Outputs](https://docs.langflow.org/<#outputs-11>)
  * [NVIDIA](https://docs.langflow.org/<#nvidia>)
    * [Inputs](https://docs.langflow.org/<#inputs-13>)
    * [Outputs](https://docs.langflow.org/<#outputs-12>)
  * [Ollama](https://docs.langflow.org/<#ollama>)
    * [Inputs](https://docs.langflow.org/<#inputs-14>)
    * [Outputs](https://docs.langflow.org/<#outputs-13>)
  * [OpenAI](https://docs.langflow.org/<#openai>)
    * [Inputs](https://docs.langflow.org/<#inputs-15>)
    * [Outputs](https://docs.langflow.org/<#outputs-14>)
  * [OpenRouter](https://docs.langflow.org/<#openrouter>)
    * [Inputs](https://docs.langflow.org/<#inputs-16>)
    * [Outputs](https://docs.langflow.org/<#outputs-15>)
  * [Perplexity](https://docs.langflow.org/<#perplexity>)
    * [Inputs](https://docs.langflow.org/<#inputs-17>)
    * [Outputs](https://docs.langflow.org/<#outputs-16>)
  * [Qianfan](https://docs.langflow.org/<#qianfan>)
  * [SambaNova](https://docs.langflow.org/<#sambanova>)
    * [Inputs](https://docs.langflow.org/<#inputs-18>)
    * [Outputs](https://docs.langflow.org/<#outputs-17>)
  * [VertexAI](https://docs.langflow.org/<#vertexai>)
    * [Inputs](https://docs.langflow.org/<#inputs-19>)
    * [Outputs](https://docs.langflow.org/<#outputs-18>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
