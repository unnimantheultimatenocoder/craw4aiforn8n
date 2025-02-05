[Skip to main content](https://docs.langflow.org/api/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/api/</>)
[](https://docs.langflow.org/api/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/api/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/api/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/api/</>)
  * [Chat](https://docs.langflow.org/api/</api/retrieve-vertices-order>)
  * [Base](https://docs.langflow.org/api/</api/get-all>)
    * [Get All](https://docs.langflow.org/api/</api/get-all>)
    * [Simplified Run Flow](https://docs.langflow.org/api/</api/simplified-run-flow>)
    * [Webhook Run Flow](https://docs.langflow.org/api/</api/webhook-run-flow>)
    * [Experimental Run Flow](https://docs.langflow.org/api/</api/experimental-run-flow>)
    * [Process](https://docs.langflow.org/api/</api/process>)
    * [Process](https://docs.langflow.org/api/</api/process-1>)
    * [Get Task Status](https://docs.langflow.org/api/</api/get-task-status>)
    * [Create Upload File](https://docs.langflow.org/api/</api/create-upload-file>)
    * [Get Version](https://docs.langflow.org/api/</api/get-version>)
    * [Custom Component](https://docs.langflow.org/api/</api/custom-component>)
    * [Custom Component Update](https://docs.langflow.org/api/</api/custom-component-update>)
    * [Get Config](https://docs.langflow.org/api/</api/get-config>)
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


# Simplified Run Flow
Executes a specified flow by ID with support for streaming and telemetry.
This endpoint executes a flow identified by ID or name, with options for streaming the response and tracking execution metrics. It handles both streaming and non-streaming execution modes.
Args: background_tasks (BackgroundTasks): FastAPI background task manager flow (FlowRead | None): The flow to execute, loaded via dependency input_request (SimplifiedAPIRequest | None): Input parameters for the flow stream (bool): Whether to stream the response api_key_user (UserRead): Authenticated user from API key request (Request): The incoming HTTP request
Returns: Union[StreamingResponse, RunResponse]: Either a streaming response for real-time results or a RunResponse with the complete execution results
Raises: HTTPException: For flow not found (404) or invalid input (400) APIException: For internal execution errors (500)
Notes:
  * Supports both streaming and non-streaming execution modes
  * Tracks execution time and success/failure via telemetry
  * Handles graceful client disconnection in streaming mode
  * Provides detailed error handling with appropriate HTTP status codes
  * In streaming mode, uses EventManager to handle events: 
    * "add_message": New messages during execution
    * "token": Individual tokens during streaming
    * "end": Final execution result

Path Parameters  
---  
`flow_id_or_name` Flow Id Or Name — **REQUIRED**  
Query Parameters  
---  
`stream` Stream  
`user_id` User Id  
Request Body   
---  
undefined  
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
[PreviousGet All](https://docs.langflow.org/api/</api/get-all>)[NextWebhook Run Flow](https://docs.langflow.org/api/</api/webhook-run-flow>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
