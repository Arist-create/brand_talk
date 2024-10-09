from typing import AsyncGenerator
from .db_session import SessionLocal
from sqlalchemy.orm import Session

class DatabaseContextManager:
    """
    Класс-менеджер контекста для сессии БД.
    
    Создает сессию БД, когда мы заходим в контекст,
    и закрывает ее, когда мы выходим из контекста.
    """
    def __init__(self) -> None:
        self.db = SessionLocal()

    def __enter__(self) -> Session:
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db() -> AsyncGenerator:

    """
    Асинхронный менеджер контекста для сессии БД.
    
    Создает сессию БД, когда мы заходим в контекст,
    и закрывает ее, когда мы выходим из контекста.
    
    fastapi может использовать это как зависимость для обработчиков.
    """
    with DatabaseContextManager() as db:
        yield db