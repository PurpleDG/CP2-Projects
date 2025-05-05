#Evan McCabe, Simple Morse Code Translator

#List of every letter in the alphabet(and numbers):
english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#List of every letter in morse:
morseCode = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__..", "/", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", "_____"]

#Introduce the program to the user:
print("\nHello! I am the morse code translator. I can translate letters and numbers.")

#Function to translate English into morse:
def englishToMorse():

    #Ask the user what they want to translate to morse:
    message = input("\nWhat message would you like translated into morse code?\n")

    #Empty list for the translated letters:
    translation = []
    
    #Translate the user's message into morse code:
    for letter in message:
        for x in english:
            if letter == x:
                morseIndex = english.index(letter)
                translation.append(morseCode[morseIndex])
                translation.append(" ")
    
    #Show the user their fully translated message:
    print("\nHere is your translated message:\n(characters entered incorrectly are discluded)\n" + "".join(translation))

#Function to translate morse code to English:
def morseToEnglish():

    #List to store the morse characters from the user:
    morseMessage = []
        
    #Explain the translation proccess to the user:
    print('\nAdd the letters one at a time, and I will print the final message when you are done.\n("_" and ".")\n(If you want to add a space, use a forward slash.)')

    #Let the user add letters to their message until they are finished:
    addLetters = True
    while addLetters == True:
        choice = input("\nWould you like to add another letter?\n1 = yes\n2 = no\n")
        if choice == "1":
            letter = input("\nWhat letter would you like to add? (in morse)\n")
            morseMessage.append(letter)
        else:
            translation = []
            
            #Translate the user's message into English:
            for letter in morseMessage:
                for x in morseCode:
                    if letter == x:
                        englishIndex = morseCode.index(letter)
                        translation.append(english[englishIndex])

            #Show the user their fully translated message:
            print("\nHere is your translated message:\n(characters entered incorrectly are discluded)\n" + "".join(translation))

            #End the translation process:
            addLetters = False

#Function to ask if the user wants to continue translating messages:
def again():

    #Ask the user if they want the program to keep running:
    choice = input("\nWould you like to translate more messages?\n1 = yes\n2 = no\n")

    #If the user chooses yes:
    if choice == "1":

        #Run the program again:
        main()

    #If the user chooses no:
    elif choice == "2":

        #Make it look nice:
        print("\nBye-bye!\n")

        #Stop the program from running:
        exit()

    #If the user does not choose yes or no:
    else:

        #Tell the user that they did not pick a valid option:
        print("\nINVALID OPTION\n\nPlease try again.")

        #Let the user try again:
        again()

#Main function to run the program:
def main():

    #Ask the user what they would like the program to do:
    choice = input("\nWhat function would  you like me to perform?\n1 = English to Morse\n2 = Morse to English\n3 = exit\n")

    #If the user chooses to translate English into morse code:
    if choice == "1":

        #Run the English to morse code function:
        englishToMorse()

        #Find out if the user wants to translate further:
        again()

    #If the user chooses to translate morse code into English:    
    elif choice == "2":

        #Run the morse code to English function:
        morseToEnglish()

        #Find out if the user wants to translate further:
        again()     

    #If the user chooses to exit the program:
    elif choice == "3":

        #Make it look nice:
        print("\nBye-bye!\n")

        #Stop the program from running:
        exit()

    #If the user does not choose a valid option:
    else:

        #Tell the user that they did not choose a valid option:
        print("\nINVALID OPTION\n\nPlease try again.")

        #Let the user try again:
        main()

#Start the program:
main()