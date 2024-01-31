from pathlib import Path
import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    download_loader,
)
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.node_parser import SimpleNodeParser

JSONReader = download_loader("JSONReader")
loader = JSONReader()
documents = loader.load_data(Path('./data/tinytweets.json'))

# Qdrant is a vector database and vector similarity search engine.

# ./qdrant_data is the path to the vector database. Here the embeddings will be stored.
client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)

# Embeddings and docs are stored within the Qdrant collection (inside tweets folder). 
# https://docs.llamaindex.ai/en/latest/api/llama_index.vector_stores.QdrantVectorStore.html#llama_index.vector_stores.QdrantVectorStore.client

# QdrantVectorStore is a wrapper around Qdrant that provides all the necessary methods to work with your vector database in LlamaIndex.
# https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/
vector_store = QdrantVectorStore(client=client, collection_name="tweets")

# The storage context container is a utility container for storing nodes, indices, and vectors. It contains the following:
storage_context = StorageContext.from_defaults(vector_store=vector_store)

print("Before model!")
llm = Ollama(model="mistral")
print("After model!")

# Node parser.
node_parser = SimpleNodeParser.from_defaults(chunk_size=1024, chunk_overlap=20)

print("Before service context")
# Service context is a bundle of commonly used resources used during indexing and querying stage in
# a llama_index, https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/service_context.html
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local",node_parser=node_parser)
print("After service context")

print("Before from_documents")
# This is a type of indexing method. Indexing is used to speed up search queries.
index = VectorStoreIndex.from_documents(documents,service_context=service_context,storage_context=storage_context)
print("After documents")

print("Before as_query_engine")
query_engine = index.as_query_engine(similarity_top_k=20)
print("after as_query_engine")

print(" before .query")
response = query_engine.query("What does the author think about Star Trek? Give details.")
print("After .query")

print(response)