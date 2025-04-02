from typing import AsyncGenerator

from advanced_alchemy import SQLAlchemyAsyncRepository
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.models.user import User

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/users_db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Получение сессии базы данных."""
    async with async_session() as session:
        yield session


class UserRepository(SQLAlchemyAsyncRepository[User]):
    """Репозиторий для работы с пользователями."""
    model_type = User
