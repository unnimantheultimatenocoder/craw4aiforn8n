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
    * [API keys](https://docs.langflow.org/</configuration-api-keys>)
    * [Authentication](https://docs.langflow.org/</configuration-authentication>)
    * [Auto-saving](https://docs.langflow.org/</configuration-auto-save>)
    * [Run Langflow in backend-only mode](https://docs.langflow.org/</configuration-backend-only>)
    * [Langflow CLI](https://docs.langflow.org/</configuration-cli>)
    * [Global variables](https://docs.langflow.org/</configuration-global-variables>)
    * [Environment variables](https://docs.langflow.org/</environment-variables>)
    * [Security best practices](https://docs.langflow.org/</configuration-security-best-practices>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Configuration
  * Security best practices


On this page
# Security best practices
This guide outlines security best practices for deploying and managing Langflow.
## Secret key protection[​](https://docs.langflow.org/<#secret-key-protection> "Direct link to Secret key protection")
The secret key is critical for encrypting sensitive data in Langflow. Follow these guidelines:
  * Always use a custom secret key in production:
`
_10
LANGFLOW_SECRET_KEY=your-secure-secret-key
`
  * Store the secret key securely:
    * Use environment variables or secure secret management systems.
    * Never commit the secret key to version control.
    * Regularly rotate the secret key.
  * Use the default secret key locations:
    * macOS: `~/Library/Caches/langflow/secret_key`
    * Linux: `~/.cache/langflow/secret_key`
    * Windows: `%USERPROFILE%\AppData\Local\langflow\secret_key`


## API keys and credentials[​](https://docs.langflow.org/<#api-keys-and-credentials> "Direct link to API keys and credentials")
  * Store API keys and credentials as encrypted global variables.
  * Use the Credential type for sensitive information.
  * Implement proper access controls for users who can view/edit credentials.
  * Regularly audit and rotate API keys.


## Database file protection[​](https://docs.langflow.org/<#database-file-protection> "Direct link to Database file protection")
  * Store the database in a secure location:
`
_10
LANGFLOW_SAVE_DB_IN_CONFIG_DIR=true
_10
LANGFLOW_CONFIG_DIR=/secure/path/to/config
`
  * Use the default database locations:
    * macOS/Linux: `PYTHON_LOCATION/site-packages/langflow/langflow.db`
    * Windows: `PYTHON_LOCATION\Lib\site-packages\langflow\langflow.db`


[PreviousEnvironment variables](https://docs.langflow.org/</environment-variables>)[NextDocker](https://docs.langflow.org/</Deployment/deployment-docker>)
  * [Secret key protection](https://docs.langflow.org/<#secret-key-protection>)
  * [API keys and credentials](https://docs.langflow.org/<#api-keys-and-credentials>)
  * [Database file protection](https://docs.langflow.org/<#database-file-protection>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
