# Evan McCabe Movie Recommender

import csv

print("\nHello! I am the movie recommender.")

def main(movies):

    filtersChosen = []

    option = input("\nWhat would you like to do?\n1 = Get Movie Reccomendations\n2 = Display All Movies\n3 = Exit\n")

    try:
        option = int(option)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        return

    if option == 1:
        num = input("\nHow many filters would you like to use to search for movies?\n")

        try:
            num = int(num)
        except ValueError:
            print("\nINVALID INPUT\n\nPlease try again.")
            return

        for i in range(num):
            choice = input("\nWhat would you like to search by?\n1 = Title\n2 = Director\n3 = Genre\n4 = ESRB Rating\n5 = Length(minutes)\n6 = Notable Actor\n7 = Exit\n")

            try:
                choice = int(choice)
            except:
                print("\nINVALID INPUT\n\nPlease try again.")
                return

            if choice == 1:
                filtersChosen.append("1")
                titleFilter = input("\nWhat is the movie title you want to search for?\n")

            elif choice == 2:
                filtersChosen.append("2")
                directorFilter = input("\nWhat director would you like to filter movies by?\n")

            elif choice == 3:
                filtersChosen.append("3")
                genreFilter = input("\nWhat genre would you like to filter movies by?\n")

            elif choice == 4:
                filtersChosen.append("4")
                ratingFilter = input("\nWhat ESRB rating would you like to filter movies by?\n")

            elif choice == 5:
                filtersChosen.append("5")
                number = input("\nWhat movie length (in minutes) would you like to filter movies by?\n")
                try:
                    number = int(number)
                except ValueError:
                    print("\nINVALID INPUT\n\nPlease try again.")
                    return

            elif choice == 6:
                filtersChosen.append("6")
                notableActorsFilter = input("\nWhat notable actor would you like to filter movies by?\n")

            elif choice == 7:
                return

            else:
                print("\nINVALID CHOICE\n\nPlease try again.")
                return

        print("\nHere are some movies you might enjoy, based on your specifications:")

        for row in movies:
            printRow = True
            if "1" in filtersChosen and printRow == True:
                if titleFilter in row[0]:
                    printRow = True
                else:
                    printRow = False
            if "2" in filtersChosen and printRow == True:
                if directorFilter in row[1]:
                    printRow = True
                else:
                    printRow = False
            if "3" in filtersChosen and printRow == True:
                if genreFilter in row[2]:
                    printRow = True
                else:
                    printRow = False
            if "4" in filtersChosen and printRow == True:
                if ratingFilter == row[3]:
                    printRow = True
                else:
                    printRow = False
            if "5" in filtersChosen and printRow == True:
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
                if row[4] == str(number) or row[4] == str(number1) or row[4] == str(number2) or row[4] == str(number3) or row[4] == str(number4) or row[4] == str(number5) or row[4] == str(number6) or row[4] == str(number7) or row[4] == str(number8) or row[4] == str(number9) or row[4] == str(number10):
                    printRow = True
                else:
                    printRow = False
            if "6" in filtersChosen and printRow == True:
                if notableActorsFilter in row[5]:
                    printRow = True
                else:
                    printRow = False

            if printRow == True:
                print("\n" + row[0] + " | Director: " + row[1] + " | Genre: " + row[2] + " | Rating: " + row[3] + " | Length(minutes): " + row[4] + " | Notable Actors: " + row[5])

    elif option == 2:
        for row in movies:
            print("\n" + row[0] + " | Director: " + row[1] + " | Genre: " + row[2] + " | Rating: " + row[3] + " | Length(minutes): " + row[4] + " | Notable Actors: " + row[5])

    elif option == 3:
        print("")
        return

    else:
        print("\nINVALID CHOICE\n\nPlease try again.")

keepGoing = True

while keepGoing == True:

    with open("movieRecommender\movies.csv") as file:

        movies = csv.reader(file)

        # Remove the first line(it's just a guide):
        next(movies)

        main(movies)
        yn = input("\nWould you like to keep using the program?\n1 = yes\n2 = no\n")
        if yn == "1":
            pass
        else:
            keepGoing = False