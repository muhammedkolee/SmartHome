import RPi.GPIO as GPIO
import time

PIR_PIN = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("Calibrating mini PIR...")
time.sleep(5)
print("Mini Pir is Ready!")

def startMiniPirSensor(enableEvent, queue, logger):
    count = 30
    isWrited = False
    try:
        while True:
            enableEvent.wait()
            if GPIO.input(PIR_PIN) == 1:
                if count >= 30:
                    logger.warning("Hareket algilandi.")
                    count = 0
                queue.put("Hareket algilandi!")
                time.sleep(6)
                isWrited = True
                
            else:
                if isWrited:
                    isWrited = False
            count += 1
            time.sleep(1)

    except Exception as e:
        GPIO.cleanup()
        print("Stopped.")
        logger.error(f"miniPir.py dosyasinda bir hata olustu: {e}")
