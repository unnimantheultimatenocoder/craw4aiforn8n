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
    * [Langflow overview](https://docs.langflow.org/</concepts-overview>)
    * [Playground](https://docs.langflow.org/</concepts-playground>)
    * [Components](https://docs.langflow.org/</concepts-components>)
    * [Flows](https://docs.langflow.org/</Concepts/concepts-flows>)
    * [Langflow objects](https://docs.langflow.org/</concepts-objects>)
    * [API pane](https://docs.langflow.org/</concepts-api>)
  * [Components](https://docs.langflow.org/</components-agents>)
  * [Agents](https://docs.langflow.org/</agents-overview>)
  * [Configuration](https://docs.langflow.org/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Concepts
  * Playground


On this page
# Playground
The **Playground** is a dynamic interface designed for real-time interaction with LLMs, allowing users to chat, access memories, and monitor inputs and outputs. Here, users can directly prototype their models, making adjustments and observing different outcomes.
As long as you have an [Input or Output](https://docs.langflow.org/</components-io>) component working, you can open it by clicking the **Playground** button. The Playground's window arrangement changes depending on what components are being used.
![](https://docs.langflow.org/assets/images/playground-b2c623fb6849024570bc9bd5285309f5.png)
## Run a flow in the playgound[​](https://docs.langflow.org/<#run-a-flow-in-the-playgound> "Direct link to Run a flow in the playgound")
When you run a flow in the **Playground** , Langflow calls the `/build/{flow_id}/flow` endpoint in [chat.py](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/api/v1/chat.py#L162>). This call retrieves the flow data, builds a graph, and executes the graph. As each component (or node) is executed, the `build_vertex` function calls `build_and_run`, which may call the individual components' `def_build` method, if it exists. If a component doesn't have a `def_build` function, the build still returns a component.
The `build` function allows components to execute logic at runtime. For example, the [Recursive character text splitter](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/components/langchain_utilities/recursive_character.py>) is a child of the `LCTextSplitterComponent` class. When text needs to be processed, the parent class's `build` method is called, which creates a `RecursiveCharacterTextSplitter` object and uses it to split the text according to the defined parameters. The split text is then passed on to the next component. This all occurs when the component is built.
## View playground messages by session ID[​](https://docs.langflow.org/<#view-playground-messages-by-session-id> "Direct link to View playground messages by session ID")
When you send a message from the **Playground** interface, the interactions are stored in the **Message Logs** by `session_id`. A single flow can have multiple chats, and different flows can share the same chat. Each chat will have a different `session_id`.
To view messages by `session_id` within the Playground, click the menu of any chat session, and then select **Message Logs**.
![](https://docs.langflow.org/assets/images/messages-logs-aec5213dc668ee51c2a40eab2ba0718c.png)
Individual messages in chat memory can be edited or deleted. Modifying these memories influences the behavior of the chatbot responses.
To learn more about chat memories in Langflow, see [Memory components](https://docs.langflow.org/</components-memories>).
## Use custom Session IDs for multiple user interactions[​](https://docs.langflow.org/<#use-custom-session-ids-for-multiple-user-interactions> "Direct link to Use custom Session IDs for multiple user interactions")
`session_id` values are used to track user interactions in a flow. By default, if the `session_id` value is empty, it is set to the same value as the `flow_id`. In this case, every chat call uses the same `session_id`, and you effectively have one chat session.
The `session_id` value can be configured in the **Advanced Settings** of the **Chat Input** and **Chat Output** components.
To have more than one session in a single flow, pass a specific Session ID to a flow with the `session_id` parameter in the URL. All the components in the flow will automatically use this `session_id` value.
To post a message to a flow with a specific Session ID with curl, enter the following command:
`
_10
  curl -X POST "http://127.0.0.1:7860/api/v1/run/$FLOW_ID" \
_10
  -H 'Content-Type: application/json' \
_10
  -d '{
_10
    "session_id": "custom_session_123",
_10
    "input_value": "message",
_10
    "input_type": "chat",
_10
    "output_type": "chat"
_10
  }'
`
Check your flow's **Playground**. In addition to the messages stored for the Default Session, a new session is started with your custom Session ID.
[PreviousLangflow overview](https://docs.langflow.org/</concepts-overview>)[NextComponents](https://docs.langflow.org/</concepts-components>)
  * [Run a flow in the playgound](https://docs.langflow.org/<#run-a-flow-in-the-playgound>)
  * [View playground messages by session ID](https://docs.langflow.org/<#view-playground-messages-by-session-id>)
  * [Use custom Session IDs for multiple user interactions](https://docs.langflow.org/<#use-custom-session-ids-for-multiple-user-interactions>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
