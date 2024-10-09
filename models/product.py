from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship
from database.db_session import Base



class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String)
    quantity = Column(Integer, CheckConstraint("quantity > 0", name="quantity_check"))


    purchases = relationship("Purchase", back_populates="product")

