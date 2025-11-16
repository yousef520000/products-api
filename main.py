from fastapi import FastAPI
from app.database import init_db
from app.routers import products

app = FastAPI(title="Products API (FastAPI + SQLModel)")

app.include_router(products.router, prefix="/products", tags=["products"])

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {"message":"Products API. See /docs for interactive API"}
