import bs4
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import Chroma
from chromadb.utils import embedding_functions
import dotenv
import os

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class OpenAIEmbeddingAdapter:
    def __init__(self, openai_embedding_function):
        self.embedding_function = openai_embedding_function

    def embed_query(self, query):
        return self.embedding_function([query])[0]

openai_ef = embedding_functions.OpenAIEmbeddingFunction(api_key=os.getenv("OPENAI_API_KEY"))
openai_adapter = OpenAIEmbeddingAdapter(openai_ef)


vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=openai_adapter)
retriever = vectorstore.as_retriever()

prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)




rag_chain = (
    {"context": retriever|format_docs,  "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

try:
    result = rag_chain.invoke("What is python?")
    print("Result:", result)
except Exception as e:
    print("Error:", e)
    raise


