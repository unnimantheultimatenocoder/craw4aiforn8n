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
  * Sequential tasks agent


On this page
# Sequential tasks agent
Build a **Sequential Tasks Agent** flow for a multi-agent application using multiple **Agent** components.
Each agent has an LLM model and a unique set of tools at its disposal, with **Prompt** components connected to the **Agent Instructions** fields to control the agent's behavior. For example, the **Researcher Agent** has a **Tavily AI Search** component connected as a tool. The **Prompt** instructs the agent how to answer your query, format the response, and pass the query and research results on to the next agent in the flow.
Each successive agent in the flow builds on the work of the previous agent, creating a chain of reasoning for solving complex problems.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [An OpenAI API key](https://docs.langflow.org/<https:/platform.openai.com/>)
  * [A Tavily AI API key](https://docs.langflow.org/<https:/www.tavily.com/>)


## Open Langflow and create a new flow[​](https://docs.langflow.org/<#open-langflow-and-create-a-new-flow> "Direct link to Open Langflow and create a new flow")
  1. Click **New Flow** , and then select **Sequential Tasks Agent**. This opens a starter template with the necessary components to run the flow.


![Starter flow for Sequential Tasks Agent](https://docs.langflow.org/assets/images/starter-flow-sequential-agent-ccd15bee6bedbe3a33c81a12c10d6475.png)
The Sequential Tasks Agent flow consists of these components:
  * The **Agent** components use the connected LLM to analyze the user's input and select among the connected tools to complete the tasks.
  * The **Chat Input** component accepts user input to the chat.
  * The **Prompt** component combines the user input with a user-defined prompt.
  * The **Chat Output** component prints the flow's output to the chat.
  * The **YFinance** tool component provides access to financial data from Yahoo Finance.
  * The **Tavily AI Search** tool component performs AI-powered web searches.
  * The **Calculator** tool component performs mathematical calculations.


## Run the Sequential Tasks Agent flow[​](https://docs.langflow.org/<#run-the-sequential-tasks-agent-flow> "Direct link to Run the Sequential Tasks Agent flow")
  1. Add your OpenAI API key to the **Agent** components.
  2. Add your Tavily API key to the **Tavily** component.
  3. Click **Playground** to start a chat session with the template's default question.


`
1
Should I invest in Tesla (TSLA) stock right now?
2
Please analyze the company's current position, market trends,
3
financial health, and provide a clear investment recommendation.
`
This question provides clear instructions to the agents about how to proceed and what question to answer.
  1. In the **Playground** , inspect the answers to see how the agents use the **Tavily AI Search** tool to research the query, the **YFinance** tool to analyze the stock data, and the **Calculator** to determine if the stock is a wise investment.
  2. Ask similar questions to see how the agents use the tools to answer your queries.


## Next steps[​](https://docs.langflow.org/<#next-steps> "Direct link to Next steps")
To create your own multi-agent flow, see [Create a problem solving agent](https://docs.langflow.org/</agents-tool-calling-agent-component>).
[PreviousMath agent](https://docs.langflow.org/</tutorials-math-agent>)[NextTravel planning agent](https://docs.langflow.org/</tutorials-travel-planning-agent>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Open Langflow and create a new flow](https://docs.langflow.org/<#open-langflow-and-create-a-new-flow>)
  * [Run the Sequential Tasks Agent flow](https://docs.langflow.org/<#run-the-sequential-tasks-agent-flow>)
  * [Next steps](https://docs.langflow.org/<#next-steps>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
