from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
from langchain.prompts import PromptTemplate

load_dotenv("C:/Users/sanja/AI-MEDICINE_BOT/venv/.env")
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

llm=ChatGroq(model="llama3-8b-8192")

from pdfminer.high_level import extract_text
text = extract_text("C:/Users/sanja/AI-MEDICINE_BOT/data/standard-treatment-guidelines.pdf")


text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
docs = [Document(page_content=text)]

chunks=text_splitter.split_documents(docs)
print(len(chunks))

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store=FAISS.from_documents(chunks,embeddings)

retreiver=vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4})

from langchain.chains import RetrievalQA

# Create the QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=retreiver, 
    return_source_documents=True  
)

response=qa_chain.invoke("Tell me medicine for stomach pain")
print("\n✅ Answer:")
print(response['result'])



