#Evan McCabe Battle Simulator

loadedCharacters = []

#When creating characters, give them an additional attribute to check if they were created by the user,
#So that the "Save Character" option only lets the user save the new characters they created

#Introduce the program to the user:
print("\nWelcome to the battle simulator.")

#Helper function to check if the user input a number:
def checkNum(num):
    try:
        num = int(num)
        return(num)
    except:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

#Main function to run the program:
def main():
    
    #Ask the user what they want the program to do:
    choice = input("\nWhat would you like to do?\n1 = Create Character\n2 = Save Character\n3 = Load Character\n4 = Your Characters' Stats\n5 = BATTLE\n")

    choice = checkNum(choice)

    #Make sure the user input a valid option:
    if choice > 0 and choice < 6:
        pass
    else:
        print("\nINVALID OPTION\n\nPlease try again.")
        main()

    #If the user chooses to create a character:
    if choice == 1:

        #name, attack, defense, speed, level, HP, saved

        newName = input("\nName: ")

        newAttack = input("\nAttack: ")
        newAttack = checkNum(newAttack)

        newDefense = input("\nDefense: ")
        newDefense = checkNum(newDefense)

        newSpeed = input("\nSpeed: ")
        newSpeed = checkNum(newSpeed)

        newHP = input("\nHP: ")
        newHP = checkNum(newHP)

        newCharacter = {"name": newName, "attack": newAttack, "defense": newDefense, "speed": newSpeed, "level": 1, "HP": newHP, "saved": False}

        loadedCharacters.append(newCharacter)

        print("\nCharacter successfully created.")

    #If the user chooses to save a character:
    if choice == 2:

        unsavedCharacters = False

        for x in loadedCharacters:

            if x["saved"] == False:
                print("\n" + str(x["name"]) + " | Attack: " + str(x["attack"]) + " | Defense: " + str(x["defense"]) + " | Speed: " + str(x["speed"]) + " | level: " + str(x["level"]) + " | HP: " + str(x["HP"]))
                unsavedCharacters = True

        if unsavedCharacters == False:
            print("\nYou have no unsaved characters!")
        else:
            validName = False
            toSaveName = input("\nWhat is the name of the character you would like to save?\n")
            for x in loadedCharacters:
                if x["name"] == toSaveName:
                    validName = True
                    fileLocation = input("\nWhat is the relative path of the file you want to save the charcter to?\n")
                    
                    #SAVE THE CHARACTER!!!!!!!
            
            if validName == False:
                print("\nThat is not one of your unsaved characters!")
            else:
                print("\nSaved.")

    #If the user chooses to load a character:
    if choice == 3:
        pass

    #If the user chooses to print character stats:
    if choice == 4:
        pass

    #If the user chooses to battle:
    if choice == 5:
        pass

    #Keep the program running in a loop:
    main()

#Start the program:
main()