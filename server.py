# server.py
import paho.mqtt.client as mqtt

class MQTTServer:
    def __init__(self, on_command_callback):
        self.on_command_callback = on_command_callback

        self.client = mqtt.Client()
        self.client.username_pw_set("yorukistan", "Muhammed18")
        self.client.tls_set()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):
        self.client.connect("4009a741e78f4f9989efe8f6315ff960.s1.eu.hivemq.cloud", 8883)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("MQTT connected.")
            client.subscribe("home/#")
        else:
            print("MQTT error:", rc)

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode()
        print(f"MQTT: {topic} => {payload}")

		# main.py fonksiyon
        self.on_command_callback(topic, payload)

    def publish(self, topic, message):
        self.client.publish(topic, message)
