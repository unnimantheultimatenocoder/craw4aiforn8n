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
    * [Agents](https://docs.langflow.org/</components-agents>)
    * [Create custom Python components](https://docs.langflow.org/</components-custom-components>)
    * [Data](https://docs.langflow.org/</components-data>)
    * [Embeddings](https://docs.langflow.org/</components-embedding-models>)
    * [Helpers](https://docs.langflow.org/</components-helpers>)
    * [Inputs and outputs](https://docs.langflow.org/</components-io>)
    * [Loaders](https://docs.langflow.org/</components-loaders>)
    * [Logic](https://docs.langflow.org/</components-logic>)
    * [Memories](https://docs.langflow.org/</components-memories>)
    * [Models](https://docs.langflow.org/</components-models>)
    * [Processing](https://docs.langflow.org/</components-processing>)
    * [Prompts](https://docs.langflow.org/</components-prompts>)
    * [Tools](https://docs.langflow.org/</components-tools>)
    * [Vector stores](https://docs.langflow.org/</components-vector-stores>)
  * [Agents](https://docs.langflow.org/<#>)
  * [Configuration](https://docs.langflow.org/<#>)
  * [Deployment](https://docs.langflow.org/<#>)
  * [Integrations](https://docs.langflow.org/<#>)
  * [Contributing](https://docs.langflow.org/<#>)
  * [API reference](https://docs.langflow.org/<#>)
  * [Changelog](https://docs.langflow.org/<#>)


  * [](https://docs.langflow.org/</>)
  * Components
  * Agents


On this page
# Agent components in Langflow
Agent components define the behavior and capabilities of AI agents in your flow.
Agents use LLMs as a reasoning engine to decide which of the connected tool components to use to solve a problem.
Tools in agentic functions are, essentially, functions that the agent can call to perform tasks or access external resources. A function is wrapped as a `Tool` object, with a common interface the agent understands. Agents become aware of tools through tool registration, where the agent is provided a list of available tools, typically at agent initialization. The `Tool` object's description tells the agent what the tool can do.
The agent then uses a connected LLM to reason through the problem to decide which tool is best for the job.
## Use an agent in a flow[​](https://docs.langflow.org/<#use-an-agent-in-a-flow> "Direct link to Use an agent in a flow")
The [simple agent starter project](https://docs.langflow.org/</starter-projects-simple-agent>) uses an [agent component](https://docs.langflow.org/<#agent-component>) connected to URL and Calculator tools to answer a user's questions. The OpenAI LLM acts as a brain for the agent to decide which tool to use. Tools are connected to agent components at the **Tools** port.
![Simple agent starter flow](https://docs.langflow.org/assets/images/starter-flow-simple-agent-71d0dec218a5da8e3110c51716f1c91e.png)
For a multi-agent example, see [Create a problem-solving agent](https://docs.langflow.org/</agents-tool-calling-agent-component>).
## Agent component[​](https://docs.langflow.org/<#agent-component> "Direct link to Agent component")
This component creates an agent that can use tools to answer questions and perform tasks based on given instructions.
The component includes an LLM model integration, a system message prompt, and a **Tools** port to connect tools to extend its capabilities.
For more information on this component, see the [tool calling agent documentation](https://docs.langflow.org/</agents-tool-calling-agent-component>).
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
agent_llm| Dropdown| The provider of the language model that the agent will use to generate responses.  
system_prompt| String| Initial instructions and context provided to guide the agent's behavior.  
tools| List| List of tools available for the agent to use.  
input_value| String| The input task or question for the agent to process.  
add_current_date_tool| Boolean| If true, adds a tool to the agent that returns the current date.  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
response| Message| The agent's response to the given input task.  
## CSV Agent[​](https://docs.langflow.org/<#csv-agent> "Direct link to CSV Agent")
This component creates a CSV agent from a CSV file and LLM.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
path| File| Path to the CSV file  
agent_type| String| Type of agent to create (zero-shot-react-description, openai-functions, or openai-tools)  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| CSV agent instance  
## CrewAI Agent[​](https://docs.langflow.org/<#crewai-agent> "Direct link to CrewAI Agent")
This component represents an Agent of CrewAI, allowing for the creation of specialized AI agents with defined roles, goals, and capabilities within a crew.
For more information, see the [CrewAI documentation](https://docs.langflow.org/<https:/docs.crewai.com/core-concepts/Agents/>).
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
role| Role| The role of the agent  
goal| Goal| The objective of the agent  
backstory| Backstory| The backstory of the agent  
tools| Tools| Tools at agent's disposal  
llm| Language Model| Language model that will run the agent  
memory| Memory| Whether the agent should have memory or not  
verbose| Verbose| Enables verbose output  
allow_delegation| Allow Delegation| Whether the agent is allowed to delegate tasks to other agents  
allow_code_execution| Allow Code Execution| Whether the agent is allowed to execute code  
kwargs| kwargs| Additional keyword arguments for the agent  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
output| Agent| The constructed CrewAI Agent object  
## Hierarchical Crew[​](https://docs.langflow.org/<#hierarchical-crew> "Direct link to Hierarchical Crew")
This component represents a group of agents, managing how they should collaborate and the tasks they should perform in a hierarchical structure. This component allows for the creation of a crew with a manager overseeing the task execution.
For more information, see the [CrewAI documentation](https://docs.langflow.org/<https:/docs.crewai.com/how-to/Hierarchical/>).
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
agents| Agents| List of Agent objects representing the crew members  
tasks| Tasks| List of HierarchicalTask objects representing the tasks to be executed  
manager_llm| Manager LLM| Language model for the manager agent (optional)  
manager_agent| Manager Agent| Specific agent to act as the manager (optional)  
verbose| Verbose| Enables verbose output for detailed logging  
memory| Memory| Specifies the memory configuration for the crew  
use_cache| Use Cache| Enables caching of results  
max_rpm| Max RPM| Sets the maximum requests per minute  
share_crew| Share Crew| Determines if the crew information is shared among agents  
function_calling_llm| Function Calling LLM| Specifies the language model for function calling  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
crew| Crew| The constructed Crew object with hierarchical task execution  
## JSON Agent[​](https://docs.langflow.org/<#json-agent> "Direct link to JSON Agent")
This component creates a JSON agent from a JSON or YAML file and an LLM.
### Inputs[​](https://docs.langflow.org/<#inputs-4> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
path| File| Path to the JSON or YAML file  
### Outputs[​](https://docs.langflow.org/<#outputs-4> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| JSON agent instance  
## OpenAI Tools Agent[​](https://docs.langflow.org/<#openai-tools-agent> "Direct link to OpenAI Tools Agent")
This component creates an OpenAI Tools Agent using LangChain.
For more information, see the [LangChain documentation](https://docs.langflow.org/<https:/python.langchain.com/v0.1/docs/modules/agents/agent_types/openai_tools/>).
### Inputs[​](https://docs.langflow.org/<#inputs-5> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent (must be tool-enabled)  
system_prompt| String| System prompt for the agent  
user_prompt| String| User prompt template (must contain 'input' key)  
chat_history| List[Data]| Optional chat history for the agent  
tools| List[Tool]| List of tools available to the agent  
### Outputs[​](https://docs.langflow.org/<#outputs-5> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| OpenAI Tools Agent instance  
## OpenAPI Agent[​](https://docs.langflow.org/<#openapi-agent> "Direct link to OpenAPI Agent")
This component creates an OpenAPI Agent to interact with APIs defined by OpenAPI specifications.
For more information, see the LangChain documentation on OpenAPI Agents.
### Inputs[​](https://docs.langflow.org/<#inputs-6> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
path| File| Path to the OpenAPI specification file (JSON or YAML)  
allow_dangerous_requests| Boolean| Whether to allow potentially dangerous API requests  
### Outputs[​](https://docs.langflow.org/<#outputs-6> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| OpenAPI Agent instance  
## SQL Agent[​](https://docs.langflow.org/<#sql-agent> "Direct link to SQL Agent")
This component creates a SQL Agent to interact with SQL databases.
### Inputs[​](https://docs.langflow.org/<#inputs-7> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
database_uri| String| URI of the SQL database to connect to  
extra_tools| List[Tool]| Additional tools to provide to the agent (optional)  
### Outputs[​](https://docs.langflow.org/<#outputs-7> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| SQL Agent instance  
## Sequential Crew[​](https://docs.langflow.org/<#sequential-crew> "Direct link to Sequential Crew")
This component represents a group of agents with tasks that are executed sequentially. This component allows for the creation of a crew that performs tasks in a specific order.
For more information, see the [CrewAI documentation](https://docs.langflow.org/<https:/docs.crewai.com/how-to/Sequential/>).
### Inputs[​](https://docs.langflow.org/<#inputs-8> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
tasks| Tasks| List of SequentialTask objects representing the tasks to be executed  
verbose| Verbose| Enables verbose output for detailed logging  
memory| Memory| Specifies the memory configuration for the crew  
use_cache| Use Cache| Enables caching of results  
max_rpm| Max RPM| Sets the maximum requests per minute  
share_crew| Share Crew| Determines if the crew information is shared among agents  
function_calling_llm| Function Calling LLM| Specifies the language model for function calling  
### Outputs[​](https://docs.langflow.org/<#outputs-8> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
crew| Crew| The constructed Crew object with sequential task execution  
## Sequential task agent[​](https://docs.langflow.org/<#sequential-task-agent> "Direct link to Sequential task agent")
This component creates a CrewAI Task and its associated Agent, allowing for the definition of sequential tasks with specific agent roles and capabilities.
For more information, see the [CrewAI documentation](https://docs.langflow.org/<https:/docs.crewai.com/how-to/Sequential/>).
### Inputs[​](https://docs.langflow.org/<#inputs-9> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
role| Role| The role of the agent  
goal| Goal| The objective of the agent  
backstory| Backstory| The backstory of the agent  
tools| Tools| Tools at agent's disposal  
llm| Language Model| Language model that will run the agent  
memory| Memory| Whether the agent should have memory or not  
verbose| Verbose| Enables verbose output  
allow_delegation| Allow Delegation| Whether the agent is allowed to delegate tasks to other agents  
allow_code_execution| Allow Code Execution| Whether the agent is allowed to execute code  
agent_kwargs| Agent kwargs| Additional kwargs for the agent  
task_description| Task Description| Descriptive text detailing task's purpose and execution  
expected_output| Expected Task Output| Clear definition of expected task outcome  
async_execution| Async Execution| Boolean flag indicating asynchronous task execution  
previous_task| Previous Task| The previous task in the sequence (for chaining)  
### Outputs[​](https://docs.langflow.org/<#outputs-9> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
task_output| Sequential Task| List of SequentialTask objects representing the created task(s)  
## Tool Calling Agent[​](https://docs.langflow.org/<#tool-calling-agent> "Direct link to Tool Calling Agent")
This component creates a Tool Calling Agent using LangChain.
### Inputs[​](https://docs.langflow.org/<#inputs-10> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
system_prompt| String| System prompt for the agent  
user_prompt| String| User prompt template (must contain 'input' key)  
chat_history| List[Data]| Optional chat history for the agent  
tools| List[Tool]| List of tools available to the agent  
### Outputs[​](https://docs.langflow.org/<#outputs-10> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| Tool Calling Agent instance  
## Vector Store Agent[​](https://docs.langflow.org/<#vector-store-agent> "Direct link to Vector Store Agent")
This component creates a Vector Store Agent using LangChain.
### Inputs[​](https://docs.langflow.org/<#inputs-11> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
vectorstore| VectorStoreInfo| Vector store information for the agent to use  
### Outputs[​](https://docs.langflow.org/<#outputs-11> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| Vector Store Agent instance  
## Vector Store Router Agent[​](https://docs.langflow.org/<#vector-store-router-agent> "Direct link to Vector Store Router Agent")
This component creates a Vector Store Router Agent using LangChain.
### Inputs[​](https://docs.langflow.org/<#inputs-12> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
vectorstores| List[VectorStoreInfo]| List of vector store information for the agent to route between  
### Outputs[​](https://docs.langflow.org/<#outputs-12> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| Vector Store Router Agent instance  
## XML Agent[​](https://docs.langflow.org/<#xml-agent> "Direct link to XML Agent")
This component creates an XML Agent using LangChain.
The agent uses XML formatting for tool instructions to the Language Model.
### Inputs[​](https://docs.langflow.org/<#inputs-13> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
llm| LanguageModel| Language model to use for the agent  
user_prompt| String| Custom prompt template for the agent (includes XML formatting instructions)  
tools| List[Tool]| List of tools available to the agent  
### Outputs[​](https://docs.langflow.org/<#outputs-13> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
agent| AgentExecutor| XML Agent instance  
[PreviousAPI pane](https://docs.langflow.org/</concepts-api>)[NextCreate custom Python components](https://docs.langflow.org/</components-custom-components>)
  * [Use an agent in a flow](https://docs.langflow.org/<#use-an-agent-in-a-flow>)
  * [Agent component](https://docs.langflow.org/<#agent-component>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [CSV Agent](https://docs.langflow.org/<#csv-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [CrewAI Agent](https://docs.langflow.org/<#crewai-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Hierarchical Crew](https://docs.langflow.org/<#hierarchical-crew>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [JSON Agent](https://docs.langflow.org/<#json-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-4>)
    * [Outputs](https://docs.langflow.org/<#outputs-4>)
  * [OpenAI Tools Agent](https://docs.langflow.org/<#openai-tools-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-5>)
    * [Outputs](https://docs.langflow.org/<#outputs-5>)
  * [OpenAPI Agent](https://docs.langflow.org/<#openapi-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-6>)
    * [Outputs](https://docs.langflow.org/<#outputs-6>)
  * [SQL Agent](https://docs.langflow.org/<#sql-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-7>)
    * [Outputs](https://docs.langflow.org/<#outputs-7>)
  * [Sequential Crew](https://docs.langflow.org/<#sequential-crew>)
    * [Inputs](https://docs.langflow.org/<#inputs-8>)
    * [Outputs](https://docs.langflow.org/<#outputs-8>)
  * [Sequential task agent](https://docs.langflow.org/<#sequential-task-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-9>)
    * [Outputs](https://docs.langflow.org/<#outputs-9>)
  * [Tool Calling Agent](https://docs.langflow.org/<#tool-calling-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-10>)
    * [Outputs](https://docs.langflow.org/<#outputs-10>)
  * [Vector Store Agent](https://docs.langflow.org/<#vector-store-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-11>)
    * [Outputs](https://docs.langflow.org/<#outputs-11>)
  * [Vector Store Router Agent](https://docs.langflow.org/<#vector-store-router-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-12>)
    * [Outputs](https://docs.langflow.org/<#outputs-12>)
  * [XML Agent](https://docs.langflow.org/<#xml-agent>)
    * [Inputs](https://docs.langflow.org/<#inputs-13>)
    * [Outputs](https://docs.langflow.org/<#outputs-13>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
