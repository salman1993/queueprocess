from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# use 'localhost' instead of 'db' as host if running locally
DATABASE_URL = "postgresql://myuser:mypassword@db/mydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
