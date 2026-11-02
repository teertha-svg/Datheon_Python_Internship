
import os
import time
import json
import traceback
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from schemas import InvoiceData
from prompts import create_invoice_prompt


# Load API key from the parent project folder
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env file!")

# Initialize Gemini client
client = genai.Client(api_key=api_key)



def extract_invoice(invoice_text: str) -> InvoiceData:

    # Step 1: Create the prompt BEFORE the retry loop
    prompt = create_invoice_prompt(invoice_text)

    # Step 2: Request response from Gemini with retries
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": InvoiceData
                }
            )
            break

        except Exception as error:
            if attempt == 2:
                raise

            print(
                f"Temporary API error. Retrying... ({attempt + 1}/3)"
            )
            time.sleep(3)

    # Step 3: Convert JSON into Python data
    extracted_data = json.loads(response.text)

    # Step 4: Validate using Pydantic
    validated_invoice = InvoiceData.model_validate(
        extracted_data
    )

    return validated_invoice


def main():
    invoice_path = Path(__file__).parent / "sample_invoice.txt"

    sample_invoice = invoice_path.read_text(encoding="utf-8")

    
    try:
        invoice = extract_invoice(sample_invoice)

        print("\nEXTRACTED INVOICE DATA")
        print("----------------------")

        print(
            json.dumps(
                invoice.model_dump(),
                indent=4
            )
        )

        print("\nInvoice validation successful!")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
