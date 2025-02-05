[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/<#>)
    * [Install Langflow](https://docs.langflow.org/</get-started-installation>)
    * [Quickstart](https://docs.langflow.org/</get-started-quickstart>)
  * [Starter projects](https://docs.langflow.org/<#>)
  * [Tutorials](https://docs.langflow.org/<#>)
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
  * Get started
  * Install Langflow


On this page
# Install Langflow
You can deploy Langflow either locally or as a hosted service with [**Datastax Langflow**](https://docs.langflow.org/<#datastax-langflow>).
## Install Langflow locally[​](https://docs.langflow.org/<#install-langflow-locally> "Direct link to Install Langflow locally")
Install Langflow locally with [uv (recommended)](https://docs.langflow.org/<https:/docs.astral.sh/uv/getting-started/installation/>), [pip](https://docs.langflow.org/<https:/pypi.org/project/pip/>), or [pipx](https://docs.langflow.org/<https:/pipx.pypa.io/stable/installation/>).
### Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [Python 3.10 to 3.12](https://docs.langflow.org/<https:/www.python.org/downloads/release/python-3100/>) installed
  * [uv](https://docs.langflow.org/<https:/docs.astral.sh/uv/getting-started/installation/>), [pip](https://docs.langflow.org/<https:/pypi.org/project/pip/>), or [pipx](https://docs.langflow.org/<https:/pipx.pypa.io/stable/installation/>) installed
  * Before installing Langflow, we recommend creating a virtual environment to isolate your Python dependencies with [uv](https://docs.langflow.org/<https:/docs.astral.sh/uv/pip/environments>), [venv](https://docs.langflow.org/<https:/docs.python.org/3/library/venv.html>), or [conda](https://docs.langflow.org/<https:/anaconda.org/anaconda/conda>)


### Install Langflow with pip or pipx[​](https://docs.langflow.org/<#install-langflow-with-pip-or-pipx> "Direct link to Install Langflow with pip or pipx")
Install Langflow with uv:
`
1
uv pip install langflow
`
Install Langflow with pip:
`
1
python -m pip install langflow
`
Install Langflow with pipx using the Python 3.10 executable:
`
1
pipx install langflow --python python3.10
`
## Run Langflow[​](https://docs.langflow.org/<#run-langflow> "Direct link to Run Langflow")
  1. To run Langflow with uv, enter the following command.


`
1
uv run langflow run
`
  1. To run Langflow with pip, enter the following command.


`
1
python -m langflow run
`
  1. Confirm that a local Langflow instance starts by visiting `http://127.0.0.1:7860` in a Chromium-based browser.


Now that Langflow is running, follow the [Quickstart](https://docs.langflow.org/</get-started-quickstart>) to create your first flow.
## Manage Langflow versions[​](https://docs.langflow.org/<#manage-langflow-versions> "Direct link to Manage Langflow versions")
To upgrade Langflow to the latest version with uv, use the uv pip upgrade command.
`
1
uv pip install langflow -U
`
To upgrade Langflow to the latest version, use the pip upgrade command.
`
1
python -m pip install langflow -U
`
To install a specific version of the Langflow package, add the required version to the command.
`
1
python -m pip install langflow==1.1
`
To reinstall Langflow and all of its dependencies, add the `--force-reinstall` flag to the command.
`
1
python -m pip install langflow --force-reinstall
`
## DataStax Langflow[​](https://docs.langflow.org/<#datastax-langflow> "Direct link to DataStax Langflow")
**DataStax Langflow** is a hosted version of Langflow integrated with [Astra DB](https://docs.langflow.org/<https:/www.datastax.com/products/datastax-astra>). Be up and running in minutes with no installation or setup required. [Sign up for free](https://docs.langflow.org/<https:/astra.datastax.com/signup?type=langflow>).
## Common installation issues[​](https://docs.langflow.org/<#common-installation-issues> "Direct link to Common installation issues")
This is a list of possible issues that you may encounter when installing and running Langflow.
### No `langflow.__main__` module[​](https://docs.langflow.org/<#no-langflow__main__-module> "Direct link to no-langflow__main__-module")
When you try to run Langflow with the command `langflow run`, you encounter the following error:
`
1
> No module named 'langflow.__main__'
`
  1. Run `python -m langflow run` instead of `langflow run`.
  2. If that doesn't work, reinstall the latest Langflow version with `python -m pip install langflow -U`.
  3. If that doesn't work, reinstall Langflow and its dependencies with `python -m pip install langflow --pre -U --force-reinstall`.


### Langflow runTraceback[​](https://docs.langflow.org/<#langflow-runtraceback> "Direct link to Langflow runTraceback")
When you try to run Langflow using the command `langflow run`, you encounter the following error:
`
1
> langflow runTraceback (most recent call last): File ".../langflow", line 5, in <module> from langflow.__main__ import mainModuleNotFoundError: No module named 'langflow.__main__'
`
There are two possible reasons for this error:
  1. You've installed Langflow using `pip install langflow` but you already had a previous version of Langflow installed in your system. In this case, you might be running the wrong executable. To solve this issue, run the correct executable by running `python -m langflow run` instead of `langflow run`. If that doesn't work, try uninstalling and reinstalling Langflow with `python -m pip install langflow --pre -U`.
  2. Some version conflicts might have occurred during the installation process. Run `python -m pip install langflow --pre -U --force-reinstall` to reinstall Langflow and its dependencies.


### Something went wrong running migrations[​](https://docs.langflow.org/<#something-went-wrong-running-migrations> "Direct link to Something went wrong running migrations")
`
1
> Something went wrong running migrations. Please, run 'langflow migration --fix'
`
Clear the cache by deleting the contents of the cache folder.
This folder can be found at:
  * **Linux or WSL2 on Windows** : `home/<username>/.cache/langflow/`
  * **MacOS** : `/Users/<username>/Library/Caches/langflow/`


This error can occur during Langflow upgrades when the new version can't override `langflow-pre.db` in `.cache/langflow/`. Clearing the cache removes this file but also erases your settings.
If you wish to retain your files, back them up before clearing the folder.
### Langflow installation freezes at pip dependency resolution[​](https://docs.langflow.org/<#langflow-installation-freezes-at-pip-dependency-resolution> "Direct link to Langflow installation freezes at pip dependency resolution")
Installing Langflow with `pip install langflow` slowly fails with this error message:
`
1
pip is looking at multiple versions of <<library>> to determine which version is compatible with other requirements. This could take a while.
`
To work around this issue, install Langflow with `uv`[](https://docs.langflow.org/<https:/docs.astral.sh/uv/getting-started/installation/>) instead of `pip`.
`
1
uv pip install langflow
`
To run Langflow with uv:
`
1
uv run langflow run
`
[PreviousWelcome to Langflow](https://docs.langflow.org/</>)[NextQuickstart](https://docs.langflow.org/</get-started-quickstart>)
  * [Install Langflow locally](https://docs.langflow.org/<#install-langflow-locally>)
    * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
    * [Install Langflow with pip or pipx](https://docs.langflow.org/<#install-langflow-with-pip-or-pipx>)
  * [Run Langflow](https://docs.langflow.org/<#run-langflow>)
  * [Manage Langflow versions](https://docs.langflow.org/<#manage-langflow-versions>)
  * [DataStax Langflow](https://docs.langflow.org/<#datastax-langflow>)
  * [Common installation issues](https://docs.langflow.org/<#common-installation-issues>)
    * [No `langflow.__main__` module](https://docs.langflow.org/<#no-langflow__main__-module>)
    * [Langflow runTraceback](https://docs.langflow.org/<#langflow-runtraceback>)
    * [Something went wrong running migrations](https://docs.langflow.org/<#something-went-wrong-running-migrations>)
    * [Langflow installation freezes at pip dependency resolution](https://docs.langflow.org/<#langflow-installation-freezes-at-pip-dependency-resolution>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4efa85e7-b852-4ab0-9e96-ba53419544af&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3cf60daa-8ebf-49ee-99c6-6d6358ac7361&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fget-started-installation&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=4efa85e7-b852-4ab0-9e96-ba53419544af&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3cf60daa-8ebf-49ee-99c6-6d6358ac7361&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fget-started-installation&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
