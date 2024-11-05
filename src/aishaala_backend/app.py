import logging
import os
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from services import postgres, redis
from routes import user
from admin import UserAdminView, OrgAdminView, authentication_backend
from .settings import settings


logging_handlers = [
    logging.FileHandler(os.path.join(settings.LOG_DIR, "rag.log")),
]

if settings.DEBUG:
    logging_handlers.append(logging.StreamHandler(sys.stdout))

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s",
    handlers=logging_handlers)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    await redis.connect()
    yield
    logger.info("disconnecting from database...")
    await postgres.disconnect()
    await redis.disconnect()
    logger.info("database disconnected...")

app = FastAPI(docs_url="/api/docs", redoc_url=None, lifespan=lifespan)

admin = Admin(app, engine=postgres.engine, authentication_backend=authentication_backend)
admin.add_view(UserAdminView)
admin.add_view(OrgAdminView)

@app.get("/")
def index() -> str:
    return "Hello world!"

app.include_router(user.router, prefix="/api/user", tags=["user"])
