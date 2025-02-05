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
  * Simple agent


On this page
# Simple agent
Build a **Simple Agent** flow for an agentic application using the **Tool-calling agent** component.
An **agent** uses an LLM as its "brain" to select among the connected tools and complete its tasks.
In this flow, the **Tool-calling agent** reasons using an **Open AI** LLM. The agent selects the **Calculator** tool for simple math problems and the **URL** tool to search a URL for content.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
To use this flow, you need an OpenAI API key.
## Open Langflow and start a new flow[​](https://docs.langflow.org/<#open-langflow-and-start-a-new-flow> "Direct link to Open Langflow and start a new flow")
Click **New Flow** , and then select the **Simple Agent** flow.
This opens a starter flow with the necessary components to run an agentic application using the Tool-calling agent.
## Simple Agent flow[​](https://docs.langflow.org/<#simple-agent-flow> "Direct link to Simple Agent flow")
![Starter flow simple agent](https://docs.langflow.org/img/starter-flow-simple-agent.png)
The **Simple Agent** flow consists of these components:
  * The **Tool calling agent** component uses the connected LLM to reason through the user's input and select among the connected tools to complete its task.
  * The **URL** tool component searches a list of URLs for content.
  * The **Calculator** component performs basic arithmetic operations.
  * The **Chat Input** component accepts user input to the chat.
  * The **Prompt** component combines the user input with a user-defined prompt.
  * The **Chat Output** component prints the flow's output to the chat.
  * The **OpenAI** model component sends the user input and prompt to the OpenAI API and receives a response.


## Run the Simple Agent flow[​](https://docs.langflow.org/<#run-the-simple-agent-flow> "Direct link to Run the Simple Agent flow")
  1. Add your credentials to the Open AI component.
  2. Click **Playground** to start a chat session.
  3. To confirm the tools are connected, ask the agent, `What tools are available to you?` The response is similar to the following:


`
1
I have access to the following tools:
2
Calculator: Perform basic arithmetic operations.
3
fetch_content: Load and retrieve data from specified URLs.
4
fetch_content_text: Load and retrieve text data from specified URLs.
5
as_dataframe: Load and retrieve data in a structured format (dataframe) from specified URLs.
6
get_current_date: Returns the current date and time in a selected timezone.
`
  1. Ask the agent a question. For example, ask it to create a tabletop character using your favorite rules set. The agent will tell you when it's using the `URL-fetch_content_text` tool to search for rules information, and when it's using `CalculatorComponent-evaluate_expression` to generate attributes with dice rolls. The final output should be similar to this:


`
1
Final Attributes
2
Strength (STR): 10
3
Constitution (CON): 12
4
Size (SIZ): 14
5
Dexterity (DEX): 9
6
Intelligence (INT): 11
7
Power (POW): 13
8
Charisma (CHA): 8
`
Now that your query has completed the journey from **Chat input** to **Chat output** , you have completed the **Simple Agent** flow.
[PreviousVector store RAG](https://docs.langflow.org/</starter-projects-vector-store-rag>)[NextBlog writer](https://docs.langflow.org/</tutorials-blog-writer>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Open Langflow and start a new flow](https://docs.langflow.org/<#open-langflow-and-start-a-new-flow>)
  * [Simple Agent flow](https://docs.langflow.org/<#simple-agent-flow>)
  * [Run the Simple Agent flow](https://docs.langflow.org/<#run-the-simple-agent-flow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
