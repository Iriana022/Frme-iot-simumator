import paho.mqtt.client as mqtt
import json
import time
import random

# Configuration
BROKER = "mqtt"
TOPIC = "ferme/couveuse/data"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, 1883, 60)

print("Simulateur démarré. Envoi de données en cours...")

try:
    while True:
        # Simulation de données cohérentes
        data = {
            "node": "couveuse_01",
            "data": {
                "temp": round(random.uniform(37.2, 38.2), 2),
                "humi": round(random.uniform(45.0, 55.0), 2),
                "lamp": random.choice([0, 1]),
                "door": 0
            }
        }
        client.publish(TOPIC, json.dumps(data))
        print(f"Envoi : {data}")
        time.sleep(5) 
except KeyboardInterrupt:
    print("Simulateur arrêté.")
    client.disconnect()