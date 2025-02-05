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
  * Vector stores


On this page
# Vector store components in Langflow
Vector databases store vector data, which backs AI workloads like chatbots and Retrieval Augmented Generation.
Vector database components establish connections to existing vector databases or create in-memory vector stores for storing and retrieving vector data.
Vector database components are distinct from [memory components](https://docs.langflow.org/</components-memories>), which are built specifically for storing and retrieving chat messages from external databases.
## Use a vector store component in a flow[​](https://docs.langflow.org/<#use-a-vector-store-component-in-a-flow> "Direct link to Use a vector store component in a flow")
Vector databases can be populated from within Langflow with document ingestion pipelines, like the following
![](https://docs.langflow.org/assets/images/vector-store-document-ingestion-fce32e9be440846a2545397e3a18b7bf.png)
This example uses the **Astra DB vector store** component. Your vector store component's parameters and authentication may be different, but the document ingestion workflow is the same. A document is loaded from a local machine and chunked. The Astra DB vector store generates embeddings with the connected [model](https://docs.langflow.org/</components-models>) component, and stores them in the connected Astra DB database.
This vector data can then be retrieved for workloads like Retrieval Augmented Generation.
![](https://docs.langflow.org/assets/images/vector-store-retrieval-452b8316c734a28f85fcddf9ff7a32e4.png)
The user's chat input is embedded and compared to the vectors embedded during document ingestion for a similarity search. The results are output from the vector database component as a [Data](https://docs.langflow.org/</concepts-objects>) object and parsed into text. This text fills the `{context}` variable in the **Prompt** component, which informs the **Open AI model** component's responses.
Alternatively, connect the vector database component's **Retriever** port to a [retriever tool](https://docs.langflow.org/</components-tools#retriever-tool>), and then to an [agent](https://docs.langflow.org/</components-agents>) component. This enables the agent to use your vector database as a tool and make decisions based on the available data.
![](https://docs.langflow.org/assets/images/vector-store-agent-retrieval-tool-79066d11008a74c40390f55f7c73bd71.png)
## Astra DB Vector Store[​](https://docs.langflow.org/<#astra-db-vector-store> "Direct link to Astra DB Vector Store")
This component implements a Vector Store using Astra DB with search capabilities.
For more information, see the [DataStax documentation](https://docs.langflow.org/<https:/docs.datastax.com/en/astra-db-serverless/databases/create-database.html>).
### Inputs[​](https://docs.langflow.org/<#inputs> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
collection_name| Collection Name| The name of the collection within Astra DB where the vectors will be stored (required)  
token| Astra DB Application Token| Authentication token for accessing Astra DB (required)  
api_endpoint| API Endpoint| API endpoint URL for the Astra DB service (required)  
search_input| Search Input| Query string for similarity search  
ingest_data| Ingest Data| Data to be ingested into the vector store  
namespace| Namespace| Optional namespace within Astra DB to use for the collection  
embedding_choice| Embedding Model or Astra Vectorize| Determines whether to use an Embedding Model or Astra Vectorize for the collection  
embedding| Embedding Model| Allows an embedding model configuration (when using Embedding Model)  
provider| Vectorize Provider| Provider for Astra Vectorize (when using Astra Vectorize)  
metric| Metric| Optional distance metric for vector comparisons  
batch_size| Batch Size| Optional number of data to process in a single batch  
setup_mode| Setup Mode| Configuration mode for setting up the vector store (options: "Sync", "Async", "Off", default: "Sync")  
pre_delete_collection| Pre Delete Collection| Boolean flag to determine whether to delete the collection before creating a new one  
number_of_results| Number of Results| Number of results to return in similarity search (default: 4)  
search_type| Search Type| Search type to use (options: "Similarity", "Similarity with score threshold", "MMR (Max Marginal Relevance)")  
search_score_threshold| Search Score Threshold| Minimum similarity score threshold for search results  
search_filter| Search Metadata Filter| Optional dictionary of filters to apply to the search query  
### Outputs[​](https://docs.langflow.org/<#outputs> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
vector_store| Vector Store| Built Astra DB vector store  
search_results| Search Results| Results of the similarity search as a list of Data objects  
## Cassandra[​](https://docs.langflow.org/<#cassandra> "Direct link to Cassandra")
This component creates a Cassandra Vector Store with search capabilities. For more information, see the [Cassandra documentation](https://docs.langflow.org/<https:/cassandra.apache.org/doc/latest/cassandra/vector-search/overview.html>).
### Inputs[​](https://docs.langflow.org/<#inputs-1> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
database_ref| String| Contact points for the database or AstraDB database ID  
username| String| Username for the database (leave empty for AstraDB)  
token| SecretString| User password for the database or AstraDB token  
keyspace| String| Table Keyspace or AstraDB namespace  
table_name| String| Name of the table or AstraDB collection  
ttl_seconds| Integer| Time-to-live for added texts  
batch_size| Integer| Number of data to process in a single batch  
setup_mode| String| Configuration mode for setting up the Cassandra table  
cluster_kwargs| Dict| Additional keyword arguments for the Cassandra cluster  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
number_of_results| Integer| Number of results to return in search  
search_type| String| Type of search to perform  
search_score_threshold| Float| Minimum similarity score for search results  
search_filter| Dict| Metadata filters for search query  
body_search| String| Document textual search terms  
enable_body_search| Boolean| Flag to enable body search  
### Outputs[​](https://docs.langflow.org/<#outputs-1> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| Cassandra| Cassandra vector store instance  
search_results| List[Data]| Results of similarity search  
## Cassandra Graph Vector Store[​](https://docs.langflow.org/<#cassandra-graph-vector-store> "Direct link to Cassandra Graph Vector Store")
This component implements a Cassandra Graph Vector Store with search capabilities.
### Inputs[​](https://docs.langflow.org/<#inputs-2> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
database_ref| Contact Points / Astra Database ID| Contact points for the database or AstraDB database ID (required)  
username| Username| Username for the database (leave empty for AstraDB)  
token| Password / AstraDB Token| User password for the database or AstraDB token (required)  
keyspace| Keyspace| Table Keyspace or AstraDB namespace (required)  
table_name| Table Name| The name of the table or AstraDB collection where vectors will be stored (required)  
setup_mode| Setup Mode| Configuration mode for setting up the Cassandra table (options: "Sync", "Off", default: "Sync")  
cluster_kwargs| Cluster arguments| Optional dictionary of additional keyword arguments for the Cassandra cluster  
search_query| Search Query| Query string for similarity search  
ingest_data| Ingest Data| Data to be ingested into the vector store (list of Data objects)  
embedding| Embedding| Embedding model to use  
number_of_results| Number of Results| Number of results to return in similarity search (default: 4)  
search_type| Search Type| Search type to use (options: "Traversal", "MMR traversal", "Similarity", "Similarity with score threshold", "MMR (Max Marginal Relevance)", default: "Traversal")  
depth| Depth of traversal| The maximum depth of edges to traverse (for "Traversal" or "MMR traversal" search types, default: 1)  
search_score_threshold| Search Score Threshold| Minimum similarity score threshold for search results (for "Similarity with score threshold" search type)  
search_filter| Search Metadata Filter| Optional dictionary of filters to apply to the search query  
### Outputs[​](https://docs.langflow.org/<#outputs-2> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
vector_store| Vector Store| Built Cassandra Graph vector store  
search_results| Search Results| Results of the similarity search as a list of Data objects  
## Chroma DB[​](https://docs.langflow.org/<#chroma-db> "Direct link to Chroma DB")
This component creates a Chroma Vector Store with search capabilities. For more information, see the [Chroma documentation](https://docs.langflow.org/<https:/docs.trychroma.com/>).
### Inputs[​](https://docs.langflow.org/<#inputs-3> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
collection_name| String| The name of the Chroma collection. Default: "langflow".  
persist_directory| String| The directory to persist the Chroma database.  
search_query| String| The query to search for in the vector store.  
ingest_data| Data| The data to ingest into the vector store (list of Data objects).  
embedding| Embeddings| The embedding function to use for the vector store.  
chroma_server_cors_allow_origins| String| CORS allow origins for the Chroma server.  
chroma_server_host| String| Host for the Chroma server.  
chroma_server_http_port| Integer| HTTP port for the Chroma server.  
chroma_server_grpc_port| Integer| gRPC port for the Chroma server.  
chroma_server_ssl_enabled| Boolean| Enable SSL for the Chroma server.  
allow_duplicates| Boolean| Allow duplicate documents in the vector store.  
search_type| String| Type of search to perform: "Similarity" or "MMR".  
number_of_results| Integer| Number of results to return from the search. Default: 10.  
limit| Integer| Limit the number of records to compare when Allow Duplicates is False.  
### Outputs[​](https://docs.langflow.org/<#outputs-3> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| Chroma| Chroma vector store instance  
search_results| List[Data]| Results of similarity search  
## Clickhouse[​](https://docs.langflow.org/<#clickhouse> "Direct link to Clickhouse")
This component implements a Clickhouse Vector Store with search capabilities. For more information, see the [CLickhouse Documentation](https://docs.langflow.org/<https:/clickhouse.com/docs/en/intro>).
### Inputs[​](https://docs.langflow.org/<#inputs-4> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
host| hostname| Clickhouse server hostname (required, default: "localhost")  
port| port| Clickhouse server port (required, default: 8123)  
database| database| Clickhouse database name (required)  
table| Table name| Clickhouse table name (required)  
username| The ClickHouse user name.| Username for authentication (required)  
password| The password for username.| Password for authentication (required)  
index_type| index_type| Type of the index (options: "annoy", "vector_similarity", default: "annoy")  
metric| metric| Metric to compute distance (options: "angular", "euclidean", "manhattan", "hamming", "dot", default: "angular")  
secure| Use https/TLS| Overrides inferred values from the interface or port arguments (default: false)  
index_param| Param of the index| Index parameters (default: "'L2Distance',100")  
index_query_params| index query params| Additional index query parameters  
search_query| Search Query| Query string for similarity search  
ingest_data| Ingest Data| Data to be ingested into the vector store  
embedding| Embedding| Embedding model to use  
number_of_results| Number of Results| Number of results to return in similarity search (default: 4)  
score_threshold| Score threshold| Threshold for similarity scores  
### Outputs[​](https://docs.langflow.org/<#outputs-4> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
vector_store| Vector Store| Built Clickhouse vector store  
search_results| Search Results| Results of the similarity search as a list of Data objects  
## Couchbase[​](https://docs.langflow.org/<#couchbase> "Direct link to Couchbase")
This component creates a Couchbase Vector Store with search capabilities. For more information, see the [Couchbase documentation](https://docs.langflow.org/<https:/docs.couchbase.com/home/index.html>).
### Inputs[​](https://docs.langflow.org/<#inputs-5> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
couchbase_connection_string| SecretString| Couchbase Cluster connection string (required).  
couchbase_username| String| Couchbase username (required).  
couchbase_password| SecretString| Couchbase password (required).  
bucket_name| String| Name of the Couchbase bucket (required).  
scope_name| String| Name of the Couchbase scope (required).  
collection_name| String| Name of the Couchbase collection (required).  
index_name| String| Name of the Couchbase index (required).  
search_query| String| The query to search for in the vector store.  
ingest_data| Data| The data to ingest into the vector store (list of Data objects).  
embedding| Embeddings| The embedding function to use for the vector store.  
number_of_results| Integer| Number of results to return from the search. Default: 4 (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-5> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| CouchbaseVectorStore| A Couchbase vector store instance configured with the specified parameters.  
## FAISS[​](https://docs.langflow.org/<#faiss> "Direct link to FAISS")
This component creates a FAISS Vector Store with search capabilities. For more information, see the [FAISS documentation](https://docs.langflow.org/<https:/faiss.ai/index.html>).
### Inputs[​](https://docs.langflow.org/<#inputs-6> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
index_name| String| The name of the FAISS index. Default: "langflow_index".  
persist_directory| String| Path to save the FAISS index. It will be relative to where Langflow is running.  
search_query| String| The query to search for in the vector store.  
ingest_data| Data| The data to ingest into the vector store (list of Data objects or documents).  
allow_dangerous_deserialization| Boolean| Set to True to allow loading pickle files from untrusted sources. Default: True (advanced).  
embedding| Embeddings| The embedding function to use for the vector store.  
number_of_results| Integer| Number of results to return from the search. Default: 4 (advanced).  
### Outputs[​](https://docs.langflow.org/<#outputs-6> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| FAISS| A FAISS vector store instance configured with the specified parameters.  
## Hyper-Converged Database (HCD) Vector Store[​](https://docs.langflow.org/<#hyper-converged-database-hcd-vector-store> "Direct link to Hyper-Converged Database \(HCD\) Vector Store")
This component implements a Vector Store using HCD.
### Inputs[​](https://docs.langflow.org/<#inputs-7> "Direct link to Inputs")
Name| Display Name| Info  
---|---|---  
collection_name| Collection Name| The name of the collection within HCD where the vectors will be stored (required)  
username| HCD Username| Authentication username for accessing HCD (default: "hcd-superuser", required)  
password| HCD Password| Authentication password for accessing HCD (required)  
api_endpoint| HCD API Endpoint| API endpoint URL for the HCD service (required)  
search_input| Search Input| Query string for similarity search  
ingest_data| Ingest Data| Data to be ingested into the vector store  
namespace| Namespace| Optional namespace within HCD to use for the collection (default: "default_namespace")  
ca_certificate| CA Certificate| Optional CA certificate for TLS connections to HCD  
metric| Metric| Optional distance metric for vector comparisons (options: "cosine", "dot_product", "euclidean")  
batch_size| Batch Size| Optional number of data to process in a single batch  
bulk_insert_batch_concurrency| Bulk Insert Batch Concurrency| Optional concurrency level for bulk insert operations  
bulk_insert_overwrite_concurrency| Bulk Insert Overwrite Concurrency| Optional concurrency level for bulk insert operations that overwrite existing data  
bulk_delete_concurrency| Bulk Delete Concurrency| Optional concurrency level for bulk delete operations  
setup_mode| Setup Mode| Configuration mode for setting up the vector store (options: "Sync", "Async", "Off", default: "Sync")  
pre_delete_collection| Pre Delete Collection| Boolean flag to determine whether to delete the collection before creating a new one  
metadata_indexing_include| Metadata Indexing Include| Optional list of metadata fields to include in the indexing  
embedding| Embedding or Astra Vectorize| Allows either an embedding model or an Astra Vectorize configuration  
metadata_indexing_exclude| Metadata Indexing Exclude| Optional list of metadata fields to exclude from the indexing  
collection_indexing_policy| Collection Indexing Policy| Optional dictionary defining the indexing policy for the collection  
number_of_results| Number of Results| Number of results to return in similarity search (default: 4)  
search_type| Search Type| Search type to use (options: "Similarity", "Similarity with score threshold", "MMR (Max Marginal Relevance)", default: "Similarity")  
search_score_threshold| Search Score Threshold| Minimum similarity score threshold for search results (default: 0)  
search_filter| Search Metadata Filter| Optional dictionary of filters to apply to the search query  
### Outputs[​](https://docs.langflow.org/<#outputs-7> "Direct link to Outputs")
Name| Display Name| Info  
---|---|---  
vector_store| Vector Store| Built HCD vector store instance  
search_results| Search Results| Results of similarity search as a list of Data objects  
## Milvus[​](https://docs.langflow.org/<#milvus> "Direct link to Milvus")
This component creates a Milvus Vector Store with search capabilities. For more information, see the [Milvus documentation](https://docs.langflow.org/<https:/milvus.io/docs>).
### Inputs[​](https://docs.langflow.org/<#inputs-8> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
collection_name| String| Name of the Milvus collection  
collection_description| String| Description of the Milvus collection  
uri| String| Connection URI for Milvus  
password| SecretString| Password for Milvus  
username| SecretString| Username for Milvus  
batch_size| Integer| Number of data to process in a single batch  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
number_of_results| Integer| Number of results to return in search  
search_type| String| Type of search to perform  
search_score_threshold| Float| Minimum similarity score for search results  
search_filter| Dict| Metadata filters for search query  
setup_mode| String| Configuration mode for setting up the vector store  
vector_dimensions| Integer| Number of dimensions of the vectors  
pre_delete_collection| Boolean| Whether to delete the collection before creating a new one  
### Outputs[​](https://docs.langflow.org/<#outputs-8> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| Milvus| A Milvus vector store instance configured with the specified parameters.  
## MongoDB Atlas[​](https://docs.langflow.org/<#mongodb-atlas> "Direct link to MongoDB Atlas")
This component creates a MongoDB Atlas Vector Store with search capabilities. For more information, see the [MongoDB Atlas documentation](https://docs.langflow.org/<https:/www.mongodb.com/docs/atlas/atlas-vector-search/tutorials/vector-search-quick-start/>).
### Inputs[​](https://docs.langflow.org/<#inputs-9> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
mongodb_atlas_cluster_uri| SecretString| MongoDB Atlas Cluster URI  
db_name| String| Database name  
collection_name| String| Collection name  
index_name| String| Index name  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
number_of_results| Integer| Number of results to return in search  
### Outputs[​](https://docs.langflow.org/<#outputs-9> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| MongoDBAtlasVectorSearch| MongoDB Atlas vector store instance  
search_results| List[Data]| Results of similarity search  
## Opensearch[​](https://docs.langflow.org/<#opensearch> "Direct link to Opensearch")
This component creates an Opensearch vector store with search capabilities For more information, see [Opensearch documentation](https://docs.langflow.org/<https:/opensearch.org/platform/search/vector-database.html>)
### Inputs[​](https://docs.langflow.org/<#inputs-10> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
opensearch_url| String| URL for OpenSearch cluster (e.g. <https://192.168.1.1:9200>)  
index_name| String| The index name where the vectors will be stored in OpenSearch cluster  
search_input| String| Enter a search query. Leave empty to retrieve all documents or if hybrid search is being used  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
search_type| String| Valid values are "similarity", "similarity_score_threshold", "mmr"  
number_of_results| Integer| Number of results to return in search  
search_score_threshold| Float| Minimum similarity score threshold for search results  
username| String| username for the opensource cluster  
password| SecretString| password for the opensource cluster  
use_ssl| Boolean| Use SSL  
verify_certs| Boolean| Verify certificates  
hybrid_search_query| String| Provide a custom hybrid search query in JSON format. This allows you to combine vector similarity and keyword matching  
### Outputs[​](https://docs.langflow.org/<#outputs-10> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| OpenSearchVectorSearch| OpenSearch vector store instance  
search_results| List[Data]| Results of similarity search  
## PGVector[​](https://docs.langflow.org/<#pgvector> "Direct link to PGVector")
This component creates a PGVector Vector Store with search capabilities. For more information, see the [PGVector documentation](https://docs.langflow.org/<https:/github.com/pgvector/pgvector>).
### Inputs[​](https://docs.langflow.org/<#inputs-11> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
pg_server_url| SecretString| PostgreSQL server connection string  
collection_name| String| Table name for the vector store  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
number_of_results| Integer| Number of results to return in search  
### Outputs[​](https://docs.langflow.org/<#outputs-11> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| PGVector| PGVector vector store instance  
search_results| List[Data]| Results of similarity search  
## Pinecone[​](https://docs.langflow.org/<#pinecone> "Direct link to Pinecone")
This component creates a Pinecone Vector Store with search capabilities. For more information, see the [Pinecone documentation](https://docs.langflow.org/<https:/docs.pinecone.io/home>).
### Inputs[​](https://docs.langflow.org/<#inputs-12> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
index_name| String| Name of the Pinecone index  
namespace| String| Namespace for the index  
distance_strategy| String| Strategy for calculating distance between vectors  
pinecone_api_key| SecretString| API key for Pinecone  
text_key| String| Key in the record to use as text  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
number_of_results| Integer| Number of results to return in search  
### Outputs[​](https://docs.langflow.org/<#outputs-12> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| Pinecone| Pinecone vector store instance  
search_results| List[Data]| Results of similarity search  
## Qdrant[​](https://docs.langflow.org/<#qdrant> "Direct link to Qdrant")
This component creates a Qdrant Vector Store with search capabilities. For more information, see the [Qdrant documentation](https://docs.langflow.org/<https:/qdrant.tech/documentation/>).
### Inputs[​](https://docs.langflow.org/<#inputs-13> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
collection_name| String| Name of the Qdrant collection  
host| String| Qdrant server host  
port| Integer| Qdrant server port  
grpc_port| Integer| Qdrant gRPC port  
api_key| SecretString| API key for Qdrant  
prefix| String| Prefix for Qdrant  
timeout| Integer| Timeout for Qdrant operations  
path| String| Path for Qdrant  
url| String| URL for Qdrant  
distance_func| String| Distance function for vector similarity  
content_payload_key| String| Key for content payload  
metadata_payload_key| String| Key for metadata payload  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
number_of_results| Integer| Number of results to return in search  
### Outputs[​](https://docs.langflow.org/<#outputs-13> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| Qdrant| Qdrant vector store instance  
search_results| List[Data]| Results of similarity search  
## Redis[​](https://docs.langflow.org/<#redis> "Direct link to Redis")
This component creates a Redis Vector Store with search capabilities. For more information, see the [Redis documentation](https://docs.langflow.org/<https:/redis.io/docs/latest/develop/interact/search-and-query/advanced-concepts/vectors/>).
### Inputs[​](https://docs.langflow.org/<#inputs-14> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
redis_server_url| SecretString| Redis server connection string  
redis_index_name| String| Name of the Redis index  
code| String| Custom code for Redis (advanced)  
schema| String| Schema for Redis index  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
number_of_results| Integer| Number of results to return in search  
embedding| Embeddings| Embedding function to use  
### Outputs[​](https://docs.langflow.org/<#outputs-14> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| Redis| Redis vector store instance  
search_results| List[Data]| Results of similarity search  
## Supabase[​](https://docs.langflow.org/<#supabase> "Direct link to Supabase")
This component creates a connection to a Supabase Vector Store with search capabilities. For more information, see the [Supabase documentation](https://docs.langflow.org/<https:/supabase.com/docs/guides/ai>).
### Inputs[​](https://docs.langflow.org/<#inputs-15> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
supabase_url| String| URL of the Supabase instance  
supabase_service_key| SecretString| Service key for Supabase authentication  
table_name| String| Name of the table in Supabase  
query_name| String| Name of the query to use  
search_query| String| Query for similarity search  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use  
number_of_results| Integer| Number of results to return in search  
### Outputs[​](https://docs.langflow.org/<#outputs-15> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| SupabaseVectorStore| Supabase vector store instance  
search_results| List[Data]| Results of similarity search  
## Upstash[​](https://docs.langflow.org/<#upstash> "Direct link to Upstash")
This component creates an Upstash Vector Store with search capabilities. For more information, see the [Upstash documentation](https://docs.langflow.org/<https:/upstash.com/docs/introduction>).
### Inputs[​](https://docs.langflow.org/<#inputs-16> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
index_url| String| The URL of the Upstash index  
index_token| SecretString| The token for the Upstash index  
text_key| String| The key in the record to use as text  
namespace| String| Namespace for the index  
search_query| String| Query for similarity search  
metadata_filter| String| Filters documents by metadata  
ingest_data| Data| Data to be ingested into the vector store  
embedding| Embeddings| Embedding function to use (optional)  
number_of_results| Integer| Number of results to return in search  
### Outputs[​](https://docs.langflow.org/<#outputs-16> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| UpstashVectorStore| Upstash vector store instance  
search_results| List[Data]| Results of similarity search  
## Vectara[​](https://docs.langflow.org/<#vectara> "Direct link to Vectara")
This component creates a Vectara Vector Store with search capabilities. For more information, see the [Vectara documentation](https://docs.langflow.org/<https:/docs.vectara.com/docs/>).
### Inputs[​](https://docs.langflow.org/<#inputs-17> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
vectara_customer_id| String| Vectara customer ID  
vectara_corpus_id| String| Vectara corpus ID  
vectara_api_key| SecretString| Vectara API key  
embedding| Embeddings| Embedding function to use (optional)  
ingest_data| List[Document/Data]| Data to be ingested into the vector store  
search_query| String| Query for similarity search  
number_of_results| Integer| Number of results to return in search  
### Outputs[​](https://docs.langflow.org/<#outputs-17> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| VectaraVectorStore| Vectara vector store instance  
search_results| List[Data]| Results of similarity search  
## Vectara Search[​](https://docs.langflow.org/<#vectara-search> "Direct link to Vectara Search")
This component searches a Vectara Vector Store for documents based on the provided input. For more information, see the [Vectara documentation](https://docs.langflow.org/<https:/docs.vectara.com/docs/>).
### Inputs[​](https://docs.langflow.org/<#inputs-18> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
search_type| String| Type of search, such as "Similarity" or "MMR"  
input_value| String| Search query  
vectara_customer_id| String| Vectara customer ID  
vectara_corpus_id| String| Vectara corpus ID  
vectara_api_key| SecretString| Vectara API key  
files_url| List[String]| Optional URLs for file initialization  
### Outputs[​](https://docs.langflow.org/<#outputs-18> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
search_results| List[Data]| Results of similarity search  
## Vectara RAG[​](https://docs.langflow.org/<#vectara-rag> "Direct link to Vectara RAG")
This component leverages Vectara's Retrieval Augmented Generation (RAG) capabilities to search and summarize documents based on the provided input. For more information, see the [Vectara documentation](https://docs.langflow.org/<https:/docs.vectara.com/docs/>).
### Inputs[​](https://docs.langflow.org/<#inputs-19> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
vectara_customer_id| String| Vectara customer ID  
vectara_corpus_id| String| Vectara corpus ID  
vectara_api_key| SecretString| Vectara API key  
search_query| String| The query to receive an answer on  
lexical_interpolation| Float| Hybrid search factor (0.005 to 0.1)  
filter| String| Metadata filters to narrow the search  
reranker| String| Reranker type (mmr, rerank_multilingual_v1, none)  
reranker_k| Integer| Number of results to rerank (1 to 100)  
diversity_bias| Float| Diversity bias for MMR reranker (0 to 1)  
max_results| Integer| Maximum number of search results to summarize (1 to 100)  
response_lang| String| Language code for the response (for example, "eng", "auto")  
prompt| String| Prompt name for summarization  
### Outputs[​](https://docs.langflow.org/<#outputs-19> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
answer| Message| Generated RAG response  
## Weaviate[​](https://docs.langflow.org/<#weaviate> "Direct link to Weaviate")
This component facilitates a Weaviate Vector Store setup, optimizing text and document indexing and retrieval. For more information, see the [Weaviate Documentation](https://docs.langflow.org/<https:/weaviate.io/developers/weaviate>).
### Inputs[​](https://docs.langflow.org/<#inputs-20> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
weaviate_url| String| Default instance URL  
search_by_text| Boolean| Indicates whether to search by text  
api_key| SecretString| Optional API key for authentication  
index_name| String| Optional index name  
text_key| String| Default text extraction key  
input| Document| Document or record  
embedding| Embeddings| Model used  
attributes| List[String]| Optional additional attributes  
### Outputs[​](https://docs.langflow.org/<#outputs-20> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
vector_store| WeaviateVectorStore| Weaviate vector store instance  
**Note:** Ensure Weaviate instance is running and accessible. Verify API key, index name, text key, and attributes are set correctly.
## Weaviate Search[​](https://docs.langflow.org/<#weaviate-search> "Direct link to Weaviate Search")
This component searches a Weaviate Vector Store for documents similar to the input. For more information, see the [Weaviate Documentation](https://docs.langflow.org/<https:/weaviate.io/developers/weaviate>).
### Inputs[​](https://docs.langflow.org/<#inputs-21> "Direct link to Inputs")
Name| Type| Description  
---|---|---  
search_type| String| Type of search, such as "Similarity" or "MMR"  
input_value| String| Search query  
weaviate_url| String| Default instance URL  
search_by_text| Boolean| Indicates whether to search by text  
api_key| SecretString| Optional API key for authentication  
index_name| String| Optional index name  
text_key| String| Default text extraction key  
embedding| Embeddings| Model used  
attributes| List[String]| Optional additional attributes  
### Outputs[​](https://docs.langflow.org/<#outputs-21> "Direct link to Outputs")
Name| Type| Description  
---|---|---  
search_results| List[Data]| Results of similarity search  
[PreviousTools](https://docs.langflow.org/</components-tools>)[NextAgents overview](https://docs.langflow.org/</agents-overview>)
  * [Use a vector store component in a flow](https://docs.langflow.org/<#use-a-vector-store-component-in-a-flow>)
  * [Astra DB Vector Store](https://docs.langflow.org/<#astra-db-vector-store>)
    * [Inputs](https://docs.langflow.org/<#inputs>)
    * [Outputs](https://docs.langflow.org/<#outputs>)
  * [Cassandra](https://docs.langflow.org/<#cassandra>)
    * [Inputs](https://docs.langflow.org/<#inputs-1>)
    * [Outputs](https://docs.langflow.org/<#outputs-1>)
  * [Cassandra Graph Vector Store](https://docs.langflow.org/<#cassandra-graph-vector-store>)
    * [Inputs](https://docs.langflow.org/<#inputs-2>)
    * [Outputs](https://docs.langflow.org/<#outputs-2>)
  * [Chroma DB](https://docs.langflow.org/<#chroma-db>)
    * [Inputs](https://docs.langflow.org/<#inputs-3>)
    * [Outputs](https://docs.langflow.org/<#outputs-3>)
  * [Clickhouse](https://docs.langflow.org/<#clickhouse>)
    * [Inputs](https://docs.langflow.org/<#inputs-4>)
    * [Outputs](https://docs.langflow.org/<#outputs-4>)
  * [Couchbase](https://docs.langflow.org/<#couchbase>)
    * [Inputs](https://docs.langflow.org/<#inputs-5>)
    * [Outputs](https://docs.langflow.org/<#outputs-5>)
  * [FAISS](https://docs.langflow.org/<#faiss>)
    * [Inputs](https://docs.langflow.org/<#inputs-6>)
    * [Outputs](https://docs.langflow.org/<#outputs-6>)
  * [Hyper-Converged Database (HCD) Vector Store](https://docs.langflow.org/<#hyper-converged-database-hcd-vector-store>)
    * [Inputs](https://docs.langflow.org/<#inputs-7>)
    * [Outputs](https://docs.langflow.org/<#outputs-7>)
  * [Milvus](https://docs.langflow.org/<#milvus>)
    * [Inputs](https://docs.langflow.org/<#inputs-8>)
    * [Outputs](https://docs.langflow.org/<#outputs-8>)
  * [MongoDB Atlas](https://docs.langflow.org/<#mongodb-atlas>)
    * [Inputs](https://docs.langflow.org/<#inputs-9>)
    * [Outputs](https://docs.langflow.org/<#outputs-9>)
  * [Opensearch](https://docs.langflow.org/<#opensearch>)
    * [Inputs](https://docs.langflow.org/<#inputs-10>)
    * [Outputs](https://docs.langflow.org/<#outputs-10>)
  * [PGVector](https://docs.langflow.org/<#pgvector>)
    * [Inputs](https://docs.langflow.org/<#inputs-11>)
    * [Outputs](https://docs.langflow.org/<#outputs-11>)
  * [Pinecone](https://docs.langflow.org/<#pinecone>)
    * [Inputs](https://docs.langflow.org/<#inputs-12>)
    * [Outputs](https://docs.langflow.org/<#outputs-12>)
  * [Qdrant](https://docs.langflow.org/<#qdrant>)
    * [Inputs](https://docs.langflow.org/<#inputs-13>)
    * [Outputs](https://docs.langflow.org/<#outputs-13>)
  * [Redis](https://docs.langflow.org/<#redis>)
    * [Inputs](https://docs.langflow.org/<#inputs-14>)
    * [Outputs](https://docs.langflow.org/<#outputs-14>)
  * [Supabase](https://docs.langflow.org/<#supabase>)
    * [Inputs](https://docs.langflow.org/<#inputs-15>)
    * [Outputs](https://docs.langflow.org/<#outputs-15>)
  * [Upstash](https://docs.langflow.org/<#upstash>)
    * [Inputs](https://docs.langflow.org/<#inputs-16>)
    * [Outputs](https://docs.langflow.org/<#outputs-16>)
  * [Vectara](https://docs.langflow.org/<#vectara>)
    * [Inputs](https://docs.langflow.org/<#inputs-17>)
    * [Outputs](https://docs.langflow.org/<#outputs-17>)
  * [Vectara Search](https://docs.langflow.org/<#vectara-search>)
    * [Inputs](https://docs.langflow.org/<#inputs-18>)
    * [Outputs](https://docs.langflow.org/<#outputs-18>)
  * [Vectara RAG](https://docs.langflow.org/<#vectara-rag>)
    * [Inputs](https://docs.langflow.org/<#inputs-19>)
    * [Outputs](https://docs.langflow.org/<#outputs-19>)
  * [Weaviate](https://docs.langflow.org/<#weaviate>)
    * [Inputs](https://docs.langflow.org/<#inputs-20>)
    * [Outputs](https://docs.langflow.org/<#outputs-20>)
  * [Weaviate Search](https://docs.langflow.org/<#weaviate-search>)
    * [Inputs](https://docs.langflow.org/<#inputs-21>)
    * [Outputs](https://docs.langflow.org/<#outputs-21>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
![](https://t.co/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e6d308f6-8a3f-4d1e-8558-d950ade1171e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8bce2f4c-96a0-4c3a-aa35-53ab77a84e11&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-vector-stores&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=Asia%2FCalcutta%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2612%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e6d308f6-8a3f-4d1e-8558-d950ade1171e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8bce2f4c-96a0-4c3a-aa35-53ab77a84e11&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fcomponents-vector-stores&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)
