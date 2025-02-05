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
  * Document QA


On this page
# Document QA
Build a question-and-answer chatbot with a document loaded from local memory.
## Prerequisites[​](https://docs.langflow.org/<#6555c100a30e4a21954af25e2e05403a> "Direct link to Prerequisites")
  * [Langflow installed and running](https://docs.langflow.org/</get-started-installation>)
  * [OpenAI API key created](https://docs.langflow.org/<https:/platform.openai.com/>)


## Create the document QA flow[​](https://docs.langflow.org/<#204500104f024553aab2b633bb99f603> "Direct link to Create the document QA flow")
  1. From the Langflow dashboard, click **New Flow**.
  2. Select **Document QA**.
  3. The **Document QA** flow is created.


![](https://docs.langflow.org/assets/images/starter-flow-document-qa-5bcc799ecdc4c136281079972402019b.png)
This flow is composed of a standard chatbot with the **Chat Input** , **Prompt** , **OpenAI** , and **Chat Output** components, but it also incorporates a **File** component, which loads a file from your local machine. **Parse Data** is used to convert the data from **File** into the **Prompt** component as `{Document}`. The **Prompt** component is instructed to answer questions based on the contents of `{Document}`. This gives the **OpenAI** component context it would not otherwise have access to.
### Run the document QA flow[​](https://docs.langflow.org/<#f58fcc2b9e594156a829b1772b6a7191> "Direct link to Run the document QA flow")
  1. To select a document to load, in the **File** component, click the **Path** field. Select a local file, and then click **Open**. The file name appears in the field.
  2. Click the **Playground** button. Here you can chat with the AI that has access to your document's content.
  3. Type in a question about the document content and press Enter. You should see a contextual response.


[PreviousBlog writer](https://docs.langflow.org/</tutorials-blog-writer>)[NextMemory chatbot](https://docs.langflow.org/</tutorials-memory-chatbot>)
  * [Prerequisites](https://docs.langflow.org/<#6555c100a30e4a21954af25e2e05403a>)
  * [Create the document QA flow](https://docs.langflow.org/<#204500104f024553aab2b633bb99f603>)
    * [Run the document QA flow](https://docs.langflow.org/<#f58fcc2b9e594156a829b1772b6a7191>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
