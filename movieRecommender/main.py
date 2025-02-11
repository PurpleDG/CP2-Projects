# Evan McCabe Movie Recommender

import csv

with open("movieRecommender\movies.csv") as file:
    movies = csv.reader(file)
    #Remove the first line(it's just a guide):
    next(movies)
    for row in movies:
        print(row)