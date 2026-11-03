
# Task 2: Document Q&A Assistant with RAG

## Project Overview
This project is a PDF-based Question Answering Assistant built using Retrieval-Augmented Generation (RAG), LangChain, Gemini API, and ChromaDB.

Users can ask questions about a PDF document and receive answers based on its content, along with source page references.

## Technologies Used
- Python
- LangChain
- Google Gemini API
- Gemini Embeddings
- ChromaDB
- PyPDF

## Workflow
1. Load PDF documents using PyPDFLoader.
2. Split documents into smaller chunks.
3. Generate vector embeddings using Gemini.
4. Store embeddings in ChromaDB.
5. Retrieve relevant chunks using similarity search.
6. Generate answers using Gemini.
7. Display source page numbers.

## Project Structure
```text
Task_2_RAG_Document_QA/
├── data/
│   └── sample.pdf
├── main.py
├── requirements.txt
└── README.md
```

## Installation
Activate the project's virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration
Add your Gemini API key to the root `.env` file:

```text
GEMINI_API_KEY=your_api_key
```

Never upload your API key to GitHub.

## Run the Project
From the Task 2 folder:

```bash
python main.py
```

Ask questions about the loaded PDF in the terminal.

## Features
- PDF document loading
- Recursive text chunking
- Vector embeddings
- ChromaDB storage
- Similarity-based retrieval
- Context-based question answering
- Source page references
