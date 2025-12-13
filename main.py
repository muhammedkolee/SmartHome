import threading
from queue import LifoQueue
import Sensors.waterSensor as ws
import Sensors.gasSensor as gs
import Sensors.temperatureSensor as tm
import Sensors.miniPir as mp
import Sensors.ledScreen as lcd
from logger import setup_logger

message_queue = LifoQueue()
logger = setup_logger()

def log_listener():
    while True:
        pass

waterThread = threading.Thread(
    target=ws.startWaterSensor,
    args=(message_queue, logger),
    daemon=True
)

gasThread = threading.Thread(
    target=gs.startGasSensor,
    args=(message_queue, logger),
    daemon=True
)

tempThread = threading.Thread(
    target=tm.startTemperatureSensor,
    args=(message_queue, logger),
    daemon=True
)

pirThread = threading.Thread(
    target=mp.startMiniPirSensor,
    args=(message_queue, logger),
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

while True:
    pass
