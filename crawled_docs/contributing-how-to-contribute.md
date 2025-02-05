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
  * [Contributing](https://docs.langflow.org/</contributing-community>)
    * [Join the Langflow community](https://docs.langflow.org/</contributing-community>)
    * [Contribute components](https://docs.langflow.org/</contributing-components>)
    * [Ask for help on the Discussions board](https://docs.langflow.org/</contributing-github-discussions>)
    * [Request an enhancement or report a bug](https://docs.langflow.org/</contributing-github-issues>)
    * [Contribute to Langflow](https://docs.langflow.org/</contributing-how-to-contribute>)
    * [Telemetry](https://docs.langflow.org/</contributing-telemetry>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Contributing
  * Contribute to Langflow


On this page
# Contribute to Langflow
This guide is intended to help you start contributing to Langflow. As an open-source project in a rapidly developing field, Langflow welcomes contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.
To contribute code or documentation to this project, follow the [fork and pull request](https://docs.langflow.org/<https:/docs.github.com/en/get-started/quickstart/contributing-to-projects>) workflow.
## Contribute code[​](https://docs.langflow.org/<#contribute-code> "Direct link to Contribute code")
Develop Langflow locally with [uv](https://docs.langflow.org/<https:/docs.astral.sh/uv/getting-started/installation/>) and [Node.js](https://docs.langflow.org/<https:/nodejs.org/en/download/package-manager>).
### Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
  * [uv(>=0.4)](https://docs.langflow.org/<https:/docs.astral.sh/uv/getting-started/installation/>)
  * [Node.js](https://docs.langflow.org/<https:/nodejs.org/en/download/package-manager>)


### Clone the Langflow Repository[​](https://docs.langflow.org/<#clone-the-langflow-repository> "Direct link to Clone the Langflow Repository")
  1. Navigate to the [Langflow GitHub repository](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>), and then click **Fork**.
  2. Add the new remote to your local repository on your local machine:


`
_10
git remote add fork https://github.com/<your_git_username>/langflow.git
`
### Prepare the development environment[​](https://docs.langflow.org/<#prepare-the-development-environment> "Direct link to Prepare the development environment")
  1. Create development hooks.


`
_10
make init
`
This command sets up the development environment by installing backend and frontend dependencies, building the frontend static files, and initializing the project. It runs `make install_backend`, `make install_frontend`, `make build_frontend`, and finally `uv run langflow run` to start the application.
  1. Run `make lint`, `make format`, and `make unit_tests` before pushing to the repository.


### Debug[​](https://docs.langflow.org/<#debug> "Direct link to Debug")
The repo includes a `.vscode/launch.json` file for debugging the backend in VSCode, which is faster than debugging with Docker Compose. To debug Langflow with the `launch.json` file in VSCode:
  1. Open Langflow in VSCode.
  2. Press **Ctrl+Shift+D** for Windows **or Cmd+Shift+D** for Mac to open the Run and Debug view.
  3. From the **Run and Debug** dropdown, choose a debugging configuration.
  4. Click the green **Play** button or press F5 to start debugging.


Use `launch.json` to quickly debug different parts of your application, like the backend, frontend, or CLI, directly from VSCode.
### Run Langflow locally[​](https://docs.langflow.org/<#run-langflow-locally> "Direct link to Run Langflow locally")
After setting up the environment with `make init`, you can run Langflow's backend and frontend separately for development. Langflow recommends using a virtual environment like [venv](https://docs.langflow.org/<https:/docs.python.org/3/library/venv.html>) or [conda](https://docs.langflow.org/<https:/anaconda.org/anaconda/conda>) to isolate dependencies.
Before you begin, ensure you have [uv](https://docs.langflow.org/<https:/docs.astral.sh/uv/getting-started/installation/>) and [Node.js](https://docs.langflow.org/<https:/nodejs.org/en/download/package-manager>) installed.
  1. In the repository root, install the dependencies and start the development server for the backend:


`
_10
make backend
`
  1. Install dependencies and start the frontend:


`
_10
make frontend
`
This approach allows you to work on the backend and frontend independently, with hot-reloading for faster development.
## Contribute documentation[​](https://docs.langflow.org/<#contribute-documentation> "Direct link to Contribute documentation")
The documentation is built using [Docusaurus](https://docs.langflow.org/<https:/docusaurus.io/>) and written in [Markdown](https://docs.langflow.org/<https:/docusaurus.io/docs/markdown-features>).
### Prerequisites[​](https://docs.langflow.org/<#prerequisites-1> "Direct link to Prerequisites")
  * [Node.js](https://docs.langflow.org/<https:/nodejs.org/en/download/package-manager>)


### Clone the Langflow repository[​](https://docs.langflow.org/<#clone-the-langflow-repository-1> "Direct link to Clone the Langflow repository")
  1. Navigate to the [Langflow GitHub repository](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>), and then click **Fork**.
  2. Add the new remote to your local repository on your local machine:


`
_10
git remote add fork https://github.com/<your_git_username>/langflow.git
`
  1. To run the documentation locally, run the following commands:


`
_10
cd docs
_10
npm install
_10
npm run start
`
The documentation will be available at `localhost:3000` and all the files are located in the `docs/docs` folder.
## Open a pull request[​](https://docs.langflow.org/<#open-a-pull-request> "Direct link to Open a pull request")
Once you have written and manually tested your changes with `make lint` and `make unit_tests`, open a pull request to send your changes upstream to the main Langflow repository.
  1. Open a new GitHub pull request with your patch against the `main` branch.
  2. Ensure the PR title follows semantic commit conventions. For example, features are `feat: add new feature` and fixes are `fix: correct issue with X`.
  3. A Langflow maintainer will review your pull request. Thanks for your contribution!


Some additional guidance on pull request titles:
  * Ensure the pull request description clearly describes the problem and solution. If the PR fixes an issue, include a link to the fixed issue in the PR description with `Fixes #1234`.
  * Pull request titles appear in Langflow's release notes, so they should explain what the PR does as explicitly as possible.
  * Pull requests should strive to fix one thing **only** , and should contain a good description of what is being fixed.


For more information, see the [Python Developer's Guide](https://docs.langflow.org/<https:/devguide.python.org/getting-started/pull-request-lifecycle/index.html#making-good-commits>).
[PreviousRequest an enhancement or report a bug](https://docs.langflow.org/</contributing-github-issues>)[NextTelemetry](https://docs.langflow.org/</contributing-telemetry>)
  * [Contribute code](https://docs.langflow.org/<#contribute-code>)
    * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
    * [Clone the Langflow Repository](https://docs.langflow.org/<#clone-the-langflow-repository>)
    * [Prepare the development environment](https://docs.langflow.org/<#prepare-the-development-environment>)
    * [Debug](https://docs.langflow.org/<#debug>)
    * [Run Langflow locally](https://docs.langflow.org/<#run-langflow-locally>)
  * [Contribute documentation](https://docs.langflow.org/<#contribute-documentation>)
    * [Prerequisites](https://docs.langflow.org/<#prerequisites-1>)
    * [Clone the Langflow repository](https://docs.langflow.org/<#clone-the-langflow-repository-1>)
  * [Open a pull request](https://docs.langflow.org/<#open-a-pull-request>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
