while True:
    testletter = input('Phrase: ')
    counter = len(testletter)
    testphrase_braiile = print(testletter[i])
    for i in range (1, counter):
        print(testphrase_braiile)
        
    checkletnum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '*']
    corresponding_braille = ['100000', '101000', '110000', '100100', '111000', '111100', '101100', '011000', '011100', '100010', '101010', '110010', '110110', '100110', '111010', '111110', '101110', '011010', '011110', '100011', '101011', '011101', '110011', '110111', '100111', '000000']
    for i in range(0, 26):
        if testletter.lower() == checkletnum[i]:
            print('Corresponding braille: ' + corresponding_braille[i])
