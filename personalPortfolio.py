#Evan McCabe Personal Portfolio

#The 6 programs I will be including in my portfolio:
# Movie Recommender
# Coin Change Problem
# Random Password Generator
# Morse Code Translator
# To-Do List
# Personal Library

#Introduce the portfolio to the user:
input('\nHello!\n\nI am Evan McCabe, and this is my personal portfolio. It is a collection of six programs I have previously written that I feel proud of.\n\nThis portfolio can be used by selecting the program you want to learn more about(or try for yourself), or choosing to exit the portfolio.\n\nAre you ready to choose a program? (Press "Enter.")\n')

#Main function to run the program:
def main():

    #Ask the user which program they want to pick:
    whichProgram = input("\nWhich program would you like to choose?\n\n1. Movie Recommender\n2. Coin Change Problem\n3. Random Password Generator\n4. Morse Code Translator\n5. To-Do List\n6. Personal Library\n")

    #If the user chooses Movie Recommender:
    if whichProgram == "1":
        pass

        #from movieRecommender.main import main as recommendMovies

    #If the user chooses Coin Change Problem:
    elif whichProgram == "2":
        pass

    #If the user chooses Random Password Generator:
    elif whichProgram == "3":
        pass

    #If the user chooses Morse Code Translator:
    elif whichProgram == "4":
        pass

    #If the user chooses To-Do List:
    elif whichProgram == "5":
        pass

    #If the user chooses Personal Library:
    elif whichProgram == "6":
        pass

    #If the user does not choose any of the valid options:
    else:

        #Tell the user that they did not pick a valid option:
        print("\nThat's not an option!\n\nPlease try again.")

        #Let the user try again:
        main()

#Run the program:
main()