"""
Run this ONCE to populate the products table with women's fashion data.
    python seed_products.py
"""
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='987654321',   # ← change this to your MySQL password
    database='shoppingdb'
)
cursor = conn.cursor()

womens_products = [
    ('Floral Wrap Midi Dress',          'Zara',   49.99, 'https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=400&h=500&fit=crop', 50, 'womens'),
    ('Oversized Linen Blazer',          'H&M',    59.99, 'https://images.unsplash.com/photo-1585487000160-6ebcfceb0d03?w=400&h=500&fit=crop', 30, 'womens'),
    ('High Waist Straight Jeans',       'Mango',  39.99, 'https://images.unsplash.com/photo-1618932260643-eee4a2f652a6?w=400&h=500&fit=crop', 60, 'womens'),
    ('Satin Slip Skirt',                'Zara',   34.99, 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=400&h=500&fit=crop', 40, 'womens'),
    ('Ribbed Knit Cardigan',            'ASOS',   29.99, 'https://images.unsplash.com/photo-1502716119720-b23a93e5fe1b?w=400&h=500&fit=crop', 80, 'womens'),
    ('Printed Chiffon Blouse',          'H&M',    24.99, 'https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=400&h=500&fit=crop', 55, 'womens'),
    ('Tailored Wide Leg Trousers',      'Mango',  44.99, 'https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=400&h=500&fit=crop', 35, 'womens'),
    ('Leather Look Mini Skirt',         'Zara',   37.99, 'https://images.unsplash.com/photo-1550639525-c97d455acf70?w=400&h=500&fit=crop', 45, 'womens'),
    ('Puff Sleeve Cotton Dress',        'ASOS',   42.99, 'https://images.unsplash.com/photo-1516762689617-e1cffcef479d?w=400&h=500&fit=crop', 25, 'womens'),
    ('Cropped Denim Jacket',            'H&M',    54.99, 'https://images.unsplash.com/photo-1554568218-0f1715e72254?w=400&h=500&fit=crop', 20, 'womens'),
    ('Striped Breton Top',              'Mango',  19.99, 'https://images.unsplash.com/photo-1525507119028-ed4c629a60a3?w=400&h=500&fit=crop', 90, 'womens'),
    ('Ruched Bodycon Dress',            'Zara',   47.99, 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=500&fit=crop', 30, 'womens'),
    ('Utility Cargo Trousers',          'ASOS',   36.99, 'https://images.unsplash.com/photo-1509631179647-0177331693ae?w=400&h=500&fit=crop', 50, 'womens'),
    ('V-Neck Wrap Blouse',              'H&M',    22.99, 'https://images.unsplash.com/photo-1603344204980-4edb0ea63148?w=400&h=500&fit=crop', 70, 'womens'),
    ('Pleated Midi Skirt',              'Mango',  32.99, 'https://images.unsplash.com/photo-1566206091558-7f218b696731?w=400&h=500&fit=crop', 40, 'womens'),
    ('Cut Out Shoulder Top',            'Zara',   27.99, 'https://images.unsplash.com/photo-1604575271932-716d5e4fa4a3?w=400&h=500&fit=crop', 60, 'womens'),
    ('Flared Corduroy Trousers',        'ASOS',   41.99, 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=500&fit=crop', 35, 'womens'),
    ('Classic White Shirt',             'H&M',    25.99, 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=500&fit=crop', 100,'womens'),
    ('Knitted Turtleneck Sweater',      'Mango',  45.99, 'https://images.unsplash.com/photo-1583496661160-fb5218afa9a4?w=400&h=500&fit=crop', 30, 'womens'),
    ('Belted Trench Coat',              'Zara',   89.99, 'https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?w=400&h=500&fit=crop', 15, 'womens'),
]

cursor.executemany("""
    INSERT INTO products (name, brand, price, image_url, stock, category)
    VALUES (%s, %s, %s, %s, %s, %s)
""", womens_products)

conn.commit()
print(f"✅ {len(womens_products)} women's products inserted successfully!")

cursor.close()
conn.close()