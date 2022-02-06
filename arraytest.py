from EmulatorGUI import GPIO  
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

x = 2

for i in range(6):
    GPIO.output(x, 1)
    time.sleep(1)
    GPIO.output(x, 0)
    x = x + 1 