from sqlalchemy.orm import Session
from models.product import Product
from fastapi import HTTPException
from pydantic import UUID4
from schemas.product import ProductResponse
from typing import List

class CrudForProduct:
    """
    Класс для работы с моделью Product
    """
    async def get(self, db: Session, id_product: UUID4) -> ProductResponse | HTTPException:
        """
        Возвращает продукт по id.
        """
        product = db.query(Product).filter(Product.id == id_product).first()

        if not product:
            raise HTTPException(status_code=404, detail="Продукта с таким id не существует")
        product = ProductResponse(
            name=product.name, quantity=product.quantity)
        return product
    
    async def get_all(self, db: Session) -> List[ProductResponse]:
        """
        Возвращает список всех продуктов.
        """
        products = db.query(Product).all()
        arr = [ProductResponse(name=product.name, quantity=product.quantity) for product in products]
        return arr

ProductCrud = CrudForProduct()