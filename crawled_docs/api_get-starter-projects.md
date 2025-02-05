[Skip to main content](https://docs.langflow.org/api/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/api/</>)
[](https://docs.langflow.org/api/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/api/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/api/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/api/</>)
  * [Chat](https://docs.langflow.org/api/</api/retrieve-vertices-order>)
  * [Base](https://docs.langflow.org/api/</api/get-all>)
  * [Validate](https://docs.langflow.org/api/</api/post-validate-code>)
  * [Components Store](https://docs.langflow.org/api/</api/check-if-store-is-enabled>)
  * [Flows](https://docs.langflow.org/api/</api/create-flow>)
    * [Create Flow](https://docs.langflow.org/api/</api/create-flow>)
    * [Read Flows](https://docs.langflow.org/api/</api/read-flows>)
    * [Delete Multiple Flows](https://docs.langflow.org/api/</api/delete-multiple-flows>)
    * [Read Flow](https://docs.langflow.org/api/</api/read-flow>)
    * [Update Flow](https://docs.langflow.org/api/</api/update-flow>)
    * [Delete Flow](https://docs.langflow.org/api/</api/delete-flow>)
    * [Create Flows](https://docs.langflow.org/api/</api/create-flows>)
    * [Upload File](https://docs.langflow.org/api/</api/upload-file>)
    * [Download Multiple File](https://docs.langflow.org/api/</api/download-multiple-file>)
    * [Read Basic Examples](https://docs.langflow.org/api/</api/read-basic-examples>)
    * [Get Starter Projects](https://docs.langflow.org/api/</api/get-starter-projects>)
  * [Users](https://docs.langflow.org/api/</api/add-user>)
  * [APIKey](https://docs.langflow.org/api/</api/get-api-keys-route>)
  * [Login](https://docs.langflow.org/api/</api/login-to-get-access-token>)
  * [Variables](https://docs.langflow.org/api/</api/read-variables>)
  * [Files](https://docs.langflow.org/api/</api/upload-file-1>)
  * [Monitor](https://docs.langflow.org/api/</api/get-vertex-builds>)
  * [Folders](https://docs.langflow.org/api/</api/read-folders>)
  * [mcp](https://docs.langflow.org/api/</api/handle-sse>)
  * [Health Check](https://docs.langflow.org/api/</api/health>)
  * [Log](https://docs.langflow.org/api/</api/stream-logs>)


# Get Starter Projects
Get a list of starter projects.
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
object[]| `data` object — **OPTIONAL**| `nodes` object[]| `id` Id  
---  
`data` object  
`dragging` Dragging — **OPTIONAL**  
`height` Height — **OPTIONAL**  
`width` Width — **OPTIONAL**  
`position` object — **OPTIONAL**| `x` X  
---  
`y` Y  
`positionAbsolute` object — **OPTIONAL**| `x` X  
---  
`y` Y  
`selected` Selected — **OPTIONAL**  
`parent_node_id` Parent Node Id — **OPTIONAL**  
`type` NodeTypeEnum — **OPTIONAL****Possible values:** [`noteNode`, `genericNode`]  
`edges` object[]| `source` Source — **OPTIONAL**  
---  
`target` Target — **OPTIONAL**  
`data` object — **OPTIONAL**| `sourceHandle` object| `baseClasses` string[] — **OPTIONAL**  
---  
`dataType` Datatype — **OPTIONAL**  
`id` Id — **OPTIONAL**  
`name` Name — **OPTIONAL**  
`output_types` string[] — **OPTIONAL**  
`targetHandle` object| `fieldName` Fieldname  
---  
`id` Id  
`inputTypes` Inputtypes  
`type` Type  
`viewport` object — **OPTIONAL**| `x` X  
---  
`y` Y  
`zoom` Zoom  
`is_component` Is Component — **OPTIONAL**  
`name` Name — **OPTIONAL**  
`description` Description — **OPTIONAL**  
`endpoint_name` Endpoint Name — **OPTIONAL**  
[ PreviousUpload File](https://docs.langflow.org/api/</api/upload-file-2>)[NextHandle Sse](https://docs.langflow.org/api/</api/handle-sse>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
