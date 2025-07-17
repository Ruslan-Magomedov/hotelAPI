from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import settings


engine = create_async_engine(settings.DB_URL)