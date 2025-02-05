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


# Build Vertex Stream
Build a vertex instead of the entire graph.
This function is responsible for building a single vertex instead of the entire graph. It takes the `flow_id` and `vertex_id` as required parameters, and an optional `session_id`. It also depends on the `ChatService` and `SessionService` services.
If `session_id` is not provided, it retrieves the graph from the cache using the `chat_service`. If `session_id` is provided, it loads the session data using the `session_service`.
Once the graph is obtained, it retrieves the specified vertex using the `vertex_id`. If the vertex does not support streaming, an error is raised. If the vertex has a built result, it sends the result as a chunk. If the vertex is not frozen or not built, it streams the vertex data. If the vertex has a result, it sends the result as a chunk. If none of the above conditions are met, an error is raised.
If any exception occurs during the process, an error message is sent. Finally, the stream is closed.
Returns: A `StreamingResponse` object with the streamed vertex data in text/event-stream format.
Raises: HTTPException: If an error occurs while building the vertex.
Path Parameters  
---  
`flow_id` uuid — **REQUIRED**  
`vertex_id` Vertex Id — **REQUIRED**  
Responses  
---  
`200`Successful Response  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousBuild Vertex](https://docs.langflow.org/api/</api/build-vertex>)[NextGet All](https://docs.langflow.org/api/</api/get-all>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
