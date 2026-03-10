from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from model import Order, OrderItem, BagItem
from schemas import OrderOut
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/{user_id}", response_model=List[OrderOut])
def get_orders(user_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.user_id == user_id).all()

@router.post("/{user_id}")
def place_order(user_id: int, db: Session = Depends(get_db)):
    bag = db.query(BagItem).filter(BagItem.user_id == user_id).all()
    if not bag:
        raise HTTPException(status_code=400, detail="Bag is empty")

    total = sum(item.product.price * item.quantity for item in bag)
    order = Order(user_id=user_id, total_price=total)
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in bag:
        db.add(OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        ))

    db.query(BagItem).filter(BagItem.user_id == user_id).delete()
    db.commit()
    return {"message": "Order placed", "order_id": order.id}