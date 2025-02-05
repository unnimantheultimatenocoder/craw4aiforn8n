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


# Build Vertex
Build a vertex instead of the entire graph.
Args: flow_id (str): The ID of the flow. vertex_id (str): The ID of the vertex to build. background_tasks (BackgroundTasks): The background tasks dependency. inputs (Optional[InputValueRequest], optional): The input values for the vertex. Defaults to None. files (List[str], optional): The files to use. Defaults to None. current_user (Any, optional): The current user dependency. Defaults to Depends(get_current_active_user).
Returns: VertexBuildResponse: The response containing the built vertex information.
Raises: HTTPException: If there is an error building the vertex.
Path Parameters  
---  
`flow_id` uuid — **REQUIRED**  
`vertex_id` Vertex Id — **REQUIRED**  
Request Body   
---  
`inputs`  
`files` Files  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
`id` Id — **OPTIONAL**  
`inactivated_vertices` Inactivated Vertices — **OPTIONAL**  
`next_vertices_ids` Next Vertices Ids — **OPTIONAL**  
`top_level_vertices` Top Level Vertices — **OPTIONAL**  
`valid` Valid  
`params` Params — **OPTIONAL**  
`data` object  
`timestamp` Timestamp — **OPTIONAL**  
`422` Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousBuild Flow](https://docs.langflow.org/api/</api/build-flow>)[NextBuild Vertex Stream](https://docs.langflow.org/api/</api/build-vertex-stream>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
