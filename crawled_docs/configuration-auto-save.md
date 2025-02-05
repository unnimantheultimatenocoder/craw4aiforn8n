[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/<#>)
  * [Starter projects](https://docs.langflow.org/<#>)
  * [Tutorials](https://docs.langflow.org/<#>)
  * [Concepts](https://docs.langflow.org/<#>)
  * [Components](https://docs.langflow.org/<#>)
  * [Agents](https://docs.langflow.org/<#>)
  * [Configuration](https://docs.langflow.org/<#>)
    * [API keys](https://docs.langflow.org/</configuration-api-keys>)
    * [Authentication](https://docs.langflow.org/</configuration-authentication>)
    * [Auto-saving](https://docs.langflow.org/</configuration-auto-save>)
    * [Run Langflow in backend-only mode](https://docs.langflow.org/</configuration-backend-only>)
    * [Langflow CLI](https://docs.langflow.org/</configuration-cli>)
    * [Global variables](https://docs.langflow.org/</configuration-global-variables>)
    * [Environment variables](https://docs.langflow.org/</environment-variables>)
    * [Security best practices](https://docs.langflow.org/</configuration-security-best-practices>)
  * [Deployment](https://docs.langflow.org/<#>)
  * [Integrations](https://docs.langflow.org/<#>)
  * [Contributing](https://docs.langflow.org/<#>)
  * [API reference](https://docs.langflow.org/<#>)
  * [Changelog](https://docs.langflow.org/<#>)


  * [](https://docs.langflow.org/</>)
  * Configuration
  * Auto-saving


On this page
# Auto-saving
Langflow supports both manual and auto-saving functionality.
## Auto-saving[​](https://docs.langflow.org/<#auto-saving> "Direct link to Auto-saving")
When Langflow is in auto-saving mode, all changes are saved automatically. Auto-save progress is indicated in the left side of the top bar.
  * When a flow is being saved, a loading icon indicates that the flow is being saved in the database.
  * If you try to exit the flow page before auto-save completes, you are prompted to confirm you want to exit before the flow has saved.
  * When the flow has successfully saved, click **Exit**.


## Disable auto-saving[​](https://docs.langflow.org/<#environment> "Direct link to Disable auto-saving")
To disable auto-saving,
  1. Set an environment variable in your `.env` file.


`
1
LANGFLOW_AUTO_SAVING=false
`
  1. Start Langflow with the values from your `.env` file.


`
1
python -m langflow run --env-file .env
`
Alternatively, disable auto-saving by passing the `--no-auto-saving` flag at startup.
`
1
python -m langflow --no-auto-saving
`
## Save a flow manually[​](https://docs.langflow.org/<#manual-saving> "Direct link to Save a flow manually")
When auto-saving is disabled, you will need to manually save your flow when making changes.
To manually save your flow, click the **Save** button or enter Ctrl+S or Command+S.
If you try to exit after making changes and not saving, a confirmation dialog appears.
[PreviousAuthentication](https://docs.langflow.org/</configuration-authentication>)[NextRun Langflow in backend-only mode](https://docs.langflow.org/</configuration-backend-only>)
  * [Auto-saving](https://docs.langflow.org/<#auto-saving>)
  * [Disable auto-saving](https://docs.langflow.org/<#environment>)
  * [Save a flow manually](https://docs.langflow.org/<#manual-saving>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=79f71f29-351c-41db-828c-004fe4d5d317&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bf3cad6d-fa99-4a53-9957-9c79be7f1d8f&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fconfiguration-auto-save&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=79f71f29-351c-41db-828c-004fe4d5d317&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bf3cad6d-fa99-4a53-9957-9c79be7f1d8f&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fconfiguration-auto-save&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
