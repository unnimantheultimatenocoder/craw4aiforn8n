[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/<#>)
    * [Install Langflow](https://docs.langflow.org/</get-started-installation>)
    * [Quickstart](https://docs.langflow.org/</get-started-quickstart>)
  * [Starter projects](https://docs.langflow.org/<#>)
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
  * Get started
  * Quickstart


On this page
# Quickstart
Get to know Langflow by building an OpenAI-powered chatbot application. After you've constructed a chatbot, add Retrieval Augmented Generation (RAG) to chat with your own data.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [An OpenAI API key](https://docs.langflow.org/<https:/platform.openai.com/>)
  * [An Astra DB vector database](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/get-started/quickstart.html>) with: 
    * An AstraDB application token
    * [A collection in Astra](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/manage-collections.html#create-collection>)


## Open Langflow and start a new project[​](https://docs.langflow.org/<#open-langflow-and-start-a-new-project> "Direct link to Open Langflow and start a new project")
  1. From the Langflow dashboard, click **New Flow** , and then select **Blank Flow**. A blank workspace opens where you can build your flow.


tip
If you don't want to create a blank flow, click **New Flow** , and then select **Basic Prompting** for a pre-built flow. Continue to [Run the basic prompting flow](https://docs.langflow.org/<#run-basic-prompting-flow>).
  1. Select **Basic Prompting**.
  2. The **Basic Prompting** flow is created.


## Build the basic prompting flow[​](https://docs.langflow.org/<#build-the-basic-prompting-flow> "Direct link to Build the basic prompting flow")
The Basic Prompting flow will look like this when it's completed:
![](https://docs.langflow.org/assets/images/starter-flow-basic-prompting-09331815d7282bd6a3feedf84838ba20.png)
To build the **Basic Prompting** flow, follow these steps:
  1. Click **Inputs** , select the **Chat Input** component, and then drag it to the canvas. The [Chat Input](https://docs.langflow.org/</components-io#chat-input>) component accepts user input to the chat.
  2. Click **Prompt** , select the **Prompt** component, and then drag it to the canvas. The [Prompt](https://docs.langflow.org/</components-prompts>) component combines the user input with a user-defined prompt.
  3. Click **Outputs** , select the **Chat Output** component, and then drag it to the canvas. The [Chat Output](https://docs.langflow.org/</components-io#chat-output>) component prints the flow's output to the chat.
  4. Click **Models** , select the **OpenAI** component, and then drag it to the canvas. The [OpenAI](https://docs.langflow.org/</components-models#openai>) model component sends the user input and prompt to the OpenAI API and receives a response.


You should now have a flow that looks like this:
![](https://docs.langflow.org/assets/images/quickstart-basic-prompt-no-connections-f5887f67c3448c39b74f7e28b65a0b18.png)
With no connections between them, the components won't interact with each other. You want data to flow from **Chat Input** to **Chat Output** through the connections between the components. Each component accepts inputs on its left side, and sends outputs on its right side. Hover over the connection ports to see the data types that the component accepts. For more on component inputs and outputs, see [Components overview](https://docs.langflow.org/</concepts-components>).
  1. To connect the **Chat Input** component to the OpenAI model component, click and drag a line from the blue **Message** port to the OpenAI model component's **Input** port.
  2. To connect the **Prompt** component to the OpenAI model component, click and drag a line from the blue **Prompt Message** port to the OpenAI model component's **System Message** port.
  3. To connect the **OpenAI** model component to the **Chat Output** , click and drag a line from the blue **Text** port to the **Chat Output** component's **Text** port.


Your finished basic prompting flow should look like this:
![](https://docs.langflow.org/assets/images/starter-flow-basic-prompting-09331815d7282bd6a3feedf84838ba20.png)
### Run the Basic Prompting flow[​](https://docs.langflow.org/<#run-basic-prompting-flow> "Direct link to Run the Basic Prompting flow")
Add your OpenAI API key to the OpenAI model component, and add a prompt to the Prompt component to instruct the model how to respond.
  1. Add your credentials to the OpenAI component. The fastest way to complete these fields is with Langflow’s [Global Variables](https://docs.langflow.org/</configuration-global-variables>).
    1. In the OpenAI component’s OpenAI API Key field, click the **Globe** button, and then click **Add New Variable**. Alternatively, click your username in the top right corner, and then click **Settings** , **Global Variables** , and then **Add New**.
    2. Name your variable. Paste your OpenAI API key (sk-…​) in the Value field.
    3. In the **Apply To Fields** field, select the OpenAI API Key field to apply this variable to all OpenAI Embeddings components.
  2. To add a prompt to the **Prompt** component, click the **Template** field, and then enter your prompt. The prompt guides the bot's responses to input. If you're unsure, use `Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.`
  3. Click **Playground** to start a chat session.
  4. Enter a query, and then make sure the bot responds according to the prompt you set in the **Prompt** component.


You have successfully created a chatbot application using OpenAI in the Langflow Workspace.
## Add vector RAG to your application[​](https://docs.langflow.org/<#add-vector-rag-to-your-application> "Direct link to Add vector RAG to your application")
You created a chatbot application with Langflow, but let's try an experiment.
  1. Ask the bot: `Who won the Oscar in 2024 for best movie?`
  2. The bot's response is similar to this:


`
1
I'm sorry, but I don't have information on events or awards that occurred after
2
October 2023, including the Oscars in 2024.
3
You may want to check the latest news or the official Oscars website
4
for the most current information.
`
Well, that's unfortunate, but you can load more up-to-date data with **Retrieval Augmented Generation** , or **RAG**.
Vector RAG allows you to load your own data and chat with it, unlocking a wider range of possibilities for your chatbot application.
## Add vector RAG with the Astra DB component[​](https://docs.langflow.org/<#add-vector-rag-with-the-astra-db-component> "Direct link to Add vector RAG with the Astra DB component")
Build on the basic prompting flow and add vector RAG to your chatbot application with the **Astra DB Vector Store** component.
Add document ingestion to your basic prompting flow, with the **Astra DB** component as the vector store.
tip
If you don't want to create a blank flow, click **New Flow** , and then select **Vector RAG** for a pre-built flow.
Adding vector RAG to the basic prompting flow will look like this when completed:
![](https://docs.langflow.org/assets/images/quickstart-add-document-ingestion-5f9756b0a4b7e232b1507e12f335b15e.png)
To build the flow, follow these steps:
  1. Disconnect the **Chat Input** component from the **OpenAI** component by double-clicking on the connecting line.
  2. Click **Vector Stores** , select the **Astra DB** component, and then drag it to the canvas. The [Astra DB vector store](https://docs.langflow.org/</components-vector-stores#astra-db-vector-store>) component connects to your **Astra DB** database.
  3. Click **Data** , select the **File** component, and then drag it to the canvas. The [File](https://docs.langflow.org/</components-data#file>) component loads files from your local machine.
  4. Click **Processing** , select the **Split Text** component, and then drag it to the canvas. The [Split Text](https://docs.langflow.org/</components-processing#split-text>) component splits the loaded text into smaller chunks.
  5. Click **Processing** , select the **Parse Data** component, and then drag it to the canvas. The [Parse Data](https://docs.langflow.org/</components-processing#parse-data>) component converts the data from the **Astra DB** component into plain text.
  6. Click **Embeddings** , select the **OpenAI Embeddings** component, and then drag it to the canvas. The [OpenAI Embeddings](https://docs.langflow.org/</components-embedding-models#openai-embeddings>) component generates embeddings for the user's input, which are compared to the vector data in the database.
  7. Connect the new components into the existing flow, so your flow looks like this:


![](https://docs.langflow.org/assets/images/quickstart-add-document-ingestion-5f9756b0a4b7e232b1507e12f335b15e.png)
  1. Configure the **Astra DB** component. 
    1. In the **Astra DB Application Token** field, add your **Astra DB** application token. The component connects to your database and populates the menus with existing databases and collections.
    2. Select your **Database**.
    3. Select your **Collection**. Collections are created in your [Astra DB deployment](https://docs.langflow.org/<https:/astra.datastax.com>) for storing vector data. If you don't have a collection, see the [DataStax Astra DB Serverless documentation](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/manage-collections.html#create-collection>).
    4. Select **Embedding Model** to bring your own embeddings model, which is the connected **OpenAI Embeddings** component. The **Dimensions** value must match the dimensions of your collection. This value can be found in your **Collection** in your [Astra DB deployment](https://docs.langflow.org/<https:/astra.datastax.com>).


If you used Langflow's **Global Variables** feature, the RAG application flow components are already configured with the necessary credentials.
### Run the chatbot with retrieved context[​](https://docs.langflow.org/<#run-the-chatbot-with-retrieved-context> "Direct link to Run the chatbot with retrieved context")
  1. Modify the **Prompt** component to contain variables for both `{user_question}` and `{context}`. The `{context}` variable gives the bot additional context for answering `{user_question}` beyond what the LLM was trained on.


`
1
Given the context
2
{context}
3
Answer the question
4
{user_question}
`
  1. In the **File** component, upload a text file from your local machine with data you want to ingest into the **Astra DB** component database. This example uploads an up-to-date CSV about Oscar winners.
  2. Click **Playground** to start a chat session.
  3. Ask the bot: `Who won the Oscar in 2024 for best movie?`
  4. The bot's response should be similar to this:


`
1
The Oscar for Best Picture in 2024 was awarded to "Oppenheimer,"
2
produced by Emma Thomas, Charles Roven, and Christopher Nolan.
`
Adding an **Astra DB** vector store brought your chatbot all the way into 2024. You have successfully added RAG to your chatbot application using the **Astra DB** component.
## Next steps[​](https://docs.langflow.org/<#next-steps> "Direct link to Next steps")
This example used movie data, but the RAG pattern can be used with any data you want to load and chat with.
Make the **Astra DB** database the brain that [Agents](https://docs.langflow.org/</agents-overview>) use to make decisions.
Expose this flow as an [API](https://docs.langflow.org/</concepts-api>) and call it from your external applications.
For more on the **Astra DB** component, see [Astra DB vector store](https://docs.langflow.org/</components-vector-stores#astra-db-vector-store>).
[PreviousInstall Langflow](https://docs.langflow.org/</get-started-installation>)[NextBasic prompting](https://docs.langflow.org/</starter-projects-basic-prompting>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Open Langflow and start a new project](https://docs.langflow.org/<#open-langflow-and-start-a-new-project>)
  * [Build the basic prompting flow](https://docs.langflow.org/<#build-the-basic-prompting-flow>)
    * [Run the Basic Prompting flow](https://docs.langflow.org/<#run-basic-prompting-flow>)
  * [Add vector RAG to your application](https://docs.langflow.org/<#add-vector-rag-to-your-application>)
  * [Add vector RAG with the Astra DB component](https://docs.langflow.org/<#add-vector-rag-with-the-astra-db-component>)
    * [Run the chatbot with retrieved context](https://docs.langflow.org/<#run-the-chatbot-with-retrieved-context>)
  * [Next steps](https://docs.langflow.org/<#next-steps>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=3f1ad5e0-1c99-430c-85c8-166440a6f56f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=74d02a41-092f-4845-86db-ef0296487386&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fget-started-quickstart&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=3f1ad5e0-1c99-430c-85c8-166440a6f56f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=74d02a41-092f-4845-86db-ef0296487386&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fget-started-quickstart&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
