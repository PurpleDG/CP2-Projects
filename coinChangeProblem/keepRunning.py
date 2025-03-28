#Function to ask the user if they want to keep using the program:
def keepRunning():

    #Ask the user if they want to keep using the program:
    keepUsing = input("\nDo you want to keep using the program? (y/n)\n")

    #If the user says yes:
    if keepUsing == "y":
        pass

    #If the user says no:
    elif keepUsing == "n":
        print("\nThank you! Goodbye!\n")
        exit()

    #If the user does not input a valid action:
    else:

        #Tell the user they did not input a valid action and let them try again:
        print("\nINVALID OPTION\n\nPlease try again.")
        keepRunning()