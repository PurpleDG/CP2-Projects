# Evan McCabe Random Password Generator

import random

#List of lowercase letters:
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#List of uppercase letters:
upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#List of numbers:
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#List of special characters:
specialCharacters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

#Introduce the user to the program:
print("\nHello! I am the random password generator.")

#Function to set the number of characters in the passwords:
def numLetters(options, optionsPicked, password):

    #Ask the user how many characters long they want their passwords to be:
    num = input("\nHow many characters long do you want your password to be?\n")

    #Make sure the user entered a number:
    try:
         num = int(num)
    except ValueError:
         print("\nINVALID INPUT\n\nPlease try again.")
         numLetters(options, optionsPicked, password)

    #Make sure the user didn't enter 0 or a negative number:
    if num <= 0:
        print("\nYou can't do that!!!")
        numLetters(options, optionsPicked, password)

    #Move to the next step of the proccess: 
    upper(num, options, optionsPicked, password)

#Function to choose whether or not to include uppercase letters in the passwords:
def upper(num, options, optionsPicked, password):
    
    #Ask the user if they want uppercase letters to be included in their passwords:
    yn = input("\nWould you like to include uppercase letters in yourpassword? (y = yes, n = no)\n")

    #If the user chooses yes:
    if yn.upper() == "Y":
        #Tell the user their choice has been taken into account successfully:
        print("\nUppercase letters will be included in your password.")
        #Add uppercase letters to the password character options:
        for i in upperLetters:
            options.append(i)
        optionsPicked += 1

    #If the user does not choose yes:
    else:
        #Tell the user that uppercase letters will not be included in their passwords:
        print("\nUppercase letters will not be included in your password.")

    #Move to the next step of the proccess:
    lower(num, options, optionsPicked, password)

#Function to choose whether or not to include lowercase letters in the passwords:
def lower(num, options, optionsPicked, password):
    
    #Ask the user if they want to include lowercase letters in their passwords:
    yn = input("\nWould you like to include lowercase letters in your password? (y = yes, n = no)\n")

    #If the user chose yes:
    if yn.upper() == "Y":
        #Tell the user their choice has been taken into account successfully:
        print("\nLowercase letters will be included in your password.")
        #Add lowercase letters to the password character options:
        for i in lowerLetters:
            options.append(i)
        optionsPicked += 1

    #If the user did not choose yes:
    else:
        #Tell the user that lowercase letters will not be included in their passwords:
        print("\nLowercase letters will not be included in your password.")

    #Move to the next step of the proccess:
    numbas(num, options, optionsPicked, password)

#Function to choose whether or not to include numbers in the passwords:
def numbas(num, options, optionsPicked, password):
    
    #Ask the user if they want to include numbers in their passwords:
    yn = input("\nWould you like to include numbers letters in your password? (y = yes, n = no)\n")

    #If the user chose yes:
    if yn.upper() == "Y":
        #Tell the user their choice has been taken into account successfully:
        print("\nNumbers will be included in your password.")
        #Add numbers to the password character options:
        for i in numbers:
            options.append(i)
        optionsPicked += 1

    #If the user did not choose yes:
    else:
        #Tell the user that numbers will not be included in their passwords:
        print("\nNumbers will not be included in your password.")

    #Move to the next step of the proccess:
    special(num, options, optionsPicked, password)

#Function to choose whether or not to include special characters in their passwords:
def special(num, options, optionsPicked, password):
    
    #Ask the user if they want to include special characters in their passwords:
    yn = input("\nWould you like to include special characters in your password? (y = yes, n = no)\n")

    #If the user chose yes:
    if yn.upper() == "Y":
        #Tell the user their choice has been taken into account successfully:
        print("\nSpecial characters will be included in your password.")
        #Add special characters to the password character options:
        for i in specialCharacters:
            options.append(i)
        optionsPicked += 1

    #If the user did not choose yes:
    else:
        #Tell the user that numbers will not be included in their passwords:
        print("\nSpecial characters will not be included in your password.")

    #Make the outputted passwords shown to the users flow naturally:
    print("/nHere are some password options with those characteristics:\n")
    #Move to the next step of the process:
    assemble(num, options, optionsPicked, password)

#Function to assemple the four passwords based on the user's specifications:
def assemble(num, options, optionsPicked, password):

    #Make sure the user didn't deny all password options:
    if optionsPicked == 0:
        print("Your password is completely empty. You didn't pick anything! :/")

    else:
        print("")
        #Form four different passwords based on the user's criteria:
        for y in range(4):
            for i in range(num):
                a = str(random.choice(options))
                password = password + a
            #Show the user the passwords that were generated:
            print(password)
            password = ""
    
    #Ask the user if they want to run the program again:
    choice = input("\nWould you like to generate more passwords?\ny = yes\nn = no\n")
    #If the user chooses yes:
    if choice.upper() == "Y":
        #Run the program again:
        main()

    #If the user does not choose yes:
    else:
        #End the program:
        pass

#Main function to run the program:            
def main():
    
    #Call or recall the variables necessary for the program functions to run:
    options = []
    optionsPicked = 0
    password = ""

    #Move to the first step of the process:
    numLetters(options, optionsPicked, password)

#Start the program:
main()