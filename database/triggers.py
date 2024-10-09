
from sqlalchemy import event
from database.database_dependencies import DatabaseContextManager
from models.product import Product
from models.purchase import Purchase


@event.listens_for(Purchase, "after_insert")
def update_product_quantity(mapper, connection, target: Purchase) -> None:
    """
    Функция триггера, которая обновляет количество продукта после каждой продажи.
    
    Если количество продукта меньше количества продажи, то поднимает ошибку ValueError.
    """
    with DatabaseContextManager() as db:
        print(target)
        id_product = target.id_product
        quantity = target.quantity

        product = db.query(Product).filter(Product.id == id_product).first()
        if product.quantity < quantity:
            raise ValueError("Недостаточное количество на складе")

        db.query(Product).filter(Product.id == id_product).update(
            {Product.quantity: Product.quantity - quantity})
        db.commit()
