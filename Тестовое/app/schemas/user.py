from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    """Базовая схема пользователя."""
    name: str
    surname: str
    password: str


class UserCreate(UserBase):
    """Схема для создания пользователя."""
    pass


class UserUpdate(UserBase):
    """Схема для обновления пользователя."""
    name: Optional[str] = None
    surname: Optional[str] = None
    password: Optional[str] = None


class User(UserBase):
    """Схема для отображения пользователя."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
