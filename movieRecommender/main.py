# Evan McCabe Movie Recommender

import csv

print("\nHello! I am the movie recommender.")

def main(movies):
    
    choice = input("\nWhat would you like to do?\n1 = Get Movie Reccomendations\n2 = Display All Movies\n3 = Exit\n")

    try:
        choice = int(choice)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main(movies)

    if choice == 1:
        pass

    elif choice == 2:
        for row in movies:
            #Title,Director,Genre,Rating,Length (min),Notable Actors
            print("\nTitle: " + row[0] + " | Director: " + row[1] + " | Genre: " + row[2] + " | Rating: " + row[3] + " | Length(minutes): " + row[4] + " | Notable Actors: " + row[5])

    elif choice == 3:
        pass

    else:
        pass

with open("movieRecommender\movies.csv") as file:

    movies = csv.reader(file)

    # Remove the first line(it's just a guide):
    next(movies)

    main(movies)