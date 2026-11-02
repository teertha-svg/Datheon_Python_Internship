
# AI Invoice Information Extractor

## Project Overview
An AI-powered invoice information extraction system built using Python, Google Gemini API, and Pydantic.

The application extracts structured information from unstructured invoice text and converts it into validated JSON.

## Features
- Gemini API integration
- Parameterized prompt templates
- Structured JSON extraction
- Pydantic data validation
- Automatic retry handling for temporary API errors
- External text file input
- Handles missing optional invoice fields

## Technologies Used
- Python 3.11
- Google Gemini API
- Google GenAI SDK
- Pydantic
- Python-dotenv
- JSON

## Project Structure

Task_1_LLM_JSON_Extractor/
- main.py
- schemas.py
- prompts.py
- sample_invoice.txt
- README.md

## Installation

1. Clone the repository.
2. Create a virtual environment:

   python -m venv .venv

3. Activate it on Windows:

   .venv\Scripts\Activate.ps1

4. Install dependencies:

   pip install google-genai pydantic python-dotenv

## API Configuration

Create a `.env` file in the project root directory.

Add:

GEMINI_API_KEY=your_api_key_here

Never upload your API key to GitHub.

## Execution

Run:

python main.py

## Expected Output

The application extracts:
- Invoice number
- Invoice date
- Vendor name
- Customer name
- Currency
- Invoice items
- Subtotal
- Tax
- Total

The extracted information is validated using Pydantic and displayed as JSON.

## Learning Outcomes

- Working with Generative AI APIs
- Prompt engineering
- Structured data extraction
- JSON processing
- Data validation
- Python project development

## Internship

Python + Generative AI & LangChain Internship

Organization: Datheon
