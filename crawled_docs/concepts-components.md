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
  * Components


On this page
# Langflow components overview
A component is a single building block within a flow with inputs, outputs, functions, and parameters that define its functionality. A single component is like a class within a larger application.
To add a component to a flow, drag it from the **Component** menu to the **Workspace**.
Learn more about components and how they work on this page.
## Component menu[​](https://docs.langflow.org/<#component-menu> "Direct link to Component menu")
Each component is unique, but all have a menu bar at the top that looks something like the following:
![Open AI component](https://docs.langflow.org/img/openai-model-component.png)
Use the component controls to do the following:
  * **Code** — Modify the component's Python code and save your changes.
  * **Controls** — Adjust all component parameters.
  * **Freeze Path** — After a component runs, lock its previous output state to prevent it from re-running.


Click **All** to see additional options for a component.
To view a component’s output and logs, click the icon.
To run a single component, click **Play**.
A **Checkmark** indicates that the component ran successfully.
Running a single component with the **Play** button is different from running the entire flow. In a single component run, the `build_vertex` function is called, which builds and runs only the single component with direct inputs provided through the UI (the `inputs_dict` parameter). The `VertexBuildResult` data is passed to the `build_and_run` method, which calls the component's `build` method and runs it. Unlike running the full flow, running a single component does not automatically execute its upstream dependencies.
## Component ports[​](https://docs.langflow.org/<#component-ports> "Direct link to Component ports")
Handles () on the side of a component indicate the types of inputs and outputs that can be connected at that port. Hover over a handle to see connection details.
![Prompt component](https://docs.langflow.org/img/prompt-component.png)
### Component port data type colors[​](https://docs.langflow.org/<#component-port-data-type-colors> "Direct link to Component port data type colors")
The following table lists the handle colors and their corresponding data types:
Data type| Handle color| Handle  
---|---|---  
BaseLanguageModel| Fuchsia  
Data| Red  
Document| Lime  
Embeddings| Emerald  
LanguageModel| Fuchsia  
Message| Indigo  
Prompt| Violet  
str| Indigo  
Text| Indigo  
unknown| Gray  
## Component code[​](https://docs.langflow.org/<#component-code> "Direct link to Component code")
A component inherits from a base `Component` class that defines its interface and behavior.
For example, the [Recursive character text splitter](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/components/langchain_utilities/recursive_character.py>) is a child of the [LCTextSplitterComponent](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/base/textsplitters/model.py>) class.
`
1
from typing import Any
23
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter
45
from langflow.base.textsplitters.model import LCTextSplitterComponent
6
from langflow.inputs.inputs import DataInput, IntInput, MessageTextInput
7
from langflow.utils.util import unescape_string
89
class RecursiveCharacterTextSplitterComponent(LCTextSplitterComponent):
10
  display_name: str = "Recursive Character Text Splitter"
11
  description: str = "Split text trying to keep all related text together."
12
  documentation: str = "https://docs.langflow.org/components-processing"
13
  name = "RecursiveCharacterTextSplitter"
14
  icon = "LangChain"
1516
  inputs = [
17
    IntInput(
18
      name="chunk_size",
19
      display_name="Chunk Size",
20
      info="The maximum length of each chunk.",
21
      value=1000,
22
    ),
23
    IntInput(
24
      name="chunk_overlap",
25
      display_name="Chunk Overlap",
26
      info="The amount of overlap between chunks.",
27
      value=200,
28
    ),
29
    DataInput(
30
      name="data_input",
31
      display_name="Input",
32
      info="The texts to split.",
33
      input_types=["Document", "Data"],
34
    ),
35
    MessageTextInput(
36
      name="separators",
37
      display_name="Separators",
38
      info='The characters to split on.\nIf left empty defaults to ["\\n\\n", "\\n", " ", ""].',
39
      is_list=True,
40
    ),
41
  ]
4243
  def get_data_input(self) -> Any:
44
    return self.data_input
4546
  def build_text_splitter(self) -> TextSplitter:
47
    if not self.separators:
48
      separators: list[str] | None = None
49
    else:
50
      # check if the separators list has escaped characters
51
      # if there are escaped characters, unescape them
52
      separators = [unescape_string(x) for x in self.separators]
5354
    return RecursiveCharacterTextSplitter(
55
      separators=separators,
56
      chunk_size=self.chunk_size,
57
      chunk_overlap=self.chunk_overlap,
58
    )
`
Components include definitions for inputs and outputs, which are represented in the UI with color-coded ports.
**Input Definition:** Each input (like `IntInput` or `DataInput`) specifies an input's type, name, and display properties, which appear as configurable fields in the component's UI panel.
**Methods:** Components have methods or functions that handle their functionality. This component has two methods. `get_data_input` retrieves the text data to be split from the component's input. This makes the data available to the class. `build_text_splitter` creates a `RecursiveCharacterTextSplitter` object by calling its parent class's `build` method. The text is split with the created splitter and passed to the next component. When used in a flow, this component:
  1. Displays its configuration options in the UI.
  2. Validates user inputs based on the input types.
  3. Processes data using the configured parameters.
  4. Passes results to the next component.


## Freeze path[​](https://docs.langflow.org/<#freeze-path> "Direct link to Freeze path")
After a component runs, **Freeze Path** locks the component's previous output state to prevent it from re-running.
If you’re expecting consistent output from a component and don’t need to re-run it, click **Freeze Path**.
Enabling **Freeze Path** freezes all components upstream of the selected component.
If you only want to freeze a single component, select **Freeze** instead.
A icon appears on all frozen components.
## Additional component options[​](https://docs.langflow.org/<#additional-component-options> "Direct link to Additional component options")
Click **All** to see additional options for a component.
To modify a component's name or description, double-click in the **Name** or **Description** fields. Component descriptions accept Markdown syntax.
### Component shortcuts[​](https://docs.langflow.org/<#component-shortcuts> "Direct link to Component shortcuts")
The following keyboard shortcuts are available when a component is selected.
Menu item| Windows shortcut| Mac shortcut| Description  
---|---|---|---  
Code| Space| Space| Opens the code editor for the component.  
Advanced Settings| Ctrl + Shift + A| ⌘ + Shift + A| Opens advanced settings for the component.  
Save Changes| Ctrl + S| ⌘ + S| Saves changes to the current flow.  
Save Component| Ctrl + Alt + S| ⌘ + Alt + S| Saves the current component to Saved components.  
Duplicate| Ctrl + D| ⌘ + D| Creates a duplicate of the component.  
Copy| Ctrl + C| ⌘ + C| Copies the selected component.  
Cut| Ctrl + X| ⌘ + X| Cuts the selected component.  
Paste| Ctrl + V| ⌘ + V| Pastes the copied/cut component.  
Docs| Ctrl + Shift + D| ⌘ + Shift + D| Opens related documentation.  
Minimize| Ctrl + .| ⌘ + .| Minimizes the current component.  
Freeze| Ctrl + F| ⌘ + F| Freezes the current component state.  
Freeze Path| Ctrl + Shift + F| ⌘ + Shift + F| Freezes component state and upstream components.  
Download| Ctrl + J| ⌘ + J| Downloads the component as JSON.  
Delete| Backspace| Backspace| Deletes the component.  
Group| Ctrl + G| ⌘ + G| Groups selected components.  
Undo| Ctrl + Z| ⌘ + Z| Undoes the last action.  
Redo| Ctrl + Y| ⌘ + Y| Redoes the last undone action.  
Redo (alternative)| Ctrl + Shift + Z| ⌘ + Shift + Z| Alternative shortcut for redo.  
Share Component| Ctrl + Shift + S| ⌘ + Shift + S| Shares the component.  
Share Flow| Ctrl + Shift + B| ⌘ + Shift + B| Shares the entire flow.  
Toggle Sidebar| Ctrl + B| ⌘ + B| Shows/hides the sidebar.  
Search Components| /| /| Focuses the component search bar.  
Tool Mode| Ctrl + Shift + M| ⌘ + Shift + M| Toggles tool mode.  
Update| Ctrl + U| ⌘ + U| Updates the component.  
Open Playground| Ctrl + K| ⌘ + K| Opens the playground.  
Output Inspection| O| O| Opens output inspection.  
Play| P| P| Plays/executes the flow.  
API| R| R| Opens the API view.  
## Group components in the workspace[​](https://docs.langflow.org/<#group-components-in-the-workspace> "Direct link to Group components in the workspace")
Multiple components can be grouped into a single component for reuse. This is useful when combining large flows into single components, for example RAG with a vector database, and saving space.
  1. Hold **Shift** and drag to select components.
  2. Select **Group**. The components merge into a single component.
  3. Double-click the name and description to change them.
  4. Save your grouped component to the sidebar for later use.


## Component version[​](https://docs.langflow.org/<#component-version> "Direct link to Component version")
A component's initial state is stored in a database. As soon as you drag a component from the sidebar to the workspace, the two components are no longer in parity.
A component keeps the version number it is initialized to the workspace with. If a component is at version `1.0` when it is dragged to the workspace, it will stay at version `1.0` until you update it.
Langflow notifies you when a component's workspace version is behind the database version and an update is available. Click the **Update Component** icon to update the component to the `latest` version. This will change the code of the component in place so you can validate that the component was updated by checking its Python code before and after updating it.
## Components sidebar[​](https://docs.langflow.org/<#components-sidebar> "Direct link to Components sidebar")
Components are listed in the sidebar by component type.
Component **bundles** are components grouped by provider. For example, Langchain modules like **RunnableExecutor** and **CharacterTextSplitter** are grouped under the **Langchain** bundle.
The sidebar includes a component **Search** bar, and includes flags for showing or hiding **Beta** and **Legacy** components.
**Beta** components are still being tested and are not suitable for production workloads.
**Legacy** components are available to use but no longer supported.
[PreviousPlayground](https://docs.langflow.org/</concepts-playground>)[NextFlows](https://docs.langflow.org/</Concepts/concepts-flows>)
  * [Component menu](https://docs.langflow.org/<#component-menu>)
  * [Component ports](https://docs.langflow.org/<#component-ports>)
    * [Component port data type colors](https://docs.langflow.org/<#component-port-data-type-colors>)
  * [Component code](https://docs.langflow.org/<#component-code>)
  * [Freeze path](https://docs.langflow.org/<#freeze-path>)
  * [Additional component options](https://docs.langflow.org/<#additional-component-options>)
    * [Component shortcuts](https://docs.langflow.org/<#component-shortcuts>)
  * [Group components in the workspace](https://docs.langflow.org/<#group-components-in-the-workspace>)
  * [Component version](https://docs.langflow.org/<#component-version>)
  * [Components sidebar](https://docs.langflow.org/<#components-sidebar>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b579e9bb-7763-4cdd-ae77-0431d538d123&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b87dc520-de57-4b80-9050-0c1f0076cdc9&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fconcepts-components&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b579e9bb-7763-4cdd-ae77-0431d538d123&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b87dc520-de57-4b80-9050-0c1f0076cdc9&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fconcepts-components&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
