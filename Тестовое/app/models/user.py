from datetime import datetime
from typing import Optional

from advanced_alchemy import SQLAlchemyBase, SQLAlchemyBaseModel
from sqlalchemy import BigInteger, String, DateTime, func


class User(SQLAlchemyBase):
    """Модель пользователя."""
    __tablename__ = "user"

    id: int = SQLAlchemyBaseModel.primary_key(BigInteger, autoincrement=True)
    name: str = SQLAlchemyBaseModel.column(String(255), nullable=False)
    surname: str = SQLAlchemyBaseModel.column(String(255), nullable=False)
    password: str = SQLAlchemyBaseModel.column(String(255), nullable=False)
    created_at: datetime = SQLAlchemyBaseModel.column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: datetime = SQLAlchemyBaseModel.column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
