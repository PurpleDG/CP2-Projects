# Evan McCabe Random Password Generator

import string

import random

lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

specialCharacters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("\nHello! I am the random password generator.")

def numLetters(options, optionsPicked, password):

    num = input("\nHow many characters long do you want your password to be?\n")

    try:
         num = int(num)
    except ValueError:
         print("\nINVALID INPUT\n\nPlease try again.")
         numLetters(options, optionsPicked, password)

    upperLetters(num, options, optionsPicked, password)

def upperLetters(num, options, optionsPicked, password):
    
    yn = input("\nWould you like to include uppercase letters in yourpassword? (y = yes, n = no)\n")

    if yn.upper() == "Y":
        print("\nUppercase letters will be included in your password.")
        for i in upperLetters:
            options.append(i)
        optionsPicked += 1

    else:
        print("\nUppercase letters will not be included in your password.")

    lowerLetters(num, options, optionsPicked, password)

def lowerLetters(num, options, optionsPicked, password):
    
    yn = input("\nWould you like to include lowercase letters in your password? (y = yes, n = no)\n")

    if yn.upper() == "Y":
        print("\nLowercase letters will be included in your password.")
        for i in lowerLetters:
            options.append(i)
        optionsPicked += 1

    else:
        print("\nLowercase letters will not be included in your password.")

    numbers(num, options, optionsPicked, password)

def numbers(num, options, optionsPicked, password):
    
    yn = input("\nWould you like to include numbers letters in your password? (y = yes, n = no)\n")

    if yn.upper() == "Y":
        print("\nNumbers will be included in your password.")
        for i in numbers:
            options.append(i)
        optionsPicked += 1

    else:
        print("\nNumbers will not be included in your password.")

    specialCharacters(num, options, optionsPicked, password)

def specialCharacters(num, options, optionsPicked, password):
    
    yn = input("\nWould you like to include special characters in your password? (y = yes, n = no)\n")

    if yn.upper() == "Y":
        print("\nSpecial characters will be included in your password.")
        for i in specialCharacters:
            options.append(i)
        optionsPicked += 1

    else:
        print("\nSpecial characters will not be included in your password.")

    assemble(num, options, optionsPicked, password)

def assemble(num, options, optionsPicked, password):

    if optionsPicked == 0:
        print("Your password is completely empty. You didn't pick anything! :/")

    else:
        print("")
        for y in range(4):
            for i in range(num):
                a = str(random.choice(options))
                password = password + a
            print(password)
            password = ""
            
def main():
    
    options = []

    optionsPicked = 0

    password = ""

    numLetters(options, optionsPicked, password)

main()