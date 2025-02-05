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
  * [Variables](https://docs.langflow.org/api/</api/read-variables>)
  * [Files](https://docs.langflow.org/api/</api/upload-file-1>)
  * [Monitor](https://docs.langflow.org/api/</api/get-vertex-builds>)
  * [Folders](https://docs.langflow.org/api/</api/read-folders>)
    * [Read Folders](https://docs.langflow.org/api/</api/read-folders>)
    * [Create Folder](https://docs.langflow.org/api/</api/create-folder>)
    * [Read Folder](https://docs.langflow.org/api/</api/read-folder>)
    * [Update Folder](https://docs.langflow.org/api/</api/update-folder>)
    * [Delete Folder](https://docs.langflow.org/api/</api/delete-folder>)
    * [Download File](https://docs.langflow.org/api/</api/download-file-1>)
    * [Upload File](https://docs.langflow.org/api/</api/upload-file-2>)
  * [mcp](https://docs.langflow.org/api/</api/handle-sse>)
  * [Health Check](https://docs.langflow.org/api/</api/health>)
  * [Log](https://docs.langflow.org/api/</api/stream-logs>)


# Create Folder
Create Folder
Request Body  — **REQUIRED**  
---  
`name` Name — **REQUIRED**  
`description` Description  
`components_list` Components List  
`flows_list` Flows List  
Responses  
---  
`201`Successful Response| Schema  — **OPTIONAL**  
---  
`name` Name  
`description` Description — **OPTIONAL**  
`id` uuid  
`parent_id` Parent Id  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousRead Folders](https://docs.langflow.org/api/</api/read-folders>)[NextRead Folder](https://docs.langflow.org/api/</api/read-folder>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
