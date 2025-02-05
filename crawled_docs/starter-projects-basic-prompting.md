[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/<#>)
  * [Starter projects](https://docs.langflow.org/<#>)
    * [Basic prompting](https://docs.langflow.org/</starter-projects-basic-prompting>)
    * [Vector store RAG](https://docs.langflow.org/</starter-projects-vector-store-rag>)
    * [Simple agent](https://docs.langflow.org/</starter-projects-simple-agent>)
  * [Tutorials](https://docs.langflow.org/<#>)
  * [Concepts](https://docs.langflow.org/<#>)
  * [Components](https://docs.langflow.org/<#>)
  * [Agents](https://docs.langflow.org/<#>)
  * [Configuration](https://docs.langflow.org/<#>)
  * [Deployment](https://docs.langflow.org/<#>)
  * [Integrations](https://docs.langflow.org/<#>)
  * [Contributing](https://docs.langflow.org/<#>)
  * [API reference](https://docs.langflow.org/<#>)
  * [Changelog](https://docs.langflow.org/<#>)


  * [](https://docs.langflow.org/</>)
  * Starter projects
  * Basic prompting


On this page
# Basic prompting
Prompts serve as the inputs to a large language model (LLM), acting as the interface between human instructions and computational tasks.
By submitting natural language requests in a prompt to an LLM, you can obtain answers, generate text, and solve problems.
This article demonstrates how to use Langflow's prompt tools to issue basic prompts to an LLM, and how various prompting strategies can affect your outcomes.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [Langflow installed and running](https://docs.langflow.org/</get-started-installation>)
  * [OpenAI API key created](https://docs.langflow.org/<https:/platform.openai.com/>)


## Create the basic prompting flow[​](https://docs.langflow.org/<#create-the-basic-prompting-flow> "Direct link to Create the basic prompting flow")
  1. From the Langflow dashboard, click **New Flow**.
  2. Select **Basic Prompting**.
  3. The **Basic Prompting** flow is created.


![](https://docs.langflow.org/assets/images/starter-flow-basic-prompting-09331815d7282bd6a3feedf84838ba20.png)
This flow allows you to chat with the **OpenAI model** component. The model will respond according to the prompt constructed in the **Prompt** component.
  1. To examine the **Template** , in the **Prompt** component, click the **Template** field.


`
1
Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.
`
  1. To create an environment variable for the **OpenAI** component, in the **OpenAI API Key** field, click the **Globe** button, and then click **Add New Variable**.
    1. In the **Variable Name** field, enter `openai_api_key`.
    2. In the **Value** field, paste your OpenAI API Key (`sk-...`).
    3. Click **Save Variable**.


## Run the basic prompting flow[​](https://docs.langflow.org/<#run-the-basic-prompting-flow> "Direct link to Run the basic prompting flow")
  1. Click the **Playground** button.
  2. Type a message and press Enter. The bot should respond in a markedly piratical manner!


## Modify the prompt for a different result[​](https://docs.langflow.org/<#modify-the-prompt-for-a-different-result> "Direct link to Modify the prompt for a different result")
  1. To modify your prompt results, in the **Prompt** component, click the **Template** field. The **Edit Prompt** window opens.
  2. Change the existing prompt to a different character, perhaps `Answer the user as if you were Hermione Granger.`
  3. Run the workflow again and notice how the prompt changes the model's response.


[PreviousQuickstart](https://docs.langflow.org/</get-started-quickstart>)[NextVector store RAG](https://docs.langflow.org/</starter-projects-vector-store-rag>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Create the basic prompting flow](https://docs.langflow.org/<#create-the-basic-prompting-flow>)
  * [Run the basic prompting flow](https://docs.langflow.org/<#run-the-basic-prompting-flow>)
  * [Modify the prompt for a different result](https://docs.langflow.org/<#modify-the-prompt-for-a-different-result>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6aeeb690-2bb1-4898-994f-a176407c23fc&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e9805172-578e-4865-ab63-1c808db0a56f&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fstarter-projects-basic-prompting&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=6aeeb690-2bb1-4898-994f-a176407c23fc&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e9805172-578e-4865-ab63-1c808db0a56f&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fstarter-projects-basic-prompting&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
