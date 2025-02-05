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
  * Create custom Python components


On this page
# Create custom Python components
Custom components are created within Langflow and extend the platform's functionality with custom, reusable Python code.
Since Langflow operates with Python behind the scenes, you can implement any Python function within a Custom Component. This means you can leverage the power of libraries such as Pandas, Scikit-learn, Numpy, and thousands of other packages to create components that handle data processing in unlimited ways. You can use any type as long as the type is properly annotated in the output methods (e.g., `> list[int]`).
Custom Components create reusable and configurable components to enhance the capabilities of Langflow, making it a powerful tool for developing complex processing between user and AI messages.
## Directory structure requirements[​](https://docs.langflow.org/<#directory-structure-requirements> "Direct link to Directory structure requirements")
By default, Langflow looks for custom components in the `langflow/components` directory.
If you're creating custom components in a different location using the [LANGFLOW_COMPONENTS_PATH](https://docs.langflow.org/</environment-variables#LANGFLOW_COMPONENTS_PATH>) `LANGFLOW_COMPONENTS_PATH` environment variable, components must be organized in a specific directory structure to be properly loaded and displayed in the UI:
`
_10
/your/custom/components/path/  # Base directory (set by LANGFLOW_COMPONENTS_PATH)
_10
  └── category_name/     # Required category subfolder (determines menu name)
_10
    └── custom_component.py # Component file
`
Components must be placed inside **category folders** , not directly in the base directory. The category folder name determines where the component appears in the UI menu.
For example, to add a component to the **Helpers** menu, place it in a `helpers` subfolder:
`
_10
/app/custom_components/     # LANGFLOW_COMPONENTS_PATH
_10
  └── helpers/         # Shows up as "Helpers" menu
_10
    └── custom_component.py # Your component
`
You can have **multiple category folders** to organize components into different menus:
`
_10
/app/custom_components/
_10
  ├── helpers/
_10
  │  └── helper_component.py
_10
  └── tools/
_10
    └── tool_component.py
`
This folder structure is required for Langflow to properly discover and load your custom components. Components placed directly in the base directory will not be loaded.
`
_10
/app/custom_components/     # LANGFLOW_COMPONENTS_PATH
_10
  └── custom_component.py   # Won't be loaded - missing category folder!
`
## Create a custom component in Langflow[​](https://docs.langflow.org/<#create-a-custom-component-in-langflow> "Direct link to Create a custom component in Langflow")
Creating custom components in Langflow involves creating a Python class that defines the component's functionality, inputs, and outputs. The default code provides a working structure for your custom component.
`
_25
# from langflow.field_typing import Data
_25
from langflow.custom import Component
_25
from langflow.io import MessageTextInput, Output
_25
from langflow.schema import Data
_25
_25
_25
class CustomComponent(Component):
_25
  display_name = "Custom Component"
_25
  description = "Use as a template to create your own component."
_25
  documentation: str = "https://docs.langflow.org/components-custom-components"
_25
  icon = "custom_components"
_25
  name = "CustomComponent"
_25
_25
  inputs = [
_25
    MessageTextInput(name="input_value", display_name="Input Value", value="Hello, World!"),
_25
  ]
_25
_25
  outputs = [
_25
    Output(display_name="Output", name="output", method="build_output"),
_25
  ]
_25
_25
  def build_output(self) -> Data:
_25
    data = Data(value=self.input_value)
_25
    self.status = data
_25
    return data
`
You can create your class in your favorite text editor outside of Langflow and paste it in later, or just follow along in the code pane.
  1. In Langflow, click **+ Custom Component** to add a custom component into the workspace.
  2. Open the component's code pane.
  3. Import dependencies. Your custom component inherits from the langflow `Component` class so you need to include it.


`
_10
from langflow.custom import Component
_10
from langflow.io import MessageTextInput, Output
_10
from langflow.schema import Data
`
  1. **Define the Class** : Start by defining a Python class that inherits from `Component`. This class will encapsulate the functionality of your custom component.


`
_10
class CustomComponent(Component):
_10
  display_name = "Custom Component"
_10
  description = "Use as a template to create your own component."
_10
  documentation: str = "http://docs.langflow.org/components/custom"
_10
  icon = "custom_components"
_10
  name = "CustomComponent"
`
  1. **Specify Inputs and Outputs** : Use Langflow's input and output classes to define the inputs and outputs of your component. They should be declared as class attributes.


`
_10
  inputs = [
_10
    MessageTextInput(name="input_value", display_name="Input Value", value="Hello, World!"),
_10
  ]
_10
_10
  outputs = [
_10
    Output(display_name="Output", name="output", method="build_output"),
_10
  ]
`
  1. **Implement Output Methods** : Implement methods for each output, which contains the logic of your component. These methods can access input values using `self.<input_name>` , return processed values and define what to be displayed in the component with the `self.status` attribute.


`
_10
  def build_output(self) -> Data:
_10
    data = Data(value=self.input_value)
_10
    self.status = data
_10
    return data
`
  1. **Use Proper Annotations** : Ensure that output methods are properly annotated with their types. Langflow uses these annotations to validate and handle data correctly. For example, this method is annotated to output `Data`.


`
_10
  def build_output(self) -> Data:
`
  1. Click **Check & Save** to confirm your component works. You now have an operational custom component.


## Add inputs and modify output methods[​](https://docs.langflow.org/<#add-inputs-and-modify-output-methods> "Direct link to Add inputs and modify output methods")
This code defines a custom component that accepts 5 inputs and outputs a Message.
Copy and paste it into the Custom Component code pane and click **Check & Save.**
`
_55
from langflow.custom import Component
_55
from langflow.inputs import StrInput, MultilineInput, SecretStrInput, IntInput, DropdownInput
_55
from langflow.template import Output, Input
_55
from langflow.schema.message import Message
_55
_55
class MyCustomComponent(Component):
_55
  display_name = "My Custom Component"
_55
  description = "An example of a custom component with various input types."
_55
_55
  inputs = [
_55
    StrInput(
_55
      name="username",
_55
      display_name="Username",
_55
      info="Enter your username."
_55
    ),
_55
    SecretStrInput(
_55
      name="password",
_55
      display_name="Password",
_55
      info="Enter your password."
_55
    ),
_55
    MessageTextInput(
_55
      name="special_message",
_55
      display_name="special_message",
_55
      info="Enter a special message.",
_55
    ),
_55
    IntInput(
_55
      name="age",
_55
      display_name="Age",
_55
      info="Enter your age."
_55
    ),
_55
    DropdownInput(
_55
      name="gender",
_55
      display_name="Gender",
_55
      options=["Male", "Female", "Other"],
_55
      info="Select your gender."
_55
    )
_55
  ]
_55
_55
  outputs = [
_55
    Output(display_name="Result", name="result", method="process_inputs"),
_55
  ]
_55
_55
  def process_inputs(self) -> Message:
_55
    """
_55
    Process the user inputs and return a Message object.
_55
_55
    Returns:
_55
      Message: A Message object containing the processed information.
_55
    """
_55
    try:
_55
      processed_text = f"User {self.username} (Age: {self.age}, Gender: {self.gender}) " \
_55
               f"sent the following special message: {self.special_message}"
_55
      return Message(text=processed_text)
_55
    except AttributeError as e:
_55
      return Message(text=f"Error processing inputs: {str(e)}")
`
Since the component outputs a `Message`, you can wire it into a chat and pass messages to yourself.
Your Custom Component accepts the Chat Input message through `MessageTextInput`, fills in the variables with the `process_inputs` method, and finally passes the message `User Username (Age: 49, Gender: Male) sent the following special message: Hello!` to Chat Output.
By defining inputs this way, Langflow can automatically handle the validation and display of these fields in the user interface, making it easier to create robust and user-friendly custom components.
All of the types detailed above derive from a general class that can also be accessed through the generic `Input` class.
tip
Use `MessageInput` to get the entire Message object instead of just the text.
## Input Types[​](https://docs.langflow.org/<#3815589831f24ab792328ed233c8b00d> "Direct link to Input Types")
Langflow provides several higher-level input types to simplify the creation of custom components. These input types standardize how inputs are defined, validated, and used. Here’s a guide on how to use these inputs and their primary purposes:
### **HandleInput**[​](https://docs.langflow.org/<#fb06c48a326043ffa46badc1ab3ba467> "Direct link to fb06c48a326043ffa46badc1ab3ba467")
Represents an input that has a handle to a specific type (e.g., `BaseLanguageModel`, `BaseRetriever`, etc.).
  * **Usage:** Useful for connecting to specific component types in a flow.


### **DataInput**[​](https://docs.langflow.org/<#0e1dcb768e38487180d720b0884a90f5> "Direct link to 0e1dcb768e38487180d720b0884a90f5")
Represents an input that receives a `Data` object.
  * **Usage:** Ideal for components that process or manipulate data objects.
  * **Input Types:** `["Data"]`


### **StrInput**[​](https://docs.langflow.org/<#4ec6e68ad9ab4cd194e8e607bc5b3411> "Direct link to 4ec6e68ad9ab4cd194e8e607bc5b3411")
Represents a standard string input field.
  * **Usage:** Used for any text input where the user needs to provide a string.
  * **Input Types:** `["Text"]`


### **MessageInput**[​](https://docs.langflow.org/<#9292ac0105e14177af5eff2131b9c71b> "Direct link to 9292ac0105e14177af5eff2131b9c71b")
Represents an input field specifically for `Message` objects.
  * **Usage:** Used in components that handle or process messages.
  * **Input Types:** `["Message"]`


### **MessageTextInput**[​](https://docs.langflow.org/<#5511f5e32b944b4e973379a6bd5405e4> "Direct link to 5511f5e32b944b4e973379a6bd5405e4")
Represents a text input for messages.
  * **Usage:** Suitable for components that need to extract text from message objects.
  * **Input Types:** `["Message"]`


### **MultilineInput**[​](https://docs.langflow.org/<#e6d8315b0fb44a2fb8c62c3f3184bbe9> "Direct link to e6d8315b0fb44a2fb8c62c3f3184bbe9")
Represents a text field that supports multiple lines.
  * **Usage:** Ideal for longer text inputs where the user might need to write extended text.
  * **Input Types:** `["Text"]`
  * **Attributes:** `multiline=True`


### **SecretStrInput**[​](https://docs.langflow.org/<#2283c13aa5f745b8b0009f7d40e59419> "Direct link to 2283c13aa5f745b8b0009f7d40e59419")
Represents a password input field.
  * **Usage:** Used for sensitive text inputs where the input should be hidden (e.g., passwords, API keys).
  * **Attributes:** `password=True`
  * **Input Types:** Does not accept input types, meaning it has no input handles for previous nodes/components to connect to it.


### **IntInput**[​](https://docs.langflow.org/<#612680db6578451daef695bd19827a56> "Direct link to 612680db6578451daef695bd19827a56")
Represents an integer input field.
  * **Usage:** Used for numeric inputs where the value should be an integer.
  * **Input Types:** `["Integer"]`


### **FloatInput**[​](https://docs.langflow.org/<#a15e1fdae15b49fc9bfbf38f8bd7b203> "Direct link to a15e1fdae15b49fc9bfbf38f8bd7b203")
Represents a float input field.
  * **Usage:** Used for numeric inputs where the value should be a floating-point number.
  * **Input Types:** `["Float"]`


### **BoolInput**[​](https://docs.langflow.org/<#3083671e0e7f4390a03396485114be66> "Direct link to 3083671e0e7f4390a03396485114be66")
Represents a boolean input field.
  * **Usage:** Used for true/false or yes/no type inputs.
  * **Input Types:** `["Boolean"]`


### **NestedDictInput**[​](https://docs.langflow.org/<#2866fc4018e743d8a45afde53f1e57be> "Direct link to 2866fc4018e743d8a45afde53f1e57be")
Represents an input field for nested dictionaries.
  * **Usage:** Used for more complex data structures where the input needs to be a dictionary.
  * **Input Types:** `["NestedDict"]`


### **DictInput**[​](https://docs.langflow.org/<#daa2c2398f694ec199b425e2ed4bcf93> "Direct link to daa2c2398f694ec199b425e2ed4bcf93")
Represents an input field for dictionaries.
  * **Usage:** Suitable for inputs that require a dictionary format.
  * **Input Types:** `["Dict"]`


### **DropdownInput**[​](https://docs.langflow.org/<#14dcdef11bab4d3f8127eaf2e36a77b9> "Direct link to 14dcdef11bab4d3f8127eaf2e36a77b9")
Represents a dropdown input field.
  * **Usage:** Used where the user needs to select from a predefined list of options.
  * **Attributes:** `options` to define the list of selectable options.
  * **Input Types:** `["Text"]`


### **FileInput**[​](https://docs.langflow.org/<#73e6377dc5f446f39517a558a1291410> "Direct link to 73e6377dc5f446f39517a558a1291410")
Represents a file input field.
  * **Usage:** Used to upload files.
  * **Attributes:** `file_types` to specify the types of files that can be uploaded.
  * **Input Types:** `["File"]`


### Generic Input[​](https://docs.langflow.org/<#278e2027493e45b68746af0a5b6c06f6> "Direct link to Generic Input")
Langflow offers native input types, but you can use any type as long as they are properly annotated in the output methods (e.g., `-> list[int]`).
The `Input` class is highly customizable, allowing you to specify a wide range of attributes for each input field. It has several attributes that can be customized:
  * `field_type`: Specifies the type of field (e.g., `str`, `int`). Default is `str`.
  * `required`: Boolean indicating if the field is required. Default is `False`.
  * `placeholder`: Placeholder text for the input field. Default is an empty string.
  * `is_list`: Boolean indicating if the field should accept a list of values. Default is `False`.
  * `show`: Boolean indicating if the field should be shown. Default is `True`.
  * `multiline`: Boolean indicating if the field should allow multi-line input. Default is `False`.
  * `value`: Default value for the input field. Default is `None`.
  * `file_types`: List of accepted file types (for file inputs). Default is an empty list.
  * `file_path`: File path if the field is a file input. Default is `None`.
  * `password`: Boolean indicating if the field is a password. Default is `False`.
  * `options`: List of options for the field (for dropdowns). Default is `None`.
  * `name`: Name of the input field. Default is `None`.
  * `display_name`: Display name for the input field. Default is `None`.
  * `advanced`: Boolean indicating if the field is an advanced parameter. Default is `False`.
  * `input_types`: List of accepted input types. Default is `None`.
  * `dynamic`: Boolean indicating if the field is dynamic. Default is `False`.
  * `info`: Additional information or tooltip for the input field. Default is an empty string.
  * `real_time_refresh`: Boolean indicating if the field should refresh in real-time. Default is `None`.
  * `refresh_button`: Boolean indicating if the field should have a refresh button. Default is `None`.
  * `refresh_button_text`: Text for the refresh button. Default is `None`.
  * `range_spec`: Range specification for numeric fields. Default is `None`.
  * `load_from_db`: Boolean indicating if the field should load from the database. Default is `False`.
  * `title_case`: Boolean indicating if the display name should be in title case. Default is `True`.


## Create a Custom Component with Generic Input[​](https://docs.langflow.org/<#create-a-custom-component-with-generic-input> "Direct link to Create a Custom Component with Generic Input")
Here is an example of how to define inputs for a component using the `Input` class.
Copy and paste it into the Custom Component code pane and click **Check & Save.**
`
_76
from langflow.template import Input, Output
_76
from langflow.custom import Component
_76
from langflow.field_typing import Text
_76
from langflow.schema.message import Message
_76
from typing import Dict, Any
_76
_76
class TextAnalyzerComponent(Component):
_76
  display_name = "Text Analyzer"
_76
  description = "Analyzes input text and provides basic statistics."
_76
_76
  inputs = [
_76
    Input(
_76
      name="input_text",
_76
      display_name="Input Text",
_76
      field_type="Message",
_76
      required=True,
_76
      placeholder="Enter text to analyze",
_76
      multiline=True,
_76
      info="The text you want to analyze.",
_76
      input_types=["Text"]
_76
    ),
_76
    Input(
_76
      name="include_word_count",
_76
      display_name="Include Word Count",
_76
      field_type="bool",
_76
      required=False,
_76
      info="Whether to include word count in the analysis.",
_76
    ),
_76
    Input(
_76
      name="perform_sentiment_analysis",
_76
      display_name="Perform Sentiment Analysis",
_76
      field_type="bool",
_76
      required=False,
_76
      info="Whether to perform basic sentiment analysis.",
_76
    ),
_76
  ]
_76
_76
  outputs = [
_76
    Output(display_name="Analysis Results", name="results", method="analyze_text"),
_76
  ]
_76
_76
  def analyze_text(self) -> Message:
_76
    # Extract text from the Message object
_76
    if isinstance(self.input_text, Message):
_76
      text = self.input_text.text
_76
    else:
_76
      text = str(self.input_text)
_76
_76
    results = {
_76
      "character_count": len(text),
_76
      "sentence_count": text.count('.') + text.count('!') + text.count('?')
_76
    }
_76
_76
    if self.include_word_count:
_76
      results["word_count"] = len(text.split())
_76
_76
    if self.perform_sentiment_analysis:
_76
      # Basic sentiment analysis
_76
      text_lower = text.lower()
_76
      if "happy" in text_lower or "good" in text_lower:
_76
        sentiment = "positive"
_76
      elif "sad" in text_lower or "bad" in text_lower:
_76
        sentiment = "negative"
_76
      else:
_76
        sentiment = "neutral"
_76
_76
      results["sentiment"] = sentiment
_76
_76
    # Convert the results dictionary to a formatted string
_76
    formatted_results = "\n".join([f"{key}: {value}" for key, value in results.items()])
_76
_76
    # Return a Message object
_76
    return Message(text=formatted_results)
_76
_76
# Define how to use the inputs and outputs
_76
component = TextAnalyzerComponent()
`
In this custom component:
  * The `input_text` input is a required multi-line text field that accepts a Message object or a string. It's used to provide the text for analysis.
  * The `include_word_count` input is an optional boolean field. When set to True, it adds a word count to the analysis results.
  * The `perform_sentiment_analysis` input is an optional boolean field. When set to True, it triggers a basic sentiment analysis of the input text.


The component performs basic text analysis, including character count and sentence count (based on punctuation marks). If word count is enabled, it splits the text and counts the words. If sentiment analysis is enabled, it performs a simple keyword-based sentiment classification (positive, negative, or neutral).
Since the component inputs and outputs a `Message`, you can wire the component into a chat and see how the basic custom component logic interacts with your input.
## Create a Custom Component with Multiple Outputs[​](https://docs.langflow.org/<#6f225be8a142450aa19ee8e46a3b3c8c> "Direct link to Create a Custom Component with Multiple Outputs")
In Langflow, custom components can have multiple outputs. Each output can be associated with a specific method in the component, allowing you to define distinct behaviors for each output path. This feature is particularly useful when you want to route data based on certain conditions or process it in multiple ways.
  1. **Definition of Outputs** : Each output is defined in the `outputs` list of the component. Each output is associated with a display name, an internal name, and a method that gets called to generate the output.
  2. **Output Methods** : The methods associated with outputs are responsible for generating the data for that particular output. These methods are called when the component is executed, and each method can independently produce its result.


This example component has two outputs:
  * `process_data`: Processes the input text (e.g., converts it to uppercase) and returns it.
  * `get_processing_function`: Returns the `process_data` method itself to be reused in composition.


`
_33
from typing import Callable
_33
from langflow.custom import Component
_33
from langflow.inputs import StrInput
_33
from langflow.template import Output
_33
from langflow.field_typing import Text
_33
_33
class DualOutputComponent(Component):
_33
  display_name = "Dual Output"
_33
  description = "Processes input text and returns both the result and the processing function."
_33
  icon = "double-arrow"
_33
_33
  inputs = [
_33
    StrInput(
_33
      name="input_text",
_33
      display_name="Input Text",
_33
      info="The text input to be processed.",
_33
    ),
_33
  ]
_33
_33
  outputs = [
_33
    Output(display_name="Processed Data", name="processed_data", method="process_data"),
_33
    Output(display_name="Processing Function", name="processing_function", method="get_processing_function"),
_33
  ]
_33
_33
  def process_data(self) -> Text:
_33
    # Process the input text (e.g., convert to uppercase)
_33
    processed = self.input_text.upper()
_33
    self.status = processed
_33
    return processed
_33
_33
  def get_processing_function(self) -> Callable[[], Text]:
_33
    # Return the processing function itself
_33
    return self.process_data
`
This example shows how to define multiple outputs in a custom component. The first output returns the processed data, while the second output returns the processing function itself.
The `processing_function` output can be used in scenarios where the function itself is needed for further processing or dynamic flow control. Notice how both outputs are properly annotated with their respective types, ensuring clarity and type safety.
## Special Operations[​](https://docs.langflow.org/<#special-operations> "Direct link to Special Operations")
Advanced methods and attributes offer additional control and functionality. Understanding how to leverage these can enhance your custom components' capabilities.
  * `self.inputs`: Access all defined inputs. Useful when an output method needs to interact with multiple inputs.
  * `self.outputs`: Access all defined outputs. This is particularly useful if an output function needs to trigger another output function.
  * `self.status`: Use this to update the component's status or intermediate results. It helps track the component's internal state or store temporary data.
  * `self.graph.flow_id`: Retrieve the flow ID, useful for maintaining context or debugging.
  * `self.stop("output_name")`: Use this method within an output function to prevent data from being sent through other components. This method stops next component execution and is particularly useful for specific operations where a component should stop from running based on specific conditions.


## Contribute Custom Components to Langflow[​](https://docs.langflow.org/<#contribute-custom-components-to-langflow> "Direct link to Contribute Custom Components to Langflow")
See [How to Contribute](https://docs.langflow.org/</contributing-components>) to contribute your custom component to Langflow.
[PreviousAgents](https://docs.langflow.org/</components-agents>)[NextData](https://docs.langflow.org/</components-data>)
  * [Directory structure requirements](https://docs.langflow.org/<#directory-structure-requirements>)
  * [Create a custom component in Langflow](https://docs.langflow.org/<#create-a-custom-component-in-langflow>)
  * [Add inputs and modify output methods](https://docs.langflow.org/<#add-inputs-and-modify-output-methods>)
  * [Input Types](https://docs.langflow.org/<#3815589831f24ab792328ed233c8b00d>)
    * [**HandleInput**](https://docs.langflow.org/<#fb06c48a326043ffa46badc1ab3ba467>)
    * [**DataInput**](https://docs.langflow.org/<#0e1dcb768e38487180d720b0884a90f5>)
    * [**StrInput**](https://docs.langflow.org/<#4ec6e68ad9ab4cd194e8e607bc5b3411>)
    * [**MessageInput**](https://docs.langflow.org/<#9292ac0105e14177af5eff2131b9c71b>)
    * [**MessageTextInput**](https://docs.langflow.org/<#5511f5e32b944b4e973379a6bd5405e4>)
    * [**MultilineInput**](https://docs.langflow.org/<#e6d8315b0fb44a2fb8c62c3f3184bbe9>)
    * [**SecretStrInput**](https://docs.langflow.org/<#2283c13aa5f745b8b0009f7d40e59419>)
    * [**IntInput**](https://docs.langflow.org/<#612680db6578451daef695bd19827a56>)
    * [**FloatInput**](https://docs.langflow.org/<#a15e1fdae15b49fc9bfbf38f8bd7b203>)
    * [**BoolInput**](https://docs.langflow.org/<#3083671e0e7f4390a03396485114be66>)
    * [**NestedDictInput**](https://docs.langflow.org/<#2866fc4018e743d8a45afde53f1e57be>)
    * [**DictInput**](https://docs.langflow.org/<#daa2c2398f694ec199b425e2ed4bcf93>)
    * [**DropdownInput**](https://docs.langflow.org/<#14dcdef11bab4d3f8127eaf2e36a77b9>)
    * [**FileInput**](https://docs.langflow.org/<#73e6377dc5f446f39517a558a1291410>)
    * [Generic Input](https://docs.langflow.org/<#278e2027493e45b68746af0a5b6c06f6>)
  * [Create a Custom Component with Generic Input](https://docs.langflow.org/<#create-a-custom-component-with-generic-input>)
  * [Create a Custom Component with Multiple Outputs](https://docs.langflow.org/<#6f225be8a142450aa19ee8e46a3b3c8c>)
  * [Special Operations](https://docs.langflow.org/<#special-operations>)
  * [Contribute Custom Components to Langflow](https://docs.langflow.org/<#contribute-custom-components-to-langflow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=9b8a7f39-54d7-428b-99fe-ac42d4124d02&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=55b271a7-11b9-4dff-beed-5ebd09ea09e3&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-custom-components&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=9b8a7f39-54d7-428b-99fe-ac42d4124d02&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=55b271a7-11b9-4dff-beed-5ebd09ea09e3&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-custom-components&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
