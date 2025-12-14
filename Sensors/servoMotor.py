import pigpio
import time

SERVO = 7
STOP = 1500
SPEED = 120

pi = pigpio.pi()
if not pi.connected:
    exit()

def stop():
    pi.set_servo_pulsewidth(SERVO, STOP)

def cw(speed=SPEED):
    pi.set_servo_pulsewidth(SERVO, STOP + 100)

def ccw(speed=SPEED):
    pi.set_servo_pulsewidth(SERVO, STOP - 100)

def openCurtain():
    ccw()
    time.sleep(23)
    stop()
    pi.set_servo_pulsewidth(SERVO, 0)

def closeCurtain():
    cw()
    time.sleep(23)
    stop()
    pi.set_servo_pulsewidth(SERVO, 0)