[Skip to main content](https://docs.langflow.org/api/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/api/</>)
[](https://docs.langflow.org/api/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/api/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/api/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/api/</>)
  * [Chat](https://docs.langflow.org/api/</api/retrieve-vertices-order>)
    * [Retrieve Vertices Order](https://docs.langflow.org/api/</api/retrieve-vertices-order>)
    * [Build Flow](https://docs.langflow.org/api/</api/build-flow>)
    * [Build Vertex](https://docs.langflow.org/api/</api/build-vertex>)
    * [Build Vertex Stream](https://docs.langflow.org/api/</api/build-vertex-stream>)
  * [Base](https://docs.langflow.org/api/</api/get-all>)
  * [Validate](https://docs.langflow.org/api/</api/post-validate-code>)
  * [Components Store](https://docs.langflow.org/api/</api/check-if-store-is-enabled>)
  * [Flows](https://docs.langflow.org/api/</api/create-flow>)
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


# Build Flow
Build Flow
Path Parameters  
---  
`flow_id` uuid — **REQUIRED**  
Query Parameters  
---  
`stop_component_id` Stop Component Id  
`start_component_id` Start Component Id  
`log_builds` Log Builds  
Request Body   
---  
`inputs`  
`data`  
`files` Files  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
undefined  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousRetrieve Vertices Order](https://docs.langflow.org/api/</api/retrieve-vertices-order>)[NextBuild Vertex](https://docs.langflow.org/api/</api/build-vertex>)
Authorize
`**build_flow_api_v1_build__flow_id__flow_post**`
```
POST /api/v1/build/:flow_id/flow
```

`flow_id`— path
Show optional parameters
`stop_component_id` — query
`start_component_id` — query
`log_builds` — query
`Body`
Loading...
cURLNodeGoPython
Copy
Execute
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d4fb74e2-56dc-4a2c-b565-2b586678cc50&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=fad84b55-77ec-4a01-ba16-023797b128c8&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fbuild-flow&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=d4fb74e2-56dc-4a2c-b565-2b586678cc50&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=fad84b55-77ec-4a01-ba16-023797b128c8&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fbuild-flow&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
