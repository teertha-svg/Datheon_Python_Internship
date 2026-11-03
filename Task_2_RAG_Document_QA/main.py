
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate


# 1. Load Gemini API key from the root .env file
ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in root .env file")


# 2. Load PDF document
PDF_PATH = Path(__file__).parent / "data" / "sample.pdf"

if not PDF_PATH.exists():
    raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

loader = PyPDFLoader(str(PDF_PATH))
documents = loader.load()

print(f"PDF loaded successfully: {len(documents)} pages")


# 3. Split document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Document split into {len(chunks)} chunks")


# 4. Generate embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)


# 5. Store embeddings in ChromaDB
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="document_qa",
    persist_directory=str(
        Path(__file__).parent / "chroma_db"
    )
)

print("Embeddings stored in ChromaDB successfully!")


# 6. Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=api_key,
    temperature=0
)


# 7. Create question-answering prompt
prompt = ChatPromptTemplate.from_template("""
You are a document question-answering assistant.

Answer the question using ONLY the context below.
If the answer is not available in the context, say:
"The answer is not available in the provided document."

Context:
{context}

Question:
{question}

Give a clear and simple answer.
""")


def ask_question(question):

    # Retrieve relevant chunks
    results = vector_store.similarity_search(
        question,
        k=3
    )

    # Prepare context
    context = "\n\n".join(
        document.page_content for document in results
    )

    # Generate answer
    response = llm.invoke(
        prompt.format(
            context=context,
            question=question
        )
    )

    # Display answer
    answer = response.content

    if isinstance(answer, list):
        answer = "\n".join(
            item["text"]
            for item in answer
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    print("\nANSWER:")
    print(answer)

    # Display source pages
    print("\nSOURCE PAGES:")

    pages = sorted({
        document.metadata.get("page", 0) + 1
        for document in results
    })

    for page in pages:
        print(f"Page {page}")



# 9. Interactive question-answering loop
if __name__ == "__main__":

    print("\n===== PDF QUESTION ANSWERING ASSISTANT =====")
    print("Ask questions about your PDF.")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("Your question: ")

        if question.lower() == "exit":
            print("Thank you for using the assistant!")
            break

        if question.strip():
            try:
                ask_question(question)
            except Exception as error:
                print("Error:", error)
