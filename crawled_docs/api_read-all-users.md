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
    * [Add User](https://docs.langflow.org/api/</api/add-user>)
    * [Read All Users](https://docs.langflow.org/api/</api/read-all-users>)
    * [Read Current User](https://docs.langflow.org/api/</api/read-current-user>)
    * [Patch User](https://docs.langflow.org/api/</api/patch-user>)
    * [Delete User](https://docs.langflow.org/api/</api/delete-user>)
    * [Reset Password](https://docs.langflow.org/api/</api/reset-password>)
  * [APIKey](https://docs.langflow.org/api/</api/get-api-keys-route>)
  * [Login](https://docs.langflow.org/api/</api/login-to-get-access-token>)
  * [Variables](https://docs.langflow.org/api/</api/read-variables>)
  * [Files](https://docs.langflow.org/api/</api/upload-file-1>)
  * [Monitor](https://docs.langflow.org/api/</api/get-vertex-builds>)
  * [Folders](https://docs.langflow.org/api/</api/read-folders>)
  * [mcp](https://docs.langflow.org/api/</api/handle-sse>)
  * [Health Check](https://docs.langflow.org/api/</api/health>)
  * [Log](https://docs.langflow.org/api/</api/stream-logs>)


# Read All Users
Retrieve a list of users from the database with pagination.
Query Parameters  
---  
`skip` Skip  
`limit` Limit  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
`total_count` Total Count  
`users` object[]| `id` uuid — **OPTIONAL**  
---  
`username` Username  
`profile_image` Profile Image  
`store_api_key` Store Api Key  
`is_active` Is Active  
`is_superuser` Is Superuser  
`create_at` date-time  
`updated_at` date-time  
`last_login_at` Last Login At  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousAdd User](https://docs.langflow.org/api/</api/add-user>)[NextRead Current User](https://docs.langflow.org/api/</api/read-current-user>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
