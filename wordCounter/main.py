#Evan McCabe

import time

#OVERVIEW:

#Write a program that look at a document that a user has written on and update it with the word count and a timestamp for when that wordcount was last updated

#REQUIREMENTS:

#Uses at least 3 pages (main, file handling, and time handling) NOTE: main is the only file name I've given you
#Reads and Writes to the file
#Uses functional decomposition
#Lets the user tell what file to use it on
#Uses good naming practices
#Has good white space

#Fetch functions from other pages of the program to be used in the main page:
from trackTime import getTime
from addToFile import update

#Introduce the program to the user:
print("\nI am the file updater bot! I can add a word count to a document, along with a timestamp showing when it was updated.")

#Use all functions from other pages to run the entirety of the program:
while True:

    #Ask the user for the relative path of the file they want to update:
    path = input("\nWhat is the relative path of the file you would like to update?\n")

    #Update the user's desired text file with a word count and "date updated" using the update function:
    keepGoing = update(path, getTime())

    #Keep the program running or stop it based on the user's choice:
    if keepGoing == "No":
        break