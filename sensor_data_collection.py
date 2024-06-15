import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Initialize the IoT Hub Device Client
CONNECTION_STRING = "YourIoTHubConnectionString"
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def get_sensor_data():
    # Simulate sensor data
    data = {
        "soil_moisture": random.uniform(20.0, 50.0),
        "temperature": random.uniform(15.0, 35.0),
        "humidity": random.uniform(30.0, 70.0)
    }
    return data

while True:
    sensor_data = get_sensor_data()
    message = Message(str(sensor_data))
    client.send_message(message)
    print("Message sent: {}".format(message))
    time.sleep(10)
