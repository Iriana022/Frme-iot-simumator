import paho.mqtt.client as mqtt
import json
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# CONFIGURATION
TOKEN = "vUdCS5VkIN8JqLraVVCGa4E3sXNbUlvGZ-vzdj2WAQ1r1Un1KCWlWZW3VTo6PQZwO5GZqtbiV_GJXOyhgqYT1g=="
ORG = "Iriana_farm"
BUCKET = "farm_bucket"

client_db = InfluxDBClient(url="http://influxdb:8086", token=TOKEN, org=ORG)
write_api = client_db.write_api(write_options=SYNCHRONOUS)

def on_connect(client, userdata, flags, rc):
    print("CONNECTÉ AU BROKER", flush=True)
    client.subscribe("ferme/couveuse/#")

def on_message(client, userdata, msg):
    print(f"Message reçu sur {msg.topic}: {msg.payload.decode()}", flush=True)
    try:
        payload = json.loads(msg.payload.decode())
        node = payload.get("node", "default")
        d = payload.get("data", {})
        point = Point(node)
        for key, value in d.items():
            point.field(key, value)
        
        write_api.write(BUCKET, ORG, point)
        print(f"Données enregistrées pour {node}: {d}")
    except Exception as e:
        print(f"Erreur de traitement: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt", 1883, 60)
client.loop_forever()