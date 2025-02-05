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
  * Notion Conversational Agent


On this page
# Notion Conversational Agent
The Notion Conversational Agent is an AI-powered assistant that interacts with your Notion workspace through natural language conversations. This flow performs Notion-related tasks like creating pages, searching for information, and managing content, all through a chat interface.
## Prerequisites[​](https://docs.langflow.org/integrations/notion/<#prerequisites> "Direct link to Prerequisites")
  * [Notion App](https://docs.langflow.org/integrations/notion/</integrations/notion/setup>)
  * [Notion account and API key](https://docs.langflow.org/integrations/notion/<https:/www.notion.so/my-integrations>)
  * [OpenAI API key](https://docs.langflow.org/integrations/notion/<https:/platform.openai.com/account/api-keys>)
  * [Download Flow Conversation Agent Flow](https://docs.langflow.org/integrations/notion/</assets/files/Conversational_Notion_Agent-7d8e27bbde8676e7772af60972898335.json>)(Download link)


![Notion Components Toolkit](https://docs.langflow.org/assets/images/notion_conversational_agent_tools-6952705eb98e10bd4a67b74500a6189d.png)
## Flow Components[​](https://docs.langflow.org/integrations/notion/<#flow-components> "Direct link to Flow Components")
### Input and Output[​](https://docs.langflow.org/integrations/notion/<#input-and-output> "Direct link to Input and Output")
  * **Chat Input** : Accepts user queries and commands
  * **Chat Output** : Displays the agent's responses


### Language Model[​](https://docs.langflow.org/integrations/notion/<#language-model> "Direct link to Language Model")
  * **OpenAI Model** : Processes user input and generates responses


### Agent and Tools[​](https://docs.langflow.org/integrations/notion/<#agent-and-tools> "Direct link to Agent and Tools")
  * **Tool Calling Agent** : Coordinates the use of various Notion tools based on user input
  * **Toolkit** : Combines multiple Notion-specific tools into a single toolkit
  * **Notion Tools** : Various components for interacting with Notion, including: 
    * List Users
    * List Database Properties
    * List Pages
    * Page Content Viewer
    * Create Page
    * Update Page Property
    * Add Content to Page
    * Search


### Memory and Prompt[​](https://docs.langflow.org/integrations/notion/<#memory-and-prompt> "Direct link to Memory and Prompt")
  * **Chat Memory** : Stores conversation history
  * **Prompt** : Provides system instructions and context for the agent
  * **Current Date** : Supplies the current date and time for context


## Run the Conversational Notion Agent[​](https://docs.langflow.org/integrations/notion/<#run-the-conversational-notion-agent> "Direct link to Run the Conversational Notion Agent")
  1. Open Langflow and create a new project.
  2. Add the components listed above to your flow canvas, or Download the [Conversation Agent Flow](https://docs.langflow.org/integrations/notion/</assets/files/Conversational_Notion_Agent-7d8e27bbde8676e7772af60972898335.json>)(Download link) and **Import** the JSON file into Langflow.
  3. Connect the components as shown in the flow diagram.
  4. Input the Notion and OpenAI API keys in their respective components.
  5. To start the flow, click the "Play" button in Langflow.
  6. In the chat interface, enter a Notion-related request or question. For example: 
     * "Create a new page in my task database"
     * "Search for pages about project management"
     * "List all users in my Notion workspace"
  7. The agent will process your request, use the appropriate Notion tools, and provide a response.
  8. Continue the conversation, asking follow-up questions or giving new commands as needed.


## Example Interactions[​](https://docs.langflow.org/integrations/notion/<#example-interactions> "Direct link to Example Interactions")
`
_46
User: List all the users in my Notion workspace.
_46
_46
Agent: Certainly! I'll use the Notion User List tool to retrieve that information for you. One moment please.
_46
_46
[Agent uses the Notion User List tool]
_46
_46
Here's a list of users in your Notion workspace:
_46
_46
1. John Doe (john@example.com)
_46
2. Jane Smith (jane@example.com)
_46
3. Alex Johnson (alex@example.com)
_46
_46
Is there anything specific you'd like to know about these users or any other Notion-related task I can help you with?
_46
_46
User: Create a new page in my Projects database with the title "Website Redesign".
_46
_46
Agent: Certainly! I'd be happy to create a new page in your Projects database with the title "Website Redesign". I'll use the Notion Page Creator tool to do this. First, let me check the properties of your Projects database to ensure we include all necessary information.
_46
_46
[Agent uses the Notion Database Properties tool]
_46
_46
I've retrieved the properties for your Projects database. Now, I'll create the new page with the title "Website Redesign". One moment please.
_46
_46
[Agent uses the Notion Page Creator tool]
_46
_46
Great news! I've successfully created a new page in your Projects database with the title "Website Redesign". Here are the details:
_46
_46
- Title: Website Redesign
_46
- Page ID: [page_id_here]
_46
- URL: [page_url_here]
_46
_46
Is there any additional information you'd like me to add to this new project page, such as a description, due date, or assigned team members?
_46
_46
User: Yes, please add a description: "Redesign company website to improve user experience and modernize the look."
_46
_46
Agent: Certainly! I'd be happy to add that description to the "Website Redesign" project page. I'll use the Add Content to Page tool to update the page with this information.
_46
_46
[Agent uses the Add Content to Page tool]
_46
_46
I've successfully added the description to your "Website Redesign" project page. Here's a summary of what I've done:
_46
_46
1. Located the "Website Redesign" page using the page ID from our previous interaction.
_46
2. Added the following content to the page:
_46
_46
  Description: Redesign company website to improve user experience and modernize the look.
_46
_46
The description has been added as a new text block on the page. Is there anything else you'd like me to add or modify on this project page?
`
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
[PreviousSetup](https://docs.langflow.org/integrations/notion/</integrations/notion/setup>)[NextNotion Meeting Notes Agent](https://docs.langflow.org/integrations/notion/</integrations/notion/notion-agent-meeting-notes>)
  * [Prerequisites](https://docs.langflow.org/integrations/notion/<#prerequisites>)
  * [Flow Components](https://docs.langflow.org/integrations/notion/<#flow-components>)
    * [Input and Output](https://docs.langflow.org/integrations/notion/<#input-and-output>)
    * [Language Model](https://docs.langflow.org/integrations/notion/<#language-model>)
    * [Agent and Tools](https://docs.langflow.org/integrations/notion/<#agent-and-tools>)
    * [Memory and Prompt](https://docs.langflow.org/integrations/notion/<#memory-and-prompt>)
  * [Run the Conversational Notion Agent](https://docs.langflow.org/integrations/notion/<#run-the-conversational-notion-agent>)
  * [Example Interactions](https://docs.langflow.org/integrations/notion/<#example-interactions>)
  * [Customization](https://docs.langflow.org/integrations/notion/<#customization>)
  * [Troubleshooting](https://docs.langflow.org/integrations/notion/<#troubleshooting>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
