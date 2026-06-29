from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
def retrieve_context(query):

    results = retriever.invoke(query)

    context = "\n".join(
        [doc.page_content for doc in results]
    )

    return context
# Load documents
documents = []

for file in [
    "pricing.txt",
    "policy.txt",
    "technical_manual.txt",
    "faq.txt"
]:
    loader = TextLoader(file)
    documents.extend(loader.load())

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector store
vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 1}
)