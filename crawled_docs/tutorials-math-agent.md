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
  * Math agent


On this page
# Math agent
Build a **Math Agent** flow for an agentic application using the **Tool-calling agent** component.
In this flow, the **Tool-calling agent** reasons using an **Open AI** LLM to solve math problems. It selects the **Calculator** tool for simpler math and the **Python REPL** tool (with the Python `math` library) for more complex problems.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
To use this flow, you need an OpenAI API key.
## Open Langflow and start a new flow[​](https://docs.langflow.org/<#open-langflow-and-start-a-new-flow> "Direct link to Open Langflow and start a new flow")
Click **New Flow** , and then select the **Math Agent** flow.
This opens a starter flow with the necessary components to run an agentic application using the Tool-calling agent.
## Math Agent flow[​](https://docs.langflow.org/<#math-agent-flow> "Direct link to Math Agent flow")
![](https://docs.langflow.org/assets/images/starter-flow-simple-agent-repl-6c6df85ce6d01bfafebe3e4247cefc83.png)
The **Math Agent** flow consists of these components:
  * The **Tool calling agent** component uses the connected LLM to reason through the user's input and select among the connected tools to complete its task.
  * The **Python REPL tool** component executes Python code in a REPL (Read-Evaluate-Print Loop) interpreter.
  * The **Calculator** component performs basic arithmetic operations.
  * The **Chat Input** component accepts user input to the chat.
  * The **Prompt** component combines the user input with a user-defined prompt.
  * The **Chat Output** component prints the flow's output to the chat.
  * The **OpenAI** model component sends the user input and prompt to the OpenAI API and receives a response.


## Run the Math Agent flow[​](https://docs.langflow.org/<#run-the-math-agent-flow> "Direct link to Run the Math Agent flow")
  1. Add your credentials to the Open AI component.
  2. Click **Playground** to start a chat session.
  3. Enter a simple math problem, like `2 + 2`, and then make sure the bot responds with the correct answer.
  4. To confirm the REPL interpreter is working, prompt the `math` library directly with `math.sqrt(4)` and see if the bot responds with `4`.
  5. The agent will also reason through more complex word problems. For example, prompt the agent with the following math problem:


`
1
The equation 24x2+25x−47ax−2=−8x−3−53ax−2 is true for all values of x≠2a, where a is a constant.
2
What is the value of a?
3
A) -16
4
B) -3
5
C) 3
6
D) 16
`
The agent should respond with `B`.
Now that your query has completed the journey from **Chat input** to **Chat output** , you have completed the **Math Agent** flow.
[PreviousMemory chatbot](https://docs.langflow.org/</tutorials-memory-chatbot>)[NextSequential tasks agent](https://docs.langflow.org/</tutorials-sequential-agent>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Open Langflow and start a new flow](https://docs.langflow.org/<#open-langflow-and-start-a-new-flow>)
  * [Math Agent flow](https://docs.langflow.org/<#math-agent-flow>)
  * [Run the Math Agent flow](https://docs.langflow.org/<#run-the-math-agent-flow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
