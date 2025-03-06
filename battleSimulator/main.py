#Evan McCabe Battle Simulator

loadedCharacters = []

#When creating characters, give them an additional attribute to check if they were created by the user,
#So that the "Save Character" option only lets the user save the new characters they created

#Introduce the program to the user:
print("\nWelcome to the battle simulator.")

#Main function to run the program:
def main():
    
    #Ask the user what they want the program to do:
    choice = input("\nWhat would you like to do?\n1 = Create Character\n2 = Save Character\n3 = Load Character\n4 = Your Characters' Stats")

    try:
        choice = int(choice)
    except:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

    

    #Keep the program running in a loop:
    main()

#Start the program:
main()