import RPi.GPIO as GPIO
def button_callback(channel):
    print('Next letter')
def button_callback2(channel):
    print('Prev. letter')
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=button_callback)
GPIO.add_event_detect(15,GPIO.RISING,callback=button_callback2)


