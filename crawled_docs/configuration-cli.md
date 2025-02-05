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
  * Langflow CLI


On this page
# Langflow CLI
The Langflow command line interface (Langflow CLI) is the main interface for managing and running the Langflow server.
## CLI commands[​](https://docs.langflow.org/<#cli-commands> "Direct link to CLI commands")
The following sections describe the available CLI commands and their options, as well as their corresponding [environment variables](https://docs.langflow.org/</environment-variables>).
### langflow[​](https://docs.langflow.org/<#langflow> "Direct link to langflow")
Running the CLI without any arguments displays a list of available options and commands.
`
_10
langflow [OPTIONS]
_10
# or
_10
python -m langflow [OPTIONS]
`
#### Options[​](https://docs.langflow.org/<#options> "Direct link to Options")
Option| Default| Values| Description  
---|---|---|---  
`--install-completion`|  _Not applicable_|  _Not applicable_|  Install auto-completion for the current shell.  
`--show-completion`| _Not applicable_|  _Not applicable_|  Show the location of the auto-completion config file (if installed).  
`--help`| _Not applicable_|  _Not applicable_|  Display information about the command usage and its options and arguments.  
### langflow api-key[​](https://docs.langflow.org/<#langflow-api-key> "Direct link to langflow api-key")
Create an API key for the default superuser if the [`LANGFLOW_AUTO_LOGIN` environment variable] is set to `true`.
`
_10
langflow api-key [OPTIONS]
_10
# or
_10
python -m langflow api-key [OPTIONS]
`
#### Options[​](https://docs.langflow.org/<#options-1> "Direct link to Options")
Option| Default| Values| Description  
---|---|---|---  
`--install-completion`|  _Not applicable_|  _Not applicable_|  Install auto-completion for the current shell.  
`--show-completion`| _Not applicable_|  _Not applicable_|  Show the location of the auto-completion config file (if installed).  
`--help`| _Not applicable_|  _Not applicable_|  Display information about the command usage and its options and arguments.  
### langflow copy-db[​](https://docs.langflow.org/<#langflow-copy-db> "Direct link to langflow copy-db")
Copy the database files to the current directory. Copy the Langflow database files, `langflow.db` and `langflow-pre.db` (if they exist), from the cache directory to the current directory.
note
The current directory is the directory containing `__main__.py`. You can find this directory by running `which langflow`.
`
_10
langflow copy-db
_10
# or
_10
python -m langflow copy-db
`
#### Options[​](https://docs.langflow.org/<#options-2> "Direct link to Options")
Option| Default| Values| Description  
---|---|---|---  
`--help`|  _Not applicable_|  _Not applicable_|  Display information about the command usage and its options and arguments.  
### langflow migration[​](https://docs.langflow.org/<#langflow-migration> "Direct link to langflow migration")
Run or test database migrations.
`
_10
langflow migration [OPTIONS]
_10
# or
_10
python -m langflow migration [OPTIONS]
`
#### Options[​](https://docs.langflow.org/<#options-3> "Direct link to Options")
Option| Default| Values| Description  
---|---|---|---  
`--test`| `true`| [Boolean](https://docs.langflow.org/<#boolean>)| Run migrations in test mode. Use `--no-test` to disable test mode.  
`--fix`| `false` (`--no-fix`)| [Boolean](https://docs.langflow.org/<#boolean>)| Fix migrations. This is a destructive operation, and all affected data will be deleted. Only use this option if you know what you are doing.  
`--help`| _Not applicable_|  _Not applicable_|  Display information about the command usage and its options and arguments.  
### langflow run[​](https://docs.langflow.org/<#langflow-run> "Direct link to langflow run")
Start the Langflow server.
`
_10
langflow run [OPTIONS]
_10
# or
_10
python -m langflow run [OPTIONS]
`
#### Options[​](https://docs.langflow.org/<#options-4> "Direct link to Options")
Option| Default| Values| Description  
---|---|---|---  
`--host`| `127.0.0.1`| String| The host on which the Langflow server will run.See `LANGFLOW_HOST`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_HOST>).  
`--workers`| `1`| Integer| Number of worker processes.See `LANGFLOW_WORKERS`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_WORKERS>).  
`--worker-timeout`| `300`| Integer| Worker timeout in seconds.See `LANGFLOW_WORKER_TIMEOUT`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_WORKER_TIMEOUT>).  
`--port`| `7860`| Integer| The port on which the Langflow server will run. The server automatically selects a free port if the specified port is in use.See `LANGFLOW_PORT`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_PORT>).  
`--components-path`| `langflow/components`| String| Path to the directory containing custom components.See `LANGFLOW_COMPONENTS_PATH`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_COMPONENTS_PATH>).  
`--env-file`| Not set| String| Path to the `.env` file containing environment variables.See [Import environment variables from a .env file](https://docs.langflow.org/</environment-variables#configure-variables-env-file>).  
`--log-level`| `critical`| `debug``info``warning``error``critical`| Set the logging level.See `LANGFLOW_LOG_LEVEL`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_LOG_LEVEL>).  
`--log-file`| `logs/langflow.log`| String| Set the path to the log file for Langflow.See `LANGFLOW_LOG_FILE`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_LOG_FILE>).  
`--cache`| `InMemoryCache`| `InMemoryCache``SQLiteCache`| Type of cache to use.See `LANGFLOW_LANGCHAIN_CACHE`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_LANGCHAIN_CACHE>).  
`--dev`| `false` (`--no-dev`)| [Boolean](https://docs.langflow.org/<#boolean>)| Run Langflow in development mode (may contain bugs).See `LANGFLOW_DEV`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_DEV>).  
`--frontend-path`| `./frontend`| String| Path to the frontend directory containing build files. This is for development purposes only.See `LANGFLOW_FRONTEND_PATH`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_FRONTEND_PATH>).  
`--open-browser`| `true`| [Boolean](https://docs.langflow.org/<#boolean>)| Open the system web browser on startup. Use `--no-open-browser` to disable opening the system web browser on startup. See `LANGFLOW_OPEN_BROWSER`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_OPEN_BROWSER>).  
`--remove-api-keys`| `false` (`--no-remove-api-keys`)| [Boolean](https://docs.langflow.org/<#boolean>)| Remove API keys from the projects saved in the database. See `LANGFLOW_REMOVE_API_KEYS`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_REMOVE_API_KEYS>).  
`--backend-only`| `false` (`--no-backend-only`)| [Boolean](https://docs.langflow.org/<#boolean>)| Only run Langflow's backend server (no frontend).See `LANGFLOW_BACKEND_ONLY`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_BACKEND_ONLY>).  
`--store`| `true`| [Boolean](https://docs.langflow.org/<#boolean>)| Enable the Langflow Store features. Use `--no-store` to disable the Langflow Store features.See `LANGFLOW_STORE`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_STORE>).  
`--auto-saving`| `true`| [Boolean](https://docs.langflow.org/<#boolean>)| Enable flow auto-saving. Use `--no-auto-saving` to disable flow auto-saving.See `LANGFLOW_AUTO_SAVING`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_AUTO_SAVING>).  
`--auto-saving-interval`| `1000`| Integer| Set the interval for flow auto-saving in milliseconds.See `LANGFLOW_AUTO_SAVING_INTERVAL`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_AUTO_SAVING_INTERVAL>).  
`--health-check-max-retries`| `5`| Integer| Set the maximum number of retries for the health check. Use `--no-health-check-max-retries` to disable the maximum number of retries for the health check.See `LANGFLOW_HEALTH_CHECK_MAX_RETRIES`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_HEALTH_CHECK_MAX_RETRIES>).  
`--max-file-size-upload`| `100`| Integer| Set the maximum file size for the upload in megabytes.See `LANGFLOW_MAX_FILE_SIZE_UPLOAD`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_MAX_FILE_SIZE_UPLOAD>).  
`--help`| _Not applicable_|  _Not applicable_|  Display information about the command usage and its options and arguments.  
### langflow superuser[​](https://docs.langflow.org/<#langflow-superuser> "Direct link to langflow superuser")
Create a superuser account.
`
_10
langflow superuser [OPTIONS]
_10
# or
_10
python -m langflow superuser [OPTIONS]
`
#### Options[​](https://docs.langflow.org/<#options-5> "Direct link to Options")
Option| Default| Values| Description  
---|---|---|---  
`--username`| Required| String| Specify the name for the superuser.See `LANGFLOW_SUPERUSER`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_SUPERUSER>).  
`--password`| Required| String| Specify the password for the superuser.See `LANGFLOW_SUPERUSER_PASSWORD`[ variable](https://docs.langflow.org/</environment-variables#LANGFLOW_SUPERUSER_PASSWORD>).  
`--log-level`| `critical`| `debug``info``warning``error``critical`| Set the logging level.  
## Precedence[​](https://docs.langflow.org/<#precedence> "Direct link to Precedence")
Langflow CLI options override the values of corresponding [environment variables](https://docs.langflow.org/</environment-variables>).
For example, if you have `LANGFLOW_PORT=7860` defined as an environment variable, but you run the CLI with `--port 7880`, then Langflow will set the port to **`7880`**(the value passed with the CLI).
## Assign values[​](https://docs.langflow.org/<#assign-values> "Direct link to Assign values")
There are two ways you can assign a value to a CLI option. You can write the option flag and its value with a single space between them: `--option value`. Or, you can write them using an equals sign (`=`) between the option flag and the value: `--option=value`.
Values that contain spaces must be surrounded by quotation marks: `--option 'Value with Spaces'` or `--option='Value with Spaces'`.
### Boolean values[​](https://docs.langflow.org/<#boolean> "Direct link to Boolean values")
Boolean options turn a behavior on or off, and therefore accept no arguments. To activate a boolean option, type it on the command line. For example:
`
_10
langflow run --remove-api-keys
`
All boolean options have a corresponding option that negates it. For example, the negating option for `--remove-api-keys` is `--no-remove-api-keys`. These options let you negate boolean options that you may have set using [environment variables](https://docs.langflow.org/</environment-variables>).
[PreviousRun Langflow in backend-only mode](https://docs.langflow.org/</configuration-backend-only>)[NextGlobal variables](https://docs.langflow.org/</configuration-global-variables>)
  * [CLI commands](https://docs.langflow.org/<#cli-commands>)
    * [langflow](https://docs.langflow.org/<#langflow>)
    * [langflow api-key](https://docs.langflow.org/<#langflow-api-key>)
    * [langflow copy-db](https://docs.langflow.org/<#langflow-copy-db>)
    * [langflow migration](https://docs.langflow.org/<#langflow-migration>)
    * [langflow run](https://docs.langflow.org/<#langflow-run>)
    * [langflow superuser](https://docs.langflow.org/<#langflow-superuser>)
  * [Precedence](https://docs.langflow.org/<#precedence>)
  * [Assign values](https://docs.langflow.org/<#assign-values>)
    * [Boolean values](https://docs.langflow.org/<#boolean>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
