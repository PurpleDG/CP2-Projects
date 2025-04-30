#Function to update a text file with a word count and date that it was updated:
def update(path, time):

    #Inner function to allow the user to choose whether or not to keep using the program:
    def keepRunning():

        #Ask the user if they want to keep using the program:
        yn = input("\nWould you like to keep using this program? (y/n)\n")

        #If they choose yes:
        if yn == "y":

            #Allow the while loop to continue making the program run:
            return "Yes"

        #If they choose no:
        elif yn == "n":

            #Say goodbye to the user:
            print("\nBye-bye!\n")

            #return no so that the main function can quit the program:
            return "No"

        #If the user does not choose yes or no:
        else:

            #Tell the user that they've made a mistake:
            print("\nINVALID INPUT\n\nPlease try again.")

            #Let the user try again:
            keepRunning()
    
    #Open the user's desired file so that it can be updated:
    try:
        with open(path, "a+") as file:

            # Move the file pointer to the start of the file:
            file.seek(0)

            #Save the amount of words in the file as a variable:
            wordCount = 0
            for line in file:
                separated = line.split()
                lineCount = len(separated)
                wordCount += lineCount

            #Update the user's desired file with a word count and "date updated":
            file.write("\nUPDATE: word count = " + str(wordCount) + ", date/time updated = " + str(time))

            #Tell the user that the function was successful:
            print("\nFile successfully updated!")

            #Ask the user if they want to keep using the program:
            return keepRunning()

    #If the relative path entered by the user doesn't lead to a valid file:
    except:
        print("\nThat relative path doesn't lead to a valid file!\n\nPlease try again.")