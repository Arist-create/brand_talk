
from pydantic import BaseModel
from datetime import date



class PurchaseCreate(BaseModel):
    product_name: str
    quantity: int

class PurchaseInfo(BaseModel):
    product_name: str
    quantity: int
    date: date


class PurchaseResponse(BaseModel):
    message: str
    data: PurchaseInfo


