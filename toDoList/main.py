#Evan McCabe To Do List

#Introduce the program to the user:
print("\nHello! I am a to-do list program.")

#Clear the text file so it is ready to be used by the program:
with open("toDoList/toDoList.txt", "w+") as toDoList:
    toDoList.write("\n")

#Main function that runs the program:
def main():

    #Ask the user what they want the program to do:
    choice = input("\nWhat would you like to do?\n1 = add item to to-do list\n2 = mark item as complete\n3 = delete item from list\n4 = display to-do list\n5 = exit\n")

    #Make sure that the user entered an integer:
    try:
        choice = int(choice)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

    #Make sure that the user chose a number that corresponds to one of the given options:
    if choice < 1 or choice > 5:
        print("\nINVALID NUMBER\n\nPlease try again.")
        main()

    #If the user chose to add an item to the to-do list:
    if choice == 1:

        #Ask the user what item they want to add to the to-do list:
        itemToAdd = input("\nWhat task would you like to add to the list?\n")
        
        #Add the item to the to-do list as specified by the user:
        with open("toDoList/toDoList.txt", "a+") as toDoList:
            toDoList.write(itemToAdd + "\n")

        #Tell the user that the process was successful: 
        print("\nDone.")

    #If the user chose to mark a to-do list item as completed:
    if choice == 2:

        #Open the file to be used again:
        with open("toDoList/toDoList.txt", "r+") as toDoList:

            #Ask the user what to-do list item they want to mark as completed:
            itemDone = input("\nWhich item on your list would you like to mark as completed?\n")

            #Set a variable to check if the process works successfully:
            marked = False

            #Re-write the to-do list text file with the user's desired item marked as completed:
            for line in toDoList:
                x = line
                if itemDone in x:
                    newLine = "Completed: " + x
                    with open("toDoList/toDoList.txt", "r") as f:
                        lines = f.readlines()
                    with open("toDoList/toDoList.txt", "w") as f:
                        for line in lines:
                            if line.strip("") != x:
                                f.write(line)
                    toDoList.write(newLine)

                    #Set the variable again to show that the process worked successfully:
                    marked = True

            #If the worked successfully variable is False:
            if marked == False:

                #Tell the user that the item they inputted is not in their to-do list:
                print("\nThat item is not on your to-do list.")

            #If the worked successfully variable is True:
            else:

                #Tell the user that the process worked successfully:
                print("\nDone.")

    #If the user chose to remove an item from their to-do list:
    if choice == 3:

        #Open the file to be used again:
        with open("toDoList/toDoList.txt", "r+") as toDoList:

            #Ask the user what item they want to remove from the to-do list:
            itemToRemove = input("\nWhat item would you like to remove from your list?\n")

            #Set a variable to check if the process works successfully:
            removed = False

            #Re-write the to-do list text file with the user's desired item removed:
            for line in toDoList:
                x = line
                if itemToRemove in x:
                    with open("toDoList/toDoList.txt", "r") as f:
                        lines = f.readlines()
                    with open("toDoList/toDoList.txt", "w") as f:
                        for line in lines:
                            if line.strip("") != x:
                                f.write(line)

                    #Set the variable again to show that the process worked successfully:
                    removed = True

            #If the worked successfully variable is False:
            if removed == False:

                #Tell the user that the item they inputted is not in their to-do list:
                print("\nThat item is not on your to-do list.")

            #If the worked successfully variable is True:
            else:

                #Tell the user that the process worked successfully:
                print("\nDone.")

    #If the user chose to display the entire to-do list:
    if choice == 4:

        #Print a heading at the top to make it look nicer:
        print("\nHere is your to-do list:")

        #Open the file to be used again:
        with open("toDoList/toDoList.txt", "r") as toDoList:

            #Print every line in the to-do list for the user to see:
            for line in toDoList:
                print(line)

    #If the user chose to exit the program:
    if choice == 5:

        #Make a new line because it looks nice:
        print("")

        #Exit the program:
        exit()

    #Run the main function of the program again to keep the program running:
    main()

#Run the program:
main()