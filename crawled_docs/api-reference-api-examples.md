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
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
    * [API examples](https://docs.langflow.org/</api-reference-api-examples>)
    * [API documentation](https://docs.langflow.org/</api>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * API reference
  * API examples


On this page
# API examples
This page provides examples and practices for managing Langflow using the Langflow API.
The Langflow API's OpenAPI spec can be viewed and tested at your Langflow deployment's `docs` endpoint. For example, `http://127.0.0.1:7860/docs`.
## Export values (optional)[​](https://docs.langflow.org/<#export-values-optional> "Direct link to Export values \(optional\)")
You might find it helpful to set the following environment variables:
  * Export your Langflow URL in your terminal. Langflow starts by default at `http://127.0.0.1:7860`.


`
1
export LANGFLOW_URL="http://127.0.0.1:7860"
`
  * Export the `flow-id` in your terminal. The `flow-id` is found in the [API pane](https://docs.langflow.org/</concepts-api>) or in the flow's URL.


`
1
export FLOW_ID="359cd752-07ea-46f2-9d3b-a4407ef618da"
`
  * Export the `folder-id` in your terminal. To find your folder ID, call the Langflow [/api/v1/folders/](https://docs.langflow.org/<#read-folders>) endpoint for a list of folders.


  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/folders/" \
3
 -H 'accept: application/json'
`
`
_10
[
_10
 {
_10
  "name": "My Projects",
_10
  "description": "Manage your own projects. Download and upload folders.",
_10
  "id": "1415de42-8f01-4f36-bf34-539f23e47466",
_10
  "parent_id": null
_10
 }
_10
]
`
Export the `folder-id` as an environment variable.
`
1
export FOLDER_ID="1415de42-8f01-4f36-bf34-539f23e47466"
`
  * Export the Langflow API key as an environment variable. To create a Langflow API key, run the following command in the Langflow CLI.


  * curl
  * Result


`
1
langflow api-key
`
`
_10
API Key Created Successfully:
_10
sk-...
`
Export the generated API key as an environment variable.
`
1
export LANGFLOW_API_KEY="sk-..."
`
The examples in this guide use environment variables for these values.
## Build[​](https://docs.langflow.org/<#build> "Direct link to Build")
Use the `/build` endpoint to build vertices and flows.
### Build flow[​](https://docs.langflow.org/<#build-flow> "Direct link to Build flow")
This example builds a flow with a given `flow_id`.
LLM chat responses are streamed back as `token` events until the `end` event closes the connection.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/build/$FLOW_ID/flow" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -H "x-api-key: $LANGFLOW_API_KEY" \
6
 -d '{"message": "hello, how are you doing?"}'
`
`
_13
{"event": "vertices_sorted", "data": {"ids": ["Prompt-CDhMB", "ChatInput-8VNJS"], "to_run": ["ChatOutput-Up0tW", "OpenAIModel-mXCyV", "Prompt-CDhMB", "ChatInput-8VNJS"]}}
_13
_13
{"event": "add_message", "data": {"timestamp": "2025-01-13T21:27:27", "sender": "User", "sender_name": "User", "session_id": "b68d9bfb-6382-455a-869b-b99a3a3a3cf6", "text": "", "files": [], "error": false, "edit": false, "properties": {"text_color": "", "background_color": "", "edited": false, "source": {"id": null, "display_name": null, "source": null}, "icon": "", "allow_markdown": false, "positive_feedback": null, "state": "complete", "targets": []}, "category": "message", "content_blocks": [], "id": "3942f4e3-4fff-4507-bb58-c96c7b6b8515", "flow_id": "b68d9bfb-6382-455a-869b-b99a3a3a3cf6"}}
_13
_13
{"event": "end_vertex", "data": {"build_data": {"id": "Prompt-CDhMB", "inactivated_vertices": [], "next_vertices_ids": [], "top_level_vertices": [], "valid": true, "params": "None", "data": {"results": {}, "outputs": {"prompt": {"message": "You are a helpful AI assistant", "type": "text"}}, "logs": {"prompt": []}, "message": {"prompt": {"repr": "You are a helpful AI assistant", "raw": "You are a helpful AI assistant", "type": "text"}}, "artifacts": {"prompt": {"repr": "You are a helpful AI assistant", "raw": "You are a helpful AI assistant", "type": "text"}}, "timedelta": 0.007543042069301009, "duration": "8 ms", "used_frozen_result": false}, "timestamp": "2025-01-13T21:27:27.231841Z"}}}
_13
_13
{"event": "token", "data": {"chunk": "", "id": "fda55d2e-d24c-498e-92a8-03ca2141265e", "timestamp": "2025-01-13 21:27:27 UTC"}}
_13
_13
{"event": "token", "data": {"chunk": "Hello", "id": "fda55d2e-d24c-498e-92a8-03ca2141265e", "timestamp": "2025-01-13 21:27:27 UTC"}}
_13
_13
{"event": "token", "data": {"chunk": "!", "id": "fda55d2e-d24c-498e-92a8-03ca2141265e", "timestamp": "2025-01-13 21:27:27 UTC"}}
_13
_13
{"event": "end", "data": {}}
`
This output is abbreviated, but the order of events illustrates how Langflow runs components.
  1. Langflow first sorts the vertices by dependencies (edges) in the `vertices_sorted` event:


`
1
ChatInput-8VNJS → Prompt-CDhMB → OpenAIModel-mXCyV → ChatOutput-Up0tW
`
  1. The Chat Input component receives user input in the `add_message` event.
  2. The Prompt component is built and executed with the received input in the `end_vertex` event.
  3. The Open AI model's responses stream as `token` events. The `token` event represents individual pieces of text as they're generated by an LLM.
  4. The clean `end` event tells you the flow executed with no errors. If your flow executes with errors, the `error` event handler prints the errors to the playground.


You can also pass values for `start_component_id` and `stop_component_id` in the body of the command to control where the flow run will start and stop. For example, to stop flow execution at the Open AI model component, run the following command:
`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/build/$FLOW_ID/flow" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -H "x-api-key: $LANGFLOW_API_KEY" \
6
 -d '{"stop_component_id": "OpenAIModel-Uksag"}'
`
## Flows[​](https://docs.langflow.org/<#flows> "Direct link to Flows")
Use the `/flows` endpoint to create, read, update, and delete flows.
### Create flow[​](https://docs.langflow.org/<#create-flow> "Direct link to Create flow")
Create a new flow.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/flows/" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "name": "string2",
7
 "description": "string",
8
 "icon": "string",
9
 "icon_bg_color": "#FF0000",
10
 "gradient": "string",
11
 "data": {},
12
 "is_component": false,
13
 "updated_at": "2024-12-30T15:48:01.519Z",
14
 "webhook": false,
15
 "endpoint_name": "string",
16
 "tags": [
17
  "string"
18
 ],
19
 "locked": false,
20
 "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
21
 "folder_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
22
}'
`
`
_25
{
_25
  "name": "Untitled document (2)",
_25
  "description": "Conversational Cartography Unlocked.",
_25
  "icon": null,
_25
  "icon_bg_color": null,
_25
  "gradient": null,
_25
  "data": {
_25
    "nodes": [],
_25
    "edges": [],
_25
    "viewport": {
_25
      "zoom": 1,
_25
      "x": 0,
_25
      "y": 0
_25
    }
_25
  },
_25
  "is_component": false,
_25
  "updated_at": "2024-12-30T15:48:53+00:00",
_25
  "webhook": false,
_25
  "endpoint_name": null,
_25
  "tags": null,
_25
  "locked": false,
_25
  "id": "91be355a-3cd1-46b2-89c0-6b416391ad95",
_25
  "user_id": "f58396d4-a387-4bb8-b749-f40825c3d9f3",
_25
  "folder_id": "1415de42-8f01-4f36-bf34-539f23e47466"
_25
}
`
### Read flows[​](https://docs.langflow.org/<#read-flows> "Direct link to Read flows")
Retrieve a list of flows with pagination support.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/flows/?remove_example_flows=false&components_only=false&get_all=true&header_flows=false&page=1&size=50" \
3
 -H 'accept: application/json'
`
`
_10
A JSON object containing a list of flows.
`
To retrieve only the flows from a specific folder, pass `folder_id` in the query string.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/flows/?remove_example_flows=true&components_only=false&get_all=false&folder_id=$FOLDER_ID&header_flows=false&page=1&size=1" \
3
 -H 'accept: application/json'
`
`
_10
A JSON object containing a list of flows.
`
### Read flow[​](https://docs.langflow.org/<#read-flow> "Direct link to Read flow")
Read a specific flow by its ID.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/flows/$FLOW_ID" \
3
 -H 'accept: application/json'
`
`
_12
{
_12
 "name": "Basic Prompting",
_12
 "description": "Perform basic prompting with an OpenAI model.",
_12
 "icon": "Braces",
_12
 "icon_bg_color": null,
_12
 "gradient": "2",
_12
 "data": {
_12
  "nodes": [
_12
   ...
_12
  ]
_12
 }
_12
}
`
### Update flow[​](https://docs.langflow.org/<#update-flow> "Direct link to Update flow")
Update an existing flow by its ID.
This example changes the value for `endpoint_name` from a random UUID to `my_new_endpoint_name`.
  * curl
  * Result


`
1
curl -X 'PATCH' \
2
 "$LANGFLOW_URL/api/v1/flows/$FLOW_ID" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "name": "string",
7
 "description": "string",
8
 "data": {},
9
 "folder_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
10
 "endpoint_name": "my_new_endpoint_name",
11
 "locked": true
12
}'
`
`
_17
{
_17
 "name": "string",
_17
 "description": "string",
_17
 "icon": "Braces",
_17
 "icon_bg_color": null,
_17
 "gradient": "2",
_17
 "data": {},
_17
 "is_component": false,
_17
 "updated_at": "2024-12-30T18:30:22+00:00",
_17
 "webhook": false,
_17
 "endpoint_name": "my_new_endpoint_name",
_17
 "tags": null,
_17
 "locked": true,
_17
 "id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
_17
 "user_id": "f58396d4-a387-4bb8-b749-f40825c3d9f3",
_17
 "folder_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
_17
}
`
### Delete flow[​](https://docs.langflow.org/<#delete-flow> "Direct link to Delete flow")
Delete a specific flow by its ID.
  * curl
  * Result


`
1
curl -X 'DELETE' \
2
 "$LANGFLOW_URL/api/v1/flows/$FLOW_ID" \
3
 -H 'accept: application/json'
`
`
_10
{
_10
 "message": "Flow deleted successfully"
_10
}
`
### Create flows[​](https://docs.langflow.org/<#create-flows> "Direct link to Create flows")
Create multiple new flows.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/flows/batch/" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "flows": [
7
  {
8
   "name": "string",
9
   "description": "string",
10
   "icon": "string",
11
   "icon_bg_color": "string",
12
   "gradient": "string",
13
   "data": {},
14
   "is_component": false,
15
   "updated_at": "2024-12-30T18:36:02.737Z",
16
   "webhook": false,
17
   "endpoint_name": "string",
18
   "tags": [
19
    "string"
20
   ],
21
   "locked": false,
22
   "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
23
   "folder_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
24
  },
25
  {
26
   "name": "string",
27
   "description": "string",
28
   "icon": "string",
29
   "icon_bg_color": "string",
30
   "gradient": "string",
31
   "data": {},
32
   "is_component": false,
33
   "updated_at": "2024-12-30T18:36:02.737Z",
34
   "webhook": false,
35
   "endpoint_name": "string",
36
   "tags": [
37
    "string"
38
   ],
39
   "locked": false,
40
   "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
41
   "folder_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
42
  }
43
 ]
44
}'
`
`
_10
[
_10
 {
_10
  // FlowRead objects
_10
 }
_10
]
`
### Upload flows[​](https://docs.langflow.org/<#upload-flows> "Direct link to Upload flows")
Upload flows from a file.
This example uploads a local file named `agent-with-astra-db-tool.json`.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/flows/upload/?folder_id=$FOLDER_ID" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: multipart/form-data' \
5
 -F 'file=@agent-with-astra-db-tool.json;type=application/json'
`
`
_11
[
_11
 {
_11
  "name": "agent-with-astra-db-tool",
_11
  "description": "",
_11
  "icon": null,
_11
  "icon_bg_color": null,
_11
  "gradient": null,
_11
  "data": {}
_11
 ...
_11
 }
_11
]
`
To specify a target folder for the flow, include the query parameter `folder_id`. The target `folder_id` must already exist before uploading a flow. Call the [/api/v1/folders/](https://docs.langflow.org/<#read-folders>) endpoint for a list of available folders.
`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/flows/upload/?folder_id=$FOLDER_ID" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: multipart/form-data' \
5
 -F 'file=@agent-with-astra-db-tool.json;type=application/json'
`
### Download all flows[​](https://docs.langflow.org/<#download-all-flows> "Direct link to Download all flows")
Download all flows as a ZIP file.
This endpoint downloads a ZIP file containing flows for all `flow-id` values listed in the command's body.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/flows/download/" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '[
6
 "e1e40c77-0541-41a9-88ab-ddb3419398b5", "92f9a4c5-cfc8-4656-ae63-1f0881163c28"
7
]' \
8
 --output langflow-flows.zip
`
`
_10
 % Total  % Received % Xferd Average Speed  Time  Time   Time Current
_10
                 Dload Upload  Total  Spent  Left Speed
_10
100 76437  0 76353 100  84 4516k  5088 --:--:-- --:--:-- --:--:-- 4665k
`
### Read basic examples[​](https://docs.langflow.org/<#read-basic-examples> "Direct link to Read basic examples")
Retrieve a list of basic example flows.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/flows/basic_examples/" \
3
 -H 'accept: application/json'
`
`
_10
A list of example flows.
`
## Monitor[​](https://docs.langflow.org/<#monitor> "Direct link to Monitor")
Use the `/monitor` endpoint to monitor and modify messages passed between Langflow components, vertex builds, and transactions.
### Get Vertex builds[​](https://docs.langflow.org/<#get-vertex-builds> "Direct link to Get Vertex builds")
Retrieve Vertex builds for a specific flow.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/monitor/builds?flow_id=$FLOW_ID" \
3
 -H 'accept: application/json'
`
`
_10
{"vertex_builds":{"ChatInput-NCmix":[{"data":{"results":{"message":{"text_key":"text","data":{"timestamp":"2024-12-23 19:10:57","sender":"User","sender_name":"User","session_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","text":"Hello","files":[],"error":"False","edit":"False","properties":{"text_color":"","background_color":"","edited":"False","source":{"id":"None","display_name":"None","source":"None"},"icon":"","allow_markdown":"False","positive_feedback":"None","state":"complete","targets":[]},"category":"message","content_blocks":[],"id":"c95bed34-f906-4aa6-84e4-68553f6db772","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"},"default_value":"","text":"Hello","sender":"User","sender_name":"User","files":[],"session_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","timestamp":"2024-12-23 19:10:57+00:00","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","error":"False","edit":"False","properties":{"text_color":"","background_color":"","edited":"False","source":{"id":"None","display_name":"None","source":"None"},"icon":"","allow_markdown":"False","positive_feedback":"None","state":"complete","targets":[]},"category":"message","content_blocks":[]}},"outputs":{"message":{"message":{"timestamp":"2024-12-23T19:10:57","sender":"User","sender_name":"User","session_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","text":"Hello","files":[],"error":false,"edit":false,"properties":{"text_color":"","background_color":"","edited":false,"source":{"id":null,"display_name":null,"source":null},"icon":"","allow_markdown":false,"positive_feedback":null,"state":"complete","targets":[]},"category":"message","content_blocks":[],"id":"c95bed34-f906-4aa6-84e4-68553f6db772","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"},"type":"object"}},"logs":{"message":[]},"message":{"message":"Hello","sender":"User","sender_name":"User","files":[],"type":"object"},"artifacts":{"message":"Hello","sender":"User","sender_name":"User","files":[],"type":"object"},"timedelta":0.015060124918818474,"duration":"15 ms","used_frozen_result":false},"artifacts":{"message":"Hello","sender":"User","sender_name":"User","files":[],"type":"object"},"params":"- Files: []\n Message: Hello\n Sender: User\n Sender Name: User\n Type: object\n","valid":true,"build_id":"40aa200e-74db-4651-b698-f80301d2b26b","id":"ChatInput-NCmix","timestamp":"2024-12-23T19:10:58.772766Z","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"}],"Prompt-BEn9c":[{"data":{"results":{},"outputs":{"prompt":{"message":"Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.","type":"text"}},"logs":{"prompt":[]},"message":{"prompt":{"repr":"Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.","raw":"Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.","type":"text"}},"artifacts":{"prompt":{"repr":"Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.","raw":"Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.","type":"text"}},"timedelta":0.0057758750626817346,"duration":"6 ms","used_frozen_result":false},"artifacts":{"prompt":{"repr":"Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.","raw":"Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.","type":"text"}},"params":"None","valid":true,"build_id":"39bbbfde-97fd-42a5-a9ed-d42a5c5d532b","id":"Prompt-BEn9c","timestamp":"2024-12-23T19:10:58.781019Z","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"}],"OpenAIModel-7AjrN":[{"data":{"results":{},"outputs":{"text_output":{"message":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","type":"text"},"model_output":{"message":"","type":"unknown"}},"logs":{"text_output":[]},"message":{"text_output":{"repr":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","raw":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","type":"text"}},"artifacts":{"text_output":{"repr":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","raw":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","type":"text"}},"timedelta":1.034765167045407,"duration":"1.03 seconds","used_frozen_result":false},"artifacts":{"text_output":{"repr":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","raw":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","type":"text"}},"params":"None","valid":true,"build_id":"4f0ae730-a266-4d35-b89f-7b825c620a0f","id":"OpenAIModel-7AjrN","timestamp":"2024-12-23T19:10:58.790484Z","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"}],"ChatOutput-sfUhT":[{"data":{"results":{"message":{"text_key":"text","data":{"timestamp":"2024-12-23 19:10:58","sender":"Machine","sender_name":"AI","session_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","text":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","files":[],"error":"False","edit":"False","properties":{"text_color":"","background_color":"","edited":"False","source":{"id":"OpenAIModel-7AjrN","display_name":"OpenAI","source":"gpt-4o-mini"},"icon":"OpenAI","allow_markdown":"False","positive_feedback":"None","state":"complete","targets":[]},"category":"message","content_blocks":[],"id":"5688356d-9f30-40ca-9907-79a7a2fc16fd","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"},"default_value":"","text":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","sender":"Machine","sender_name":"AI","files":[],"session_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","timestamp":"2024-12-23 19:10:58+00:00","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","error":"False","edit":"False","properties":{"text_color":"","background_color":"","edited":"False","source":{"id":"OpenAIModel-7AjrN","display_name":"OpenAI","source":"gpt-4o-mini"},"icon":"OpenAI","allow_markdown":"False","positive_feedback":"None","state":"complete","targets":[]},"category":"message","content_blocks":[]}},"outputs":{"message":{"message":{"timestamp":"2024-12-23T19:10:58","sender":"Machine","sender_name":"AI","session_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","text":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","files":[],"error":false,"edit":false,"properties":{"text_color":"","background_color":"","edited":false,"source":{"id":"OpenAIModel-7AjrN","display_name":"OpenAI","source":"gpt-4o-mini"},"icon":"OpenAI","allow_markdown":false,"positive_feedback":null,"state":"complete","targets":[]},"category":"message","content_blocks":[],"id":"5688356d-9f30-40ca-9907-79a7a2fc16fd","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"},"type":"object"}},"logs":{"message":[]},"message":{"message":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","sender":"Machine","sender_name":"AI","files":[],"type":"object"},"artifacts":{"message":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","sender":"Machine","sender_name":"AI","files":[],"type":"object"},"timedelta":0.017838125000707805,"duration":"18 ms","used_frozen_result":false},"artifacts":{"message":"Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!","sender":"Machine","sender_name":"AI","files":[],"type":"object"},"params":"- Files: []\n Message: Hello! 🌟 I'm excited to help you get started on your journey to building\n  something fresh! What do you have in mind? Whether it's a project, an idea, or\n  a concept, let's dive in and make it happen!\n Sender: Machine\n Sender Name: AI\n Type: object\n","valid":true,"build_id":"1e8b908b-aba7-403b-9e9b-eca92bb78668","id":"ChatOutput-sfUhT","timestamp":"2024-12-23T19:10:58.813268Z","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"}]}}
`
### Delete Vertex builds[​](https://docs.langflow.org/<#delete-vertex-builds> "Direct link to Delete Vertex builds")
Delete Vertex builds for a specific flow.
  * curl
  * Result


`
1
curl -X 'DELETE' \
2
 "$LANGFLOW_URL/api/v1/monitor/builds?flow_id=$FLOW_ID" \
3
 -H 'accept: */*'
`
`
_10
204 No Content
`
### Get messages[​](https://docs.langflow.org/<#get-messages> "Direct link to Get messages")
Retrieve messages with optional filters.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 'http://127.0.0.1:7860/api/v1/monitor/messages' \
3
 -H 'accept: application/json'
`
`
_10
A list of all messages.
`
You can filter messages by `flow_id`, `session_id`, `sender`, and `sender_name`. Results can be ordered with the `order_by` query string.
This example retrieves messages sent by `Machine` and `AI` in a given chat session (`session_id`) and orders the messages by timestamp.
  * curl
  * Result


`
1
curl -X "GET" \
2
 "$LANGFLOW_URL/api/v1/monitor/messages?flow_id=$FLOW_ID&session_id=01ce083d-748b-4b8d-97b6-33adbb6a528a&sender=Machine&sender_name=AI&order_by=timestamp" \
3
 -H "accept: application/json"
`
`
_30
[
_30
 {
_30
  "id": "1c1d6134-9b8b-4079-931c-84dcaddf19ba",
_30
  "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
_30
  "timestamp": "2024-12-23 19:20:11 UTC",
_30
  "sender": "Machine",
_30
  "sender_name": "AI",
_30
  "session_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
_30
  "text": "Hello! It's great to see you here! What exciting project or idea are you thinking about diving into today? Whether it's something fresh and innovative or a classic concept with a twist, I'm here to help you get started! Let's brainstorm together!",
_30
  "files": "[]",
_30
  "edit": false,
_30
  "properties": {
_30
   "text_color": "",
_30
   "background_color": "",
_30
   "edited": false,
_30
   "source": {
_30
    "id": "OpenAIModel-7AjrN",
_30
    "display_name": "OpenAI",
_30
    "source": "gpt-4o-mini"
_30
   },
_30
   "icon": "OpenAI",
_30
   "allow_markdown": false,
_30
   "positive_feedback": null,
_30
   "state": "complete",
_30
   "targets": []
_30
  },
_30
  "category": "message",
_30
  "content_blocks": []
_30
 }
_30
]
`
### Delete messages[​](https://docs.langflow.org/<#delete-messages> "Direct link to Delete messages")
Delete specific messages by their IDs.
This example deletes the message retrieved in the previous Get messages example.
  * curl
  * Result


`
1
curl -v -X 'DELETE' \
2
 '$LANGFLOW_URL/api/v1/monitor/messages' \
3
 -H 'accept: */*' \
4
 -H 'Content-Type: application/json' \
5
 -d '[
6
 "1c1d6134-9b8b-4079-931c-84dcaddf19ba"
7
]'
`
`
_10
204 No Content
`
To delete multiple messages, list the IDs within the array.
`
1
curl -v -X 'DELETE' \
2
 '$LANGFLOW_URL/api/v1/monitor/messages' \
3
 -H 'accept: */*' \
4
 -H 'Content-Type: application/json' \
5
 -d '["MESSAGE_ID_1", "MESSAGE_ID_2"]'
`
### Update message[​](https://docs.langflow.org/<#update-message> "Direct link to Update message")
Update a specific message by its ID.
This example updates the `text` value of message `3ab66cc6-c048-48f8-ab07-570f5af7b160`.
  * curl
  * Result


`
1
curl -X 'PUT' \
2
 "$LANGFLOW_URL/api/v1/monitor/messages/3ab66cc6-c048-48f8-ab07-570f5af7b160" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "text": "testing 1234"
7
}'
`
`
_10
{"timestamp":"2024-12-23T18:49:06","sender":"string","sender_name":"string","session_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a","text":"testing 1234","files":["string"],"error":true,"edit":true,"properties":{"text_color":"string","background_color":"string","edited":false,"source":{"id":"string","display_name":"string","source":"string"},"icon":"string","allow_markdown":false,"positive_feedback":true,"state":"complete","targets":[]},"category":"message","content_blocks":[],"id":"3ab66cc6-c048-48f8-ab07-570f5af7b160","flow_id":"01ce083d-748b-4b8d-97b6-33adbb6a528a"}
`
### Update session ID[​](https://docs.langflow.org/<#update-session-id> "Direct link to Update session ID")
Update the session ID for messages.
This example updates the `session_ID` value `01ce083d-748b-4b8d-97b6-33adbb6a528a` to `different_session_id`.
  * curl
  * Result


`
1
curl -X 'PATCH' \
2
 "$LANGFLOW_URL/api/v1/monitor/messages/session/01ce083d-748b-4b8d-97b6-33adbb6a528a?new_session_id=different_session_id" \
3
 -H 'accept: application/json'
`
`
_30
[
_30
 {
_30
  "id": "8dd7f064-e63a-4773-b472-ca0475249dfd",
_30
  "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
_30
  "timestamp": "2024-12-23 18:49:55 UTC",
_30
  "sender": "User",
_30
  "sender_name": "User",
_30
  "session_id": "different_session_id",
_30
  "text": "message",
_30
  "files": "[]",
_30
  "edit": false,
_30
  "properties": {
_30
   "text_color": "",
_30
   "background_color": "",
_30
   "edited": false,
_30
   "source": {
_30
    "id": null,
_30
    "display_name": null,
_30
    "source": null
_30
   },
_30
   "icon": "",
_30
   "allow_markdown": false,
_30
   "positive_feedback": null,
_30
   "state": "complete",
_30
   "targets": []
_30
  },
_30
  "category": "message",
_30
  "content_blocks": []
_30
 },
_30
]
`
### Delete messages by session[​](https://docs.langflow.org/<#delete-messages-by-session> "Direct link to Delete messages by session")
Delete all messages for a specific session.
  * curl
  * Result


`
1
curl -X 'DELETE' \
2
 '$LANGFLOW_URL/api/v1/monitor/messages/session/different_session_id_2' \
3
 -H 'accept: */*'
`
`
_10
HTTP/1.1 204 No Content
`
### Get transactions[​](https://docs.langflow.org/<#get-transactions> "Direct link to Get transactions")
Retrieve all transactions (interactions between components) for a specific flow.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 '$LANGFLOW_URL/api/v1/monitor/transactions?flow_id=$FLOW_ID&page=1&size=50' \
3
 -H 'accept: application/json'
`
`
_19
{
_19
 "items": [
_19
  {
_19
   "timestamp": "2024-12-23T20:05:01.061Z",
_19
   "vertex_id": "string",
_19
   "target_id": "string",
_19
   "inputs": {},
_19
   "outputs": {},
_19
   "status": "string",
_19
   "error": "string",
_19
   "flow_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
_19
   "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
_19
  }
_19
 ],
_19
 "total": 0,
_19
 "page": 1,
_19
 "size": 1,
_19
 "pages": 0
_19
}
`
## Folders[​](https://docs.langflow.org/<#folders> "Direct link to Folders")
Use the `/folders` endpoint to create, read, update, and delete folders.
Folders store your flows and components.
### Read folders[​](https://docs.langflow.org/<#read-folders> "Direct link to Read folders")
Get a list of Langflow folders.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 '$LANGFLOW_URL/api/v1/folders/' \
3
 -H 'accept: application/json'
`
`
_10
[
_10
 {
_10
  "name": "My Projects",
_10
  "description": "Manage your own projects. Download and upload folders.",
_10
  "id": "1415de42-8f01-4f36-bf34-539f23e47466",
_10
  "parent_id": null
_10
 }
_10
]
`
### Create folder[​](https://docs.langflow.org/<#create-folder> "Direct link to Create folder")
Create a new folder.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/folders/" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "name": "new_folder_name",
7
 "description": "string",
8
 "components_list": [],
9
 "flows_list": []
10
}'
`
`
_10
{
_10
 "name": "new_folder_name",
_10
 "description": "string",
_10
 "id": "b408ddb9-6266-4431-9be8-e04a62758331",
_10
 "parent_id": null
_10
}
`
To add flows and components at folder creation, retrieve the `components_list` and `flows_list` values from the [/api/v1/store/components](https://docs.langflow.org/<#get-all-components>) and [/api/v1/flows/read](https://docs.langflow.org/<#read-flows>) endpoints and add them to the request body.
Adding a flow to a folder moves the flow from its previous location. The flow is not copied.
`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/folders/" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "name": "new_folder_name",
7
 "description": "string",
8
 "components_list": [
9
  "3fa85f64-5717-4562-b3fc-2c963f66afa6"
10
 ],
11
 "flows_list": [
12
  "3fa85f64-5717-4562-b3fc-2c963f66afa6"
13
 ]
14
}'
`
### Read folder[​](https://docs.langflow.org/<#read-folder> "Direct link to Read folder")
Retrieve details of a specific folder.
To find the UUID of your folder, call the [read folders](https://docs.langflow.org/<#read-folders>) endpoint.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 '$LANGFLOW_URL/api/v1/folders/$FOLDER_ID' \
3
 -H 'accept: application/json'
`
`
_10
[
_10
  {
_10
    "name": "My Projects",
_10
    "description": "Manage your own projects. Download and upload folders.",
_10
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
_10
    "parent_id": null
_10
  }
_10
]
`
### Update folder[​](https://docs.langflow.org/<#update-folder> "Direct link to Update folder")
Update the information of a specific folder with a `PATCH` request.
Each PATCH request updates the folder with the values you send. Only the fields you include in your request are updated. If you send the same values multiple times, the update is still processed, even if the values are unchanged.
  * curl
  * Result


`
1
curl -X 'PATCH' \
2
 '$LANGFLOW_URL/api/v1/folders/b408ddb9-6266-4431-9be8-e04a62758331' \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "name": "string",
7
 "description": "string",
8
 "parent_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
9
 "components": [
10
  "3fa85f64-5717-4562-b3fc-2c963f66afa6"
11
 ],
12
 "flows": [
13
  "3fa85f64-5717-4562-b3fc-2c963f66afa6"
14
 ]
15
}'
`
`
_10
{
_10
 "name": "string",
_10
 "description": "string",
_10
 "id": "b408ddb9-6266-4431-9be8-e04a62758331",
_10
 "parent_id": null
_10
}
`
### Delete folder[​](https://docs.langflow.org/<#delete-folder> "Direct link to Delete folder")
Delete a specific folder.
  * curl
  * Result


`
1
curl -X 'DELETE' \
2
 '$LANGFLOW_URL/api/v1/folders/$FOLDER_ID' \
3
 -H 'accept: */*'
`
`
_10
204 No Content
`
### Download folder[​](https://docs.langflow.org/<#download-folder> "Direct link to Download folder")
Download all flows from a folder as a zip file.
The `--output` flag is optional.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 '$LANGFLOW_URL/api/v1/folders/download/b408ddb9-6266-4431-9be8-e04a62758331' \
3
 -H 'accept: application/json' \
4
 --output langflow-folder.zip
`
`
_10
The folder contents.
`
### Upload folder[​](https://docs.langflow.org/<#upload-folder> "Direct link to Upload folder")
Upload a folder to Langflow.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 '$LANGFLOW_URL/api/v1/folders/upload/' \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: multipart/form-data' \
5
 -F 'file=@20241230_135006_langflow_flows.zip;type=application/zip'
`
`
_10
The folder contents are uploaded to Langflow.
`
## Files[​](https://docs.langflow.org/<#files> "Direct link to Files")
Use the `/files` endpoint to add or delete files between your local machine and Langflow.
### Upload file[​](https://docs.langflow.org/<#upload-file> "Direct link to Upload file")
Upload a file to an existing flow.
This example uploads `the_oscar_award.csv`.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 '$LANGFLOW_URL/api/v1/files/upload/$FLOW_ID' \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: multipart/form-data' \
5
 -F 'file=@the_oscar_award.csv'
`
`
_10
{
_10
 "flowId": "92f9a4c5-cfc8-4656-ae63-1f0881163c28",
_10
 "file_path": "92f9a4c5-cfc8-4656-ae63-1f0881163c28/2024-12-30_15-19-43_the_oscar_award.csv"
_10
}
`
#### Upload image files[​](https://docs.langflow.org/<#upload-image-files> "Direct link to Upload image files")
Send image files to the Langflow API for AI analysis.
The default file limit is 100 MB. To configure this value, change the `LANGFLOW_MAX_FILE_SIZE_UPLOAD` environment variable. For more information, see [Supported environment variables](https://docs.langflow.org/</environment-variables#supported-variables>).
  1. To send an image to your flow with the API, POST the image file to the `v1/files/upload/<YOUR-FLOW-ID>` endpoint of your flow.


`
1
curl -X POST "$LANGFLOW_URL/api/v1/files/upload/a430cc57-06bb-4c11-be39-d3d4de68d2c4" \
2
 -H "Content-Type: multipart/form-data" \
3
 -F "file=@image-file.png"
`
The API returns the image file path in the format `"file_path":"<YOUR-FLOW-ID>/<TIMESTAMP>_<FILE-NAME>"}`.
`
1
{"flowId":"a430cc57-06bb-4c11-be39-d3d4de68d2c4","file_path":"a430cc57-06bb-4c11-be39-d3d4de68d2c4/2024-11-27_14-47-50_image-file.png"}
`
  1. Post the image file to the **Chat Input** component of a **Basic prompting** flow. Pass the file path value as an input in the **Tweaks** section of the curl call to Langflow.


`
1
curl -X POST \
2
  "$LANGFLOW_URL/api/v1/run/a430cc57-06bb-4c11-be39-d3d4de68d2c4?stream=false" \
3
  -H 'Content-Type: application/json'\
4
  -d '{
5
  "output_type": "chat",
6
  "input_type": "chat",
7
  "tweaks": {
8
 "ChatInput-b67sL": {
9
  "files": "a430cc57-06bb-4c11-be39-d3d4de68d2c4/2024-11-27_14-47-50_image-file.png",
10
  "input_value": "what do you see?"
11
 }
12
}}'
`
Your chatbot describes the image file you sent.
`
1
"text": "This flowchart appears to represent a complex system for processing financial inquiries using various AI agents and tools. Here's a breakdown of its components and how they might work together..."
`
### List files[​](https://docs.langflow.org/<#list-files> "Direct link to List files")
List all files associated with a specific flow.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/files/list/$FLOW_ID" \
3
 -H 'accept: application/json'
`
`
_10
{
_10
 "files": [
_10
  "2024-12-30_15-19-43_the_oscar_award.csv"
_10
 ]
_10
}
`
### Download file[​](https://docs.langflow.org/<#download-file> "Direct link to Download file")
Download a specific file for a given flow.
To look up the file name in Langflow, use the `/list` endpoint.
This example downloads the `2024-12-30_15-19-43_the_oscar_award.csv` file from Langflow to a file named `output-file.csv`.
The `--output` flag is optional.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/files/download/$FLOW_ID/2024-12-30_15-19-43_the_oscar_award.csv" \
3
 -H 'accept: application/json' \
4
 --output output-file.csv
`
`
_10
The file contents.
`
### Download image[​](https://docs.langflow.org/<#download-image> "Direct link to Download image")
Download an image file for a given flow.
To look up the file name in Langflow, use the `/list` endpoint.
This example downloads the `2024-12-30_15-42-44_image-file.png` file from Langflow to a file named `output-image.png`.
The `--output` flag is optional.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/files/images/$FLOW_ID/2024-12-30_15-42-44_image-file.png" \
3
 -H 'accept: application/json' \
4
 --output output-image.png
`
`
_10
Image file content.
`
### Delete file[​](https://docs.langflow.org/<#delete-file> "Direct link to Delete file")
Delete a specific file from a flow.
This example deletes the `2024-12-30_15-42-44_image-file.png` file from Langflow.
  * curl
  * Result


`
1
curl -X 'DELETE' \
2
 "$LANGFLOW_URL/api/v1/files/delete/$FLOW_ID/2024-12-30_15-42-44_image-file.png" \
3
 -H 'accept: application/json'
`
`
_10
{
_10
 "message": "File 2024-12-30_15-42-44_image-file.png deleted successfully"
_10
}
`
## Logs[​](https://docs.langflow.org/<#logs> "Direct link to Logs")
Retrieve logs for your Langflow flow.
This endpoint requires log retrieval to be enabled in your Langflow application.
To enable log retrieval, include these values in your `.env` file:
`
1
LANGFLOW_ENABLE_LOG_RETRIEVAL=true
2
LANGFLOW_LOG_RETRIEVER_BUFFER_SIZE=10000
3
LANGFLOW_LOG_LEVEL=DEBUG
`
For log retrieval to function, `LANGFLOW_LOG_RETRIEVER_BUFFER_SIZE` needs to be greater than 0. The default value is `10000`.
Start Langflow with this `.env`:
`
1
uv run langflow run --env-file .env
`
### Stream logs[​](https://docs.langflow.org/<#stream-logs> "Direct link to Stream logs")
Stream logs in real-time using Server-Sent Events (SSE).
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/logs-stream" \
3
 -H 'accept: text/event-stream'
`
`
_17
keepalive
_17
_17
{"1736355791151": "2025-01-08T12:03:11.151218-0500 DEBUG Building Chat Input\n"}
_17
_17
{"1736355791485": "2025-01-08T12:03:11.485380-0500 DEBUG consumed event add_message-153bcd5d-ef4d-4ece-8cc0-47c6b6a9ef92 (time in queue, 0.0000, client 0.0001)\n"}
_17
_17
{"1736355791499": "2025-01-08T12:03:11.499704-0500 DEBUG consumed event end_vertex-3d7125cd-7b8a-44eb-9113-ed5b785e3cf3 (time in queue, 0.0056, client 0.0047)\n"}
_17
_17
{"1736355791502": "2025-01-08T12:03:11.502510-0500 DEBUG consumed event end-40d0b363-5618-4a23-bbae-487cd0b9594d (time in queue, 0.0001, client 0.0004)\n"}
_17
_17
{"1736355791513": "2025-01-08T12:03:11.513097-0500 DEBUG Logged vertex build: 729ff2f8-6b01-48c8-9ad0-3743c2af9e8a\n"}
_17
_17
{"1736355791834": "2025-01-08T12:03:11.834982-0500 DEBUG Telemetry data sent successfully.\n"}
_17
_17
{"1736355791941": "2025-01-08T12:03:11.941840-0500 DEBUG Telemetry data sent successfully.\n"}
_17
_17
keepalive
`
### Retrieve logs with optional parameters[​](https://docs.langflow.org/<#retrieve-logs-with-optional-parameters> "Direct link to Retrieve logs with optional parameters")
Retrieve logs with optional query parameters.
  * `lines_before`: The number of logs before the timestamp or the last log.
  * `lines_after`: The number of logs after the timestamp.
  * `timestamp`: The timestamp to start getting logs from.


The default values for all three parameters is `0`. With these values, the endpoint returns the last 10 lines of logs.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/logs?lines_before=0&lines_after=0&timestamp=0" \
3
 -H 'accept: application/json'
`
`
_12
{
_12
 "1736354770500": "2025-01-08T11:46:10.500363-0500 DEBUG Creating starter project Document Q&A\n",
_12
 "1736354770511": "2025-01-08T11:46:10.511146-0500 DEBUG Creating starter project Image Sentiment Analysis\n",
_12
 "1736354770521": "2025-01-08T11:46:10.521018-0500 DEBUG Creating starter project SEO Keyword Generator\n",
_12
 "1736354770532": "2025-01-08T11:46:10.532677-0500 DEBUG Creating starter project Sequential Tasks Agents\n",
_12
 "1736354770544": "2025-01-08T11:46:10.544010-0500 DEBUG Creating starter project Custom Component Generator\n",
_12
 "1736354770555": "2025-01-08T11:46:10.555513-0500 DEBUG Creating starter project Prompt Chaining\n",
_12
 "1736354770588": "2025-01-08T11:46:10.588105-0500 DEBUG Create service ServiceType.CHAT_SERVICE\n",
_12
 "1736354771021": "2025-01-08T11:46:11.021817-0500 DEBUG Telemetry data sent successfully.\n",
_12
 "1736354775619": "2025-01-08T11:46:15.619545-0500 DEBUG Create service ServiceType.STORE_SERVICE\n",
_12
 "1736354775699": "2025-01-08T11:46:15.699661-0500 DEBUG File 046-rocket.svg retrieved successfully from flow /Users/mendon.kissling/Library/Caches/langflow/profile_pictures/Space.\n"
_12
}
`
## Base[​](https://docs.langflow.org/<#base> "Direct link to Base")
Use the base Langflow API for running your flow and retrieving configuration information.
### Get all components[​](https://docs.langflow.org/<#get-all-components> "Direct link to Get all components")
This operation returns a dictionary of all Langflow components.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/all" \
3
 -H 'accept: application/json'
`
`
_10
A dictionary of all Langflow components.
`
### Run flow[​](https://docs.langflow.org/<#run-flow> "Direct link to Run flow")
Execute a specified flow by ID or name.
  * curl
  * Result


`
1
curl -X 'POST' \
2
 "$LANGFLOW_URL/api/v1/run/$FLOW_ID?stream=false" \
3
 -H 'accept: application/json' \
4
 -H 'Content-Type: application/json' \
5
 -d '{
6
 "input_value": "string",
7
 "input_type": "chat",
8
 "output_type": "chat",
9
 "output_component": "",
10
 "tweaks": {
11
  "Component Name": {
12
   "parameter_name": "value"
13
  },
14
  "component_id": {
15
   "parameter_name": "value"
16
  },
17
  "parameter_name": "value"
18
 },
19
 "session_id": "string"
20
}'
`
`
_10
{
_10
 "result": "Flow execution result",
_10
 "session_id": "session_uuid"
_10
}
`
### Webhook run flow[​](https://docs.langflow.org/<#webhook-run-flow> "Direct link to Webhook run flow")
The webhook endpoint triggers flow execution with an HTTP POST request.
  * curl
  * Result


`
1
curl -X POST \
2
 "$LANGFLOW_URL/api/v1/webhook/$FLOW_ID" \
3
 -H "Content-Type: application/json" \
4
 -d '{"path": "/tmp/test_file.txt"}'
`
`
_10
{
_10
 {"message":"Task started in the background","status":"in progress"}
_10
}
`
### Process[​](https://docs.langflow.org/<#process> "Direct link to Process")
info
This endpoint is deprecated. Use the `/run` endpoint instead.
### Predict[​](https://docs.langflow.org/<#predict> "Direct link to Predict")
info
This endpoint is deprecated. Use the `/run` endpoint instead.
### Get task status[​](https://docs.langflow.org/<#get-task-status> "Direct link to Get task status")
Get the status of a task.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/task/TASK_ID" \
3
 -H 'accept: application/json'
`
`
_10
{
_10
 "status": "Task status",
_10
 "result": "Task result if completed"
_10
}
`
### Create upload file (Deprecated)[​](https://docs.langflow.org/<#create-upload-file-deprecated> "Direct link to Create upload file \(Deprecated\)")
info
This endpoint is deprecated. Use the `/file` endpoint instead.
### Get version[​](https://docs.langflow.org/<#get-version> "Direct link to Get version")
Get the version of the Langflow API.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/version" \
3
 -H 'accept: application/json'
`
`
_10
{
_10
  "version": "1.1.1",
_10
  "main_version": "1.1.1",
_10
  "package": "Langflow"
_10
}
`
### Get config[​](https://docs.langflow.org/<#get-config> "Direct link to Get config")
Retrieve the Langflow configuration information.
  * curl
  * Result


`
1
curl -X 'GET' \
2
 "$LANGFLOW_URL/api/v1/config" \
3
 -H 'accept: application/json'
`
`
_10
{
_10
  "feature_flags": {
_10
    "mvp_components": false
_10
  },
_10
  "frontend_timeout": 0,
_10
  "auto_saving": true,
_10
  "auto_saving_interval": 1000,
_10
  "health_check_max_retries": 5,
_10
  "max_file_size_upload": 100
_10
}
`
[PreviousTelemetry](https://docs.langflow.org/</contributing-telemetry>)
  * [Export values (optional)](https://docs.langflow.org/<#export-values-optional>)
  * [Build](https://docs.langflow.org/<#build>)
    * [Build flow](https://docs.langflow.org/<#build-flow>)
  * [Flows](https://docs.langflow.org/<#flows>)
    * [Create flow](https://docs.langflow.org/<#create-flow>)
    * [Read flows](https://docs.langflow.org/<#read-flows>)
    * [Read flow](https://docs.langflow.org/<#read-flow>)
    * [Update flow](https://docs.langflow.org/<#update-flow>)
    * [Delete flow](https://docs.langflow.org/<#delete-flow>)
    * [Create flows](https://docs.langflow.org/<#create-flows>)
    * [Upload flows](https://docs.langflow.org/<#upload-flows>)
    * [Download all flows](https://docs.langflow.org/<#download-all-flows>)
    * [Read basic examples](https://docs.langflow.org/<#read-basic-examples>)
  * [Monitor](https://docs.langflow.org/<#monitor>)
    * [Get Vertex builds](https://docs.langflow.org/<#get-vertex-builds>)
    * [Delete Vertex builds](https://docs.langflow.org/<#delete-vertex-builds>)
    * [Get messages](https://docs.langflow.org/<#get-messages>)
    * [Delete messages](https://docs.langflow.org/<#delete-messages>)
    * [Update message](https://docs.langflow.org/<#update-message>)
    * [Update session ID](https://docs.langflow.org/<#update-session-id>)
    * [Delete messages by session](https://docs.langflow.org/<#delete-messages-by-session>)
    * [Get transactions](https://docs.langflow.org/<#get-transactions>)
  * [Folders](https://docs.langflow.org/<#folders>)
    * [Read folders](https://docs.langflow.org/<#read-folders>)
    * [Create folder](https://docs.langflow.org/<#create-folder>)
    * [Read folder](https://docs.langflow.org/<#read-folder>)
    * [Update folder](https://docs.langflow.org/<#update-folder>)
    * [Delete folder](https://docs.langflow.org/<#delete-folder>)
    * [Download folder](https://docs.langflow.org/<#download-folder>)
    * [Upload folder](https://docs.langflow.org/<#upload-folder>)
  * [Files](https://docs.langflow.org/<#files>)
    * [Upload file](https://docs.langflow.org/<#upload-file>)
    * [List files](https://docs.langflow.org/<#list-files>)
    * [Download file](https://docs.langflow.org/<#download-file>)
    * [Download image](https://docs.langflow.org/<#download-image>)
    * [Delete file](https://docs.langflow.org/<#delete-file>)
  * [Logs](https://docs.langflow.org/<#logs>)
    * [Stream logs](https://docs.langflow.org/<#stream-logs>)
    * [Retrieve logs with optional parameters](https://docs.langflow.org/<#retrieve-logs-with-optional-parameters>)
  * [Base](https://docs.langflow.org/<#base>)
    * [Get all components](https://docs.langflow.org/<#get-all-components>)
    * [Run flow](https://docs.langflow.org/<#run-flow>)
    * [Webhook run flow](https://docs.langflow.org/<#webhook-run-flow>)
    * [Process](https://docs.langflow.org/<#process>)
    * [Predict](https://docs.langflow.org/<#predict>)
    * [Get task status](https://docs.langflow.org/<#get-task-status>)
    * [Create upload file (Deprecated)](https://docs.langflow.org/<#create-upload-file-deprecated>)
    * [Get version](https://docs.langflow.org/<#get-version>)
    * [Get config](https://docs.langflow.org/<#get-config>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b82a4449-db66-44a5-93df-22c8d810334a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=63e1f583-bfa0-4a53-929a-d804dd47bcd8&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi-reference-api-examples&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b82a4449-db66-44a5-93df-22c8d810334a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=63e1f583-bfa0-4a53-929a-d804dd47bcd8&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi-reference-api-examples&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
