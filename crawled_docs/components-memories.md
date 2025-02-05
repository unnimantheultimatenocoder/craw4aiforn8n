[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/</get-started-installation>)
  * [Starter projects](https://docs.langflow.org/</starter-projects-basic-prompting>)
  * [Tutorials](https://docs.langflow.org/</tutorials-blog-writer>)
  * [Concepts](https://docs.langflow.org/</concepts-overview>)
  * [Components](https://docs.langflow.org/</components-agents>)
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
  * [Agents](https://docs.langflow.org/</agents-overview>)
  * [Configuration](https://docs.langflow.org/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Components
  * Memories


On this page
# Memory components in Langflow
Memory components store and retrieve chat messages by `session_id`.
They are distinct from vector store components, because they are built specifically for storing and retrieving chat messages from external databases.
Memory components provide access to their respective external databases **as memory**. This allows Large Language Models (LLMs) or [agents](https://docs.langflow.org/</components-agents>) to access external memory for persistence and context retention.
## Use a memory component in a flow[​](https://docs.langflow.org/<#use-a-memory-component-in-a-flow> "Direct link to Use a memory component in a flow")
This example flow stores and retrieves chat history from an **Astra DB Chat Memory** component with **Store Message** and **Chat Memory** components.
The **Store Message** helper component stores chat memories as [Data](https://docs.langflow.org/</concepts-objects>) objects, and the **Message History** helper component retrieves chat messages as [Data](https://docs.langflow.org/</concepts-objects>) objects or strings.
![Sample Flow storing Chat Memory in AstraDB](https://docs.langflow.org/assets/images/astra_db_chat_memory_rounded-9746ca2bb69d3b07ac0a071f4b9471b3.png)
## AstraDBChatMemory Component[​](https://docs.langflow.org/<#astradbchatmemory-component> "Direct link to AstraDBChatMemory Component")
This component creates an `AstraDBChatMessageHistory` instance, which stores and retrieves chat messages using Astra DB, a cloud-native database service.
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
collection_name| String| Name of the Astra DB collection for storing messages. Required.  
token| SecretString| Authentication token for Astra DB access. Required.  
api_endpoint| SecretString| API endpoint URL for the Astra DB service. Required.  
namespace| String| Optional namespace within Astra DB for the collection.  
session_id| MessageText| Chat session ID. Uses current session ID if not provided.  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
message_history| BaseChatMessageHistory| An instance of AstraDBChatMessageHistory for the session.  
## CassandraChatMemory Component[​](https://docs.langflow.org/<#cassandrachatmemory-component> "Direct link to CassandraChatMemory Component")
This component creates a `CassandraChatMessageHistory` instance, enabling storage and retrieval of chat messages using Apache Cassandra or DataStax Astra DB.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
database_ref| MessageText| Contact points for Cassandra or Astra DB database ID. Required.  
username| MessageText| Username for Cassandra (leave empty for Astra DB).  
token| SecretString| Password for Cassandra or token for Astra DB. Required.  
keyspace| MessageText| Keyspace in Cassandra or namespace in Astra DB. Required.  
table_name| MessageText| Name of the table or collection for storing messages. Required.  
session_id| MessageText| Unique identifier for the chat session. Optional.  
cluster_kwargs| Dictionary| Additional keyword arguments for Cassandra cluster configuration. Optional.  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
message_history| BaseChatMessageHistory| An instance of CassandraChatMessageHistory for the session.  
## ZepChatMemory Component[​](https://docs.langflow.org/<#zepchatmemory-component> "Direct link to ZepChatMemory Component")
This component creates a `ZepChatMessageHistory` instance, enabling storage and retrieval of chat messages using Zep, a memory server for Large Language Models (LLMs).
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
url| MessageText| URL of the Zep instance. Required.  
api_key| SecretString| API Key for authentication with the Zep instance.  
api_base_path| Dropdown| API version to use. Options: "api/v1" or "api/v2".  
session_id| MessageText| Unique identifier for the chat session. Optional.  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
message_history| BaseChatMessageHistory| An instance of ZepChatMessageHistory for the session.  
[PreviousLogic](https://docs.langflow.org/</components-logic>)[NextModels](https://docs.langflow.org/</components-models>)
  * [Use a memory component in a flow](https://docs.langflow.org/<#use-a-memory-component-in-a-flow>)
  * [AstraDBChatMemory Component](https://docs.langflow.org/<#astradbchatmemory-component>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [CassandraChatMemory Component](https://docs.langflow.org/<#cassandrachatmemory-component>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [ZepChatMemory Component](https://docs.langflow.org/<#zepchatmemory-component>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
