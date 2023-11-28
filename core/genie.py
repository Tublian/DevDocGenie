import bs4
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import Chroma
from chromadb.utils import embedding_functions
import dotenv
import os
import sys

dotenv.load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(api_key=os.getenv("OPENAI_API_KEY"))
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=openai_ef)
retriever = vectorstore.as_retriever()

prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

rag_chain.invoke("What is Task Decomposition?")
