from datetime import datetime, date

from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy import event
from database.database_dependencies import DatabaseContextManager


from models.product import Product
from database.db_session import Base


class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid4)
    date = Column(Date, default=datetime.now().date())
    id_product = Column(UUID(as_uuid=True), ForeignKey("product.id"))
    quantity = Column(Integer)

    product = relationship("Product", back_populates="purchases")


# @event.listens_for(Purchase, "after_insert")
# def update_product_quantity(mapper, connection, target: Purchase) -> None:
#     with DatabaseContextManager() as db:
#         print(target)
#         id_product = target.id_product
#         quantity = target.quantity

#         product = db.query(Product).filter(Product.id == id_product).first()
#         if product.quantity < quantity:
#             raise ValueError("Недостаточное количество на складе")

#         db.query(Product).filter(Product.id == id_product).update(
#             {Product.quantity: Product.quantity - quantity})
#         db.commit()
