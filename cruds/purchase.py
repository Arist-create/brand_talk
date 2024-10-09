from sqlalchemy.orm import Session
from models.product import Product
from models.purchase import Purchase
from fastapi import HTTPException
from schemas.purchase import PurchaseResponse, PurchaseInfo



class CrudForPurchase:
    """
    Класс для работы с моделью Purchase.
    """
    def __init__(self):
        """
        Инициализирует объект CrudForPurchase.
        self.products - set с именами продуктов, которые могут быть куплены.
        """
        self.products = {"Яблоко", "Груша", "Aбрикос"}

    async def create(self, db: Session, product_name: str, quantity: int) -> PurchaseResponse | HTTPException:

        """
        Создает продажу. Если такого продукта нет, то возвращает ошибку 404.
        Если недостаточно на складе, то возвращает ошибку 400.
        """
        if product_name not in self.products:
            raise HTTPException(status_code=404, detail="Такого продукта нет")
        
        if quantity <= 0:
            raise HTTPException(status_code=400, detail="Количество должно быть больше нуля")

        product_obj = db.query(Product).filter(
            Product.name == product_name).first()

        if product_obj.quantity < quantity:
            raise HTTPException(
                status_code=400, detail="Недостаточное количество на складе")

        purchase = Purchase(id_product=product_obj.id, quantity=quantity)
        db.add(purchase)
        db.commit()
        db.refresh(purchase)

        purchase = PurchaseResponse(
            message="Продажа успешно завершена",
            data=PurchaseInfo(
                product_name=product_name,
                quantity=quantity,
                date=purchase.date
            )
        )

        return purchase


PurchaseCrud = CrudForPurchase()
