import RPi.GPIO as GPIO
import time

GAS_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_PIN, GPIO.IN)

def startGasSensor(enableEvent, queue, logger):
    isWrited = False
    while True:
        enableEvent.wait()
        status = GPIO.input(GAS_PIN)

        if status == 0:
            queue.put("Gaz algilandi!!!")
            logger.warning("Gaz algilandi.")
            isWrited = True
        else:
            if isWrited:
                isWrited = False
                
        time.sleep(0.2)
