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
  * Vector store RAG


On this page
# Vector store RAG
Retrieval Augmented Generation, or RAG, is a pattern for training LLMs on your data and querying it.
RAG is backed by a **vector store** , a vector database which stores embeddings of the ingested data.
This enables **vector search** , a more powerful and context-aware search.
We've chosen [Astra DB](https://docs.langflow.org/<https:/astra.datastax.com/signup?utm_source=langflow-pre-release&utm_medium=referral&utm_campaign=langflow-announcement&utm_content=create-a-free-astra-db-account>) as the vector database for this starter flow, but you can follow along with any of Langflow's vector database options.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [An OpenAI API key](https://docs.langflow.org/<https:/platform.openai.com/>)
  * [An Astra DB vector database](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/get-started/quickstart.html>) with: 
    * An Astra DB application token
    * [A collection in Astra](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/manage-collections.html#create-collection>)


## Open Langflow and start a new project[​](https://docs.langflow.org/<#open-langflow-and-start-a-new-project> "Direct link to Open Langflow and start a new project")
  1. From the Langflow dashboard, click **New Flow**.
  2. Select **Vector Store RAG**.
  3. The **Vector Store RAG** flow is created.


## Build the vector RAG flow[​](https://docs.langflow.org/<#build-the-vector-rag-flow> "Direct link to Build the vector RAG flow")
The vector store RAG flow is built of two separate flows for ingestion and query.
![](https://docs.langflow.org/assets/images/starter-flow-vector-rag-d83743e5e049082b9c7a37aaa7b930e9.png)
The **Load Data Flow** (bottom of the screen) creates a searchable index to be queried for contextual similarity. This flow populates the vector store with data from a local file. It ingests data from a local file, splits it into chunks, indexes it in Astra DB, and computes embeddings for the chunks using the OpenAI embeddings model.
The **Retriever Flow** (top of the screen) embeds the user's queries into vectors, which are compared to the vector store data from the **Load Data Flow** for contextual similarity.
  * **Chat Input** receives user input from the **Playground**.
  * **OpenAI Embeddings** converts the user query into vector form.
  * **Astra DB** performs similarity search using the query vector.
  * **Parse Data** processes the retrieved chunks.
  * **Prompt** combines the user query with relevant context.
  * **OpenAI** generates the response using the prompt.
  * **Chat Output** returns the response to the **Playground**.


  1. Configure the **OpenAI** model component. 
    1. To create a global variable for the **OpenAI** component, in the **OpenAI API Key** field, click the **Globe** button, and then click **Add New Variable**.
    2. In the **Variable Name** field, enter `openai_api_key`.
    3. In the **Value** field, paste your OpenAI API Key (`sk-...`).
    4. Click **Save Variable**.
  2. Configure the **Astra DB** component. 
    1. In the **Astra DB Application Token** field, add your **Astra DB** application token. The component connects to your database and populates the menus with existing databases and collections.
    2. Select your **Database**.
    3. Select your **Collection**. Collections are created in your [Astra DB deployment](https://docs.langflow.org/<https:/astra.datastax.com>) for storing vector data. If you don't have a collection, see the [DataStax Astra DB Serverless documentation](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/manage-collections.html#create-collection>).
    4. Select **Embedding Model** to bring your own embeddings model, which is the connected **OpenAI Embeddings** component. The **Dimensions** value must match the dimensions of your collection. You can find this value in the **Collection** in your [Astra DB deployment](https://docs.langflow.org/<https:/astra.datastax.com>).


If you used Langflow's **Global Variables** feature, the RAG application flow components are already configured with the necessary credentials.
## Run the Vector Store RAG flow[​](https://docs.langflow.org/<#run-the-vector-store-rag-flow> "Direct link to Run the Vector Store RAG flow")
  1. Click the **Playground** button. Here you can chat with the AI that uses context from the database you created.
  2. Type a message and press Enter. (Try something like "What topics do you know about?")
  3. The bot will respond with a summary of the data you've embedded.


[PreviousBasic prompting](https://docs.langflow.org/</starter-projects-basic-prompting>)[NextSimple agent](https://docs.langflow.org/</starter-projects-simple-agent>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Open Langflow and start a new project](https://docs.langflow.org/<#open-langflow-and-start-a-new-project>)
  * [Build the vector RAG flow](https://docs.langflow.org/<#build-the-vector-rag-flow>)
  * [Run the Vector Store RAG flow](https://docs.langflow.org/<#run-the-vector-store-rag-flow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
