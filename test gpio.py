import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(7, GPIO.LOW)

time.sleep(1)

GPIO.output(2, GPIO.HIGH)
time.sleep(1)
GPIO.output(3, GPIO.HIGH)
time.sleep(1)
GPIO.output(4, GPIO.HIGH)
time.sleep(1)
GPIO.output(5, GPIO.HIGH)
time.sleep(1)
GPIO.output(6, GPIO.HIGH)
time.sleep(1)
GPIO.output(7, GPIO.HIGH)

time.sleep(10)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(7, GPIO.LOW)

