[Skip to main content](https://docs.langflow.org/integrations/notion/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/integrations/notion/</>)
[](https://docs.langflow.org/integrations/notion/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/integrations/notion/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/integrations/notion/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/integrations/notion/</>)
  * [Welcome to Langflow](https://docs.langflow.org/integrations/notion/</>)
  * [Get started](https://docs.langflow.org/integrations/notion/</get-started-installation>)
  * [Starter projects](https://docs.langflow.org/integrations/notion/</starter-projects-basic-prompting>)
  * [Tutorials](https://docs.langflow.org/integrations/notion/</tutorials-blog-writer>)
  * [Concepts](https://docs.langflow.org/integrations/notion/</concepts-overview>)
  * [Components](https://docs.langflow.org/integrations/notion/</components-agents>)
  * [Agents](https://docs.langflow.org/integrations/notion/</agents-overview>)
  * [Configuration](https://docs.langflow.org/integrations/notion/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/integrations/notion/</Deployment/deployment-docker>)
  * [Integrations](https://docs.langflow.org/integrations/notion/</integrations-assemblyai>)
    * [AssemblyAI](https://docs.langflow.org/integrations/notion/</integrations-assemblyai>)
    * [Integrate Composio with Langflow](https://docs.langflow.org/integrations/notion/</integrations-composio>)
    * [Langfuse](https://docs.langflow.org/integrations/notion/</integrations-langfuse>)
    * [LangSmith](https://docs.langflow.org/integrations/notion/</integrations-langsmith>)
    * [LangWatch](https://docs.langflow.org/integrations/notion/</integrations-langwatch>)
    * [Google](https://docs.langflow.org/integrations/notion/</integrations-setup-google-oauth-langflow>)
    * [Notion](https://docs.langflow.org/integrations/notion/</integrations/notion/setup>)
      * [Setup](https://docs.langflow.org/integrations/notion/</integrations/notion/setup>)
      * [Notion Conversational Agent](https://docs.langflow.org/integrations/notion/</integrations/notion/notion-agent-conversational>)
      * [Notion Meeting Notes Agent](https://docs.langflow.org/integrations/notion/</integrations/notion/notion-agent-meeting-notes>)
  * [Contributing](https://docs.langflow.org/integrations/notion/</contributing-community>)
  * [API reference](https://docs.langflow.org/integrations/notion/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/integrations/notion/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/integrations/notion/</>)
  * Integrations
  * Notion
  * Notion Meeting Notes Agent


On this page
# Notion Meeting Notes Agent
The Notion Agent for Meeting Notes is an AI-powered tool that automatically processes meeting transcripts and updates your Notion workspace. It identifies tasks, action items, and key points from your meetings, then creates new tasks or updates existing ones in Notion without manual input.
## Prerequisites[​](https://docs.langflow.org/integrations/notion/<#prerequisites> "Direct link to Prerequisites")
  * [Notion App](https://docs.langflow.org/integrations/notion/</integrations/notion/setup>)
  * [Notion API key](https://docs.langflow.org/integrations/notion/<https:/www.notion.so/my-integrations>)
  * [OpenAI API key](https://docs.langflow.org/integrations/notion/<https:/platform.openai.com/account/api-keys>)
  * [Download Flow Meeting Agent Flow](https://docs.langflow.org/integrations/notion/</assets/files/Meeting_Notes_Agent-b29188c0cb70736d19dd52965db5f352.json>)(Download link)


warning
Before using this flow, ensure you have obtained the necessary API keys from Notion and OpenAI. These keys are essential for the flow to function properly. Keep them secure and do not share them publicly.
## Components[​](https://docs.langflow.org/integrations/notion/<#components> "Direct link to Components")
![Notion Meeting Agent Part 1](https://docs.langflow.org/assets/images/notion_meeting_agent_part_1-58b920a4f8129f18bbf4483b3e3255a5.png)
### Meeting Transcript (Text Input)[​](https://docs.langflow.org/integrations/notion/<#meeting-transcript-text-input> "Direct link to Meeting Transcript \(Text Input\)")
This component allows users to input the meeting transcript directly into the flow.
### List Users (Notion Component)[​](https://docs.langflow.org/integrations/notion/<#list-users-notion-component> "Direct link to List Users \(Notion Component\)")
  * **Purpose** : Retrieves a list of users from the Notion workspace.
  * **Input** : Notion Secret (API key)
  * **Output** : List of user data


### List Databases (Notion Component)[​](https://docs.langflow.org/integrations/notion/<#list-databases-notion-component> "Direct link to List Databases \(Notion Component\)")
  * **Purpose** : Searches and lists all databases in the Notion workspace.
  * **Input** : 
    * Notion Secret (API key)
    * Query (optional)
    * Filter Type (default: database)
    * Sort Direction
  * **Output** : List of database data


### Prompt[​](https://docs.langflow.org/integrations/notion/<#prompt> "Direct link to Prompt")
This component creates a dynamic prompt template using the following inputs:
  * Meeting Transcript
  * List of Users
  * List of Databases
  * Current Date


### Meeting Summarizer (Tool Calling Agent)[​](https://docs.langflow.org/integrations/notion/<#meeting-summarizer-tool-calling-agent> "Direct link to Meeting Summarizer \(Tool Calling Agent\)")
  * **Purpose** : Analyzes the meeting transcript and identifies tasks and action items.
  * **Inputs** : 
    * System Prompt (from the Prompt component)
    * Language Model (OpenAI)
    * Tools: 
      * Notion Search
      * List Database Properties
      * Create Page
      * Update Page Property
      * Add Content to Page


![Notion Meeting Agent Part 2](https://docs.langflow.org/assets/images/notion_meeting_agent_part_2-cbaa61a7a2dc7af1fc8541bfae8491ac.png)
### Notion Agent (Tool Calling Agent)[​](https://docs.langflow.org/integrations/notion/<#notion-agent-tool-calling-agent> "Direct link to Notion Agent \(Tool Calling Agent\)")
  * **Purpose** : Executes actions in Notion based on the meeting summary.
  * **Inputs** : 
    * System Prompt (from the second Prompt component)
    * Language Model (OpenAI)
    * Tools: 
      * List Database Properties
      * Create Page
      * Update Page Property
      * Add Content to Page


### Notion Components (Tools)[​](https://docs.langflow.org/integrations/notion/<#notion-components-tools> "Direct link to Notion Components \(Tools\)")
#### List Database Properties[​](https://docs.langflow.org/integrations/notion/<#list-database-properties> "Direct link to List Database Properties")
  * **Purpose** : Retrieves the properties of a specified Notion database.
  * **Input** : 
    * Database ID
    * Notion Secret (API key)


#### Create Page[​](https://docs.langflow.org/integrations/notion/<#create-page> "Direct link to Create Page")
  * **Purpose** : Creates a new page in a Notion database.
  * **Inputs** : 
    * Database ID
    * Notion Secret (API key)
    * Properties (JSON)


#### Update Page Property[​](https://docs.langflow.org/integrations/notion/<#update-page-property> "Direct link to Update Page Property")
  * **Purpose** : Updates the properties of an existing Notion page.
  * **Inputs** : 
    * Page ID
    * Notion Secret (API key)
    * Properties to update


#### Add Content to Page[​](https://docs.langflow.org/integrations/notion/<#add-content-to-page> "Direct link to Add Content to Page")
  * **Purpose** : Converts markdown text to Notion blocks and appends them to a specified Notion page.
  * **Inputs** : 
    * Page/Block ID
    * Notion Secret (API key)
    * Markdown text


### Chat Output[​](https://docs.langflow.org/integrations/notion/<#chat-output> "Direct link to Chat Output")
Displays the final output of the Notion Agent in the Playground.
## Flow Process[​](https://docs.langflow.org/integrations/notion/<#flow-process> "Direct link to Flow Process")
  1. The user inputs a meeting transcript.
  2. The flow retrieves the list of Notion users and databases.
  3. A prompt is generated using the transcript, user list, database list, and current date.
  4. The Meeting Summarizer analyzes the transcript and identifies tasks and action items.
  5. The Notion Agent uses the meeting summary to: 
     * Create new pages for new tasks
     * Update existing pages for existing tasks
     * Add content to pages with meeting notes
  6. The Chat Output displays a summary of actions taken in Notion.


## Run the Notion Meeting Notes flow[​](https://docs.langflow.org/integrations/notion/<#run-the-notion-meeting-notes-flow> "Direct link to Run the Notion Meeting Notes flow")
To run the Notion Agent for Meeting Notes:
  1. Open Langflow and create a new project.
  2. Add the components listed above to your flow canvas, or download the [Flow Meeting Agent Flow](https://docs.langflow.org/integrations/notion/</assets/files/Meeting_Notes_Agent-b29188c0cb70736d19dd52965db5f352.json>)(Download link) and **Import** the JSON file into Langflow.
  3. Connect the components as shown in the flow diagram.
  4. Input the Notion and OpenAI API keys in their respective components.
  5. Paste your meeting transcript into the Meeting Transcript component.
  6. Run the flow by clicking **Play** on the **Chat Output** component.
  7. Review the output in the Chat Output component, which will summarize the actions taken in your Notion workspace.


For optimal results, use detailed meeting transcripts. The quality of the output depends on the comprehensiveness of the input provided.
## Customization[​](https://docs.langflow.org/integrations/notion/<#customization> "Direct link to Customization")
The flow can be customized to meet your team's specific needs.
Customize this flow by:
  1. Adjusting the system prompt to change the agent's behavior or knowledge base.
  2. Adding or removing Notion tools based on your specific needs.
  3. Modifying the OpenAI model parameters (e.g., temperature) to adjust the agent's response style.


## Troubleshooting[​](https://docs.langflow.org/integrations/notion/<#troubleshooting> "Direct link to Troubleshooting")
If you encounter issues:
  1. Ensure all API keys are correctly set and have the necessary permissions.
  2. Check that your Notion integration has access to the relevant pages and databases.
  3. Verify that all components are properly connected in the flow.
  4. Review the Langflow logs for any error messages.


For more advanced usage and integration options, refer to the [Notion API documentation](https://docs.langflow.org/integrations/notion/<https:/developers.notion.com/>) and [Langflow documentation](https://docs.langflow.org/integrations/notion/</>).
[PreviousNotion Conversational Agent](https://docs.langflow.org/integrations/notion/</integrations/notion/notion-agent-conversational>)[NextJoin the Langflow community](https://docs.langflow.org/integrations/notion/</contributing-community>)
  * [Prerequisites](https://docs.langflow.org/integrations/notion/<#prerequisites>)
  * [Components](https://docs.langflow.org/integrations/notion/<#components>)
    * [Meeting Transcript (Text Input)](https://docs.langflow.org/integrations/notion/<#meeting-transcript-text-input>)
    * [List Users (Notion Component)](https://docs.langflow.org/integrations/notion/<#list-users-notion-component>)
    * [List Databases (Notion Component)](https://docs.langflow.org/integrations/notion/<#list-databases-notion-component>)
    * [Prompt](https://docs.langflow.org/integrations/notion/<#prompt>)
    * [Meeting Summarizer (Tool Calling Agent)](https://docs.langflow.org/integrations/notion/<#meeting-summarizer-tool-calling-agent>)
    * [Notion Agent (Tool Calling Agent)](https://docs.langflow.org/integrations/notion/<#notion-agent-tool-calling-agent>)
    * [Notion Components (Tools)](https://docs.langflow.org/integrations/notion/<#notion-components-tools>)
    * [Chat Output](https://docs.langflow.org/integrations/notion/<#chat-output>)
  * [Flow Process](https://docs.langflow.org/integrations/notion/<#flow-process>)
  * [Run the Notion Meeting Notes flow](https://docs.langflow.org/integrations/notion/<#run-the-notion-meeting-notes-flow>)
  * [Customization](https://docs.langflow.org/integrations/notion/<#customization>)
  * [Troubleshooting](https://docs.langflow.org/integrations/notion/<#troubleshooting>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
