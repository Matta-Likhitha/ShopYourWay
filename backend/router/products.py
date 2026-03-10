from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from model import Product
from schemas import ProductOut
from typing import List, Optional

router = APIRouter(prefix="/products", tags=["Products"])


# ✅ GET /products/ — all products
@router.get("/", response_model=List[ProductOut])
def get_products(
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    return query.all()


# ✅ GET /products/womens — MUST be above /{product_id}
@router.get("/womens", response_model=List[ProductOut])
def get_womens_products(db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.category == "womens").all()


# ✅ GET /products/{id} — MUST be below /womens
@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == product_id).first()