from ensurepip import bootstrap
import time
import json
from kafka import KafkaProducer
import psycopg2
from faker import Faker
import random


ORDER_KAFKA_TOPIC="order_details"
ORDER_LIMIT = 15

producer=KafkaProducer(bootstrap_servers="localhost:9092")

print("Going to be generating order after 10 seconds")
print("will generate one unique order after every 10 seconds")

conn = psycopg2.connect(database="postgres", user="postgres", password="tayyarbey", host="127.0.0.1", port="5432")
print("Database Connected....")
cur = conn.cursor()

cur.execute("CREATE TABLE abur_cubur(id SERIAL PRIMARY KEY, item_name VARCHAR(20), price INT)")

cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Cola', 10)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Fanta', 8)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Sprite', 9)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Pepsi', 1)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('7up', 7)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Lipton', 11)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Tea', 3)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Coffee', 5)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Tutku', 15)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Metro', 12)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Kinder', 16)")
cur.execute("INSERT INTO abur_cubur(item_name, price) VALUES('Probis', 6)")


user_list =[]
for i in range(20):
    fake = Faker()
    name = fake.unique.name()
    email= fake.unique.email()
    user_list.append(name)
    user_list.append(email)

cur.execute("CREATE TABLE users(id SERIAL PRIMARY KEY, user_name VARCHAR(50), user_surname VARCHAR(50),user_email VARCHAR(50))")

for i in range(0, len(user_list), 2):
    cur.execute("INSERT INTO users(user_name, user_surname, user_email) VALUES(%s, %s, %s)", (user_list[i].split()[0], user_list[i].split()[1], user_list[i+1]))

cur.execute("CREATE TABLE orders(id SERIAL PRIMARY KEY, order_time TIMESTAMP, order_status VARCHAR(50), user_id INT, FOREIGN KEY (user_id) REFERENCES users(id))")

conn.commit()


cur.execute("SELECT user_name FROM users")
user_list = cur.fetchall()
user_list = [i[0] for i in user_list]

cur.execute("SELECT user_email FROM users")
email_list = cur.fetchall()
email_list = [i[0] for i in email_list]

def create_cart_list():
    cur.execute("SELECT item_name, price FROM abur_cubur")
    item_list = cur.fetchall()
    cart_list = []
    for i in range(random.randint(1, 5)):
        cart_list.append(random.choice(item_list))
    return cart_list

def calculate_total_price(cart_list):
    total_price = 0
    for i in cart_list:
        total_price += i[1]
    return total_price

for i in range(1, ORDER_LIMIT):
    time.sleep(5)
    data = {
        "order_id": i,
        "user_id": user_list[i],
        "user_email": email_list[i],
        "order_status": "Confirmed",
        "cart_list": create_cart_list(),
        "total_cost": calculate_total_price(create_cart_list()),
        "order_time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    producer.send(
        ORDER_KAFKA_TOPIC,
        json.dumps(data).encode("utf-8")
    )

    print(f"Done sending...{i}")
    time.sleep(3)