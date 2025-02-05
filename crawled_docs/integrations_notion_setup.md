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
  * Setup


On this page
# Set up a Notion App
To use Notion components in Langflow, you first need to create a Notion integration and configure it with the necessary capabilities. This guide will walk you through the process of setting up a Notion integration and granting it access to your Notion databases.
## Prerequisites[​](https://docs.langflow.org/integrations/notion/<#prerequisites> "Direct link to Prerequisites")
  * A Notion account with access to the workspace where you want to use the integration.
  * Admin permissions in the Notion workspace to create and manage integrations.


## Create a Notion Integration[​](https://docs.langflow.org/integrations/notion/<#create-a-notion-integration> "Direct link to Create a Notion Integration")
  1. Go to the [Notion Integrations](https://docs.langflow.org/integrations/notion/<https:/www.notion.com/my-integrations>) page.
  2. Click on the "New integration" button.
  3. Give your integration a name and select the workspace where you want to use it.
  4. Click "Submit" to create the integration.


info
When creating the integration, make sure to enable the necessary capabilities based on your requirements. Refer to the [Notion Integration Capabilities](https://docs.langflow.org/integrations/notion/<https:/developers.notion.com/reference/capabilities>) documentation for more information on each capability.
## Configure Integration Capabilities[​](https://docs.langflow.org/integrations/notion/<#configure-integration-capabilities> "Direct link to Configure Integration Capabilities")
After creating the integration, you need to configure its capabilities to define what actions it can perform and what data it can access.
  1. In the integration settings page, go to the **Capabilities** tab.
  2. Enable the required capabilities for your integration. For example: 
     * If your integration needs to read data from Notion, enable the "Read content" capability.
     * If your integration needs to create new content in Notion, enable the "Insert content" capability.
     * If your integration needs to update existing content in Notion, enable the "Update content" capability.
  3. Configure the user information access level based on your integration's requirements.
  4. Save the changes.


## Obtain Integration Token[​](https://docs.langflow.org/integrations/notion/<#obtain-integration-token> "Direct link to Obtain Integration Token")
To authenticate your integration with Notion, you need to obtain an integration token.
  1. In the integration settings page, go to the "Secrets" tab.
  2. Copy the "Internal Integration Token" value. This token will be used to authenticate your integration with Notion.


warning
Your integration token is a sensitive piece of information. Make sure to keep it secure and never share it publicly. Store it safely in your Langflow configuration or environment variables.
## Grant Integration Access to Notion Databases[​](https://docs.langflow.org/integrations/notion/<#grant-integration-access-to-notion-databases> "Direct link to Grant Integration Access to Notion Databases")
For your integration to interact with Notion databases, you need to grant it access to the specific databases it will be working with.
  1. Open the Notion database that you want your integration to access.
  2. Click on the "Share" button in the top-right corner of the page.
  3. In the "Invite" section, select your integration from the list.
  4. Click "Invite" to grant the integration access to the database.


info
If your database contains references to other databases, you need to grant the integration access to those referenced databases as well. Repeat step 4 for each referenced database to ensure your integration has the necessary access.
## Build with Notion Components in Langflow[​](https://docs.langflow.org/integrations/notion/<#build-with-notion-components-in-langflow> "Direct link to Build with Notion Components in Langflow")
Once you have set up your Notion integration and granted it access to the required databases, you can start using the Notion components in Langflow.
Langflow provides the following Notion components:
  * **Search** : Searches all pages and databases that have been shared with the integration. You can filter results to either pages or databases and specify the sort direction.
  * **List Users** : Retrieves a list of users from the Notion workspace.
  * **List Database Properties** : Retrieves the properties of a specified Notion database.
  * **Create Page** : Creates a new page in a specified Notion database with the provided properties.
  * **Update Page Property** : Updates the properties of an existing Notion page.
  * **Add Content to Page** : Converts markdown text to Notion blocks and appends them to a specified Notion page.
  * **List Pages** : Queries a Notion database with filtering and sorting options.
  * **Page Content Viewer** : Retrieves the content of a Notion page as plain text.


Each of these components output both "Data" and "Tool":
  * The "Data" output can be used directly in your Langflow for further processing or display.
  * The "Tool" output can be utilized in Langflow Agents, allowing them to interact with Notion programmatically.


## Additional Resources[​](https://docs.langflow.org/integrations/notion/<#additional-resources> "Direct link to Additional Resources")
  * [Notion API Documentation](https://docs.langflow.org/integrations/notion/<https:/developers.notion.com/docs/getting-started>)
  * [Notion Integration Capabilities](https://docs.langflow.org/integrations/notion/<https:/developers.notion.com/reference/capabilities>)


If you encounter any issues or have questions, please reach out to our support team or consult the Langflow community forums.
[PreviousIntegrate Google Cloud Vertex AI with Langflow](https://docs.langflow.org/integrations/notion/</integrations-setup-google-cloud-vertex-ai-langflow>)[NextNotion Conversational Agent](https://docs.langflow.org/integrations/notion/</integrations/notion/notion-agent-conversational>)
  * [Prerequisites](https://docs.langflow.org/integrations/notion/<#prerequisites>)
  * [Create a Notion Integration](https://docs.langflow.org/integrations/notion/<#create-a-notion-integration>)
  * [Configure Integration Capabilities](https://docs.langflow.org/integrations/notion/<#configure-integration-capabilities>)
  * [Obtain Integration Token](https://docs.langflow.org/integrations/notion/<#obtain-integration-token>)
  * [Grant Integration Access to Notion Databases](https://docs.langflow.org/integrations/notion/<#grant-integration-access-to-notion-databases>)
  * [Build with Notion Components in Langflow](https://docs.langflow.org/integrations/notion/<#build-with-notion-components-in-langflow>)
  * [Additional Resources](https://docs.langflow.org/integrations/notion/<#additional-resources>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
