#Evan McCabe Advanced Functions Notes

#1. What is a helper function?
    #a function written to be called in another function

def isInt(userInput):
    try:
        int(userInput)
    except:
        print("\nPlease give me a number.")
        userInput = isInt(input("\nHow old are you?\n"))
        return userInput
    
def age():
    old = isInt(input("\nHow old are you?\n"))

    print(f"Cool. You are {old}.\n")

age()

#2. What is the purpose of a helper function?
    #to make functions easier to read and less complex

#3. What is an inner function?
    #a function that is inside of another function

def add(a):
    b = int(input("\nGive me a number:\n"))

    def addition():
        print(a+b)

    addition()

#add(3)

import logging

logging.basicConfig(level=logging.INFO)

def logger(func):

    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")
        return func(*args, *kwargs)
    return wrapper

#@logger
def adder(a,b):
    return a+b
print(adder(3,4), "\n")

#4. What is the scope of a variable in a function WITH an inner function?
    #everything contained within the outer function

#5. Why do we use inner functions?
    #less parameters
    #less returns

#6. What is a closure function?
    #allows a function to remember information accross multiple functions

def add(a):
   
    def addition(b):
       return a+b

    return addition

base = add(10)

#print("\n", base(5))

#EXAMPLE

def math(income):
    def perc(amount, type):
        percent = amount/income
        print(f"\nYour {type} is ${amount}, and that is {percent} of your income.")

def userInputs(type):
    return int(input(f"\nWhat is your monthly {type}\n$"))

income = userInputs("income")
rent = userInputs("rent")
utilities = userInputs("utilities")
groceries = userInputs("groceries")
transportation = userInputs("transportation")

start = math()

#7. Why do we write closure functions?
    #because it saves information accross multiple calls of the function

#8. What is recursion?
    #when you call a function inside of itself

#9. How does recursion work?
    #a function is called again, now with NEW information