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
  * Langflow objects


On this page
# Langflow objects
In Langflow, objects are [Pydantic](https://docs.langflow.org/<https:/docs.pydantic.dev/latest/api/base_model/>) models that serve as structured, functional representations of data.
## Data object[​](https://docs.langflow.org/<#data-object> "Direct link to Data object")
The `Data` object is a [Pydantic](https://docs.langflow.org/<https:/docs.pydantic.dev/latest/api/base_model/>) model that serves as a container for storing and manipulating data. It carries `data`—a dictionary that can be accessed as attributes—and uses `text_key` to specify which key in the dictionary should be considered the primary text content.
  * **Main Attributes:**
    * `text_key`: Specifies the key to retrieve the primary text data.
    * `data`: A dictionary to store additional data.
    * `default_value`: default value when the `text_key` is not present in the `data` dictionary.


### Create a Data Object[​](https://docs.langflow.org/<#create-a-data-object> "Direct link to Create a Data Object")
Create a `Data` object by directly assigning key-value pairs to it. For example:
`
1
from langflow.schema import Data
23
# Creating a Data object with specified key-value pairs
4
data = Data(text="my_string", bar=3, foo="another_string")
56
# Outputs:
7
print(data.text) # Outputs: "my_string"
8
print(data.bar)  # Outputs: 3
9
print(data.foo)  # Outputs: "another_string"
`
The `text_key` specifies which key in the `data` dictionary should be considered the primary text content. The `default_value` provides a fallback if the `text_key` is not present.
`
1
# Creating a Data object with a specific text_key and default_value
2
data = Data(data={"title": "Hello, World!"}, text_key="content", default_value="No content available")
34
# Accessing the primary text using text_key and default_value
5
print(data.get_text()) # Outputs: "No content available" because "content" key is not in the data dictionary
67
# Accessing data keys by calling the attribute directly
8
print(data.title) # Outputs: "Hello, World!" because "title" key is in the data dictionary
`
The `Data` object is also convenient for visualization of outputs, since the output preview has visual elements to inspect data as a table and its cells as pop ups for basic types. The idea is to create a unified way to work and visualize complex information in Langflow.
To receive `Data` objects in a component input, use the `DataInput` input type.
`
1
inputs = [
2
    DataInput(name="data", display_name="Data", info="Helpful info about the incoming data object.", is_list=True),
3
]
`
## Message object[​](https://docs.langflow.org/<#message-object> "Direct link to Message object")
The `Message` object extends the functionality of `Data` and includes additional attributes and methods for chat interactions.
  * **Core message data:**
    * `text`: The main text content of the message
    * `sender`: Identifier for the sender ("User" or "AI")
    * `sender_name`: Name of the sender
    * `session_id`: Identifier for the chat session (`string` or `UUID`)
    * `timestamp`: Timestamp when the message was created (UTC)
    * `flow_id`: Identifier for the flow (`string` or `UUID`)
    * `id`: Unique identifier for the message
  * **Content and files:**
    * `files`: List of files or images associated with the message
    * `content_blocks`: List of structured content block objects
    * `properties`: Additional properties including visual styling and source information
  * **Message state:**
    * `error`: Boolean indicating if there was an error
    * `edit`: Boolean indicating if the message was edited
    * `category`: Message category ("message", "error", "warning", "info")


The `Message` object can be used to send, store, and manipulate chat messages within Langflow.
### Create a Message object[​](https://docs.langflow.org/<#create-a-message-object> "Direct link to Create a Message object")
You can create a `Message` object by directly assigning key-value pairs to it. For example:
`
1
from langflow.schema.message import Message
23
message = Message(text="Hello, AI!", sender="User", sender_name="John Doe")
`
To receive `Message` objects in a component input, you can use the `MessageInput` input type or `MessageTextInput` when the goal is to extract just the `text` field of the `Message` object.
## ContentBlock object[​](https://docs.langflow.org/<#contentblock-object> "Direct link to ContentBlock object")
The `ContentBlock` object is a list of multiple `ContentTypes`. It allows you to include multiple types of content within a single `Message`, including images, videos, and text.
Content types are Pydantic base classes constructed from the types in [content_types.py](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/schema/content_types.py>).
Each content type has specific fields related to its data type. For example:
  * `TextContent` has a `text` field for storing strings of text
  * `MediaContent` has a `urls` field for storing media file URLs
  * `CodeContent` has `code` and `language` fields for code snippets
  * `JSONContent` has a `data` field for storing arbitrary JSON data
  * `ToolContent` has a `tool_input` field for storing input parameters for the tool


### Create a ContentBlock object[​](https://docs.langflow.org/<#create-a-contentblock-object> "Direct link to Create a ContentBlock object")
Create a `ContentBlock` object with a list of different content types.
`
1
content_block = ContentBlock(
2
  title="Mixed Content Example",
3
  contents=[
4
    TextContent(text="This is a text content"),
5
    MediaContent(urls=["http://example.com/image.jpg"]),
6
    JSONContent(data={"key": "value"}),
7
    CodeContent(code="print('Hello')", language="python")
8
  ],
9
  media_url=["http://example.com/additional_image.jpg"]
10
)
`
### Add ContentBlocks objects to a message[​](https://docs.langflow.org/<#add-contentblocks-objects-to-a-message> "Direct link to Add ContentBlocks objects to a message")
In this example, a text and a media `ContentBlock` are added to a message.
`
1
from langflow.schema.message import Message
2
from langflow.schema.content_block import ContentBlock
3
from langflow.schema.content_types import TextContent, MediaContent
45
message = Message(
6
  text="Main message text",
7
  sender="User",
8
  sender_name="John Doe",
9
  content_blocks=[
10
    ContentBlock(
11
      title="Text Block",
12
      contents=[
13
        TextContent(type="text", text="This is some text content")
14
      ]
15
    ),
16
    ContentBlock(
17
      title="Media Block",
18
      contents=[
19
        MediaContent(type="media", urls=["http://example.com/image.jpg"])
20
      ]
21
    )
22
  ]
23
)
`
## DataFrame object[​](https://docs.langflow.org/<#dataframe-object> "Direct link to DataFrame object")
The `DataFrame` class is a custom extension of the Pandas [DataFrame](https://docs.langflow.org/<https:/pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>) class, specifically designed to work seamlessly with Langflow's `Data` objects. The class includes methods for converting between `DataFrame` and lists of `Data` objects.
A `DataFrame` object accepts various input formats, including lists of `Data` objects, dictionaries, and existing `DataFrames`.
### Create a DataFrame object[​](https://docs.langflow.org/<#create-a-dataframe-object> "Direct link to Create a DataFrame object")
You can create a DataFrame object using different data formats:
`
1
from langflow.schema import Data
2
from langflow.schema.data import DataFrame
34
# From a list of Data objects
5
data_list = [Data(data={"name": "John"}), Data(data={"name": "Jane"})]
6
df = DataFrame(data_list)
78
# From a list of dictionaries
9
dict_list = [{"name": "John"}, {"name": "Jane"}]
10
df = DataFrame(dict_list)
1112
# From a dictionary of lists
13
data_dict = {"name": ["John", "Jane"], "age": [30, 25]}
14
df = DataFrame(data_dict)
15
Key Methods
16
to_data_list(): Converts the DataFrame back to a list of Data objects.
17
add_row(data): Adds a single row (either a Data object or a dictionary) to the DataFrame.
18
add_rows(data): Adds multiple rows (list of Data objects or dictionaries) to the DataFrame.
19
Usage Example
20
python
21
# Create a DataFrame
22
df = DataFrame([Data(data={"name": "John"}), Data(data={"name": "Jane"})])
2324
# Add a new row
25
df = df.add_row({"name": "Alice"})
2627
# Convert back to a list of Data objects
28
data_list = df.to_data_list()
2930
# Use pandas functionality
31
filtered_df = df[df["name"].str.startswith("J")]
`
To use DataFrame objects in a component input,use the DataFrameInput input type.
`
1
DataFrameInput(
2
  name="dataframe_input", display_name="DataFrame Input", info="Input for DataFrame objects.", tool_mode=True
3
),
`
[PreviousFlows](https://docs.langflow.org/</Concepts/concepts-flows>)[NextAPI pane](https://docs.langflow.org/</concepts-api>)
  * [Data object](https://docs.langflow.org/<#data-object>)
    * [Create a Data Object](https://docs.langflow.org/<#create-a-data-object>)
  * [Message object](https://docs.langflow.org/<#message-object>)
    * [Create a Message object](https://docs.langflow.org/<#create-a-message-object>)
  * [ContentBlock object](https://docs.langflow.org/<#contentblock-object>)
    * [Create a ContentBlock object](https://docs.langflow.org/<#create-a-contentblock-object>)
    * [Add ContentBlocks objects to a message](https://docs.langflow.org/<#add-contentblocks-objects-to-a-message>)
  * [DataFrame object](https://docs.langflow.org/<#dataframe-object>)
    * [Create a DataFrame object](https://docs.langflow.org/<#create-a-dataframe-object>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
