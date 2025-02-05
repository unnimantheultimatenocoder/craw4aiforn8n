[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
  * [Chat](https://docs.langflow.org/</api/retrieve-vertices-order>)
    * [Retrieve Vertices Order](https://docs.langflow.org/</api/retrieve-vertices-order>)
    * [Build Flow](https://docs.langflow.org/</api/build-flow>)
    * [Build Vertex](https://docs.langflow.org/</api/build-vertex>)
    * [Build Vertex Stream](https://docs.langflow.org/</api/build-vertex-stream>)
  * [Base](https://docs.langflow.org/</api/get-all>)
  * [Validate](https://docs.langflow.org/</api/post-validate-code>)
  * [Components Store](https://docs.langflow.org/</api/check-if-store-is-enabled>)
  * [Flows](https://docs.langflow.org/</api/create-flow>)
  * [Users](https://docs.langflow.org/</api/add-user>)
  * [APIKey](https://docs.langflow.org/</api/get-api-keys-route>)
  * [Login](https://docs.langflow.org/</api/login-to-get-access-token>)
  * [Variables](https://docs.langflow.org/</api/read-variables>)
  * [Files](https://docs.langflow.org/</api/upload-file-1>)
  * [Monitor](https://docs.langflow.org/</api/get-vertex-builds>)
  * [Folders](https://docs.langflow.org/</api/read-folders>)
  * [mcp](https://docs.langflow.org/</api/handle-sse>)
  * [Health Check](https://docs.langflow.org/</api/health>)
  * [Log](https://docs.langflow.org/</api/stream-logs>)


# Retrieve Vertices Order
Retrieve the vertices order for a given flow.
Args: flow_id (str): The ID of the flow. background_tasks (BackgroundTasks): The background tasks. data (Optional[FlowDataRequest], optional): The flow data. Defaults to None. stop_component_id (str, optional): The ID of the stop component. Defaults to None. start_component_id (str, optional): The ID of the start component. Defaults to None. session (AsyncSession, optional): The session dependency.
Returns: VerticesOrderResponse: The response containing the ordered vertex IDs and the run ID.
Raises: HTTPException: If there is an error checking the build status.
Path Parameters  
---  
`flow_id` uuid — **REQUIRED**  
Query Parameters  
---  
`data` Data  
`stop_component_id` Stop Component Id  
`start_component_id` Start Component Id  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
`ids` string[]  
`run_id` uuid  
`vertices_to_run` string[]  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[NextBuild Flow](https://docs.langflow.org/</api/build-flow>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
