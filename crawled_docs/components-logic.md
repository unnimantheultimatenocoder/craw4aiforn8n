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
    * [Agents](https://docs.langflow.org/</components-agents>)
    * [Create custom Python components](https://docs.langflow.org/</components-custom-components>)
    * [Data](https://docs.langflow.org/</components-data>)
    * [Embeddings](https://docs.langflow.org/</components-embedding-models>)
    * [Helpers](https://docs.langflow.org/</components-helpers>)
    * [Inputs and outputs](https://docs.langflow.org/</components-io>)
    * [Loaders](https://docs.langflow.org/</components-loaders>)
    * [Logic](https://docs.langflow.org/</components-logic>)
    * [Memories](https://docs.langflow.org/</components-memories>)
    * [Models](https://docs.langflow.org/</components-models>)
    * [Processing](https://docs.langflow.org/</components-processing>)
    * [Prompts](https://docs.langflow.org/</components-prompts>)
    * [Tools](https://docs.langflow.org/</components-tools>)
    * [Vector stores](https://docs.langflow.org/</components-vector-stores>)
  * [Agents](https://docs.langflow.org/</agents-overview>)
  * [Configuration](https://docs.langflow.org/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Components
  * Logic


On this page
# Logic components in Langflow
Logic components provide functionalities for routing, conditional processing, and flow management.
## Use a logic component in a flow[​](https://docs.langflow.org/<#use-a-logic-component-in-a-flow> "Direct link to Use a logic component in a flow")
This flow creates a summarizing "for each" loop with the [Loop](https://docs.langflow.org/</components-logic#loop>) component.
The component iterates over a list of [Data](https://docs.langflow.org/</concepts-objects#data-object>) objects until it's completed, and then the **Done** loop aggregates the results.
The **File** component loads text files from your local machine, and then the **Parse Data** component parses them into a list of structured `Data` objects. The **Loop** component passes each `Data` object to a **Prompt** to be summarized.
When the **Loop** component runs out of `Data`, the **Done** loop activates, which counts the number of pages and summarizes their tone with another **Prompt**. This is represented in Langflow by connecting the Parse Data component's **Data List** output to the Loop component's `Data` loop input.
![Sample Flow looping summarizer](https://docs.langflow.org/assets/images/loop-text-summarizer-bd1d7be6d26bb47765931e3ab9f98dfa.png)
The output will look similar to this:
`
_10
Document Summary
_10
Total Pages Processed
_10
Total Pages: 2
_10
Overall Tone of Document
_10
Tone: Informative and Instructional
_10
The documentation outlines microservices architecture patterns and best practices.
_10
It emphasizes service isolation and inter-service communication protocols.
_10
The use of asynchronous messaging patterns is recommended for system scalability.
_10
It includes code examples of REST and gRPC implementations to demonstrate integration approaches.
`
## Conditional router[​](https://docs.langflow.org/<#conditional-router> "Direct link to Conditional router")
This component routes an input message to a corresponding output based on text comparison.
The ConditionalRouterComponent routes messages based on text comparison. It evaluates a condition by comparing two text inputs using a specified operator and routes the message accordingly.
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
input_text| String| The primary text input for the operation.  
match_text| String| The text input to compare against.  
operator| Dropdown| The operator to apply for comparing the texts.  
case_sensitive| Boolean| If true, the comparison will be case sensitive.  
message| Message| The message to pass through either route.  
max_iterations| Integer| The maximum number of iterations for the conditional router.  
default_route| Dropdown| The default route to take when max iterations are reached.  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
true_result| Message| The output when the condition is true.  
false_result| Message| The output when the condition is false.  
## Data conditional router[​](https://docs.langflow.org/<#data-conditional-router> "Direct link to Data conditional router")
This component routes `Data` objects based on a condition applied to a specified key, including boolean validation.
This component is particularly useful in workflows that require conditional routing of complex data structures, enabling dynamic decision-making based on data content.
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
data_input| Data| The data object or list of data objects to process.  
key_name| String| The name of the key in the data object to check.  
operator| Dropdown| The operator to apply for comparing the values.  
compare_value| String| The value to compare against (not used for boolean validator).  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
true_output| Data/List| Output when the condition is met.  
false_output| Data/List| Output when the condition is not met.  
## Flow as Tool[​](https://docs.langflow.org/<#flow-as-tool> "Direct link to Flow as Tool")
This component constructs a tool from a function that runs a loaded flow.
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
flow_name| Dropdown| The name of the flow to run.  
tool_name| String| The name of the tool.  
tool_description| String| The description of the tool.  
return_direct| Boolean| If true, returns the result directly from the tool.  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
api_build_tool| Tool| The constructed tool from the flow.  
## Listen[​](https://docs.langflow.org/<#listen> "Direct link to Listen")
This component listens for a notification and retrieves its associated state.
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
name| String| The name of the notification to listen for.  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
output| Data| The state associated with the notification.  
## Loop[​](https://docs.langflow.org/<#loop> "Direct link to Loop")
This component iterates over a list of [Data](https://docs.langflow.org/</concepts-objects#data-object>) objects, outputting one item at a time and aggregating results from loop inputs.
### Inputs[​](https://docs.langflow.org/<#inputs-4> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
data| Data/List| The initial list of Data objects to iterate over.  
### Outputs[​](https://docs.langflow.org/<#outputs-4> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
item| Data| Outputs one item at a time from the data list.  
done| Data| Triggered when iteration complete, returns aggregated results.  
## Notify[​](https://docs.langflow.org/<#notify> "Direct link to Notify")
This component generates a notification for the Listen component to use.
### Inputs[​](https://docs.langflow.org/<#inputs-5> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
name| String| The name of the notification.  
data| Data| The data to store in the notification.  
append| Boolean| If true, the record will be appended to the existing notification.  
### Outputs[​](https://docs.langflow.org/<#outputs-5> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
output| Data| The data stored in the notification.  
## Run flow[​](https://docs.langflow.org/<#run-flow> "Direct link to Run flow")
This component allows you to run a specified flow with given inputs and tweaks.
The RunFlowComponent executes a specified flow within a larger workflow. It provides the ability to run a flow with custom inputs and apply tweaks to modify its behavior.
### Inputs[​](https://docs.langflow.org/<#inputs-6> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
input_value| String| The input value for the flow to process.  
flow_name| Dropdown| The name of the flow to run.  
tweaks| Nested Dict| Tweaks to apply to the flow.  
### Outputs[​](https://docs.langflow.org/<#outputs-6> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
run_outputs| List[Data]| The results generated from running the flow.  
## Sub Flow[​](https://docs.langflow.org/<#sub-flow> "Direct link to Sub Flow")
This `SubFlowComponent` generates a component from a flow with all of its inputs and outputs.
This component can integrate entire flows as components within a larger workflow. It dynamically generates inputs based on the selected flow and executes the flow with provided parameters.
### Inputs[​](https://docs.langflow.org/<#inputs-7> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
flow_name| Dropdown| The name of the flow to run.  
### Outputs[​](https://docs.langflow.org/<#outputs-7> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
flow_outputs| List[Data]| The outputs generated from the flow.  
[PreviousLoaders](https://docs.langflow.org/</components-loaders>)[NextMemories](https://docs.langflow.org/</components-memories>)
  * [Use a logic component in a flow](https://docs.langflow.org/<#use-a-logic-component-in-a-flow>)
  * [Conditional router](https://docs.langflow.org/<#conditional-router>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [Data conditional router](https://docs.langflow.org/<#data-conditional-router>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Flow as Tool](https://docs.langflow.org/<#flow-as-tool>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Listen](https://docs.langflow.org/<#listen>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [Loop](https://docs.langflow.org/<#loop>)
    * [Inputs](https://docs.langflow.org/<#inputs-4>)
    * [Outputs](https://docs.langflow.org/<#outputs-4>)
  * [Notify](https://docs.langflow.org/<#notify>)
    * [Inputs](https://docs.langflow.org/<#inputs-5>)
    * [Outputs](https://docs.langflow.org/<#outputs-5>)
  * [Run flow](https://docs.langflow.org/<#run-flow>)
    * [Inputs](https://docs.langflow.org/<#inputs-6>)
    * [Outputs](https://docs.langflow.org/<#outputs-6>)
  * [Sub Flow](https://docs.langflow.org/<#sub-flow>)
    * [Inputs](https://docs.langflow.org/<#inputs-7>)
    * [Outputs](https://docs.langflow.org/<#outputs-7>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
