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
  * Environment variables


On this page
# Environment variables
Langflow lets you configure a number of settings using environment variables.
## Configure environment variables[​](https://docs.langflow.org/<#configure-environment-variables> "Direct link to Configure environment variables")
Langflow recognizes [supported environment variables](https://docs.langflow.org/<#supported-variables>) from the following sources:
  * Environment variables that you've set in your terminal.
  * Environment variables that you've imported from a `.env` file using the `--env-file` option in the Langflow CLI.


You can choose to use one source exclusively, or use both sources together. If you choose to use both sources together, be aware that environment variables imported from a `.env` file take [precedence](https://docs.langflow.org/<#precedence>) over those set in your terminal.
### Set environment variables in your terminal[​](https://docs.langflow.org/<#configure-variables-terminal> "Direct link to Set environment variables in your terminal")
Run the following commands to set environment variables for your current terminal session:
  * Linux or macOS
  * Windows
  * Docker


`
_10
export VARIABLE_NAME='VALUE'
`
`
_10
set VARIABLE_NAME='VALUE'
`
`
_10
docker run -it --rm \
_10
  -p 7860:7860 \
_10
  -e VARIABLE_NAME='VALUE' \
_10
  langflowai/langflow:latest
`
When you start Langflow, it looks for environment variables that you've set in your terminal. If it detects a supported environment variable, then it automatically adopts the specified value, subject to [precedence rules](https://docs.langflow.org/<#precedence>).
### Import environment variables from a .env file[​](https://docs.langflow.org/<#configure-variables-env-file> "Direct link to Import environment variables from a .env file")
  1. Create a `.env` file and open it in your preferred editor.
  2. Add your environment variables to the file:
`
_10
VARIABLE_NAME='VALUE'
_10
VARIABLE_NAME='VALUE'
`
tip
The Langflow project includes a `.env.example`[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/.env.example>) file to help you get started. You can copy the contents of this file into your own `.env` file and replace the example values with your own preferred settings.
  3. Save and close the file.
  4. Start Langflow using the `--env-file` option to define the path to your `.env` file:
     * Local
     * Docker
`
_10
python -m langflow run --env-file .env
`
`
_10
docker run -it --rm \
_10
  -p 7860:7860 \
_10
  --env-file .env \
_10
  langflowai/langflow:latest
`


On startup, Langflow imports the environment variables from your `.env` file, as well as any that you [set in your terminal](https://docs.langflow.org/<#configure-variables-terminal>), and adopts their specified values.
## Precedence[​](https://docs.langflow.org/<#precedence> "Direct link to Precedence")
Environment variables [defined in the .env file](https://docs.langflow.org/<#configure-variables-env-file>) take precedence over those [set in your terminal](https://docs.langflow.org/<#configure-variables-terminal>). That means, if you happen to set the same environment variable in both your terminal and your `.env` file, Langflow adopts the value from the the `.env` file.
CLI precedence
[Langflow CLI options](https://docs.langflow.org/</configuration-cli>) override the value of corresponding environment variables defined in the `.env` file as well as any environment variables set in your terminal.
## Supported environment variables[​](https://docs.langflow.org/<#supported-variables> "Direct link to Supported environment variables")
The following table lists the environment variables supported by Langflow.
Variable| Format / Values| Default| Description  
---|---|---|---  
`DO_NOT_TRACK`| Boolean| `false`| If enabled, Langflow will not track telemetry.  
`LANGFLOW_AUTO_LOGIN`| Boolean| `true`| Enable automatic login for Langflow. Set to `false` to disable automatic login and require the login form to log into the Langflow UI. Setting to `false` requires `LANGFLOW_SUPERUSER`[](https://docs.langflow.org/<#LANGFLOW_SUPERUSER>) and `LANGFLOW_SUPERUSER_PASSWORD`[](https://docs.langflow.org/</environment-variables#LANGFLOW_SUPERUSER_PASSWORD>) to be set.  
`LANGFLOW_AUTO_SAVING`| Boolean| `true`| Enable flow auto-saving.See `--auto-saving`[ option](https://docs.langflow.org/</configuration-cli#run-auto-saving>).  
`LANGFLOW_AUTO_SAVING_INTERVAL`| Integer| `1000`| Set the interval for flow auto-saving in milliseconds.See `--auto-saving-interval`[ option](https://docs.langflow.org/</configuration-cli#run-auto-saving-interval>).  
`LANGFLOW_BACKEND_ONLY`| Boolean| `false`| Only run Langflow's backend server (no frontend).See `--backend-only`[ option](https://docs.langflow.org/</configuration-cli#run-backend-only>).  
`LANGFLOW_CACHE_TYPE`| `async``redis``memory``disk``critical`| `async`| Set the cache type for Langflow.If you set the type to `redis`, then you must also set the following environment variables: `LANGFLOW_REDIS_HOST`[](https://docs.langflow.org/<#LANGFLOW_REDIS_HOST>), `LANGFLOW_REDIS_PORT`[](https://docs.langflow.org/<#LANGFLOW_REDIS_PORT>), `LANGFLOW_REDIS_DB`[](https://docs.langflow.org/<#LANGFLOW_REDIS_DB>), and `LANGFLOW_REDIS_CACHE_EXPIRE`[](https://docs.langflow.org/<#LANGFLOW_REDIS_CACHE_EXPIRE>).  
`LANGFLOW_COMPONENTS_PATH`| String| `langflow/components`| Path to the directory containing custom components.See `--components-path`[ option](https://docs.langflow.org/</configuration-cli#run-components-path>).  
`LANGFLOW_CONFIG_DIR`| String| **Linux/WSL** : `~/.cache/langflow/`**macOS** : `/Users/<username>/Library/Caches/langflow/`**Windows** : `%LOCALAPPDATA%\langflow\langflow\Cache`| Set the Langflow configuration directory where files, logs, and the Langflow database are stored.  
`LANGFLOW_DATABASE_URL`| String| Not set| Set the database URL for Langflow. If not provided, Langflow will use a SQLite database.  
`LANGFLOW_DATABASE_CONNECTION_RETRY`| Boolean| `false`| If True, Langflow will retry to connect to the database if it fails.  
`LANGFLOW_DB_POOL_SIZE`| Integer| `10`| **DEPRECATED:** Use `LANGFLOW_DB_CONNECTION_SETTINGS` instead. The number of connections to keep open in the connection pool.  
`LANGFLOW_DB_MAX_OVERFLOW`| Integer| `20`| **DEPRECATED:** Use `LANGFLOW_DB_CONNECTION_SETTINGS` instead. The number of connections to allow that can be opened beyond the pool size.  
`LANGFLOW_DB_CONNECT_TIMEOUT`| Integer| `20`| The number of seconds to wait before giving up on a lock to be released or establishing a connection to the database.  
`LANGFLOW_DB_CONNECTION_SETTINGS`| JSON| Not set| A JSON dictionary to centralize database connection parameters. Example: `{"pool_size": 10, "max_overflow": 20}`  
`LANGFLOW_DEV`| Boolean| `false`| Run Langflow in development mode (may contain bugs).See `--dev`[ option](https://docs.langflow.org/</configuration-cli#run-dev>).  
`LANGFLOW_FALLBACK_TO_ENV_VAR`| Boolean| `true`| If enabled, [global variables](https://docs.langflow.org/</configuration-global-variables>) set in the Langflow UI fall back to an environment variable with the same name when Langflow fails to retrieve the variable value.  
`LANGFLOW_FRONTEND_PATH`| String| `./frontend`| Path to the frontend directory containing build files. This is for development purposes only.See `--frontend-path`[ option](https://docs.langflow.org/</configuration-cli#run-frontend-path>).  
`LANGFLOW_HEALTH_CHECK_MAX_RETRIES`| Integer| `5`| Set the maximum number of retries for the health check.See `--health-check-max-retries`[ option](https://docs.langflow.org/</configuration-cli#run-health-check-max-retries>).  
`LANGFLOW_HOST`| String| `127.0.0.1`| The host on which the Langflow server will run.See `--host`[ option](https://docs.langflow.org/</configuration-cli#run-host>).  
`LANGFLOW_LANGCHAIN_CACHE`| `InMemoryCache``SQLiteCache`| `InMemoryCache`| Type of cache to use.See `--cache`[ option](https://docs.langflow.org/</configuration-cli#run-cache>).  
`LANGFLOW_MAX_FILE_SIZE_UPLOAD`| Integer| `100`| Set the maximum file size for the upload in megabytes.See `--max-file-size-upload`[ option](https://docs.langflow.org/</configuration-cli#run-max-file-size-upload>).  
`LANGFLOW_MCP_SERVER_ENABLED`| Boolean| `true`| If set to False, Langflow will not enable the MCP server.  
`LANGFLOW_MCP_SERVER_ENABLE_PROGRESS_NOTIFICATIONS`| Boolean| `false`| If set to True, Langflow will send progress notifications in the MCP server.  
`LANGFLOW_NEW_USER_IS_ACTIVE`| Boolean| `false`| When enabled, new users are automatically activated and can log in without requiring explicit activation by the superuser.  
`LANGFLOW_OPEN_BROWSER`| Boolean| `false`| Open the system web browser on startup.See `--open-browser`[ option](https://docs.langflow.org/</configuration-cli#run-open-browser>).  
`LANGFLOW_PORT`| Integer| `7860`| The port on which the Langflow server will run. The server automatically selects a free port if the specified port is in use.See `--port`[ option](https://docs.langflow.org/</configuration-cli#run-port>).  
`LANGFLOW_PROMETHEUS_ENABLED`| Boolean| `false`| Expose Prometheus metrics.  
`LANGFLOW_PROMETHEUS_PORT`| Integer| `9090`| Set the port on which Langflow exposes Prometheus metrics.  
`LANGFLOW_REDIS_CACHE_EXPIRE`| Integer| `3600`| See `LANGFLOW_CACHE_TYPE`[](https://docs.langflow.org/<#LANGFLOW_CACHE_TYPE>).  
`LANGFLOW_REDIS_DB`| Integer| `0`| See `LANGFLOW_CACHE_TYPE`[](https://docs.langflow.org/<#LANGFLOW_CACHE_TYPE>).  
`LANGFLOW_REDIS_HOST`| String| `localhost`| See `LANGFLOW_CACHE_TYPE`[](https://docs.langflow.org/<#LANGFLOW_CACHE_TYPE>).  
`LANGFLOW_REDIS_PORT`| String| `6379`| See `LANGFLOW_CACHE_TYPE`[](https://docs.langflow.org/<#LANGFLOW_CACHE_TYPE>).  
`LANGFLOW_REMOVE_API_KEYS`| Boolean| `false`| Remove API keys from the projects saved in the database.See `--remove-api-keys`[ option](https://docs.langflow.org/</configuration-cli#run-remove-api-keys>).  
`LANGFLOW_SAVE_DB_IN_CONFIG_DIR`| Boolean| `false`| Save the Langflow database in `LANGFLOW_CONFIG_DIR`[](https://docs.langflow.org/<#LANGFLOW_CONFIG_DIR>) instead of in the Langflow package directory. Note, when this variable is set to default (`false`), the database isn't shared between different virtual environments and the database is deleted when you uninstall Langflow.  
`LANGFLOW_SECRET_KEY`| String| Auto-generated| Key used for encrypting sensitive data like API keys. If not provided, a secure key will be auto-generated. For production environments with multiple instances, you should explicitly set this to ensure consistent encryption across instances.  
`LANGFLOW_STORE`| Boolean| `true`| Enable the Langflow Store.See `--store`[ option](https://docs.langflow.org/</configuration-cli#run-store>).  
`LANGFLOW_STORE_ENVIRONMENT_VARIABLES`| Boolean| `true`| Store environment variables as [global variables](https://docs.langflow.org/</configuration-global-variables>) in the database.  
`LANGFLOW_SUPERUSER`| String| `langflow`| Set the name for the superuser. Required if `LANGFLOW_AUTO_LOGIN`[](https://docs.langflow.org/<#LANGFLOW_AUTO_LOGIN>) is set to `false`.See `superuser --username`[ option](https://docs.langflow.org/</configuration-cli#superuser-username>).  
`LANGFLOW_SUPERUSER_PASSWORD`| String| `langflow`| Set the password for the superuser. Required if `LANGFLOW_AUTO_LOGIN`[](https://docs.langflow.org/<#LANGFLOW_AUTO_LOGIN>) is set to `false`.See `superuser --password`[ option](https://docs.langflow.org/</configuration-cli#superuser-password>).  
`LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT`| String| Not set| Comma-separated list of environment variables to get from the environment and store as [global variables](https://docs.langflow.org/</configuration-global-variables>).  
`LANGFLOW_LOAD_FLOWS_PATH`| String| Not set| Path to a directory containing flow JSON files to be loaded on startup. Note that this feature only works if `LANGFLOW_AUTO_LOGIN` is enabled.  
`LANGFLOW_WORKER_TIMEOUT`| Integer| `300`| Worker timeout in seconds.See `--worker-timeout`[ option](https://docs.langflow.org/</configuration-cli#run-worker-timeout>).  
`LANGFLOW_WORKERS`| Integer| `1`| Number of worker processes.See `--workers`[ option](https://docs.langflow.org/</configuration-cli#run-workers>).  
[PreviousGlobal variables](https://docs.langflow.org/</configuration-global-variables>)[NextSecurity best practices](https://docs.langflow.org/</configuration-security-best-practices>)
  * [Configure environment variables](https://docs.langflow.org/<#configure-environment-variables>)
    * [Set environment variables in your terminal](https://docs.langflow.org/<#configure-variables-terminal>)
    * [Import environment variables from a .env file](https://docs.langflow.org/<#configure-variables-env-file>)
  * [Precedence](https://docs.langflow.org/<#precedence>)
  * [Supported environment variables](https://docs.langflow.org/<#supported-variables>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ef4baef0-6e23-474d-af8c-f70844a04869&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4f161f19-9fed-4795-a880-75bd0c22075a&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fenvironment-variables&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=ef4baef0-6e23-474d-af8c-f70844a04869&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4f161f19-9fed-4795-a880-75bd0c22075a&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fenvironment-variables&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
