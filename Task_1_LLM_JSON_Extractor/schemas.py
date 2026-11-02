
from pydantic import BaseModel, Field
from typing import List, Optional


class InvoiceItem(BaseModel):
    description: str
    quantity: float
    unit_price: float
    amount: float


class InvoiceData(BaseModel):
    invoice_number: str
    invoice_date: Optional[str] = None
    vendor_name: str
    customer_name: Optional[str] = None
    currency: str
    subtotal: float
    tax: float
    total: float
    items: List[InvoiceItem]
