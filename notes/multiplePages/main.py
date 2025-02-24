#Evan McCabe Multiple Pages Notes

#1. How do you make multiple files in python?
    #Make a new file ending in .py
    #snake case file names
    #descriptive file names (shoty)

#2. How do you get a function from another file
from calc import addition as add, subtraction as sub
    #a * allows you to import everything
    #aliasing is where you import a function and give it a new keyword

print(add())
print(sub())

#3. How do you get variables from another file?
    #They can be obtained the same way as functions...
from calc import num
    #Better to return from a function, though.

#4. How do you have a function with multiple returns?
def getUserInfo():
    name = input("What is your name?\n")
    age = input("How old are you?\n")
    color = input("What is your favorite color?\n")
    return name, age, color

name, age, color = getUserInfo()

print(name)

#5. Why would you use multiple pages for a python project?
    #It makes it easier to merge GitHub branches if you are writing on multiple pages.
    #Modularity - breaking a program into smaller, more manageable pieces.
    #Main should ONLY INCLUDE: Introduction + User Interface
    #Functionality - keeps your code clean.