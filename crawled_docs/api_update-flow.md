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
    * [Create Flow](https://docs.langflow.org/api/</api/create-flow>)
    * [Read Flows](https://docs.langflow.org/api/</api/read-flows>)
    * [Delete Multiple Flows](https://docs.langflow.org/api/</api/delete-multiple-flows>)
    * [Read Flow](https://docs.langflow.org/api/</api/read-flow>)
    * [Update Flow](https://docs.langflow.org/api/</api/update-flow>)
    * [Delete Flow](https://docs.langflow.org/api/</api/delete-flow>)
    * [Create Flows](https://docs.langflow.org/api/</api/create-flows>)
    * [Upload File](https://docs.langflow.org/api/</api/upload-file>)
    * [Download Multiple File](https://docs.langflow.org/api/</api/download-multiple-file>)
    * [Read Basic Examples](https://docs.langflow.org/api/</api/read-basic-examples>)
    * [Get Starter Projects](https://docs.langflow.org/api/</api/get-starter-projects>)
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


# Update Flow
Update a flow.
Path Parameters  
---  
`flow_id` uuid — **REQUIRED**  
Request Body  — **REQUIRED**  
---  
`name` Name  
`description` Description  
`data` Data  
`folder_id` Folder Id  
`endpoint_name` Endpoint Name  
`locked` Locked  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
`name` Name  
`description` Description — **OPTIONAL**  
`icon` Icon — **OPTIONAL**  
`icon_bg_color` Icon Bg Color — **OPTIONAL**  
`gradient` Gradient — **OPTIONAL**  
`data` Data — **OPTIONAL**  
`is_component` Is Component — **OPTIONAL**  
`updated_at` Updated At — **OPTIONAL**  
`webhook` Webhook — **OPTIONAL** Can be used on the webhook endpoint  
`endpoint_name` Endpoint Name — **OPTIONAL**  
`tags` Tags — **OPTIONAL**  
`locked` Locked — **OPTIONAL**  
`id` uuid  
`user_id` User Id  
`folder_id` Folder Id  
`422`Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousRead Flow](https://docs.langflow.org/api/</api/read-flow>)[NextDelete Flow](https://docs.langflow.org/api/</api/delete-flow>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4227d606-b63e-48f1-9341-b5c3eb3e6d54&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=98b6ead8-cc4d-41a9-95ce-d216b1ee25b7&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fupdate-flow&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4227d606-b63e-48f1-9341-b5c3eb3e6d54&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=98b6ead8-cc4d-41a9-95ce-d216b1ee25b7&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fupdate-flow&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
