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
op=2

textin = input('Enter word: ')
lengthoftextin = len(textin)

for i in range(0, lengthoftextin):
    letter = textin[i]
    print(letter)
    if letter  == 'a':
        GPIO.output(op, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        time.sleep(2)
    if letter  == 'b':
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        time.sleep(2)

    if letter  == 'c':
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        time.sleep(2)
    if letter  == 'd':
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        time.sleep(2)
