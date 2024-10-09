from fastapi import APIRouter
from cruds.product import ProductCrud
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database.database_dependencies import get_db
from pydantic import UUID4
from typing import List, Union, Optional
from schemas.product import ProductResponse

router = APIRouter(
    prefix="/product",
    tags=["Product"],
)


@router.get('', summary="Get product info", response_model=Union[List[ProductResponse], ProductResponse])
async def get_product(*, db: Session = Depends(get_db), id_product: Optional[UUID4] = None) -> List[ProductResponse] | ProductResponse | HTTPException:

    """
    Возвращает все продукты или продукт по id.
    
    Если id_product равен None, то возвращает список всех продуктов.
    Если id_product не равен None, то возвращает продукт с указанным id.
    
    Выбрасывает HTTPException, если продукт с указанным id не существует.
    """
    if id_product is None:
        return await ProductCrud.get_all(db)

    return await ProductCrud.get(db, id_product)