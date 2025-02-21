#Evan McCabe To Do List

print("\nHello! I am a to-do list program.")

def main(toDoList):
    
    choice = input("\nWhat would you like to do?\n1 = add item to to-do list\n2 = mark item as complete\n3 = delete item from list\n4 = display to-do list\n5 = exit\n")

    try:
        choice = int(choice)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main(toDoList)

    if choice < 1 or choice > 5:
        print("\nINVALID NUMBER\n\nPlease try again.")
        main(toDoList)

    if choice == 1:
        itemToAdd = input("\nWhat task would you like to add to the list?\n")
        newlineItem = itemToAdd + "\n"
        toDoList.write(newlineItem)

    if choice == 2:
        pass
    if choice == 3:
        pass
    if choice == 4:
        for i in toDoList:
            print(i)
    if choice == 5:
        print("")
        exit()

    main(toDoList)

def start():
    with open("toDoList/toDoList.txt", "a+") as toDoList:
        toDoList.write("asdfasdfsaa")

start()

with open("toDoList/toDoList.txt", "a+") as toDoList:
    main(toDoList)