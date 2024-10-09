
from database.database_dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from cruds.purchase import PurchaseCrud
from schemas.purchase import PurchaseCreate, PurchaseResponse


router = APIRouter(
    prefix="/purchase",
    tags=["Purchase"],
)


@router.post("/create", summary="Create purchase", response_model=PurchaseResponse)
async def create_purchase(*, db: Session = Depends(get_db), data: PurchaseCreate) -> PurchaseResponse | HTTPException:

    """
    Создает продажу. Если такого продукта нет, то возвращает ошибку 404.
    Если недостаточно на складе, то возвращает ошибку 400.
    """
    return await PurchaseCrud.create(db, data.product_name, data.quantity)
