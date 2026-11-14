
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database configuration
DATABASE_URL = "sqlite:///./secure_api.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Create database models
Base = declarative_base()


# Database connection dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
