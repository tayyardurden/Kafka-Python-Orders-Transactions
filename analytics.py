import json
from kafka import KafkaConsumer

ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"

consumer=KafkaConsumer(ORDER_CONFIRMED_KAFKA_TOPIC,bootstrap_servers="localhost:9092")

total_order_counts=0
total_revenue=0

print("Analytics is listening")


while True:
    
    for message in consumer:
        print("Updating analytics")
        consumed_message=json.loads(message.value.decode())


        total_cost=float(consumed_message["total_cost"])
        total_order_counts+=1
        total_revenue+=total_cost  

        print(f"Orders so far today : {total_order_counts}")
        print(f"Total revenue so far today : {total_revenue}")
