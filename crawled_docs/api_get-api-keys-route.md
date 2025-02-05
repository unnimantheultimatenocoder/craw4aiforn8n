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
  * [Users](https://docs.langflow.org/api/<#>)
  * [APIKey](https://docs.langflow.org/api/<#>)
    * [Get Api Keys Route](https://docs.langflow.org/api/</api/get-api-keys-route>)
    * [Create Api Key Route](https://docs.langflow.org/api/</api/create-api-key-route>)
    * [Delete Api Key Route](https://docs.langflow.org/api/</api/delete-api-key-route>)
    * [Save Store Api Key](https://docs.langflow.org/api/</api/save-store-api-key>)
  * [Login](https://docs.langflow.org/api/<#>)
  * [Variables](https://docs.langflow.org/api/<#>)
  * [Files](https://docs.langflow.org/api/<#>)
  * [Monitor](https://docs.langflow.org/api/<#>)
  * [Folders](https://docs.langflow.org/api/<#>)
  * [mcp](https://docs.langflow.org/api/<#>)
  * [Health Check](https://docs.langflow.org/api/<#>)
  * [Log](https://docs.langflow.org/api/<#>)


# Get Api Keys Route
Get Api Keys Route
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
`total_count` Total Count  
`user_id` uuid  
`api_keys` object[]| `name` Name — **OPTIONAL**  
---  
`last_used_at` Last Used At — **OPTIONAL**  
`total_uses` Total Uses — **OPTIONAL**  
`is_active` Is Active — **OPTIONAL**  
`id` uuid  
`api_key` Api Key  
`user_id` uuid  
`created_at` date-time  
[PreviousReset Password](https://docs.langflow.org/api/</api/reset-password>)[NextCreate Api Key Route](https://docs.langflow.org/api/</api/create-api-key-route>)
Authorize
`**get_api_keys_route_api_v1_api_key__get**`
```
GET /api/v1/api_key/
```

cURL NodeGoPython
Copy```
curl-L'https://docs.langflow.org/api/v1/api_key/'\
-H'Accept: application/json'

```

Execute
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c1fcb67e-e654-45e9-a9b7-093556bcbddf&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eef8b26e-3b71-45e2-a507-b0258123f016&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fget-api-keys-route&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c1fcb67e-e654-45e9-a9b7-093556bcbddf&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eef8b26e-3b71-45e2-a507-b0258123f016&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fapi%2Fget-api-keys-route&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
