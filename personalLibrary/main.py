#Evan McCabe Personal Library Program

#Introduce the program and its function to the user:
print("\nHello! I am the personal library manager. I can manage a list of your favorite songs.")

#Create the set to carry the user's music list:
music = []

#Function to add an item to the music list:
def addItem():

    #Ask the user what song they want to add:
    title = input("\nWhat is the name of the song you would like to add?\n")

    #Ask the user what the artist of the song is:
    artist = input("\nWho is the artist of the song?\n")
    
    #Ask the user what the length of the song is:
    length = input("\nHow long is the song? (minutes:seconds)\n")

    #Ask the user what the genre of the song is:
    genre = input("\nWhat genre is the song?\n")

    #Create song
    song = {
        "title": title,
        "artist": artist,
        "length": length,
        "genre": genre
    }

    #Add the song to the music list:
    music.append(song)

    #Tell the user that the song has been added:
    print("\nSong added.")

#Function for the user to search for a song or songs written by a certain artist:
def search():

    #Ask the user if they want to search for a certain song, or songs by a certain artist:
    choice = input("\nWhat would you like to search for songs by?\nt = title\na = artist\nl = length\ng = genre\n")
    
    #If the user chooses to search for a certain song:
    if artistOrSong.upper() == "T":

        #Ask the user what song they want to search for:
        song = input("\nWhat song would you like to search for?\n")
        
        #Show the user which songs in their list have the title they inputted:
        print("\nHere are the songs in your list with that title:")
        for i in music:
            if song in i:
                print(i)

    #If the user chooses to search for songs written by a certain artist:
    elif artistOrSong.upper() == "A":

        #Ask the user what artist they want to search for songs written by:
        artist = input("\nWhat artist would you like to search for?\n")
        
        #Show the user the songs in their list written by the inputted artist:
        print("\nHere are the songs in your list created by that artist:")
        for i in music:
            if artist in i:
                print(i)

    #If the user does not input a or t:
    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

#Function to remove a song from the music list:
def removeItem():
    
    #Ask the user which song they want to remove from their list:
    song = input("\nWhat song would you like to remove? (title - artist)\n")

    #Remove the desired song from the list:
    if song in music:
        music.remove(song)
        print("\nSong removed.")

    #If the user tries to remove a song that is not in their list:
    else:
        print("\nThat song is not on your list.")

#Function to print the entire music list:
def printItems():

    #Print the user's music list:
    print("\nHere is your music list:")
    for i in music:
        print(i)

#Main function to run the program:
def main():

    #Aske the user what they want the program to do:
    function = input("\nWhat function would you like me to perform?\n1: Add song\n2: Search for a song on your list\n3: Remove song\n4: Print list\n")
    
    #Make sure the user entered a number:
    try:
        function = int(function)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

    #If the user chose to add a song:
    if function == 1:
        #Run function to add a song:
        addItem()

    #If the user chose to search for a song in their list:
    elif function == 2:
        #Run the function to search for a song in the music list:
        search()

    #If the user chose to remove a song from their music list:
    elif function == 3:
        #Run the function to remove a song from the music list:
        removeItem()

    #If the user chose to print their music list:
    elif function == 4:
        #Run the function to print the music list:
        printItems()

    #If the user entered a number that isn't a valid option:
    else:
        print("\nThat isn't an option.\n\nPlease try again.")
        main()

    #Keep the program running in a loop:
    main()

#Start the program:
main()