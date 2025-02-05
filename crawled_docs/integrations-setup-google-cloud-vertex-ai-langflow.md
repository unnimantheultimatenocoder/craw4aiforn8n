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
      * [Integrate Google OAuth with Langflow](https://docs.langflow.org/</integrations-setup-google-oauth-langflow>)
      * [Integrate Google Cloud Vertex AI with Langflow](https://docs.langflow.org/</integrations-setup-google-cloud-vertex-ai-langflow>)
    * [Notion](https://docs.langflow.org/</integrations/notion/setup>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Integrations
  * Google
  * Integrate Google Cloud Vertex AI with Langflow


On this page
# Integrate Google Cloud Vertex AI with Langflow
Langflow integrates with the [Google Vertex AI API](https://docs.langflow.org/<https:/console.cloud.google.com/marketplace/product/google/aiplatform.googleapis.com>) for authenticating the [Vertex AI embeddings model](https://docs.langflow.org/</components-embedding-models#vertexai-embeddings>) and [Vertex AI](https://docs.langflow.org/</components-models#vertexai>) components.
Learn how to create a service account JSON in Google Cloud to authenticate Langflow’s Vertex AI components.
## Create a service account with Vertex AI access[​](https://docs.langflow.org/<#create-a-service-account-with-vertex-ai-access> "Direct link to Create a service account with Vertex AI access")
  1. Select and enable your Google Cloud project. For more information, see [Create a Google Cloud project](https://docs.langflow.org/<https:/developers.google.com/workspace/guides/create-project>).
  2. Create a service account in your Google Cloud project. For more information, see [Create a service account](https://docs.langflow.org/<https:/developers.google.com/workspace/guides/create-credentials#service-account>).
  3. Assign the **Vertex AI Service Agent** role to your new account. This role allows Langflow to access Vertex AI resources. For more information, see [Vertex AI access control with IAM](https://docs.langflow.org/<https:/cloud.google.com/vertex-ai/docs/general/access-control>).
  4. To generate a new JSON key for the service account, navigate to your service account.
  5. Click **Add Key** , and then click **Create new key**.
  6. Under **Key type** , select **JSON** , and then click **Create**. A JSON private key file is downloaded. Now that you have a service account and a JSON private key, you need to configure the credentials in Langflow components.


## Configure credentials in Langflow components[​](https://docs.langflow.org/<#configure-credentials-in-langflow-components> "Direct link to Configure credentials in Langflow components")
With your service account configured and your credentials JSON file created, follow these steps to authenticate the Langflow application.
  1. Create a new project in Langflow.
  2. From the components sidebar, drag and drop either the **Vertex AI** or **Vertex AI Embeddings** component to your workspace.
  3. In the Vertex AI component's **Credentials** field, add the service account JSON file.
  4. Confirm the component can access the Vertex AI resources. Connect a **Chat input** and **Chat output** component to the Vertex AI component. A successful chat confirms the component has access to the Vertex AI resources.


![Configure Vertex AI Credentials in Langflow](https://docs.langflow.org/assets/images/configure-vertex-ai-credentials-in-langflow-10c417c45f725fee46d4ef5f740316b3.gif)
[PreviousIntegrate Google OAuth with Langflow](https://docs.langflow.org/</integrations-setup-google-oauth-langflow>)[NextSetup](https://docs.langflow.org/</integrations/notion/setup>)
  * [Create a service account with Vertex AI access](https://docs.langflow.org/<#create-a-service-account-with-vertex-ai-access>)
  * [Configure credentials in Langflow components](https://docs.langflow.org/<#configure-credentials-in-langflow-components>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
