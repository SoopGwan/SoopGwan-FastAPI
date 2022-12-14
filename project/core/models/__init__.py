from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from project.core.config import MYSQL_DB_URL
from project.core.config import REDIS_HOST, REDIS_PORT
import redis

@contextmanager
def session_scope():
    engine = create_engine(
        MYSQL_DB_URL,
        encoding="utf-8",
        pool_recycle=3600,
        pool_size=20,
        max_overflow=20,
        pool_pre_ping=True,
        echo=True
    )
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

Base = declarative_base()

Redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)