import RPi.GPIO as GPIO
import time

#def button_callback2(channel):
 #   print('Prev. letter')
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
textin = input('Enter word: ')
lengthoftextin = len(textin)
c = 0

def button_callback(channel):
    global c
    c = c+1

while c < lengthoftextin:
    letter = textin[c]
    checkletnum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    corresponding_braille = ['100000', '101000', '110000', '110100', '100100', '111000', '111100', '101100', '011000', '011100', '100010', '101010', '110010', '110110', '100110', '111010', '111110', '101110', '011010', '011110', '100011', '101011', '011101', '110011', '110111', '100111']
    for i in range(0, 25):
        if letter.lower() == checkletnum[i]:
            print('Letter = '+ checkletnum[i] + '; Braille: '+ corresponding_braille[i])
            if not 'event' in locals():
                event = GPIO.add_event_detect(14, GPIO.RISING, callback=button_callback)
            else:
                time.sleep(0.5)
        if c > lengthoftextin:
            break
GPIO.cleanup()
        
