from fastapi import APIRouter, HTTPException, Depends, Query, status
from sqlmodel import Session, select
from typing import List, Optional
from app.models import Product
from app.database import get_session

router = APIRouter()

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: Product, session: Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.get("/", response_model=List[Product])
def list_products(q: Optional[str] = Query(None, description="search name"),
                  skip: int = 0, limit: int = 50,
                  session: Session = Depends(get_session)):
    statement = select(Product)
    if q:
        statement = statement.where(Product.name.contains(q))
    statement = statement.offset(skip).limit(limit)
    results = session.exec(statement).all()
    return results

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated: Product, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = updated.name
    product.description = updated.description
    product.price = updated.price
    product.in_stock = updated.in_stock
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    session.delete(product)
    session.commit()
    return None
