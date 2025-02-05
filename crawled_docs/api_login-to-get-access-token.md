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
  * [Users](https://docs.langflow.org/api/</api/add-user>)
  * [APIKey](https://docs.langflow.org/api/</api/get-api-keys-route>)
  * [Login](https://docs.langflow.org/api/</api/login-to-get-access-token>)
    * [Login To Get Access Token](https://docs.langflow.org/api/</api/login-to-get-access-token>)
    * [Auto Login](https://docs.langflow.org/api/</api/auto-login>)
    * [Refresh Token](https://docs.langflow.org/api/</api/refresh-token>)
    * [Logout](https://docs.langflow.org/api/</api/logout>)
  * [Variables](https://docs.langflow.org/api/</api/read-variables>)
  * [Files](https://docs.langflow.org/api/</api/upload-file-1>)
  * [Monitor](https://docs.langflow.org/api/</api/get-vertex-builds>)
  * [Folders](https://docs.langflow.org/api/</api/read-folders>)
  * [mcp](https://docs.langflow.org/api/</api/handle-sse>)
  * [Health Check](https://docs.langflow.org/api/</api/health>)
  * [Log](https://docs.langflow.org/api/</api/stream-logs>)


# Login To Get Access Token
Login To Get Access Token
Request Body  — **REQUIRED**  
---  
`grant_type` Grant Type  
`username` Username — **REQUIRED**  
`password` Password — **REQUIRED**  
`scope` Scope  
`client_id` Client Id  
`client_secret` Client Secret  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
`access_token` Access Token  
`refresh_token` Refresh Token  
`token_type` Token Type  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousSave Store Api Key](https://docs.langflow.org/api/</api/save-store-api-key>)[NextAuto Login](https://docs.langflow.org/api/</api/auto-login>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
