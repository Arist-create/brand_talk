from api.routers import product, purchase
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(product.router)
api_router.include_router(purchase.router)