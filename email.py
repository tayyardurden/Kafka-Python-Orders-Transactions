from kafka import KafkaConsumer
import json

ORDER_KAFKA_CONFIRMED_TOPIC="order_confirmed"

consumer=KafkaConsumer(
    ORDER_KAFKA_CONFIRMED_TOPIC,
    bootstrap_servers="localhost:9092"
)

email_sent_so_far=set()
print("Email is listening")

while True:
    for message in consumer:
        consumed_message=json.loads(message.value.decode())
        customer_email=consumed_message["customer_email"]

        print(f"Sending email to {customer_email}")
        email_sent_so_far.add(customer_email)
        print(f"So far emails sent to :{len(email_sent_so_far)} unique emails")
