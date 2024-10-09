from fastapi import FastAPI

import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from api.api_router import api_router
from configs.base import settings
from database.database_dependencies import DatabaseContextManager
from models import Product
from contextlib import asynccontextmanager

from typing import AsyncGenerator
import database.triggers as triggers

@asynccontextmanager
async def lifespan(f_app: FastAPI) -> AsyncGenerator:

    products_to_update = [
        {"name": "Яблоко", "quantity": 10},
        {"name": "Груша", "quantity": 20},
        {"name": "Абрикос", "quantity": 30}
    ]
    with DatabaseContextManager() as db:
        for product_data in products_to_update:
            # Попробуем найти продукт по имени
            product = db.query(Product).filter(Product.name == product_data["name"]).first()

            # Если продукт не найден, создадим новый
            if not product:
                product = Product(name=product_data["name"], quantity=product_data["quantity"])
                db.add(product)
            else:
                # Если продукт найден, обновим его количество
                db.query(Product).filter(Product.name == product_data["name"]).update(
                    {Product.quantity: product_data["quantity"]}
                )

        db.commit()
    yield


f_app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

f_app.include_router(api_router, prefix=settings.API_V1_STR)

app = CORSMiddleware(
    app=f_app,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)


if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)