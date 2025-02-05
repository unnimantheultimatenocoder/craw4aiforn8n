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


# Read Flows
Retrieve a list of flows with pagination support.
Args: current_user (User): The current authenticated user. session (Session): The database session. settings_service (SettingsService): The settings service. components_only (bool, optional): Whether to return only components. Defaults to False.
get_all (bool, optional): Whether to return all flows without pagination. Defaults to True. **This field must be True because of backward compatibility with the frontend - Release: 1.0.20**
folder_id (UUID, optional): The folder ID. Defaults to None. params (Params): Pagination parameters. remove_example_flows (bool, optional): Whether to remove example flows. Defaults to False. header_flows (bool, optional): Whether to return only specific headers of the flows. Defaults to False.
Returns: list[FlowRead] | Page[FlowRead] | list[FlowHeader] A list of flows or a paginated response containing the list of flows or a list of flow headers.
Query Parameters  
---  
`remove_example_flows` Remove Example Flows  
`components_only` Components Only  
`get_all` Get All  
`folder_id` Folder Id  
`header_flows` Header Flows  
`page` Page**Possible values:** 1 ≤ value  
`size` Size**Possible values:** 1 ≤ value ≤ 100  
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
[PreviousCreate Flow](https://docs.langflow.org/api/</api/create-flow>)[NextDelete Multiple Flows](https://docs.langflow.org/api/</api/delete-multiple-flows>)
Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
