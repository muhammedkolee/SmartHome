import threading
from queue import LifoQueue
import Sensors.waterSensor as ws
import Sensors.gasSensor as gs
import Sensors.temperatureSensor as tm
import Sensors.miniPir as mp
import Sensors.ledScreen as lcd
import Sensors.servoMotor as sm
from logger import setup_logger
from server import MQTTServer
import json

data = []

def readFile():
    global data
    with open("data.json", "r") as file:
        data = json.load(file)	

def writeFile(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

readFile()

message_queue = LifoQueue()
logger = setup_logger()

miniPirEnableEvent = threading.Event()
if data["miniPir"]:
    miniPirEnableEvent.set()
else:
    miniPirEnableEvent.clear()

gasEnableEvent = threading.Event()
if data["gasSensor"]:
    gasEnableEvent.set()
else:
    gasEnableEvent.clear()

temperatureEnableEvent = threading.Event()
if data["temperatureSensor"]:
    temperatureEnableEvent.set()
else:
    temperatureEnableEvent.clear()

waterEnableEvent = threading.Event()
if data["waterSensor"]:
    waterEnableEvent.set()
else:
    waterEnableEvent.clear()


def log_listener():
    while True:
        pass

waterThread = threading.Thread(
    target=ws.startWaterSensor,
    args=(waterEnableEvent, message_queue, logger),
    daemon=True
)

gasThread = threading.Thread(
    target=gs.startGasSensor,
    args=(gasEnableEvent, message_queue, logger),
    daemon=True
)

tempThread = threading.Thread(
    target=tm.startTemperatureSensor,
    args=(temperatureEnableEvent, message_queue, logger),
    daemon=True
)

pirThread = threading.Thread(
    target=mp.startMiniPirSensor,
    args=(miniPirEnableEvent, message_queue, logger),
    daemon=True
)

lcdThread = threading.Thread(
    target=lcd.startLedScreen,
    args=(message_queue,),
    daemon=True
)

waterThread.start()
gasThread.start()
tempThread.start()
pirThread.start()
lcdThread.start()

def mqtt_command_handler(topic, payload):
    global data
    if topic == "home/water":
        if payload == "ON":
            data["waterSensor"] = True
            waterEnableEvent.set()
        elif payload == "OFF":
            data["waterSensor"] = False
            waterEnableEvent.clear()

    elif topic == "home/gas":
        if payload == "ON":
            data["gasSensor"] = True
            gasEnableEvent.set()
        elif payload == "OFF":
            data["gasSensor"] = False
            gasEnableEvent.clear()

    elif topic == "home/temperature":
        if payload == "ON":
            data["temperatureSensor"] = True
            temperatureEnableEvent.set()
        elif payload == "OFF":
            data["temperatureSensor"] = False
            temperatureEnableEvent.clear()
    
    elif topic == "home/pir":
        if payload == "ON":
            data["miniPir"] = True
            miniPirEnableEvent.set()
        elif payload == "OFF":
            data["miniPir"] = False
            miniPirEnableEvent.clear()

    elif topic == "home/curtain":
        if payload == "ON":
            if data["curtain"]:
                pass    
            else:
                sm.openCurtain()
        elif payload == "OFF":
            if data["curtain"]:
                sm.closeCurtain()
    writeFile(data)
      
mqtt_server = MQTTServer(on_command_callback=mqtt_command_handler)
mqtt_server.connect()

while True:
    pass
