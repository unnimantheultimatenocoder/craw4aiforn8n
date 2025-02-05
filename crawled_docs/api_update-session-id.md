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
    * [Get Vertex Builds](https://docs.langflow.org/api/</api/get-vertex-builds>)
    * [Delete Vertex Builds](https://docs.langflow.org/api/</api/delete-vertex-builds>)
    * [Get Messages](https://docs.langflow.org/api/</api/get-messages>)
    * [Delete Messages](https://docs.langflow.org/api/</api/delete-messages>)
    * [Update Message](https://docs.langflow.org/api/</api/update-message>)
    * [Update Session Id](https://docs.langflow.org/api/</api/update-session-id>)
    * [Delete Messages Session](https://docs.langflow.org/api/</api/delete-messages-session>)
    * [Get Transactions](https://docs.langflow.org/api/</api/get-transactions>)
  * [Folders](https://docs.langflow.org/api/</api/read-folders>)
  * [mcp](https://docs.langflow.org/api/</api/handle-sse>)
  * [Health Check](https://docs.langflow.org/api/</api/health>)
  * [Log](https://docs.langflow.org/api/</api/stream-logs>)


# Update Session Id
Update Session Id
Path Parameters  
---  
`old_session_id` Old Session Id — **REQUIRED**  
Query Parameters  
---  
`new_session_id` New Session Id — **REQUIRED** The new session ID to update toThe new session ID to update to  
Responses  
---  
`200`Successful Response| Schema  — **OPTIONAL**  
---  
object[]| `id` Id — **OPTIONAL**  
---  
`flow_id` Flow Id — **OPTIONAL**  
`timestamp` date-time — **OPTIONAL**  
`sender` Sender  
`sender_name` Sender Name  
`session_id` Session Id  
`text` Text  
`files` string[] — **OPTIONAL**  
`edit` Edit  
`properties` — **OPTIONAL**  
`category` Category — **OPTIONAL**  
`content_blocks` Content Blocks — **OPTIONAL**  
`422` Validation Error| Schema  — **OPTIONAL**  
---  
`detail` object[] — **OPTIONAL**| `loc` undefined[]  
---  
`msg` Message  
`type` Error Type  
[PreviousUpdate Message](https://docs.langflow.org/api/</api/update-message>)[NextDelete Messages Session](https://docs.langflow.org/api/</api/delete-messages-session>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
