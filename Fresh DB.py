import psycopg2
from faker import Faker
import random

conn = psycopg2.connect(
    host="localhost",
    database="e_commerce",
    user="postgres",
    password="tayyarbey"
)

cur = conn.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name varchar(255), email varchar(255), password varchar(255), created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(255), price int, created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS orders (id serial PRIMARY KEY, user_id int, product_id int, created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS order_details (id serial PRIMARY KEY, order_id int, product_id int, quantity int, created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS categories (id serial PRIMARY KEY, name varchar(255), created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS product_categories (id serial PRIMARY KEY, product_id int, category_id int, created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS product_images (id serial PRIMARY KEY, product_id int, image_url varchar(255), created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS product_reviews (id serial PRIMARY KEY, product_id int, user_id int, review varchar(255), created_at timestamp, updated_at timestamp);")
cur.execute("CREATE TABLE IF NOT EXISTS product_ratings (id serial PRIMARY KEY, product_id int, user_id int, rating int, created_at timestamp, updated_at timestamp);")

cur.execute("ALTER TABLE orders ADD FOREIGN KEY (user_id) REFERENCES users(id);")
cur.execute("ALTER TABLE orders ADD FOREIGN KEY (product_id) REFERENCES products(id);")
cur.execute("ALTER TABLE order_details ADD FOREIGN KEY (order_id) REFERENCES orders(id);")
cur.execute("ALTER TABLE order_details ADD FOREIGN KEY (product_id) REFERENCES products(id);")
cur.execute("ALTER TABLE product_categories ADD FOREIGN KEY (product_id) REFERENCES products(id);")
cur.execute("ALTER TABLE product_categories ADD FOREIGN KEY (category_id) REFERENCES categories(id);")
cur.execute("ALTER TABLE product_images ADD FOREIGN KEY (product_id) REFERENCES products(id);")
cur.execute("ALTER TABLE product_reviews ADD FOREIGN KEY (product_id) REFERENCES products(id);")
cur.execute("ALTER TABLE product_reviews ADD FOREIGN KEY (user_id) REFERENCES users(id);")
cur.execute("ALTER TABLE product_ratings ADD FOREIGN KEY (product_id) REFERENCES products(id);")
cur.execute("ALTER TABLE product_ratings ADD FOREIGN KEY (user_id) REFERENCES users(id);")

conn.commit()

fake = Faker()
Faker.seed(4321)
random.seed(1234)

for i in range(100):
    cur.execute("INSERT INTO users (name, email, password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)", (fake.name(), fake.email(), fake.password(), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO products (name, price, created_at, updated_at) VALUES (%s, %s, %s, %s)", (fake.name(), random.randint(1, 1000), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO orders (user_id, product_id, created_at, updated_at) VALUES (%s, %s, %s, %s)", (random.randint(1, 100), random.randint(1, 100), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO order_details (order_id, product_id, quantity, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)", (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO categories (name, created_at, updated_at) VALUES (%s, %s, %s)", (fake.name(), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO product_categories (product_id, category_id, created_at, updated_at) VALUES (%s, %s, %s, %s)", (random.randint(1, 100), random.randint(1, 100), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO product_images (product_id, image_url, created_at, updated_at) VALUES (%s, %s, %s, %s)", (random.randint(1, 100), fake.image_url(), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO product_reviews (product_id, user_id, review, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)", (random.randint(1, 100), random.randint(1, 100), fake.text(), fake.date_time(), fake.date_time()))
conn.commit()

for i in range(100):
    cur.execute("INSERT INTO product_ratings (product_id, user_id, rating, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)", (random.randint(1, 100), random.randint(1, 100), random.randint(1, 5), fake.date_time(), fake.date_time()))
conn.commit()

cur.close()
conn.close()
