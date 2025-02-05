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
    * [Upload File](https://docs.langflow.org/api/</api/upload-file-1>)
    * [Download File](https://docs.langflow.org/api/</api/download-file>)
    * [Download Image](https://docs.langflow.org/api/</api/download-image>)
    * [Download Profile Picture](https://docs.langflow.org/api/</api/download-profile-picture>)
    * [List Profile Pictures](https://docs.langflow.org/api/</api/list-profile-pictures>)
    * [List Files](https://docs.langflow.org/api/</api/list-files>)
    * [Delete File](https://docs.langflow.org/api/</api/delete-file>)
  * [Monitor](https://docs.langflow.org/api/</api/get-vertex-builds>)
  * [Folders](https://docs.langflow.org/api/</api/read-folders>)
  * [mcp](https://docs.langflow.org/api/</api/handle-sse>)
  * [Health Check](https://docs.langflow.org/api/</api/health>)
  * [Log](https://docs.langflow.org/api/</api/stream-logs>)


# List Files
List Files
Path Parameters  
---  
`flow_id` uuid — **REQUIRED**  
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
[PreviousList Profile Pictures](https://docs.langflow.org/api/</api/list-profile-pictures>)[NextDelete File](https://docs.langflow.org/api/</api/delete-file>)
Authorize
`**list_files_api_v1_files_list__flow_id__get**`
```
GET /api/v1/files/list/:flow_id
```

`flow_id`— path
cURLNodeGoPython
Copy
Execute
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e1a8afa9-1ce0-45f7-a30c-c7213d6d1db6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=70f29cd3-6483-49a6-9c6b-087e8e1604eb&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Flist-files&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e1a8afa9-1ce0-45f7-a30c-c7213d6d1db6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=70f29cd3-6483-49a6-9c6b-087e8e1604eb&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Flist-files&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
