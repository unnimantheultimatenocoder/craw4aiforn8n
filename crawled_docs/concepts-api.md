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
  * API pane


On this page
# API pane
The **API** pane presents code templates for integrating your flow into external applications.
![](https://docs.langflow.org/assets/images/api-pane-97a01b20a262676d4e21906df0e29f46.png)
## cURL[​](https://docs.langflow.org/<#curl> "Direct link to cURL")
The **cURL** tab displays sample code for posting a query to your flow. Modify the `input_value` to change your input message. Copy the code and run it to post a query to your flow and get the result.
## Python API[​](https://docs.langflow.org/<#python-api> "Direct link to Python API")
The **Python API** tab displays code to interact with your flow using the Python HTTP `requests` library.
To use the `requests` library:
  1. Copy and paste the code into a Python script.
  2. Run the script and pass your message with it.


`
1
python3 python-api-script.py --message="tell me about something interesting"
`
## Python code[​](https://docs.langflow.org/<#python-code> "Direct link to Python code")
The **Python Code** tab displays code to interact with your flow's `.json` file using the Langflow runtime.
To use your code in a Python application using the Langflow runtime, you have to first download your flow’s JSON file.
  1. In your **Workspace** , click **Settings** , and then select **Export**.
  2. Download the flow to your local machine. Make sure the flow path in the script matches the flow’s location on your machine.
  3. Copy and paste the code from the API tab into a Python script file. It will look like this:


`
1
from langflow.load import run_flow_from_json
2
TWEAKS = {
3
 "ChatInput-kKhri": {},
4
 "Prompt-KDSi5": {},
5
 "ChatOutput-Vr3Q7": {},
6
 "OpenAIModel-4xYtx": {}
7
}
89
result = run_flow_from_json(flow="./basic-prompting-local.json",
10
              input_value="tell me about something interesting",
11
              fallback_to_env_vars=True, # False by default
12
              tweaks=TWEAKS)
1314
print(result)
`
  1. Run the script:


`
1
python3 python-api-script.py
`
## Tweaks[​](https://docs.langflow.org/<#tweaks> "Direct link to Tweaks")
The **Tweaks** tab displays the available parameters for your flow. Modifying the parameters changes the code parameters across all windows. For example, changing the **Chat Input** component's `input_value` will change that value across all API calls.
## Send image files to your flow with the API[​](https://docs.langflow.org/<#send-image-files-to-your-flow-with-the-api> "Direct link to Send image files to your flow with the API")
For information on sending files to the Langflow API, see [API examples](https://docs.langflow.org/</api-reference-api-examples#upload-image-files>).
## Chat Widget[​](https://docs.langflow.org/<#chat-widget> "Direct link to Chat Widget")
The **Chat Widget HTML** tab displays code that can be inserted in the `<body>` of your HTML to interact with your flow.
The **Langflow Chat Widget** is a powerful web component that enables communication with a Langflow project. This widget allows for a chat interface embedding, allowing the integration of Langflow into web applications effortlessly.
You can get the HTML code embedded with the chat by clicking the Code button at the Sidebar after building a flow.
Clicking the Chat Widget HTML tab, you'll get the code to be inserted. Read below to learn how to use it with HTML, React and Angular.
### Embed the chat widget into HTML[​](https://docs.langflow.org/<#embed-the-chat-widget-into-html> "Direct link to Embed the chat widget into HTML")
To embed the chat widget into any HTML page, insert the code snippet. inside a `<body>` tag.
`
1
<script src="https://cdn.jsdelivr.net/gh/logspace-ai/langflow-embedded-chat@v1.0.7/dist/build/static/js/bundle.min.js""></script>
23
 <langflow-chat
4
  window_title="Basic Prompting"
5
  flow_id="801abb1e-19b9-4278-9632-179b6d84f126"
6
  host_url="http://localhost:7860"
78
 ></langflow-chat>
`
### Embed the chat widget with React[​](https://docs.langflow.org/<#embed-the-chat-widget-with-react> "Direct link to Embed the chat widget with React")
To embed the Chat Widget using React, insert this `<script>` tag into the React  _index.html_ file, inside the `<body>`tag:
`
1
<script src="https://cdn.jsdelivr.net/gh/langflow-ai/langflow-embedded-chat@main/dist/build/static/js/bundle.min.js"></script>
`
Declare your Web Component and encapsulate it in a React component.
`
1
declare global {
2
 namespace JSX {
3
  interface IntrinsicElements {
4
   "langflow-chat": any;
5
  }
6
 }
7
}
89
export default function ChatWidget({ className }) {
10
 return (
11
  <div className={className}>
12
   <langflow-chat
13
    chat_inputs='{"your_key":"value"}'
14
    chat_input_field="your_chat_key"
15
    flow_id="your_flow_id"
16
    host_url="langflow_url"
17
   ></langflow-chat>
18
  </div>
19
 );
20
}
`
Place the component anywhere in your code to display the Chat Widget.
### Embed the chat widget with Angular[​](https://docs.langflow.org/<#embed-the-chat-widget-with-angular> "Direct link to Embed the chat widget with Angular")
To use the chat widget in Angular, first add this `<script>` tag into the Angular  _index.html_ file, inside the `<body>` tag.
`
1
<script src="https://cdn.jsdelivr.net/gh/langflow-ai/langflow-embedded-chat@main/dist/build/static/js/bundle.min.js"></script>
`
When you use a custom web component in an Angular template, the Angular compiler might show a warning when it doesn't recognize the custom elements by default. To suppress this warning, add `CUSTOM_ELEMENTS_SCHEMA` to the module's `@NgModule.schemas`.
  * Open the module file (it typically ends with  _.module.ts_) where you'd add the `langflow-chat` web component.
  * Import `CUSTOM_ELEMENTS_SCHEMA` at the top of the file:


`import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';`
  * Add `CUSTOM_ELEMENTS_SCHEMA` to the 'schemas' array inside the '@NgModule' decorator:


`
1
@NgModule({
2
 declarations: [
3
  // ... Other components and directives ...
4
 ],
5
 imports: [
6
  // ... Other imported modules ...
7
 ],
8
 schemas: [
9
  CUSTOM_ELEMENTS_SCHEMA // Add the CUSTOM_ELEMENTS_SCHEMA here
10
 ]
11
})
12
export class YourModule { }
`
In your Angular project, find the component belonging to the module where `CUSTOM_ELEMENTS_SCHEMA` was added. Inside the template, add the `langflow-chat` tag to include the Chat Widget in your component's view:
`
1
<langflow-chat chat_inputs='{"your_key":"value"}' chat_input_field="your_chat_key" flow_id="your_flow_id" host_url="langflow_url"></langflow-chat>
`
tip
`CUSTOM_ELEMENTS_SCHEMA` is a built-in schema that allows Angular to recognize custom elements. Adding `CUSTOM_ELEMENTS_SCHEMA` tells Angular to allow custom elements in your templates, and it will suppress the warning related to unknown elements like `langflow-chat`. Notice that you can only use the Chat Widget in components that are part of the module where you added `CUSTOM_ELEMENTS_SCHEMA`.
## Chat widget configuration[​](https://docs.langflow.org/<#chat-widget-configuration> "Direct link to Chat widget configuration")
Use the widget API to customize your Chat Widget:
caution
Props with the type JSON need to be passed as stringified JSONs, with the format {"key":"value"}.
Prop| Type| Required| Description  
---|---|---|---  
bot_message_style| JSON| No| Applies custom formatting to bot messages.  
chat_input_field| String| Yes| Defines the type of the input field for chat messages.  
chat_inputs| JSON| Yes| Determines the chat input elements and their respective values.  
chat_output_key| String| No| Specifies which output to display if multiple outputs are available.  
chat_position| String| No| Positions the chat window on the screen (options include: top-left, top-center, top-right, center-left, center-right, bottom-right, bottom-center, bottom-left).  
chat_trigger_style| JSON| No| Styles the chat trigger button.  
chat_window_style| JSON| No| Customizes the overall appearance of the chat window.  
error_message_style| JSON| No| Sets the format for error messages within the chat window.  
flow_id| String| Yes| Identifies the flow that the component is associated with.  
height| Number| No| Sets the height of the chat window in pixels.  
host_url| String| Yes| Specifies the URL of the host for chat component communication.  
input_container_style| JSON| No| Applies styling to the container where chat messages are entered.  
input_style| JSON| No| Sets the style for the chat input field.  
online| Boolean| No| Toggles the online status of the chat component.  
online_message| String| No| Sets a custom message to display when the chat component is online.  
placeholder| String| No| Sets the placeholder text for the chat input field.  
placeholder_sending| String| No| Sets the placeholder text to display while a message is being sent.  
send_button_style| JSON| No| Sets the style for the send button in the chat window.  
send_icon_style| JSON| No| Sets the style for the send icon in the chat window.  
tweaks| JSON| No| Applies additional custom adjustments for the associated flow.  
user_message_style| JSON| No| Determines the formatting for user messages in the chat window.  
width| Number| No| Sets the width of the chat window in pixels.  
window_title| String| No| Sets the title displayed in the chat window's header or title bar.  
[PreviousLangflow objects](https://docs.langflow.org/</concepts-objects>)[NextAgents](https://docs.langflow.org/</components-agents>)
  * [cURL](https://docs.langflow.org/<#curl>)
  * [Python API](https://docs.langflow.org/<#python-api>)
  * [Python code](https://docs.langflow.org/<#python-code>)
  * [Tweaks](https://docs.langflow.org/<#tweaks>)
  * [Send image files to your flow with the API](https://docs.langflow.org/<#send-image-files-to-your-flow-with-the-api>)
  * [Chat Widget](https://docs.langflow.org/<#chat-widget>)
    * [Embed the chat widget into HTML](https://docs.langflow.org/<#embed-the-chat-widget-into-html>)
    * [Embed the chat widget with React](https://docs.langflow.org/<#embed-the-chat-widget-with-react>)
    * [Embed the chat widget with Angular](https://docs.langflow.org/<#embed-the-chat-widget-with-angular>)
  * [Chat widget configuration](https://docs.langflow.org/<#chat-widget-configuration>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
