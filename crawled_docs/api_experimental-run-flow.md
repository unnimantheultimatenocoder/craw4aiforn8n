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


# Experimental Run Flow
Executes a specified flow by ID with optional input values, output selection, tweaks, and streaming capability.
This endpoint supports running flows with caching to enhance performance and efficiency.
### Parameters:[​](https://docs.langflow.org/api/<#parameters> "Direct link to Parameters:")
  * `flow_id` (str): The unique identifier of the flow to be executed.
  * `inputs` (List[InputValueRequest], optional): A list of inputs specifying the input values and components for the flow. Each input can target specific components and provide custom values.
  * `outputs` (List[str], optional): A list of output names to retrieve from the executed flow. If not provided, all outputs are returned.
  * `tweaks` (Optional[Tweaks], optional): A dictionary of tweaks to customize the flow execution. The tweaks can be used to modify the flow's parameters and components. Tweaks can be overridden by the input values.
  * `stream` (bool, optional): Specifies whether the results should be streamed. Defaults to False.
  * `session_id` (Union[None, str], optional): An optional session ID to utilize existing session data for the flow execution.
  * `api_key_user` (User): The user associated with the current API key. Automatically resolved from the API key.


### Returns:[​](https://docs.langflow.org/api/<#returns> "Direct link to Returns:")
A `RunResponse` object containing the selected outputs (or all if not specified) of the executed flow and the session ID. The structure of the response accommodates multiple inputs, providing a nested list of outputs for each input.
### Raises:[​](https://docs.langflow.org/api/<#raises> "Direct link to Raises:")
HTTPException: Indicates issues with finding the specified flow, invalid input formats, or internal errors during flow execution.
### Example usage:[​](https://docs.langflow.org/api/<#example-usage> "Direct link to Example usage:")
```
POST /run/{flow_id}x-api-key: YOUR_API_KEYPayload:{"inputs":[{"components":["component1"],"input_value":"value1"},{"components":["component3"],"input_value":"value2"}],"outputs":["Component Name","component_id"],"tweaks":{"parameter_name":"value","Component Name":{"parameter_name":"value"},"component_id":{"parameter_name":"value"}}"stream":false}
```

This endpoint facilitates complex flow executions with customized inputs, outputs, and configurations, catering to diverse application requirements.
Path Parameters  
---  
`flow_id` uuid — **REQUIRED**  
Request Body   
---  
`inputs` Inputs  
`outputs` Outputs  
`tweaks`  
`stream` Stream  
`session_id` Session Id  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
`outputs` Outputs — **OPTIONAL**  
`session_id` Session Id — **OPTIONAL**  
`422` Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousWebhook Run Flow](https://docs.langflow.org/api/</api/webhook-run-flow>)[NextProcess](https://docs.langflow.org/api/</api/process>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
