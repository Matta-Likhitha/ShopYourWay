from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


# ── Auth (account page)
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
    
class ProductOut(BaseModel):
    id: int
    name: str
    brand: str
    price: float
    image_url: str
    stock: int
    category: str
    class Config:
        from_attributes = True

class BagItemOut(BaseModel):
    id: int
    product: ProductOut
    quantity: int
    class Config:
        from_attributes = True

class BagItemCreate(BaseModel):
    product_id: int
    quantity: int = 1

class OrderItemOut(BaseModel):
    product: ProductOut
    quantity: int
    price: float
    class Config:
        from_attributes = True

class OrderOut(BaseModel):
    id: int
    status: str
    delivered: bool
    total_price: float
    created_at: datetime
    items: List[OrderItemOut]
    class Config:
        from_attributes = True