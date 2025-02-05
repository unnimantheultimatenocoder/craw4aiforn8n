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


# Custom Component Update
Update a custom component with the provided code request.
This endpoint generates the CustomComponentFrontendNode normally but then runs the `update_build_config` method on the latest version of the template. This ensures that every time it runs, it has the latest version of the template.
Args: code_request (CustomComponentRequest): The code request containing the updated code for the custom component. user (User, optional): The user making the request. Defaults to the current active user.
Returns: dict: The updated custom component node.
Raises: HTTPException: If there's an error building or updating the component SerializationError: If there's an error serializing the component to JSON
Request Body  — **REQUIRED**  
---  
`code` Code — **REQUIRED**  
`frontend_node` Frontend Node  
`field` Field — **REQUIRED**  
`field_value` Field Value  
`template` object — **REQUIRED**  
`tool_mode` Tool Mode  
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
[PreviousCustom Component](https://docs.langflow.org/api/</api/custom-component>)[NextGet Config](https://docs.langflow.org/api/</api/get-config>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
