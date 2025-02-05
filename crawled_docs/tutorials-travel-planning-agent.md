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
    * [Blog writer](https://docs.langflow.org/</tutorials-blog-writer>)
    * [Document QA](https://docs.langflow.org/</tutorials-document-qa>)
    * [Memory chatbot](https://docs.langflow.org/</tutorials-memory-chatbot>)
    * [Math agent](https://docs.langflow.org/</tutorials-math-agent>)
    * [Sequential tasks agent](https://docs.langflow.org/</tutorials-sequential-agent>)
    * [Travel planning agent](https://docs.langflow.org/</tutorials-travel-planning-agent>)
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
  * Tutorials
  * Travel planning agent


On this page
# Travel planning agent
Build a **Travel Planning Agent** flow for an agentic application using the multiple Tool-calling agents.
An **agent** uses an LLM as its "brain" to select among the connected tools and complete its tasks.
In this flow, multiple **Tool-calling agents** reason using an **Open AI** LLM to plan a travel journey. Each agent is given a different responsibility defined by its **System Prompt** field.
The **Chat input** defines where the user wants to go, and passes the result to the **City Selection** agent. The **Local Expert** agent then adds information based on the selected cities, and the **Travel Concierge** assembles a seven day travel plan in Markdown.
All agents have access to the **Search API** and **URL Content Fetcher** components, while only the Travel Concierge can use the **Calculator** for computing the trip costs.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
To use this flow, you need an [OpenAI API key](https://docs.langflow.org/<https:/platform.openai.com/>) and a [Search API key](https://docs.langflow.org/<https:/www.searchapi.io/>).
## Open Langflow and start a new flow[​](https://docs.langflow.org/<#open-langflow-and-start-a-new-flow> "Direct link to Open Langflow and start a new flow")
Click **New Flow** , and then select the **Travel Planning Agent** flow.
This opens a starter flow with the necessary components to run an agentic application using multiple Tool-calling agents.
## Create the travel planning agent flow[​](https://docs.langflow.org/<#create-the-travel-planning-agent-flow> "Direct link to Create the travel planning agent flow")
![](https://docs.langflow.org/assets/images/starter-flow-travel-agent-a7119af3c35c0a13a7321377ddbd0bde.png)
The **Travel Planning Agent** flow consists of these components:
  * Multiple **Tool calling agent** components that use the connected LLM to reason through the user's input and select among the connected tools to complete their tasks.
  * The **Calculator** component performs basic arithmetic operations.
  * The **URL Content Fetcher** component scrapes content from a given URL.
  * The **Chat Input** component accepts user input to the chat.
  * The **Chat Output** component prints the flow's output to the chat.
  * The **OpenAI** model component sends the user input and prompt to the OpenAI API and receives a response.


## Run the travel planning agent flow[​](https://docs.langflow.org/<#run-the-travel-planning-agent-flow> "Direct link to Run the travel planning agent flow")
  1. Add your credentials to the Open AI and Search API components.
  2. Click **Playground** to start a chat session. You should receive a detailed, helpful answer to the journey defined in the **Chat input** component.


Now that your query has completed the journey from **Chat input** to **Chat output** , you have completed the **Travel Planning Agent** flow.
[PreviousSequential tasks agent](https://docs.langflow.org/</tutorials-sequential-agent>)[NextLangflow overview](https://docs.langflow.org/</concepts-overview>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Open Langflow and start a new flow](https://docs.langflow.org/<#open-langflow-and-start-a-new-flow>)
  * [Create the travel planning agent flow](https://docs.langflow.org/<#create-the-travel-planning-agent-flow>)
  * [Run the travel planning agent flow](https://docs.langflow.org/<#run-the-travel-planning-agent-flow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
