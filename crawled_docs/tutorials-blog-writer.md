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
  * Blog writer


On this page
# Blog writer
Build a Blog Writer flow for a one-shot application using OpenAI.
This flow extends the Basic Prompting flow with the **URL** and **Parse data** components that fetch content from multiple URLs and convert the loaded data into plain text.
OpenAI uses this loaded data to generate a blog post, as instructed by the **Text input** component.
## Prerequisites[​](https://docs.langflow.org/<#899268e6c12c49b59215373a38287507> "Direct link to Prerequisites")
  * [Langflow installed and running](https://docs.langflow.org/</get-started-installation>)
  * [OpenAI API key created](https://docs.langflow.org/<https:/platform.openai.com/>)


## Create the blog writer flow[​](https://docs.langflow.org/<#0c1a9c65b7d640f693ec3aad963416ff> "Direct link to Create the blog writer flow")
  1. From the Langflow dashboard, click **New Flow**.
  2. Select **Blog Writer**.
  3. The **Blog Writer** flow is created.


![](https://docs.langflow.org/assets/images/starter-flow-blog-writer-05ef4634a1c68dba46a1144f98116700.png)
This flow creates a one-shot article generator with **Prompt** , **OpenAI** , and **Chat Output** components, augmented with reference content and instructions from the **URL** and **Text Input** components.
The **URL** component extracts raw text and metadata from one or more web links. The **Parse Data** component converts the data coming from the **URL** component into plain text to feed the prompt.
To examine the flow's prompt, click the **Template** field of the **Prompt** component.
`
1
Reference 1:
23
{references}
45
---
67
{instructions}
89
Blog:
`
The `{instructions}` value is received from the **Text input** component, and one or more `{references}` are received from a list of URLs parsed from the **URL** component.
### Run the blog writer flow[​](https://docs.langflow.org/<#b93be7a567f5400293693b31b8d0f81a> "Direct link to Run the blog writer flow")
  1. Click the **Playground** button. Here you can chat with the AI that has access to the **URL** content.
  2. Click the **Lighting Bolt** icon to run it.
  3. To write about something different, change the values in the **URL** component and adjust the instructions on the left side bar of the **Playground**. Try again and see what the LLM constructs.


[PreviousSimple agent](https://docs.langflow.org/</starter-projects-simple-agent>)[NextDocument QA](https://docs.langflow.org/</tutorials-document-qa>)
  * [Prerequisites](https://docs.langflow.org/<#899268e6c12c49b59215373a38287507>)
  * [Create the blog writer flow](https://docs.langflow.org/<#0c1a9c65b7d640f693ec3aad963416ff>)
    * [Run the blog writer flow](https://docs.langflow.org/<#b93be7a567f5400293693b31b8d0f81a>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
