
INVOICE_EXTRACTION_PROMPT = """
You are an expert invoice information extraction assistant.

Your task is to extract invoice information from the
unstructured text provided below.

INSTRUCTIONS:
1. Extract only information present in the invoice.
2. Never invent or assume missing information.
3. Use null for missing optional fields.
4. Extract all invoice items.
5. Convert quantity and prices into numeric values.
6. Preserve the original currency.
7. Return valid structured JSON matching the
   requested schema.
8. Do not include explanations outside the JSON.

INVOICE TEXT:
{invoice_text}
"""


def create_invoice_prompt(invoice_text: str) -> str:
    return INVOICE_EXTRACTION_PROMPT.format(
        invoice_text=invoice_text
    )
