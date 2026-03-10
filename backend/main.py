from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import model
from router import  bag, orders, products,account  # ✅ added account and products

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shopping App API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account.router)
app.include_router(products.router) 
app.include_router(bag.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Shopping API running!"}