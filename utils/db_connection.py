import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")  # get the database url
if not DATABASE_URL:  # if the database url is not set raise an error
    raise RuntimeError("DATABASE_URL is not set in environment")

Base = declarative_base()  # create a base class


class Database:
    def __init__(self, url: str = DATABASE_URL):
        """Initialize the database instance

        Args:
            url: The url to the database

        Returns:
            None"""
        self.engine = create_engine(url, future=True)
        self.SessionLocal = sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False
        )

    def init_db(self):
        """Create all tables for all models that inherit from Base"""
        Base.metadata.create_all(bind=self.engine)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
