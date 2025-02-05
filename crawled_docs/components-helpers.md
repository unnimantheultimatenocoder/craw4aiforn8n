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
  * Helpers


On this page
# Helper components in Langflow
Helper components provide utility functions to help manage data, tasks, and other components in your flow.
## Use a helper component in a flow[​](https://docs.langflow.org/<#use-a-helper-component-in-a-flow> "Direct link to Use a helper component in a flow")
Chat memory in Langflow is stored either in local Langflow tables with `LCBufferMemory`, or connected to an external database.
The **Store Message** helper component stores chat memories as [Data](https://docs.langflow.org/</concepts-objects>) objects, and the **Message History** helper component retrieves chat messages as data objects or strings.
This example flow stores and retrieves chat history from an [AstraDBChatMemory](https://docs.langflow.org/</components-memories#astradbchatmemory-component>) component with **Store Message** and **Chat Memory** components.
![Sample Flow storing Chat Memory in AstraDB](https://docs.langflow.org/assets/images/astra_db_chat_memory_rounded-9746ca2bb69d3b07ac0a071f4b9471b3.png)
## Create List[​](https://docs.langflow.org/<#create-list> "Direct link to Create List")
This component dynamically creates a record with a specified number of fields.
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
n_fields| Number of Fields| Number of fields to be added to the record.  
text_key| Text Key| Key used as text.  
## Current date[​](https://docs.langflow.org/<#current-date> "Direct link to Current date")
The Current Date component returns the current date and time in a selected timezone. This component provides a flexible way to obtain timezone-specific date and time information within a Langflow pipeline.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
timezone| Timezone| Select the timezone for the current date and time.  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
current_date| Current Date| The resulting current date and time in the selected timezone.  
## ID Generator[​](https://docs.langflow.org/<#id-generator> "Direct link to ID Generator")
This component generates a unique ID.
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
value| Value| Unique ID generated.  
## Message history[​](https://docs.langflow.org/<#message-history> "Direct link to Message history")
info
Prior to Langflow 1.1, this component was known as the Chat Memory component.
This component retrieves and manages chat messages from Langflow tables or an external memory.
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
memory| External Memory| Retrieve messages from an external memory. If empty, it will use the Langflow tables.  
sender| Sender Type| Filter by sender type.  
sender_name| Sender Name| Filter by sender name.  
n_messages| Number of Messages| Number of messages to retrieve.  
session_id| Session ID| The session ID of the chat. If empty, the current session ID parameter will be used.  
order| Order| Order of the messages.  
template| Template| The template to use for formatting the data. It can contain the keys `{text}`, `{sender}` or any other key in the message data.  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
messages| Messages (Data)| Retrieved messages as Data objects.  
messages_text| Messages (Text)| Retrieved messages formatted as text.  
lc_memory| Memory| A constructed Langchain [ConversationBufferMemory](https://docs.langflow.org/<https:/api.python.langchain.com/en/latest/memory/langchain.memory.buffer.ConversationBufferMemory.html>) object  
## Store Message[​](https://docs.langflow.org/<#store-message> "Direct link to Store Message")
This component stores chat messages or text into Langflow tables or an external memory.
It provides flexibility in managing message storage and retrieval within a chat system.
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
message| Message| The chat message to be stored. (Required)  
memory| External Memory| The external memory to store the message. If empty, it will use the Langflow tables.  
sender| Sender| The sender of the message. Can be Machine or User. If empty, the current sender parameter will be used.  
sender_name| Sender Name| The name of the sender. Can be AI or User. If empty, the current sender parameter will be used.  
session_id| Session ID| The session ID of the chat. If empty, the current session ID parameter will be used.  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
stored_messages| Stored Messages| The list of stored messages after the current message has been added.  
## Structured output[​](https://docs.langflow.org/<#structured-output> "Direct link to Structured output")
This component transforms LLM responses into structured data formats.
### Input[​](https://docs.langflow.org/<#input> "Direct link to Input")
Name| Display Name| Info  
---|---|---  
llm| Language Model| The language model to use to generate the structured output.  
input_value| Input message| The input message for the language model to process.  
schema_name| Schema Name| Provide a name for the output data schema.  
output_schema| Output Schema| Define the structure and data types for the model's output.  
multiple| Generate Multiple| Set to True if the model should generate a list of outputs instead of a single output.  
### Output[​](https://docs.langflow.org/<#output> "Direct link to Output")
| structured_output | Structured Output | The resulting structured output based on the defined schema. |
[PreviousEmbeddings](https://docs.langflow.org/</components-embedding-models>)[NextInputs and outputs](https://docs.langflow.org/</components-io>)
  * [Use a helper component in a flow](https://docs.langflow.org/<#use-a-helper-component-in-a-flow>)
  * [Create List](https://docs.langflow.org/<#create-list>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
  * [Current date](https://docs.langflow.org/<#current-date>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [ID Generator](https://docs.langflow.org/<#id-generator>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Message history](https://docs.langflow.org/<#message-history>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Store Message](https://docs.langflow.org/<#store-message>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [Structured output](https://docs.langflow.org/<#structured-output>)
    * [Input](https://docs.langflow.org/<#input>)
    * [Output](https://docs.langflow.org/<#output>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
