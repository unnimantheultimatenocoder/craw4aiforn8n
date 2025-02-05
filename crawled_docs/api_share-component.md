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
    * [Check If Store Is Enabled](https://docs.langflow.org/api/</api/check-if-store-is-enabled>)
    * [Check If Store Has Api Key](https://docs.langflow.org/api/</api/check-if-store-has-api-key>)
    * [Share Component](https://docs.langflow.org/api/</api/share-component>)
    * [Get Components](https://docs.langflow.org/api/</api/get-components>)
    * [Update Shared Component](https://docs.langflow.org/api/</api/update-shared-component>)
    * [Download Component](https://docs.langflow.org/api/</api/download-component>)
    * [Get Tags](https://docs.langflow.org/api/</api/get-tags>)
    * [Get List Of Components Liked By User](https://docs.langflow.org/api/</api/get-list-of-components-liked-by-user>)
    * [Like Component](https://docs.langflow.org/api/</api/like-component>)
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


# Share Component
Share Component
Request Body  — **REQUIRED**  
---  
`name` Name — **REQUIRED**  
`description` Description — **REQUIRED**  
`data` object — **REQUIRED**  
`tags` Tags — **REQUIRED**  
`parent` Parent  
`is_component` Is Component — **REQUIRED**  
`last_tested_version` Last Tested Version  
`private` Private  
Responses  
---  
`201`Successful Response| Schema  — **OPTIONAL**  
---  
`id` uuid  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousCheck If Store Has Api Key](https://docs.langflow.org/api/</api/check-if-store-has-api-key>)[NextGet Components](https://docs.langflow.org/api/</api/get-components>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
