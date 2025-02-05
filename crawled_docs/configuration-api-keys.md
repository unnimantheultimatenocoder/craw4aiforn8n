[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/<#>)
  * [Starter projects](https://docs.langflow.org/<#>)
  * [Tutorials](https://docs.langflow.org/<#>)
  * [Concepts](https://docs.langflow.org/<#>)
  * [Components](https://docs.langflow.org/<#>)
  * [Agents](https://docs.langflow.org/<#>)
  * [Configuration](https://docs.langflow.org/<#>)
    * [API keys](https://docs.langflow.org/</configuration-api-keys>)
    * [Authentication](https://docs.langflow.org/</configuration-authentication>)
    * [Auto-saving](https://docs.langflow.org/</configuration-auto-save>)
    * [Run Langflow in backend-only mode](https://docs.langflow.org/</configuration-backend-only>)
    * [Langflow CLI](https://docs.langflow.org/</configuration-cli>)
    * [Global variables](https://docs.langflow.org/</configuration-global-variables>)
    * [Environment variables](https://docs.langflow.org/</environment-variables>)
    * [Security best practices](https://docs.langflow.org/</configuration-security-best-practices>)
  * [Deployment](https://docs.langflow.org/<#>)
  * [Integrations](https://docs.langflow.org/<#>)
  * [Contributing](https://docs.langflow.org/<#>)
  * [API reference](https://docs.langflow.org/<#>)
  * [Changelog](https://docs.langflow.org/<#>)


  * [](https://docs.langflow.org/</>)
  * Configuration
  * API keys


On this page
# API keys
Langflow provides an API key functionality that allows users to access their individual components and flows without traditional login authentication. The API key is a user-specific token that can be included in the request header, query parameter, or as a command line argument to authenticate API calls. This documentation outlines how to generate, use, and manage API keys in Langflow.
info
The default user and password are set using the LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD environment variables. The default values are `langflow` and `langflow`, respectively.
## Generate an API key[​](https://docs.langflow.org/<#generate-an-api-key> "Direct link to Generate an API key")
Generate a user-specific token to use with Langflow.
### Generate an API key with the Langflow UI[​](https://docs.langflow.org/<#generate-an-api-key-with-the-langflow-ui> "Direct link to Generate an API key with the Langflow UI")
  1. Click your user icon and select **Settings**.
  2. Click **Langflow API** , and then click **Add New**.
  3. Name your key, and then click **Create Secret Key**.
  4. Copy the API key and store it in a secure location.


### Generate an API key with the Langflow CLI[​](https://docs.langflow.org/<#generate-an-api-key-with-the-langflow-cli> "Direct link to Generate an API key with the Langflow CLI")
`
1
langflow api-key
2
# or
3
python -m langflow api-key
4
╭─────────────────────────────────────────────────────────────────────╮
5
│ API Key Created Successfully:                    │
6
│                                   │
7
│ sk-O0elzoWID1izAH8RUKrnnvyyMwIzHi2Wk-uXWoNJ2Ro           │
8
│                                   │
9
│ This is the only time the API key will be displayed.        │
10
│ Make sure to store it in a secure location.             │
11
│                                   │
12
│ The API key has been copied to your clipboard. Cmd + V to paste it. │
13
╰──────────────────────────────
`
## Authenticate requests with the Langflow API key[​](https://docs.langflow.org/<#authenticate-requests-with-the-langflow-api-key> "Direct link to Authenticate requests with the Langflow API key")
Include your API key in API requests to authenticate requests to Langflow.
### Include the API key in the HTTP header[​](https://docs.langflow.org/<#include-the-api-key-in-the-http-header> "Direct link to Include the API key in the HTTP header")
To use the API key when making API requests with cURL, include the API key in the HTTP header.
`
1
curl -X POST \
2
 "http://127.0.0.1:7860/api/v1/run/*`YOUR_FLOW_ID`*?stream=false" \
3
 -H 'Content-Type: application/json' \
4
 -H 'x-api-key: *`YOUR_API_KEY`*' \
5
 -d '{"inputs": {"text":""}, "tweaks": {}}'
`
To instead pass the API key as a query parameter, do the following:
`
1
curl -X POST \
2
 "http://127.0.0.1:7860/api/v1/run/*`YOUR_FLOW_ID`*?x-api-key=*`YOUR_API_KEY`*?stream=false" \
3
 -H 'Content-Type: application/json' \
4
 -d '{"inputs": {"text":""}, "tweaks": {}}'
`
To use the API key when making API requests with the Python `requests` library, include the API key as a variable string.
`
1
import argparse
2
import json
3
from argparse import RawTextHelpFormatter
4
import requests
5
from typing import Optional
6
import warnings
7
try:
8
  from langflow.load import upload_file
9
except ImportError:
10
  warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
11
  upload_file = None
1213
BASE_API_URL = "http://127.0.0.1:7860"
14
FLOW_ID = "*`YOUR_FLOW_ID`*"
15
ENDPOINT = "" # You can set a specific endpoint name in the flow settings
1617
# You can tweak the flow by adding a tweaks dictionary
18
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
19
TWEAKS = {
20
 "ChatInput-8a86T": {},
21
 "Prompt-pKfl9": {},
22
 "ChatOutput-WcGpD": {},
23
 "OpenAIModel-5UyvQ": {}
24
}
2526
def run_flow(message: str,
27
 endpoint: str,
28
 output_type: str = "chat",
29
 input_type: str = "chat",
30
 tweaks: Optional[dict] = None,
31
 api_key: Optional[str] = None) -> dict:
32
  """
33
  Run a flow with a given message and optional tweaks.
3435
  :param message: The message to send to the flow
36
  :param endpoint: The ID or the endpoint name of the flow
37
  :param tweaks: Optional tweaks to customize the flow
38
  :return: The JSON response from the flow
39
  """
40
  api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"
4142
  payload = {
43
    "input_value": message,
44
    "output_type": output_type,
45
    "input_type": input_type,
46
  }
47
  headers = None
48
  if tweaks:
49
    payload["tweaks"] = tweaks
50
  if api_key:
51
    headers = {"x-api-key": api_key}
52
  response = requests.post(api_url, json=payload, headers=headers)
53
  return response.json()
5455
def main():
56
  parser = argparse.ArgumentParser(description="""Run a flow with a given message and optional tweaks.
57
Run it like: python <your file>.py "your message here" --endpoint "your_endpoint" --tweaks '{"key": "value"}'""",
58
    formatter_class=RawTextHelpFormatter)
59
  parser.add_argument("message", type=str, help="The message to send to the flow")
60
  parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
61
  parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
62
  parser.add_argument("--api_key", type=str, help="API key for authentication", default=None)
63
  parser.add_argument("--output_type", type=str, default="chat", help="The output type")
64
  parser.add_argument("--input_type", type=str, default="chat", help="The input type")
65
  parser.add_argument("--upload_file", type=str, help="Path to the file to upload", default=None)
66
  parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)
6768
  args = parser.parse_args()
69
  try:
70
   tweaks = json.loads(args.tweaks)
71
  except json.JSONDecodeError:
72
   raise ValueError("Invalid tweaks JSON string")
7374
  if args.upload_file:
75
    if not upload_file:
76
      raise ImportError("Langflow is not installed. Please install it to use the upload_file function.")
77
    elif not args.components:
78
      raise ValueError("You need to provide the components to upload the file to.")
79
    tweaks = upload_file(file_path=args.upload_file, host=BASE_API_URL, flow_id=args.endpoint, components=[args.components], tweaks=tweaks)
8081
  response = run_flow(
82
    message=args.message,
83
    endpoint=args.endpoint,
84
    output_type=args.output_type,
85
    input_type=args.input_type,
86
    tweaks=tweaks,
87
    api_key=args.api_key
88
  )
8990
  print(json.dumps(response, indent=2))
9192
if __name__ == "__main__":
93
  main()
`
To pass the API key to your script with a command line argument, do the following:
`
1
python your_script.py "*`YOUR_INPUT_MESSAGE`*" --api_key "*`YOUR_API_KEY`*"
`
## Security considerations[​](https://docs.langflow.org/<#security-considerations> "Direct link to Security considerations")
  * **Visibility** : For security reasons, the API key cannot be retrieved again through the UI.
  * **Scope** : The key allows access only to the flows and components of the specific user to whom it was issued.


## Custom API endpoint[​](https://docs.langflow.org/<#custom-api-endpoint> "Direct link to Custom API endpoint")
To choose a custom name for your API endpoint, select **Project Settings** > **Endpoint Name** and name your endpoint.
## Revoke an API key[​](https://docs.langflow.org/<#revoke-an-api-key> "Direct link to Revoke an API key")
To revoke an API key, delete it from the list of keys in the **Settings** menu.
  1. Click your user icon and select **Settings**.
  2. Click **Langflow API**.
  3. Select the keys you want to delete and click the trash can icon.


This action immediately invalidates the key and prevents it from being used again.
[PreviousCreate a problem-solving agent](https://docs.langflow.org/</agents-tool-calling-agent-component>)[NextAuthentication](https://docs.langflow.org/</configuration-authentication>)
  * [Generate an API key](https://docs.langflow.org/<#generate-an-api-key>)
    * [Generate an API key with the Langflow UI](https://docs.langflow.org/<#generate-an-api-key-with-the-langflow-ui>)
    * [Generate an API key with the Langflow CLI](https://docs.langflow.org/<#generate-an-api-key-with-the-langflow-cli>)
  * [Authenticate requests with the Langflow API key](https://docs.langflow.org/<#authenticate-requests-with-the-langflow-api-key>)
    * [Include the API key in the HTTP header](https://docs.langflow.org/<#include-the-api-key-in-the-http-header>)
  * [Security considerations](https://docs.langflow.org/<#security-considerations>)
  * [Custom API endpoint](https://docs.langflow.org/<#custom-api-endpoint>)
  * [Revoke an API key](https://docs.langflow.org/<#revoke-an-api-key>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
