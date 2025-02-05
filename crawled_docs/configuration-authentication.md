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
  * Authentication


On this page
# Authentication
The login functionality in Langflow serves to authenticate users and protect sensitive routes in the application.
## Create a superuser and new users in Langflow[​](https://docs.langflow.org/<#create-a-superuser-and-new-users-in-langflow> "Direct link to Create a superuser and new users in Langflow")
Learn how to create a new superuser, log in to Langflow, and add new users.
  1. Create a `.env` file and open it in your preferred editor.
  2. Add the following environment variables to your file.


`
1
LANGFLOW_AUTO_LOGIN=False
2
LANGFLOW_SUPERUSER=admin
3
LANGFLOW_SUPERUSER_PASSWORD=securepassword
4
LANGFLOW_SECRET_KEY=randomly_generated_secure_key
5
LANGFLOW_NEW_USER_IS_ACTIVE=False
`
For more information, see [Authentication configuration values](https://docs.langflow.org/<#values>).
tip
The Langflow project includes a `.env.example`[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/.env.example>) file to help you get started. You can copy the contents of this file into your own `.env` file and replace the example values with your own preferred settings.
  1. Save your `.env` file.
  2. Run Langflow with the configured environment variables.


`
1
python -m langflow run --env-file .env
`
  1. Sign in with your username `admin` and password `securepassword`.
  2. To open the **Admin Page** , click your user profile image, and then select **Admin Page**. You can also go to `http://127.0.0.1:7861/admin`.
  3. To add a new user, click **New User** , and then add the **Username** and **Password**.
  4. To activate the new user, select **Active**. The user can only sign in if you select them as **Active**.
  5. To give the user `superuser` privileges, click **Superuser**.
  6. Click **Save**.
  7. To confirm your new user has been created, sign out of Langflow, and then sign back in using your new **Username** and **Password**.


## Manage Superuser with the Langflow CLI[​](https://docs.langflow.org/<#manage-superuser-with-the-langflow-cli> "Direct link to Manage Superuser with the Langflow CLI")
Langflow provides a command-line utility for interactively creating superusers:
  1. Enter the CLI command:


`
1
langflow superuser
`
  1. Langflow prompts you for a **Username** and **Password** :


`
1
langflow superuser
2
Username: new_superuser_1
3
Password:
4
Default folder created successfully.
5
Superuser created successfully.
`
  1. To confirm your new superuser was created successfully, go to the **Admin Page** at `http://127.0.0.1:7861/admin`.


## Authentication configuration values[​](https://docs.langflow.org/<#values> "Direct link to Authentication configuration values")
The following table lists the available authentication configuration variables, their descriptions, and default values:
Variable| Description| Default  
---|---|---  
`LANGFLOW_AUTO_LOGIN`| Enables automatic login| `True`  
`LANGFLOW_SUPERUSER`| Superuser username| -  
`LANGFLOW_SUPERUSER_PASSWORD`| Superuser password| -  
`LANGFLOW_SECRET_KEY`| Key for encrypting superuser password| -  
`LANGFLOW_NEW_USER_IS_ACTIVE`| Automatically activates new users| `False`  
### LANGFLOW_AUTO_LOGIN[​](https://docs.langflow.org/<#langflow_auto_login> "Direct link to LANGFLOW_AUTO_LOGIN")
By default, this variable is set to `True`. When enabled, Langflow operates as it did in versions prior to 0.5, including automatic login without requiring explicit user authentication.
To disable automatic login and enforce user authentication:
`
1
LANGFLOW_AUTO_LOGIN=False
`
### LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD[​](https://docs.langflow.org/<#langflow_superuser-and-langflow_superuser_password> "Direct link to LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD")
These environment variables are only relevant when LANGFLOW_AUTO_LOGIN is set to False. They specify the username and password for the superuser, which is essential for administrative tasks. To create a superuser manually:
`
1
LANGFLOW_SUPERUSER=admin
2
LANGFLOW_SUPERUSER_PASSWORD=securepassword
`
### LANGFLOW_SECRET_KEY[​](https://docs.langflow.org/<#langflow_secret_key> "Direct link to LANGFLOW_SECRET_KEY")
This environment variable holds a secret key used for encrypting sensitive data like API keys.
`
1
LANGFLOW_SECRET_KEY=dBuuuB_FHLvU8T9eUNlxQF9ppqRxwWpXXQ42kM2_fb
`
Langflow uses the [Fernet](https://docs.langflow.org/<https:/pypi.org/project/cryptography/>) library for secret key encryption.
### Create a LANGFLOW_SECRET_KEY[​](https://docs.langflow.org/<#create-a-langflow_secret_key> "Direct link to Create a LANGFLOW_SECRET_KEY")
The `LANGFLOW_SECRET_KEY` is used for encrypting sensitive data. It must be:
  * At least 32 bytes long
  * URL-safe base64 encoded


  1. To create a `LANGFLOW_SECRET_KEY`, run the following command:


  * macOS/Linux
  * Windows


`
1
# Copy to clipboard (macOS)
2
python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | pbcopy
34
# Copy to clipboard (Linux)
5
python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | xclip -selection clipboard
67
# Or just print
8
python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')"
`
`
_10
# Copy to clipboard
_10
python -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | clip
_10
_10
# Or just print
_10
python -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')"
`
The command generates a secure key like `dBuuuB_FHLvU8T9eUNlxQF9ppqRxwWpXXQ42kM2_fbg`. Treat the generated secure key as you would an application access token. Do not commit the key to code and keep it in a safe place.
  1. Create a `.env` file with the following configuration, and include your generated secret key value.


`
1
LANGFLOW_AUTO_LOGIN=False
2
LANGFLOW_SUPERUSER=admin
3
LANGFLOW_SUPERUSER_PASSWORD=securepassword
4
LANGFLOW_SECRET_KEY=dBuuuB_FHLvU8T9eUNlxQF9ppqRxwWpXXQ42kM2_fbg # Your generated key
5
LANGFLOW_NEW_USER_IS_ACTIVE=False
`
  1. Start Langflow with the values from your `.env` file.


`
1
uv run langflow run --env-file .env
`
The generated secret key value is now used to encrypt your global variables.
If no key is provided, Langflow will automatically generate a secure key. This is not recommended for production environments, because in a multi-instance deployment like Kubernetes, auto-generated keys won't be able to decrypt data encrypted by other instances. Instead, you should explicitly set the `LANGFLOW_SECRET_KEY` environment variable in the deployment configuration to be the same across all instances.
### LANGFLOW_NEW_USER_IS_ACTIVE[​](https://docs.langflow.org/<#langflow_new_user_is_active> "Direct link to LANGFLOW_NEW_USER_IS_ACTIVE")
By default, this variable is set to `False`. When enabled, new users are automatically activated and can log in without requiring explicit activation by the superuser.
`
1
LANGFLOW_NEW_USER_IS_ACTIVE=False
`
[PreviousAPI keys](https://docs.langflow.org/</configuration-api-keys>)[NextAuto-saving](https://docs.langflow.org/</configuration-auto-save>)
  * [Create a superuser and new users in Langflow](https://docs.langflow.org/<#create-a-superuser-and-new-users-in-langflow>)
  * [Manage Superuser with the Langflow CLI](https://docs.langflow.org/<#manage-superuser-with-the-langflow-cli>)
  * [Authentication configuration values](https://docs.langflow.org/<#values>)
    * [LANGFLOW_AUTO_LOGIN](https://docs.langflow.org/<#langflow_auto_login>)
    * [LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD](https://docs.langflow.org/<#langflow_superuser-and-langflow_superuser_password>)
    * [LANGFLOW_SECRET_KEY](https://docs.langflow.org/<#langflow_secret_key>)
    * [Create a LANGFLOW_SECRET_KEY](https://docs.langflow.org/<#create-a-langflow_secret_key>)
    * [LANGFLOW_NEW_USER_IS_ACTIVE](https://docs.langflow.org/<#langflow_new_user_is_active>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b8d4b727-604d-4efc-a764-7597bcfb1490&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f4b22b45-3974-45bd-b6d4-01a1a51e5499&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fconfiguration-authentication&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b8d4b727-604d-4efc-a764-7597bcfb1490&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f4b22b45-3974-45bd-b6d4-01a1a51e5499&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fconfiguration-authentication&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
