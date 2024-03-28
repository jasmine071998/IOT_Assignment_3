import paho.mqtt.publish as mqtt_publish
from iot_station_connection import VirtualIoTStation 
import time
import datetime

# Configuration for the ThingSpeak Channel
channel_id = "2488627"
mqtt_server = "mqtt3.thingspeak.com"

# MQTT device authentication details
client_id = "HCIONQUbBS0HNxM3HgwwEiA"
username  = "HCIONQUbBS0HNxM3HgwwEiA"
password  = "DQIlf7GI+9F/A4X8mS54kxhf"

connection_type = "websockets"
connection_port = 80

# MQTT Topic formation
mqtt_topic = f"channels/{channel_id}/publish"

# Instantiate the IoT Station simulation
sensor_station = VirtualIoTStation()

# Continuous data publishing loop
while True:
  temp, humid, carbon_dioxide = sensor_station.generate_sensor_values()

  # Constructing the data payload
  data_payload = f"field1={temp}&field2={humid}&field3={carbon_dioxide}"

  # Log current operation with timestamp
  current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
  print(f"{current_time} Sending Data: {data_payload} to {mqtt_server} using clientID={client_id}")

  # Publish the sensor data to the configured MQTT topic
  mqtt_publish.single(mqtt_topic, data_payload, hostname=mqtt_server, transport=connection_type, port=connection_port, client_id=client_id, auth={'username':username,'password':password})

  # Wait before sending the next set of data
  time.sleep(5)
