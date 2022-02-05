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

textin = input('Enter word: ')
lengthoftextin = len(textin)
c = 0
while c < lengthoftextin:
    letter = textin[c]
    checkletnum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    corresponding_braille = ['100000', '101000', '110000', '110100', '100100', '111000', '111100', '101100', '011000', '011100', '100010', '101010', '110010', '110110', '100110', '111010', '111110', '101110', '011010', '011110', '100011', '101011', '011101', '110011', '110111', '100111']
    for i in range(26):
        if letter.lower() == checkletnum[i]:
            temporary_letter = corresponding_braille[i]
            for x in range(6):
                print(temporary_letter[x])
                GPIO.OUTPUT(x+1, temporary_letter(x))
            print('Letter = '+ checkletnum[i] + '; Braille: '+ corresponding_braille[i])
            c = c + 1
        if c > lengthoftextin:
            break

