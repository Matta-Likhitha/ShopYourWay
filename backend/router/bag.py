from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model import BagItem, Product
from schemas import BagItemOut, BagItemCreate
from typing import List

router = APIRouter(prefix="/bag", tags=["Bag"])

@router.get("/{user_id}", response_model=List[BagItemOut])
def get_bag(user_id: int, db: Session = Depends(get_db)):
    return db.query(BagItem).filter(BagItem.user_id == user_id).all()

@router.post("/{user_id}")
def add_to_bag(user_id: int, item: BagItemCreate, db: Session = Depends(get_db)):
    existing = db.query(BagItem).filter(
        BagItem.user_id == user_id,
        BagItem.product_id == item.product_id
    ).first()
    if existing:
        existing.quantity += item.quantity
    else:
        db.add(BagItem(user_id=user_id, product_id=item.product_id, quantity=item.quantity))
    db.commit()
    return {"message": "Added to bag"}

@router.delete("/{user_id}")
def clear_bag(user_id: int, db: Session = Depends(get_db)):
    db.query(BagItem).filter(BagItem.user_id == user_id).delete()
    db.commit()
    return {"message": "Bag cleared"}