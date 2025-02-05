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
  * Memory chatbot


On this page
# Memory chatbot
This flow extends the [basic prompting flow](https://docs.langflow.org/</starter-projects-basic-prompting>) with a **Chat memory** component that stores up to 100 previous chat messages and uses them to provide context for the current conversation.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [Langflow installed and running](https://docs.langflow.org/</get-started-installation>)
  * [OpenAI API key created](https://docs.langflow.org/<https:/platform.openai.com/>)


## Create the memory chatbot flow[​](https://docs.langflow.org/<#create-the-memory-chatbot-flow> "Direct link to Create the memory chatbot flow")
  1. From the Langflow dashboard, click **New Flow**.
  2. Select **Memory Chatbot**.
  3. The **Memory Chatbot** flow is created.


![](https://docs.langflow.org/assets/images/starter-flow-memory-chatbot-af37fecb79d125009712e4c1128bc461.png)
This flow adds a **Chat Memory** component to the Basic Prompting flow. This component retrieves previous messages and sends them to the **Prompt** component to fill a part of the **Template** with context.
To examine the template, click the **Template** field in the **Prompt** component. The **Prompt** tells the **OpenAI model** component how to respond to input.
`
1
You are a helpful assistant that answers questions.
23
Use markdown to format your answer, properly embedding images and urls.
45
History:
67
{memory}
`
The `{memory}` code in the prompt creates a new input port in the component called **memory**. The **Chat Memory** component is connected to this port to store chat messages from the **Playground**.
This gives the **OpenAI** component a memory of previous chat messages.
## Run the memory chatbot flow[​](https://docs.langflow.org/<#run-the-memory-chatbot-flow> "Direct link to Run the memory chatbot flow")
  1. Open the **Playground**.
  2. Type multiple questions. For example, try entering this conversation:


`
1
Hi, my name is Luca.
2
Please tell me about PostgreSQL.
3
What is my name?
4
What is the second subject I asked you about?
`
The chatbot remembers your name and previous questions.
  1. To view the **Message Logs** pane, click , and then click **Message Logs**. The **Message Logs** pane displays all previous messages, with each conversation sorted by `session_id`.


![](https://docs.langflow.org/assets/images/messages-logs-aec5213dc668ee51c2a40eab2ba0718c.png)
## Use Session ID with the memory chatbot flow[​](https://docs.langflow.org/<#use-session-id-with-the-memory-chatbot-flow> "Direct link to Use Session ID with the memory chatbot flow")
`session_id` is a unique identifier in Langflow that stores conversation sessions between the AI and a user. A `session_id` is created when a conversation is initiated, and then associated with all subsequent messages during that session.
In the **Memory Chatbot** flow you created, the **Chat Memory** component references past interactions by **Session ID**. You can demonstrate this by modifying the **Session ID** value to switch between conversation histories.
  1. In the **Session ID** field of the **Chat Memory** and **Chat Input** components, add a **Session ID** value like `MySessionID`.
  2. Now, once you send a new message the **Playground** , you should have a new memory created on the **Memories** tab.
  3. Notice how your conversation is being stored in different memory sessions.


Learn more about chat memories in the [Memory](https://docs.langflow.org/</components-memories>) section.
[PreviousDocument QA](https://docs.langflow.org/</tutorials-document-qa>)[NextMath agent](https://docs.langflow.org/</tutorials-math-agent>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Create the memory chatbot flow](https://docs.langflow.org/<#create-the-memory-chatbot-flow>)
  * [Run the memory chatbot flow](https://docs.langflow.org/<#run-the-memory-chatbot-flow>)
  * [Use Session ID with the memory chatbot flow](https://docs.langflow.org/<#use-session-id-with-the-memory-chatbot-flow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
