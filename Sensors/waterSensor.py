# Water Sensor => GPIO21
import RPi.GPIO as GPIO
import time

def startWaterSensor():
    SENSOR_PIN = 21

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)

    try:
        while True:
            if GPIO.input(SENSOR_PIN) == 1:     # If sensor's value is 1, write "Su algilandi!" in console (just now).
                print("Su algilandi!")
            else:
                print("Su yok.")
            time.sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()