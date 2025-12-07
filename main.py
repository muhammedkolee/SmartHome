import Sensors.waterSensor as ws	    # ws => water sensor
import Sensors.example as ex            # for example function
import threading

waterThread = threading.Thread(target = ws.startWaterSensor)    # Create a thread for water sensor.
exThread = threading.Thread(target = ex.greet)                  # Create a thread for example code.

waterThread.start()         # Water sensor start as thread.
exThread.start()            # Example code start as thread while water sensor is running.