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
  * Processing


On this page
# Processing components in Langflow
Processing components process and transform data within a flow.
## Use a processing component in a flow[​](https://docs.langflow.org/<#use-a-processing-component-in-a-flow> "Direct link to Use a processing component in a flow")
The **Split Text** processing component in this flow splits the incoming [data](https://docs.langflow.org/</concepts-objects>) into chunks to be embedded into the vector store component.
The component offers control over chunk size, overlap, and separator, which affect context and granularity in vector store retrieval results.
![](https://docs.langflow.org/assets/images/vector-store-document-ingestion-fce32e9be440846a2545397e3a18b7bf.png)
## Combine Text[​](https://docs.langflow.org/<#combine-text> "Direct link to Combine Text")
This component concatenates two text sources into a single text chunk using a specified delimiter.
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
first_text| First Text| The first text input to concatenate.  
second_text| Second Text| The second text input to concatenate.  
delimiter| Delimiter| A string used to separate the two text inputs. Defaults to a space.  
## DataFrame operations[​](https://docs.langflow.org/<#dataframe-operations> "Direct link to DataFrame operations")
This component performs the following operations on Pandas [DataFrame](https://docs.langflow.org/<https:/pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>):
Operation| Description| Required Inputs  
---|---|---  
Add Column| Adds a new column with a constant value| new_column_name, new_column_value  
Drop Column| Removes a specified column| column_name  
Filter| Filters rows based on column value| column_name, filter_value  
Head| Returns first n rows| num_rows  
Rename Column| Renames an existing column| column_name, new_column_name  
Replace Value| Replaces values in a column| column_name, replace_value, replacement_value  
Select Columns| Selects specific columns| columns_to_select  
Sort| Sorts DataFrame by column| column_name, ascending  
Tail| Returns last n rows| num_rows  
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
df| DataFrame| The input DataFrame to operate on.  
operation| Operation| Select the DataFrame operation to perform. Options: Add Column, Drop Column, Filter, Head, Rename Column, Replace Value, Select Columns, Sort, Tail  
column_name| Column Name| The column name to use for the operation.  
filter_value| Filter Value| The value to filter rows by.  
ascending| Sort Ascending| Whether to sort in ascending order.  
new_column_name| New Column Name| The new column name when renaming or adding a column.  
new_column_value| New Column Value| The value to populate the new column with.  
columns_to_select| Columns to Select| List of column names to select.  
num_rows| Number of Rows| Number of rows to return (for head/tail). Default: 5  
replace_value| Value to Replace| The value to replace in the column.  
replacement_value| Replacement Value| The value to replace with.  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
output| DataFrame| The resulting DataFrame after the operation.  
## Filter Data[​](https://docs.langflow.org/<#filter-data> "Direct link to Filter Data")
This component filters a Data object based on a list of keys.
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
data| Data| Data object to filter.  
filter_criteria| Filter Criteria| List of keys to filter by.  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
filtered_data| Filtered Data| A new Data object containing only the key-value pairs that match the filter criteria.  
## Parse JSON[​](https://docs.langflow.org/<#parse-json> "Direct link to Parse JSON")
This component converts and extracts JSON fields using JQ queries.
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
input_value| Input| Data object to filter. Can be a message or data object.  
query| JQ Query| JQ Query to filter the data. The input is always a JSON list.  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
filtered_data| Filtered Data| Filtered data as a list of data objects.  
## Merge Data component[​](https://docs.langflow.org/<#merge-data-component> "Direct link to Merge Data component")
This component combines multiple data sources into a single unified Data object.
The component iterates through the input list of data objects, merging them into a single data object. If the input list is empty, it returns an empty data object. If there's only one input data object, it returns that object unchanged. The merging process uses the addition operator to combine data objects.
### Inputs[​](https://docs.langflow.org/<#inputs-4> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
data| Data| A list of data objects to be merged  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
merged_data| Merged Data| A single data object containing the combined information from all input data objects  
## Parse Data[​](https://docs.langflow.org/<#parse-data> "Direct link to Parse Data")
The ParseData component converts data objects into plain text using a specified template. This component transforms structured data into human-readable text formats, allowing for customizable output through the use of templates.
### Inputs[​](https://docs.langflow.org/<#inputs-5> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
data| Data| The data to convert to text.  
template| Template| The template to use for formatting the data. It can contain the keys `{text}`, `{data}` or any other key in the data.  
sep| Separator| The separator to use between multiple data items.  
### Outputs[​](https://docs.langflow.org/<#outputs-4> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
text| Text| The resulting formatted text string as a message object.  
## Split Text[​](https://docs.langflow.org/<#split-text> "Direct link to Split Text")
This component splits text into chunks of a specified length.
### Inputs[​](https://docs.langflow.org/<#inputs-6> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
texts| Texts| Texts to split.  
separators| Separators| Characters to split on. Defaults to a space.  
max_chunk_size| Max Chunk Size| The maximum length, in characters, of each chunk.  
chunk_overlap| Chunk Overlap| The amount of character overlap between chunks.  
recursive| Recursive| Whether to split recursively.  
[PreviousModels](https://docs.langflow.org/</components-models>)[NextPrompts](https://docs.langflow.org/</components-prompts>)
  * [Use a processing component in a flow](https://docs.langflow.org/<#use-a-processing-component-in-a-flow>)
  * [Combine Text](https://docs.langflow.org/<#combine-text>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
  * [DataFrame operations](https://docs.langflow.org/<#dataframe-operations>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [Filter Data](https://docs.langflow.org/<#filter-data>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Parse JSON](https://docs.langflow.org/<#parse-json>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Merge Data component](https://docs.langflow.org/<#merge-data-component>)
    * [Inputs](https://docs.langflow.org/<#inputs-4>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [Parse Data](https://docs.langflow.org/<#parse-data>)
    * [Inputs](https://docs.langflow.org/<#inputs-5>)
    * [Outputs](https://docs.langflow.org/<#outputs-4>)
  * [Split Text](https://docs.langflow.org/<#split-text>)
    * [Inputs](https://docs.langflow.org/<#inputs-6>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
