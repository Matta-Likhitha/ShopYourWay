# ShopYourWay
ShopYourWay is a Full-stack shopping app built with Angular 17, FastAPI &amp; MySQL. Features product browsing, bag management and order tracking.

# 🛍️ ShopYourWay

A full-stack shopping web application built with Angular, FastAPI, and MySQL.

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Angular 17 |
| Backend | FastAPI (Python) |
| Database | MySQL |
| ORM | SQLAlchemy |
| Auth | JWT Tokens |

## ✨ Features

- Browse women's fashion products
- Add items to bag
- Place orders
- View order history
- Sort orders by date
- Fully connected to MySQL database

## 🗄️ Database Schema
```
users → orders → order_items → products
users → bag_items → products
```

## ⚙️ How to Run

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
ng serve
```

### Database
1. Open MySQL Workbench
2. Run `backend/schema.sql`
3. Run `python backend/seed_products.py`

## 📸 Screenshots
_Coming soon_

## 👩‍💻 Built by Likhitha
