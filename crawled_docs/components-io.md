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
  * Inputs and outputs


On this page
# Input and output components in Langflow
This category of components defines where data enters and exits your flow. They dynamically alter the Playground and can be renamed to facilitate building and maintaining your flows.
The difference between Chat Input and Text Input components is the output format, the number of configurable fields, and the way they are displayed in the Playground.
## Chat Input[​](https://docs.langflow.org/<#chat-input> "Direct link to Chat Input")
This component collects user input from the chat.
The Chat Input component creates a [Message](https://docs.langflow.org/</concepts-objects>) object that includes the input text, sender information, session ID, file attachments, and styling properties. It can optionally store the message in a chat history and supports customization of the message appearance.
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Display Name| Info| Type  
---|---|---|---  
input_value| Text| Message to be passed as input.| MultilineInput  
should_store_message| Store Messages| Store the message in the history.| BoolInput  
sender| Sender Type| Type of sender.| DropdownInput  
sender_name| Sender Name| Name of the sender.| MessageTextInput  
session_id| Session ID| The session ID of the chat. If empty, the current session ID parameter will be used.| MessageTextInput  
files| Files| Files to be sent with the message.| FileInput  
background_color| Background Color| The background color of the icon.| MessageTextInput  
chat_icon| Icon| The icon of the message.| MessageTextInput  
text_color| Text Color| The text color of the name| MessageTextInput  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
message| Message| The resulting chat message object with all specified properties.  
## Text Input[​](https://docs.langflow.org/<#text-input> "Direct link to Text Input")
The Text Input component adds an Input field on the Playground.
The Text Input component offers one input field for text, while the Chat Input has multiple fields for various chat-related features.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Display Name| Info| Type  
---|---|---|---  
input_value| Text| Text to be passed as input.| MultilineInput  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
text| Text| The resulting text message.  
## Chat Output[​](https://docs.langflow.org/<#chat-output> "Direct link to Chat Output")
The Chat Output component creates a [Message](https://docs.langflow.org/</concepts-objects>) object that includes the input text, sender information, session ID, and styling properties. It can optionally store the message in a chat history and supports customization of the message appearance, including background color, icon, and text color.
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info| Type  
---|---|---|---  
input_value| Text| Message to be passed as output.| MessageInput  
should_store_message| Store Messages| Store the message in the history.| BoolInput  
sender| Sender Type| Type of sender.| DropdownInput  
sender_name| Sender Name| Name of the sender.| MessageTextInput  
session_id| Session ID| The session ID of the chat. If empty, the current session ID parameter will be used.| MessageTextInput  
data_template| Data Template| Template to convert data to text. If left empty, it will be dynamically set to the data's text key.| MessageTextInput  
background_color| Background Color| The background color of the icon.| MessageTextInput  
chat_icon| Icon| The icon of the message.| MessageTextInput  
text_color| Text Color| The text color of the name| MessageTextInput  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
message| Message| The resulting chat message object with all specified properties.  
## Text Output[​](https://docs.langflow.org/<#text-output> "Direct link to Text Output")
The TextOutputComponent displays text output in the **Playground**. It takes a single input of text and returns a [Message](https://docs.langflow.org/</concepts-objects>) object containing that text. The component is simpler compared to the Chat Output but focuses solely on displaying text without additional chat-specific features or customizations.
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Display Name| Info| Type  
---|---|---|---  
input_value| Text| Text to be passed as output.| MultilineInput  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
text| Text| The resulting text message.  
[PreviousHelpers](https://docs.langflow.org/</components-helpers>)[NextLoaders](https://docs.langflow.org/</components-loaders>)
  * [Chat Input](https://docs.langflow.org/<#chat-input>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [Text Input](https://docs.langflow.org/<#text-input>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Chat Output](https://docs.langflow.org/<#chat-output>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Text Output](https://docs.langflow.org/<#text-output>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
