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
  * [Agents](https://docs.langflow.org/</agents-overview>)
  * [Configuration](https://docs.langflow.org/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
    * [AssemblyAI](https://docs.langflow.org/</integrations-assemblyai>)
    * [Integrate Composio with Langflow](https://docs.langflow.org/</integrations-composio>)
    * [Langfuse](https://docs.langflow.org/</integrations-langfuse>)
    * [LangSmith](https://docs.langflow.org/</integrations-langsmith>)
    * [LangWatch](https://docs.langflow.org/</integrations-langwatch>)
    * [Google](https://docs.langflow.org/</integrations-setup-google-oauth-langflow>)
    * [Notion](https://docs.langflow.org/</integrations/notion/setup>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Integrations
  * Integrate Composio with Langflow


On this page
# Integrate Composio with Langflow
Langflow integrates with [Composio](https://docs.langflow.org/<https:/docs.composio.dev/introduction/intro/overview>) as a toolset for your **Agent** component.
Instead of juggling multiple integrations and components in your flow, connect the Composio component to an **Agent** component to use all of Composio's supported APIs and actions as **Tools** for your agent.
## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [A Composio API key](https://docs.langflow.org/<https:/app.composio.dev/>)
  * [An OpenAI API key](https://docs.langflow.org/<https:/platform.openai.com/>)
  * [A Gmail account](https://docs.langflow.org/<https:/mail.google.com>)


## Connect Langflow to a Composio tool[​](https://docs.langflow.org/<#connect-langflow-to-a-composio-tool> "Direct link to Connect Langflow to a Composio tool")
  1. In the Langflow **Workspace** , add an **Agent** component.
  2. In the **Workspace** , add the **Composio Tools** component.
  3. Connect the **Agent** component's **Tools** port to the **Composio Tools** component's **Tools** port.
  4. In the **Composio API Key** field, paste your Composio API key. Alternatively, add the key as a [global variable](https://docs.langflow.org/</configuration-global-variables>).
  5. In the **App Name** field, select the tool you want your agent to have access to. For this example, select the **GMAIL** tool, which allows your agent to control an email account with the Composio tool.
  6. Click **Refresh**. The component's fields change based on the tool you selected. The **Gmail** tool requires authentication with Google, so it presents an **Authentication Link** button.
  7. Click the link to authenticate.
  8. In the Google authentication dialog, enter the credentials for the Gmail account you want to control with Composio, and then click **Authenticate**.
  9. Return to Langflow.
  10. To update the Composio component, click **Refresh**. The **Auth Status** field changes to a ✅, which indicates the Langflow component is connected to your Composio account.
  11. In the **Actions to use** field, select the action you want the **Agent** to take with the **Gmail** tool. The **Gmail** tool supports multiple actions, and also supports multiple actions within the same tool. The default value of **GMAIL_CREATE_EMAIL_DRAFT** is OK for this example. For more information, see the [Composio documentation](https://docs.langflow.org/<https:/docs.composio.dev/patterns/tools/use-tools/use-specific-actions>).


## Create a Composio flow[​](https://docs.langflow.org/<#create-a-composio-flow> "Direct link to Create a Composio flow")
  1. In the **Workspace** , add **Chat Input** and **Chat Output** components to your flow.
  2. Connect the components so they look like this.


![Create Composio Flow](https://docs.langflow.org/assets/images/composio-create-flow-1ddd9f8d3ff36ef086400f8d013d11f7.png)
  1. In the **OpenAI API Key** field of the **Agent** component, paste your OpenAI API key. Alternatively, add the key as a [global variable](https://docs.langflow.org/</configuration-global-variables>).
  2. To open the **Playground** pane, click **Playground**.
  3. Ask your AI:


`
_10
What tools are available to you?
`
The response should be similar to:
`
_10
I have access to the following tools:
_10
_10
1. **GMAIL_CREATE_EMAIL_DRAFT**: This tool allows me to create a draft email using Gmail's API. I can specify the recipient's email address, subject, body content, and whether the body content is HTML.
_10
_10
2. **CurrentDate-get_current_date**: This tool retrieves the current date and time in a specified timezone.
`
This confirms your **Agent** and **Composio** are communicating.
  1. Tell your AI to write a draft email.


`
_10
Create a draft email with the subject line "Greetings from Composio"
_10
recipient: "your.email@address.com"
_10
Body content: "Hello from composio!"
`
Inspect the response to see how the agent used the attached tool to write an email. This example response is abbreviated.
`
_10
The draft email has been successfully created with the following details:
_10
Recipient: your.email@address.com
_10
Subject: Greetings from Composio
_10
Body: Hello from composio!
`
`
_23
{
_23
 "recipient_email": "your.email@address.com",
_23
 "subject": "Greetings from Composio",
_23
 "body": "Hello from composio!",
_23
 "is_html": false
_23
}
_23
_23
{
_23
 "successfull": true,
_23
 "data": {
_23
  "response_data": {
_23
   "id": "r-7515791375860110875",
_23
   "message": {
_23
    "id": "1939d1830046d2cb",
_23
    "threadId": "1939d1830046d2cb",
_23
    "labelIds": [
_23
     "DRAFT"
_23
    ]
_23
   }
_23
  }
_23
 },
_23
 "error": null
_23
}
`
  1. To confirm further, navigate to the Gmail account you authenticated with Composio. Your email is visible in **Drafts**.


You have successfully integrated your Langflow component with Composio. To add more tools, add another Composio component.
[PreviousAssemblyAI](https://docs.langflow.org/</integrations-assemblyai>)[NextLangfuse](https://docs.langflow.org/</integrations-langfuse>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Connect Langflow to a Composio tool](https://docs.langflow.org/<#connect-langflow-to-a-composio-tool>)
  * [Create a Composio flow](https://docs.langflow.org/<#create-a-composio-flow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
