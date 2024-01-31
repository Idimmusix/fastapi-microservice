# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config
from contextlib import contextmanager


DB_TYPE = config("DB_TYPE", default="sqlite")
DB_POOL_SIZE= config("DB_POOL_SIZE", default=5, cast=int)
DB_MAX_OVERFLOW= int(config("DB_MAX_OVERFLOW", default=3, cast= int))

def get_db_url():
    DB_NAME = config("DB_NAME", default="idimma")
    DB_USER = config("DB_USER", default="idimma")
    DB_PASSWORD = config("DB_PASSWORD", default="idimma123456")
    DB_HOST = config("DB_HOST", default="localhost")
    DB_PORT = config("DB_PORT", default=3306, cast=int)
    MYSQL_DRIVER = config("MYSQL_DRIVER", default="pymsql")
    DATABASE_URL = ""

    if DB_TYPE == "mysql":
        DATABASE_URL = f'mysql+{MYSQL_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        return DATABASE_URL
    elif DB_TYPE == "postgresql":
        DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        return DATABASE_URL
    else:
        DATABASE_URL = "sqlite:///db/database.db"
    return DATABASE_URL


def get_db_engine():

    if DB_TYPE == "sqlite":
        db_engine = create_engine(get_db_url(), connect_args={"check_same_thread": False})
    else:
        # db_engine = create_engine(DATABASE_URL)
        db_engine = create_engine(get_db_url(), pool_size=DB_POOL_SIZE, max_overflow=DB_MAX_OVERFLOW)
    
    return db_engine

db_engine = get_db_engine()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


def create_database():
    return Base.metadata.create_all(bind=db_engine)

@contextmanager
def get_db_with_ctx_mgr():
    db = SessionLocal()
    try:
        yield db
    except:
        # if we fail somehow rollback the connection
        db.rollback()
        raise
    finally:
        db.close()
 
def get_db():
    with get_db_with_ctx_mgr() as db:
        yield db

def get_db_engine_replica():

    REPLICA_DB_URL = config("REPLICA_DB_URL", default="localhost:3306")

    db_engine = create_engine(REPLICA_DB_URL, pool_size=DB_POOL_SIZE, max_overflow=DB_MAX_OVERFLOW)
    
    return db_engine

replica_db_engine = get_db_engine_replica()

SessionLocalReplica = sessionmaker(autocommit=False, autoflush=False, bind=replica_db_engine)

@contextmanager
def get_replica_db_with_ctx_mgr():
    db = SessionLocalReplica()
    try:
        yield db
    except:
        # if we fail somehow rollback the connection
        db.rollback()
        raise
    finally:
        db.close()
 
def get_replica_db():
    with get_replica_db_with_ctx_mgr() as db:
        yield db
