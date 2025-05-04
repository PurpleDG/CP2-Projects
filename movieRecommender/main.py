# Evan McCabe Movie Recommender

import csv

#Introduce the program to the user:
print("\nHello! I am the movie recommender.")

#Main function of the program:
def main(movies):

    #Variable for the kinds of filters the user chooses to use:
    filtersChosen = []

    #Ask the user if they want to get movie reccomendations, display every movie, or exit the program:
    option = input("\nWhat would you like to do?\n1 = Get Movie Reccomendations\n2 = Display All Movies\n3 = Exit Program\n")

    #Make sure the user entered a number:
    try:
        option = int(option)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        return

    #If the user chose to get movie reccomendations:
    if option == 1:

        #Ask the user how many filters they want to use to search for movies:
        num = input("\nHow many filters would you like to use to search for movies?\n")

        #Make sure the user entered a number:
        try:
            num = int(num)
        except ValueError:
            print("\nINVALID INPUT\n\nPlease try again.")
            return

        #For the amount of times as the amount of filters the user wants to use:
        for i in range(num):

            #Ask the user what they want to search for movies by:
            choice = input("\nWhat would you like to search by?\n1 = Title\n2 = Director\n3 = Genre\n4 = ESRB Rating\n5 = Length(minutes)\n6 = Notable Actor\n7 = Exit\n")

            #Make sure the user entered a number:
            try:
                choice = int(choice)
            except:
                print("\nINVALID INPUT\n\nPlease try again.")
                return

            #If the user chose to search by movie title:
            if choice == 1:
                #Add the fact that the user chose to search by movie title to the filters chosen list:
                filtersChosen.append("1") 
                #Ask the user what movie title they want to search for:
                titleFilter = input("\nWhat is the movie title you want to search for?\n")

            #If the user chose to search by movie director:
            elif choice == 2:
                #Add the fact that the user chose to search by movie director to the filters chosen list:
                filtersChosen.append("2")
                #Ask the user what movie director they want to search for:
                directorFilter = input("\nWhat director would you like to filter movies by?\n")

            #If the user chose to search by movie genre:
            elif choice == 3:
                #Add the fact that the user chose to search by movie genre to the filters chosen list:
                filtersChosen.append("3")
                #Ask the user what movie genre they want to search for:
                genreFilter = input("\nWhat genre would you like to filter movies by?\n")

            #If the user chose to search by movie ESRB rating:
            elif choice == 4:
                #Add the fact that the user chose to search by movie ESRB rating to the filters chosen list:
                filtersChosen.append("4")
                #Ask the user what movie ESRB rating they want to search for:
                ratingFilter = input("\nWhat ESRB rating would you like to filter movies by?\n")

            #If the user chose to search by movie length:
            elif choice == 5:
                #Add the fact that the user chose to search by movie length to the filters chosen list:
                filtersChosen.append("5")
                #Ask the user what movie length they want to search for:
                number = input("\nWhat movie length (in minutes) would you like to filter movies by?\n")

                #Make sure the user entered a number:
                try:
                    number = int(number)
                except ValueError:
                    print("\nINVALID INPUT\n\nPlease try again.")
                    return

            #If the user chose to search by notable actors:
            elif choice == 6:
                #Add the fact that the user chose to search by notable actors to the filters chosen list:
                filtersChosen.append("6")
                #Ask the user what notable actor they want to search for:
                notableActorsFilter = input("\nWhat notable actor would you like to filter movies by?\n")

            #If the user chose to exit:
            elif choice == 7:
                #exit:
                return

            #If the user did not enter a valid option:
            else:
                #Tell the user that they did not enter a valid option:
                print("\nINVALID CHOICE\n\nPlease try again.")
                #Keep the program running:
                return

        #Prepare for the list of reccomended movies to be shown:
        print("\nHere are some movies you might enjoy, based on your specifications:")

        #For every movie in the list:
        for row in movies:
            #Set a variable to show whether or not a given movie meets the user's qualifications:
            printRow = True
            #If the user chose to search by movie title and the movie still qualifies:
            if "1" in filtersChosen and printRow == True:
                #If the title the user chose to search for is present in the title of the movie:
                if titleFilter in row[0]:
                    #The movie validity variable stays true:
                    printRow = True
                #If the title the user chose to search for is not present in the title of the movie:
                else:
                    #The movie validity variable becomes false:
                    printRow = False
            #If the user chose to search by movie director and the movie still qualifies:
            if "2" in filtersChosen and printRow == True:
                #If the director the user chose to search for is present in the director of the movie:
                if directorFilter in row[1]:
                    #The movie validity variable stays true:
                    printRow = True
                #If the director the user chose to search for is not present in the director of the movie:
                else:
                    #The movie validity variable becomes false:
                    printRow = False
            #If the user chose to search by movie genre and the movie still qualifies:
            if "3" in filtersChosen and printRow == True:
                #If the genre the user chose to search for is present in the genre of the movie:
                if genreFilter in row[2]:
                    #The movie validity variable stays true:
                    printRow = True
                #If the genre the user chose to search for is not present in the genre of the movie:
                else:
                    #The movie validity variable becomes false:
                    printRow = False
            #If the user chose to search by movie ESRB rating and the movie still qualifies:
            if "4" in filtersChosen and printRow == True:
                #If the ESRB rating the user chose to search for is the same as the ESRB rating of the movie:
                if ratingFilter == row[3]:
                    #The movie validity variable stays true:
                    printRow = True
                #If the ESRB rating the user chose to search for is not the same as the ESRB rating of the movie:
                else:
                    #The movie validity variable becomes false:
                    printRow = False
            #If the user chose to search by movie length and the movie still qualifies:
            if "5" in filtersChosen and printRow == True:
                #Set variables equal to the user's desired length, plus or minus different amounts from -5 to +5:
                number1 = number - 5
                number2 = number - 4
                number3 = number - 3
                number4 = number - 2
                number5 = number - 1
                number6 = number + 1
                number7 = number + 2
                number8 = number + 3
                number9 = number + 4
                number10 = number + 5
                #If the movies length is the same as the user's desired movie length or the new variables:
                if row[4] == str(number) or row[4] == str(number1) or row[4] == str(number2) or row[4] == str(number3) or row[4] == str(number4) or row[4] == str(number5) or row[4] == str(number6) or row[4] == str(number7) or row[4] == str(number8) or row[4] == str(number9) or row[4] == str(number10):
                    #The movie validity variable stays true:
                    printRow = True
                #If the movies length is not the same as the user's desired movie length or the new variables:
                else:
                    #The movie validity variable becomes false:
                    printRow = False
            #If the user chose to search by notable actors and the movie still qualifies:
            if "6" in filtersChosen and printRow == True:
                #If the notable actor the user chose to search for is present in the notable actors of the movie:
                if notableActorsFilter in row[5]:
                    #The movie validity variable stays true:
                    printRow = True
                #If the notable actor the user chose to search for is not present in the notable actors of the movie:
                else:
                    #The movie validity variable becomes false:
                    printRow = False

            #If the movie validity variable is still true:
            if printRow == True:
                #Nicely print the details of the qualifying movie to the user:
                print("\n" + row[0] + " | Director: " + row[1] + " | Genre: " + row[2] + " | Rating: " + row[3] + " | Length(minutes): " + row[4] + " | Notable Actors: " + row[5])

    #If the user chose to print every movie in the list:
    elif option == 2:
        #For every movie in the list:
        for row in movies:
            #Neatly display the details of the movie:
            print("\n" + row[0] + " | Director: " + row[1] + " | Genre: " + row[2] + " | Rating: " + row[3] + " | Length(minutes): " + row[4] + " | Notable Actors: " + row[5])

    #If the user chose to exit:
    elif option == 3:
        #Make it look nice:
        print("")
        #Exit:
        return "Stop"

    #If the user did not choose a valid option:
    else:
        #Tell the user they did not choose a valid option:
        print("\nINVALID CHOICE\n\nPlease try again.")

#Function to run the program:
def runProgram():
    while True:

        #With the file open:
        with open("movieRecommender\movies.csv") as file:

            #Set the movies variable equal to the contents of the file:
            movies = csv.reader(file)

            # Remove the first line(it's just a guide):
            next(movies)

            #Run the main function of the program and check if the program should keep running:
            if main(movies) == "Stop":
                exit()

runProgram()