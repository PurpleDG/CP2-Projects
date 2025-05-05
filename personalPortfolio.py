#Evan McCabe Personal Portfolio

#There's a silly little easter egg somewhere in the program... If you can find it...

#Introduce the portfolio to the user:
input('\nHello!\n\nI am Evan McCabe, and this is my personal portfolio. It is a collection of six programs I have previously written that I feel proud of.\n\nThis portfolio can be used by selecting the program you want to learn more about(or try for yourself).\n\nAre you ready to choose a program? (Press "Enter.")\n')

#Main function to run the program:
def main():

    #Ask the user which program they want to pick:
    whichProgram = input("\nWhich program would you like to choose?\n\n1. Movie Recommender\n2. Coin Change Problem\n3. Random Password Generator\n4. Morse Code Translator\n5. To-Do List\n6. Personal Library\n")

    #If the user chooses Movie Recommender:
    if whichProgram == "1":
        
        #Describe my Movie Recommender program:
        print("\nMy movie recommender project will give the user certain movies out of a list as recommendations, based on criteria that the user gives. For example, if the user sets criteria to PG-rated movies, the program will display every movie in its list that are rated PG, along with details about each movie. Aditionally, the program can simply print every movie in its list.\n\nI found the process of making this program to be easier than I expected. It was still a little rough, since I had only just started using CSV's, but the CSV was created for me, so it wasn't that bad.\n\nBy making this project I learned, well, how to use CSV's! They're good. I like CSV's.")

        #Ask the user if they are ready to run the program:
        input('\nPress "Enter" when you are ready to try the program.\n')

        #Run the program for the user to try:
        from movieRecommender.main import main as recommendMovies

    #If the user chooses Coin Change Problem:
    elif whichProgram == "2":
        
        #Describe my Coin Change Problem program:
        print("\nMy coin change problem program will take an amount of money (not just USD; some other currencies as well) and break it down into the least amount of bills possible. For example, if a user enters 12 USD, the program will tell them that they will need 1 $10 bill, and 2 $1 bills.\n\nThis program was pretty simple to make, what with my previously-learned CSV skills, but I really had to think to write the code that actually breaks down the money.\n\nThis program taught me that there are, more often than not, several ways to solve the same problem. I'm pretty sure that none of my classmates were writing their coin change problem programs the same way I was, but our programs all worked just fine!")

        #Ask the user if they are ready to run the program:
        input('\nPress "Enter" when you are ready to try the program.\n')

        #Run the program for the user to try:
        from coinChangeProblem.main import main as solveTheCoinChangeProblem

    #If the user chooses Random Password Generator:
    elif whichProgram == "3":
        
        #Describe my Random Password Generator program:
        print("\nMy random password generator program will generate 4 random passwords based on user criteria, such as password length, whether to include numbers, whether to include special characters, etc. Pretty simple, right?\n\nThis program was desceptively difficult to make. It was helpful, however, that I could copy python lists of, like, every letter in the English alphabet, or every special character, or other lists like that, online.\n\nWriting the code for this program taught me that users can be really annoying. The program itself was pretty simple, but it gets weird when you have to deal with users doing things like trying to make a password with 0 characters in it, making a password using no criteria whatsoever, or other dumb stuff like that. In fact, I think it might still be pretty easy to cause errors in the program as a user, unlike my other programs...")

        #Ask the user if they are ready to run the program:
        input('\nPress "Enter" when you are ready to try the program.\n')

        #Run the program for the user to try:
        from randomPasswordGenerator.main import main as generatePasswords

    #If the user chooses Morse Code Translator:
    elif whichProgram == "4":
        
        #Describe my Morse Code Translator program:
        print("\nMy morse code translator program does exactly what it sounds like it does. It translates english to morse code, and morse code to English.\n\nThis program wasn't that hard to write, except for one glaring problem, which I'll tell you about in the next paragraph...\n\nOne thing I learned from making this program is that, sometimes, convenience of the user must be sacrificed for the sanity of the programmer. When I was writing this program, I just could not figure out how to take an entire string of morse code and turn it into English! The rest of the program was fine, but I just couldn't figure out how to do that one specific function! In the end, I had to make it so that the user had to translate morse code into English one character at a time, which is, I know, very annoying. But it saved me time and stress, so I think it was worth it!")

        #Ask the user if they are ready to run the program:
        input('\nPress "Enter" when you are ready to try the program.\n')

        #Run the program for the user to try:
        from morseCodeTranslator.main import main as translateMoreseCode

    #If the user chooses To-Do List:
    elif whichProgram == "5":
        
        #Describe my To-Do List program:
        print("\nMy to-do list program stores a to-do list on a text file, and allows the user to modify and view it in a nice interface.\n\nI actually had some trouble writing this program, as simple as it is, because I had never used text files before.\n\nWriting this program taught me how to read and modify text files in python! It was the first real program I made that had a text file in it. I don't really like text files that much; CSV's are significantly superior...")

        #Ask the user if they are ready to run the program:
        input('\nPress "Enter" when you are ready to try the program.\n')

        #Run the program for the user to try:
        from toDoList.main import main as doToList

    #If the user chooses Personal Library:
    elif whichProgram == "6":
        
        #Describe my Personal Library program:
        print("\nMy personal library program, despite what it is named, is a program that stores a list of songs for the user. The user can input the details of a song - including the song's title, length, genre, etc. - and the song will be added to a list. The user can then have the list of songs printed out nicely to see, or change details of songs within the list. It's basically a different version of the Liked Songs playlist in Spotify.\n\nThis program was actually really fun to make, I think. No notes.\n\nThis program, in retrospect, taught me that there is always an easier way to do something. I wrote this program before my class was taught about CSV's, so I used a list of dictionaries, instead. This program would have been SO much easier to make if I had known about CSV's. SO MUCH EASIER!")

        #Ask the user if they are ready to run the program:
        input('\nPress "Enter" when you are ready to try the program.\n')

        #Run the program for the user to try:
        from personalLibrary.main import main as its_Not_Really_A_Library_Is_It_Ms_LaRose_Its_Just_A_List_Of_Dictionaries

    #If the user does not choose any of the valid options:
    else:

        #Tell the user that they did not pick a valid option:
        print("\nThat's not an option!\n\nPlease try again.")

        #Let the user try again:
        main()

#Run the program:
main()