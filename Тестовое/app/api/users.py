from typing import List

from litestar import Controller, get, post, put, delete
from litestar.dto import DTOData
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.config import UserRepository
from app.schemas.user import User, UserCreate, UserUpdate


class UserController(Controller):
    """Контроллер для работы с пользователями."""
    path = "/users"

    @get("/", return_dto=User)
    async def list_users(
        self, db: AsyncSession
    ) -> List[User]:
        """Получение списка пользователей."""
        repo = UserRepository(db)
        return await repo.list()

    @get("/{user_id:int}", return_dto=User)
    async def get_user(
        self, db: AsyncSession, user_id: int
    ) -> User:
        """Получение данных одного пользователя."""
        repo = UserRepository(db)
        return await repo.get(user_id)

    @post("/", return_dto=User)
    async def create_user(
        self, db: AsyncSession, data: DTOData[UserCreate]
    ) -> User:
        """Создание пользователя."""
        repo = UserRepository(db)
        return await repo.add(data.to_model_instance())

    @put("/{user_id:int}", return_dto=User)
    async def update_user(
        self, db: AsyncSession, user_id: int, data: DTOData[UserUpdate]
    ) -> User:
        """Обновление данных пользователя."""
        repo = UserRepository(db)
        user = await repo.get(user_id)
        return await repo.update(user, data.to_model_instance())

    @delete("/{user_id:int}")
    async def delete_user(
        self, db: AsyncSession, user_id: int
    ) -> None:
        """Удаление пользователя."""
        repo = UserRepository(db)
        user = await repo.get(user_id)
        await repo.delete(user)
