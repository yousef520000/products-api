from sqlmodel import create_engine, SQLModel, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./products.db")
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    from app.models import Product
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
