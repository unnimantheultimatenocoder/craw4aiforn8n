[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/<#>)
  * [Starter projects](https://docs.langflow.org/<#>)
  * [Tutorials](https://docs.langflow.org/<#>)
  * [Concepts](https://docs.langflow.org/<#>)
    * [Langflow overview](https://docs.langflow.org/</concepts-overview>)
    * [Playground](https://docs.langflow.org/</concepts-playground>)
    * [Components](https://docs.langflow.org/</concepts-components>)
    * [Flows](https://docs.langflow.org/</Concepts/concepts-flows>)
    * [Langflow objects](https://docs.langflow.org/</concepts-objects>)
    * [API pane](https://docs.langflow.org/</concepts-api>)
  * [Components](https://docs.langflow.org/<#>)
  * [Agents](https://docs.langflow.org/<#>)
  * [Configuration](https://docs.langflow.org/<#>)
  * [Deployment](https://docs.langflow.org/<#>)
  * [Integrations](https://docs.langflow.org/<#>)
  * [Contributing](https://docs.langflow.org/<#>)
  * [API reference](https://docs.langflow.org/<#>)
  * [Changelog](https://docs.langflow.org/<#>)


  * [](https://docs.langflow.org/</>)
  * Concepts
  * Langflow overview


On this page
# Langflow overview
This page explores the fundamental building blocks of Langflow, beginning with the question, **"What is a flow?"**
## What is a flow?[​](https://docs.langflow.org/<#what-is-a-flow> "Direct link to What is a flow?")
A **flow** is an application. It receives input, processes it, and produces output.
Flows are created in the **workspace** with components dragged from the components sidebar.
![Basic prompting flow within in the workspace](https://docs.langflow.org/assets/images/workspace-basic-prompting-5714c651361659596e80fa4a691701d9.png)
A flow can be as simple as the [basic prompting flow](https://docs.langflow.org/</get-started-quickstart>), which creates an OpenAI chatbot with four components.
  * Each component in a flow is a **node** that performs a specific task, like an AI model or a data source.
  * Each component has a **Configuration** menu. Click the **Code** pane to see a component's underlying Python code.
  * Components are connected with **edges** to form flows.


If you're familiar with [ReactFlow](https://docs.langflow.org/<https:/reactflow.dev/learn>), a **flow** is a node-based application, a **component** is a node, and the connections between components are **edges**.
When a flow is run, Langflow builds a Directed Acyclic Graph (DAG) graph object from the nodes (components) and edges (connections between components), with the nodes sorted to determine the order of execution. The graph build calls the individual components' `def_build` functions to validate and prepare the nodes. This graph is then processed in dependency order. Each node is built and executed sequentially, with results from each built node being passed to nodes that are dependent on the previous node's results.
Flows are stored on local disk at these default locations:
  * **Linux or WSL on Windows** : `home/<username>/.cache/langflow/`
  * **MacOS** : `/Users/<username>/Library/Caches/langflow/`


The flow storage location can be customized with the [LANGFLOW_CONFIG_DIR](https://docs.langflow.org/</environment-variables#LANGFLOW_CONFIG_DIR>) environment variable.
## Find your way around[​](https://docs.langflow.org/<#find-your-way-around> "Direct link to Find your way around")
If you're new to Langflow, it's OK to feel a bit lost at first. We’ll take you on a tour, so you can orient yourself and start creating applications quickly.
Langflow has four distinct regions: the [workspace](https://docs.langflow.org/<#workspace>) is the main area where you build your flows. The components sidebar is on the left, and lists the available [components](https://docs.langflow.org/<#components>). The [playground](https://docs.langflow.org/<#playground>) and [API pane](https://docs.langflow.org/<#api-pane>) are available in the upper right corner.
![](https://docs.langflow.org/assets/images/workspace-e7f86797a44d56c10b93c12b206d88f0.png)
## Workspace[​](https://docs.langflow.org/<#workspace> "Direct link to Workspace")
The **workspace** is where you create AI applications by connecting and running components in flows.
The workspace controls allow you to adjust your view and lock your flows in place.
  * Add **Notes** to flows with the **Add Note** button, similar to commenting in code.
  * To access the [Settings](https://docs.langflow.org/<#settings>) menu, click **Settings**.


This menu contains configuration for **Global Variables** , **Langflow API** , **Shortcuts** , and **Messages**.
## Components[​](https://docs.langflow.org/<#components> "Direct link to Components")
A **component** is a single building block within a flow and consists of inputs, outputs, and parameters that define its functionality.
To add a component to your flow, drag it from the sidebar onto the workspace.
To connect components, drag a line from the output handle (⚪) of one component to the input handle of another.
For more information, see [Components overview](https://docs.langflow.org/</concepts-components>).
![Prompt component](https://docs.langflow.org/img/prompt-component.png)
## Playground[​](https://docs.langflow.org/<#playground> "Direct link to Playground")
The **Playground** executes the current flow in the workspace.
Chat with your flow, view inputs and outputs, and modify your AI's memories to tune your responses in real time.
Either the **Chat Input** or **Chat Output** component can be opened in the **Playground** and tested in real time.
For more information, see the [Playground](https://docs.langflow.org/</concepts-playground>).
![](https://docs.langflow.org/assets/images/playground-b2c623fb6849024570bc9bd5285309f5.png)
## API pane[​](https://docs.langflow.org/<#api-pane> "Direct link to API pane")
The **API** pane provides code templates to integrate your flows into external applications.
For more information, see the [API pane](https://docs.langflow.org/</concepts-api>).
![](https://docs.langflow.org/assets/images/api-pane-97a01b20a262676d4e21906df0e29f46.png)
## View logs[​](https://docs.langflow.org/<#view-logs> "Direct link to View logs")
The **Logs** pane provides a detailed record of all component executions within a workspace.
To access the **Logs** pane, click your **Flow Name** , and then select **Logs**.
![](https://docs.langflow.org/assets/images/logs-6ae22cc6a87b128cbc0c7f4559b47f10.png)
## Projects and folders[​](https://docs.langflow.org/<#projects-and-folders> "Direct link to Projects and folders")
The **My Projects** page displays all the flows and components you've created in the Langflow workspace.
![](https://docs.langflow.org/assets/images/my-projects-20f73f0541b2f5b41398ef5df610b7b3.png)
**My Projects** is the default folder where all new projects and components are initially stored.
Projects, folders, and flows are exchanged as JSON objects.
  * To create a new folder, click 📁 **New Folder**.
  * To rename a folder, double-click the folder name.
  * To download a folder, click 📥 **Download**.
  * To upload a folder, click 📤 **Upload**. The default maximum file upload size is 100 MB.
  * To move a flow or component, drag and drop it into the desired folder.


## Options menu[​](https://docs.langflow.org/<#options-menu> "Direct link to Options menu")
The dropdown menu labeled with the project name offers several management and customization options for the current flow in the Langflow workspace.
  * **New** : Create a new flow from scratch.
  * **Settings** : Adjust settings specific to the current flow, such as its name, description, and endpoint name.
  * **Logs** : View logs for the current project, including execution history, errors, and other runtime events.
  * **Import** : Import a flow or component from a JSON file into the workspace.
  * **Export** : Export the current flow as a JSON file.
  * **Undo (⌘Z)** : Revert the last action taken in the project.
  * **Redo (⌘Y)** : Reapply a previously undone action.
  * **Refresh All** : Refresh all components and delete cache.


## Settings[​](https://docs.langflow.org/<#settings> "Direct link to Settings")
Click **Settings** to access **Global variables** , **Langflow API** , **Shortcuts** , and **Messages**.
[PreviousTravel planning agent](https://docs.langflow.org/</tutorials-travel-planning-agent>)[NextPlayground](https://docs.langflow.org/</concepts-playground>)
  * [What is a flow?](https://docs.langflow.org/<#what-is-a-flow>)
  * [Find your way around](https://docs.langflow.org/<#find-your-way-around>)
  * [Workspace](https://docs.langflow.org/<#workspace>)
  * [Components](https://docs.langflow.org/<#components>)
  * [Playground](https://docs.langflow.org/<#playground>)
  * [API pane](https://docs.langflow.org/<#api-pane>)
  * [View logs](https://docs.langflow.org/<#view-logs>)
  * [Projects and folders](https://docs.langflow.org/<#projects-and-folders>)
  * [Options menu](https://docs.langflow.org/<#options-menu>)
  * [Settings](https://docs.langflow.org/<#settings>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
