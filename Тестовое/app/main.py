from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyPlugin
from litestar.middleware import CORSMiddleware

from app.api.users import UserController
from app.db.config import engine


app = Litestar(
    route_handlers=[UserController],
    plugins=[
        SQLAlchemyPlugin(
            engine=engine,
            use_async=True,
        ),
    ],
    middleware=[
        CORSMiddleware(
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ],
)
