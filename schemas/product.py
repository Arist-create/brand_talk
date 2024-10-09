from pydantic import BaseModel
from datetime import date


class ProductResponse(BaseModel):
    name: str
    quantity: int