# Evan McCabe Movie Recommender

import csv

print("\nHello! I am the movie recommender.")

def main(movies):

    filters = []

    choice = input("\nWhat would you like to do?\n1 = Get Movie Reccomendations\n2 = Display All Movies\n3 = Exit\n")

    try:
        choice = int(choice)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main(movies)

    if choice == 1:
        num = input("\nHow many filters would you like to use to search for movies?\n")

        try:
            num = int(num)
        except ValueError:
            print("\nINVALID INPUT\n\nPlease try again.")
            main(movies)

        for i in range(num):
            choice = input("\nWhat would you like to search by?\n1 = Title\n2 = Director\n3 = Genre\n4 = ESRB Rating\n5 = Length(minutes)\n6 = Notable Actors\n7 = Exit\n")

            try:
                choice = int(choice)
            except:
                print("\nINVALID INPUT\n\nPlease try again.")
                main(movies)

            if choice == 1:
                titleFilter = input("\nWhat is the movie title you want to search for?\n")
                filters.append(titleFilter)

            elif choice == 2:
                directorFilter = input("\nWhat director would you like to filter movies by?\n")
                filters.append(directorFilter)

            elif choice == 3:
                genreFilter = input("\nWhat genre would you like to filter movies by?\n")
                filters.append(genreFilter)

            elif choice == 4:
                ratingFilter = input("\nWhat ESRB rating would you like to filter movies by?\n")
                filters.append(ratingFilter)

            elif choice == 5:
                lengthFilter = input("\nWhat movie length (in minutes) would you like to filter movies by?\n")
                filters.append(lengthFilter)

            elif choice == 6:
                notableActorsFilter = input("\nWhat notable actors would you like to filter movies by?\n")
                filters.append(notableActorsFilter)

            elif choice == 7:
                main(movies)

            else:
                print("\nINVALID CHOICE\n\nPlease try again.")
                main(movies)

        #filtersCopy = filters

        #for row in movies:
            #for item in row:
                #for i in filters:
                    #if i in item:
                        #filtersCopy.remove(i)
            #if filtersCopy == []:
                #print("\n" + row[0] + " | Director: " + row[1] + " | Genre: " + row[2] + " | Rating: " + row[3] + " | Length(minutes): " + row[4] + " | Notable Actors: " + row[5])
            #filtersCopy = filters


    elif choice == 2:
        for row in movies:
            print("\n" + row[0] + " | Director: " + row[1] + " | Genre: " + row[2] + " | Rating: " + row[3] + " | Length(minutes): " + row[4] + " | Notable Actors: " + row[5])

    elif choice == 3:
        print("")
        exit()

    else:
        print("\nINVALID CHOICE\n\nPlease try again.")

    main(movies)

with open("movieRecommender\movies.csv") as file:

    movies = csv.reader(file)

    # Remove the first line(it's just a guide):
    next(movies)

    main(movies)