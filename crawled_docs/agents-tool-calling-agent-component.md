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
    * [Agents overview](https://docs.langflow.org/</agents-overview>)
    * [Create a problem-solving agent](https://docs.langflow.org/</agents-tool-calling-agent-component>)
  * [Configuration](https://docs.langflow.org/<#>)
  * [Deployment](https://docs.langflow.org/<#>)
  * [Integrations](https://docs.langflow.org/<#>)
  * [Contributing](https://docs.langflow.org/<#>)
  * [API reference](https://docs.langflow.org/<#>)
  * [Changelog](https://docs.langflow.org/<#>)


  * [](https://docs.langflow.org/</>)
  * Agents
  * Create a problem-solving agent


On this page
# Create a problem-solving agent
Developing **agents** in Langchain is complex.
The `AgentComponent` is a component for easily creating an AI agent capable of analyzing tasks using tools you provide.
The component contains all of the elements you'll need for creating an agent. Instead of managing LLM models and providers, pick your model and enter your API key. Instead of connecting a **Prompt** component, enter instructions in the component's **Agent Instruction** fields.
![Prompt component](https://docs.langflow.org/img/tool-calling-agent-component.png)
Learn how to build a flow starting with the **Tool calling agent** component, and see how it can help you solve problems.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [An OpenAI API key](https://docs.langflow.org/<https:/platform.openai.com/>)
  * [A Search API key](https://docs.langflow.org/<https:/www.searchapi.io/>)


## Create a problem-solving agent with AgentComponent[​](https://docs.langflow.org/<#create-a-problem-solving-agent-with-agentcomponent> "Direct link to Create a problem-solving agent with AgentComponent")
Create a problem-solving agent in Langflow, starting with the **Tool calling agent**.
  1. Click **New Flow** , and then click **Blank Flow**.
  2. Click and drag an **Agent** component to your workspace. The default settings are acceptable for now, so this guide assumes you're using **Open AI** for the LLM.
  3. Add your **Open AI API Key** to the **Agent** component.
  4. Add **Chat input** and **Chat output** components to your flow, and connect them to the tool calling agent.

![Chat with agent component](https://docs.langflow.org/img/tool-calling-agent-add-chat.png)
This basic flow enables you to chat with the agent with the **Playground** after you've connected some **Tools**.
  1. Connect the **Search API** tool component to your agent.
  2. Add your **Search API key** to the component. Your agent can now query the Search API for information.
  3. Connect a **Calculator** tool for solving basic math problems.
  4. Connect an **API Request** component to the agent. This component is not in the **Tools** category, but the agent can still use it as a tool by enabling **Tool Mode**. **Tool Mode** makes a component into a tool by adding a **Toolset** port that can be connected to an agent's **Tools** port. To enable **Tool Mode** on the component, click **Tool Mode**. The component's fields change dynamically based on the mode it's in.

![Chat with agent component](https://docs.langflow.org/img/tool-calling-agent-add-tools.png)
## Solve problems with the agent[​](https://docs.langflow.org/<#solve-problems-with-the-agent> "Direct link to Solve problems with the agent")
Your agent now has tools for performing a web search, doing basic math, and performing API requests. You can solve many problems with just these capabilities.
  * Your tabletop game group cancelled, and you're stuck at home. Point **API Request** to an online rules document, tell your agent `You are a fun game organizer who uses the tools at your disposal`, and play a game.
  * You need to learn a new software language quickly. Point **API Request** to some docs, tell your agent `You are a knowledgeable software developer who uses the tools at your disposal`, and start learning.


See what problems you can solve with this flow. As your problem becomes more specialized, add a tool. For example, the [simple agent starter project](https://docs.langflow.org/</starter-projects-simple-agent>) adds a Python REPL component to solve math problems that are too challenging for the calculator.
## Use an agent as a tool[​](https://docs.langflow.org/<#use-an-agent-as-a-tool> "Direct link to Use an agent as a tool")
The agent component itself also supports **Tool Mode** for creating multi-agent flows.
Add an agent to your problem-solving flow that uses a different OpenAI model for more specialized problem solving.
  1. Click and drag an **Agent** component to your workspace.
  2. Add your **Open AI API Key** to the **Agent** component.
  3. In the **Model Name** field, select `gpt-4o`.
  4. Click **Tool Mode** to use this new agent as a tool.
  5. Connect the new agent's **Toolset** port to the previously created agent's **Tools** port.
  6. Connect **Search API** and **API Request** to the new agent. The new agent will use `gpt-4o` for the larger tasks of scraping and searching information that requires large context windows. The problem-solving agent will now use this agent as a tool, with its unique LLM and toolset.

![Chat with agent component](https://docs.langflow.org/img/tool-calling-agent-as-tool.png)
## Add custom components as tools[​](https://docs.langflow.org/<#components-as-tools> "Direct link to Add custom components as tools")
An agent can use custom components as tools.
  1. To add a custom component to the problem-solving agent flow, click **New Custom Component**.
  2. Add custom Python code to the custom component. Here's an example text analyzer for sentiment analysis.


`
1
from langflow.custom import Component
2
from langflow.io import MessageTextInput, Output
3
from langflow.schema import Data
4
import re
56
class TextAnalyzerComponent(Component):
7
  display_name = "Text Analyzer"
8
  description = "Analyzes and transforms input text."
9
  documentation: str = "http://docs.langflow.org/components/custom"
10
  icon = "chart-bar"
11
  name = "TextAnalyzerComponent"
1213
  inputs = [
14
    MessageTextInput(
15
      name="input_text",
16
      display_name="Input Text",
17
      info="Enter text to analyze",
18
      value="Hello, World!",
19
      tool_mode=True,
20
    ),
21
  ]
2223
  outputs = [
24
    Output(display_name="Analysis Result", name="output", method="analyze_text"),
25
  ]
2627
  def analyze_text(self) -> Data:
28
    text = self.input_text
2930
    # Perform text analysis
31
    word_count = len(text.split())
32
    char_count = len(text)
33
    sentence_count = len(re.findall(r'\w+[.!?]', text))
3435
    # Transform text
36
    reversed_text = text[::-1]
37
    uppercase_text = text.upper()
3839
    analysis_result = {
40
      "original_text": text,
41
      "word_count": word_count,
42
      "character_count": char_count,
43
      "sentence_count": sentence_count,
44
      "reversed_text": reversed_text,
45
      "uppercase_text": uppercase_text
46
    }
4748
    data = Data(value=analysis_result)
49
    self.status = data
50
    return data
`
  1. To enable the custom component as a tool, click **Tool Mode**.
  2. Connect the tool output to the agent's tools input.
  3. Ask the agent, `What tools are you using to answer my questions?` Your response will be similar to the following, and will include your custom component.


`
1
I have access to several tools that assist me in answering your questions, including:
2
Search API: This allows me to search for recent information or results on the web.
3
HTTP Requests: I can make HTTP requests to various URLs to retrieve data or interact with APIs.
4
Calculator: I can evaluate basic arithmetic expressions.
5
Text Analyzer: I can analyze and transform input text.
6
Current Date and Time: I can retrieve the current date and time in various time zones.
`
## Make any component a tool[​](https://docs.langflow.org/<#make-any-component-a-tool> "Direct link to Make any component a tool")
If the component you want to use as a tool doesn't have a **Tool Mode** button, add `tool_mode=True` to one of the component's inputs, and connect the new **Toolset** output to the agent's **Tools** input.
Langflow supports **Tool Mode** for the following data types:
  * `DataInput`
  * `DataFrameInput`
  * `PromptInput`
  * `MessageTextInput`
  * `MultilineInput`
  * `DropdownInput`


For example, the [components as tools](https://docs.langflow.org/<#components-as-tools>) example above adds `tool_mode=True` to the `MessageTextInput` input so the custom component can be used as a tool.
`
1
inputs = [
2
  MessageTextInput(
3
    name="input_text",
4
    display_name="Input Text",
5
    info="Enter text to analyze",
6
    value="Hello, World!",
7
    tool_mode=True,
8
  ),
9
]
`
## Add flows as tools[​](https://docs.langflow.org/<#add-flows-as-tools> "Direct link to Add flows as tools")
An agent can use flows that are saved in your workspace as tools with the [Flow as Tool](https://docs.langflow.org/</components-logic#flow-as-tool>) component.
  1. To add a **Flow as Tool** component, click and drag a **Flow as Tool** component to your workspace.
  2. Select the flow you want the agent to use as a tool.
  3. Connect the tool output to the agent's tools input.
  4. Ask the agent, `What tools are you using to answer my questions?` Your **Flow as Tool** flow should be visible in the response.


[PreviousAgents overview](https://docs.langflow.org/</agents-overview>)[NextAPI keys](https://docs.langflow.org/</configuration-api-keys>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Create a problem-solving agent with AgentComponent](https://docs.langflow.org/<#create-a-problem-solving-agent-with-agentcomponent>)
  * [Solve problems with the agent](https://docs.langflow.org/<#solve-problems-with-the-agent>)
  * [Use an agent as a tool](https://docs.langflow.org/<#use-an-agent-as-a-tool>)
  * [Add custom components as tools](https://docs.langflow.org/<#components-as-tools>)
  * [Make any component a tool](https://docs.langflow.org/<#make-any-component-a-tool>)
  * [Add flows as tools](https://docs.langflow.org/<#add-flows-as-tools>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
