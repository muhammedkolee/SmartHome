# Water Sensor => GPIO21
import RPi.GPIO as GPIO
import time

def startWaterSensor(queue, logger):
    SENSOR_PIN = 21
    isWrited = False

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(SENSOR_PIN, GPIO.IN)

    try:
        while True:
            if GPIO.input(SENSOR_PIN) == 1:  
                queue.put("Su algilandi!")
                logger.warning("Su algilandi.")
                isWrited = True
            else:
                if isWrited:
                    isWrited = False

            time.sleep(0.5)

    except Exception as e:
        GPIO.cleanup()
        logger.error(f"waterSensor.py dosyasinda bir hata olustu: {e}")

    finally:
        GPIO.cleanup()