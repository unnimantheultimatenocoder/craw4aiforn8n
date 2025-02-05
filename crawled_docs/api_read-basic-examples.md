[Skip to main content](https://docs.langflow.org/api/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/api/</>)
[](https://docs.langflow.org/api/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/api/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/api/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/api/</>)
  * [Chat](https://docs.langflow.org/api/<#>)
  * [Base](https://docs.langflow.org/api/<#>)
  * [Validate](https://docs.langflow.org/api/<#>)
  * [Components Store](https://docs.langflow.org/api/<#>)
  * [Flows](https://docs.langflow.org/api/<#>)
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
  * [Users](https://docs.langflow.org/api/<#>)
  * [APIKey](https://docs.langflow.org/api/<#>)
  * [Login](https://docs.langflow.org/api/<#>)
  * [Variables](https://docs.langflow.org/api/<#>)
  * [Files](https://docs.langflow.org/api/<#>)
  * [Monitor](https://docs.langflow.org/api/<#>)
  * [Folders](https://docs.langflow.org/api/<#>)
  * [mcp](https://docs.langflow.org/api/<#>)
  * [Health Check](https://docs.langflow.org/api/<#>)
  * [Log](https://docs.langflow.org/api/<#>)


# Read Basic Examples
Retrieve a list of basic example flows.
Args: session (Session): The database session.
Returns: list[FlowRead]: A list of basic example flows.
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
object[]| `name` Name  
---  
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
[PreviousDownload Multiple File](https://docs.langflow.org/api/</api/download-multiple-file>)[NextAdd User](https://docs.langflow.org/api/</api/add-user>)
`**read_basic_examples_api_v1_flows_basic_examples__get**`
```
GET /api/v1/flows/basic_examples/
```

cURL NodeGoPython
Copy```
curl-L'https://docs.langflow.org/api/v1/flows/basic_examples/'\
-H'Accept: application/json'

```

Execute
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=3c043a4f-2e05-4d0d-9494-8f1fee1ca874&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1f469b00-d0e7-4825-9d8c-7e4ad1d74a07&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fread-basic-examples&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=3c043a4f-2e05-4d0d-9494-8f1fee1ca874&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1f469b00-d0e7-4825-9d8c-7e4ad1d74a07&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fread-basic-examples&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
