## Software for Braille Reader

Welcome to the homepage for everything related to the simplistic Braille Reader! Use the download buttons to download my code.
### My Code

View a copy of my code below:

```
from EmulatorGUI import GPIO     # import GPIO library to allow control of GPIOs
import time              # import the time library for pauses

GPIO.setmode(GPIO.BCM)     #
GPIO.setwarnings(False)    #
GPIO.setup(2, GPIO.OUT)    #
GPIO.setup(3, GPIO.OUT)    #
GPIO.setup(4, GPIO.OUT)    # CONFIGURE GPIO PINS
GPIO.setup(5, GPIO.OUT)    #
GPIO.setup(6, GPIO.OUT)    #
GPIO.setup(7, GPIO.OUT)    #

GPIO.output(2, 0)
GPIO.output(3, 0)
GPIO.output(4, 0)   # CLEAR THE PINS
GPIO.output(5, 0)
GPIO.output(6, 0)
GPIO.output(7, 0)

textin = input('Enter word: ')    # take an input from the user to enter a word
lengthoftextin = len(textin)        # determine the length of the input string
c = 0    # initialise a counter variable to use as a stop in a loop
while c < lengthoftextin:
    letter = textin[c]    # assign the variable 'letter' to the position given by the 'c' counter variable
    checkletnum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']     # create an array with the letters of the alphabet
    corresponding_braille = ['100000', '101000', '110000', '110100', '100100', '111000', '111100', '101100', '011000', '011100', '100010', '101010', '110010', '110110', '100110', '111010', '111110', '101110', '011010', '011110', '100011', '101011', '011101', '110011', '110111', '100111']  # create a corresponding array with the braille equivalents of the letters in the alphabet
    for i in range(26):    # initialise a loop to go through all the letters of the alphabet
        if letter.lower() == checkletnum[i]:   # when the character stored in letter is found...
            temporary_letter = corresponding_braille[i]  # assign a variable to hold the corresponding braille value
            for x in range(6): # go through all GPIO pins
                int_temp_letter = int(temporary_letter[x])  # assign a variable to convert each character in the braille value to an integer
                GPIO.output(int(x+2), int_temp_letter) # output the GPIO value
                #time.sleep(1.5)    # pause for 3 seconds
            print('Letter = '+ checkletnum[i] + '; Braille: '+ corresponding_braille[i])   # print the results to terminal
            time.sleep(1)
            c = c + 1   # change the counter by 1
        if c > lengthoftextin:
            break     # if the last letter of the word inputted has been represented, stop the program

GPIO.output(2, 0)
GPIO.output(3, 0)
GPIO.output(4, 0)   # CLEAR THE PINS
GPIO.output(5, 0)
GPIO.output(6, 0)
GPIO.output(7, 0)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/VoicelessProximity1701/BrailleReader/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
