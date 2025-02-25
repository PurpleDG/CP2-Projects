#Evan McCabe To Do List

print("\nHello! I am a to-do list program.")

with open("toDoList/toDoList.txt", "w+") as toDoList:
    toDoList.write("")

def main():

    choice = input("\nWhat would you like to do?\n1 = add item to to-do list\n2 = mark item as complete\n3 = delete item from list\n4 = display to-do list\n5 = exit\n")

    try:
        choice = int(choice)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

    if choice < 1 or choice > 5:
        print("\nINVALID NUMBER\n\nPlease try again.")
        main()

    if choice == 1:

        itemToAdd = input("\nWhat task would you like to add to the list?\n")
        
        with open("toDoList/toDoList.txt", "a+") as toDoList:
            toDoList.write(itemToAdd + "\n")

    if choice == 2:
        with open("toDoList/toDoList.txt", "r+") as toDoList:
            itemDone = input("\nWhich item on your list would you like to mark as completed?\n")
            marked = False
            for line in toDoList:
                x = line
                if itemDone in x:
                    newLine = "Completed: " + x
                    with open("toDoList/toDoList.txt", "r") as f:
                        lines = f.readlines()
                    with open("toDoList/toDoList.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != x:
                                f.write(line)
                    toDoList.write(newLine)
                    marked = True
            if marked == False:
                print("\nThat item is not on your to-do list.")
            else:
                print("\nDone.")

    if choice == 3:
        with open("toDoList/toDoList.txt", "r+") as toDoList:
            itemToRemove = input("\nWhat item would you like to remove from your list?\n")
            removed = False
            for line in toDoList:
                x = line
                if itemToRemove in x:
                    with open("toDoList/toDoList.txt", "r") as f:
                        lines = f.readlines()
                    with open("toDoList/toDoList.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != x:
                                f.write(line)
                    removed = True
            if removed == False:
                print("\nThat item is not on your to-do list.")
            else:
                print("\nDone.")
    if choice == 4:
        print("\nHere is your to-do list:")
        with open("toDoList/toDoList.txt", "r") as toDoList:
            for line in toDoList:
                print(line)
    if choice == 5:
        print("")
        exit()

    main()

main()