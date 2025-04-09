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
    
    #If the user chooses to search by title::
    if choice.upper() == "T":

        #Ask the user what song title they want to search for:
        title = input("\nWhat song title would you like to search for?\n")
        
        #Show the user which songs in their list have the title they inputted:
        print("\nHere are the songs in your list with that title:\n\n------------------------------------------------")
        for i in music:
            if title in i["title"]:
                print("\n" + i["title"] + " by " + i["artist"] + " | genre: " + i["genre"] + " | length: " + i["length"])
        print("\n------------------------------------------------")

    #If the user chooses to search by artist:
    elif choice.upper() == "A":

        #Ask the user what artist they want to search for:
        artist = input("\nWhat artist would you like to search for?\n")
        
        #Show the user the songs in their list written by the inputted artist:
        print("\nHere are the songs in your list created by that artist:\n\n------------------------------------------------")
        for i in music:
            if artist in i["artist"]:
                print("\n" + i["title"] + " by " + i["artist"] + " | genre: " + i["genre"] + " | length: " + i["length"])
        print("\n------------------------------------------------")

    #If the user chooses to search by genre:
    elif choice.upper() == "G":

        #Ask the user what genre they want to search for:
        genre = input("\nWhat genre would you like to search for?\n")
        
        #Show the user the songs in their list written by the inputted artist:
        print("\nHere are the songs in your list with that genre:\n\n------------------------------------------------")
        for i in music:
            if genre in i["genre"]:
                print("\n" + i["title"] + " by " + i["artist"] + " | genre: " + i["genre"] + " | length: " + i["length"])
        print("\n------------------------------------------------")

    #If the user chooses to search by length:
    elif choice.upper() == "L":

        #Ask the user what length of song they want to search for:
        length = input("\nWhat song length would you like to search for?\n")
        
        #Show the user the songs in their list with the inputted length:
        print("\nHere are the songs in your list with that length:\n\n------------------------------------------------")
        for i in music:
            if length in i["length"]:
                print("\n" + i["title"] + " by " + i["artist"] + " | genre: " + i["genre"] + " | length: " + i["length"])
        print("\n------------------------------------------------")

    #If the user does not input any of the options above:
    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

#Function to remove a song from the music list:
def removeItem():
    
    #Ask the user which song they want to remove from their list:
    toBeRemoved = input("\nWhat is the tile of the song would you like to remove?\n")

    #Remove the desired song from the list:
    removed = False
    for i in music:
        if toBeRemoved in i["title"]:
            music.remove(i)
            print("\nSong removed.")
            removed = True

    #If the user tries to remove a song that isn't on their list:
    if removed == False:
        print("\nThat song is not on  your list.")

#Function to print every song in the user's music list:
def printItems():

    #Ask the user if they want a simple list or detailed list:
    choice = input("\nWhich list do you want to show?\nd = detailed list\ns = simple list\n")

    #If the user chooses to print a detailed list:
    if choice.upper() == "D":

        #Show the user a detailed list of all the songs in their music list:
        print("\nHere are all the songs in your list:\n\n-------------------------------------")
        for i in music:
            print("\n" + i["title"] + " by " + i["artist"] + " | genre: " + i["genre"] + " | length: " + i["length"])
        print("\n-------------------------------------")

    #If the user chooses to print a simple list:
    elif choice.upper() == "S":

        #Show the user a simple list of all the songs in their music list:
        print("\nHere are all the songs in your list:\n\n-------------------------------------")
        for i in music:
            print("\n" + i["title"] + " by " + i["artist"])
        print("\n-------------------------------------")

#Function to change a song on the list:
def change():

    #Ask the user which song they want to change:
    songToChange = input("\nWhat is the title of the song you want to modify?\n")

    #Make sure that the user chose a song that is on their list:
    valid = False
    for i in music:
        if songToChange in i["title"]:
            valid = True
    if valid == False:
        print("\nThat song is not on your list.")
        main()

    #Ask the user what they want to change about their selected song:
    choice = input("\nWhat do you want to change about the song?\nt = song title\na = song artist\ng = song genre\nl = song length\n")

    #If the user chooses to change the song's title:
    if choice.upper() == "T":
        
        #Ask the user what they want the song's new title to be:
        newTitle = input("\nWhat do you want to change the song's title to be?\n")

        #Apply the change as specified by the user:
        for i in music:
            if songToChange in i["title"]:
                i["title"] = newTitle
                #Tell the user the change was successful:
                print("\nChange successful.")

    #If the user chooses to change the song's artist:
    elif choice.upper() == "A":
        
        #Ask the user what they want the song's new artist to be:
        newArtist = input("\nWhat do you want to change the song's artist to be?\n")

        #Apply the change as specified by the user:
        for i in music:
            if songToChange in i["title"]:
                i["artist"] = newArtist
                #Tell the user the change was successful:
                print("\nChange successful.")

    #If the user chooses to change the song's genre:
    elif choice.upper() == "G":
        
        #Ask the user what they want the song's new genre to be:
        newGenre = input("\nWhat do you want to change the song's genre to be?\n")

        #Apply the change as specified by the user:
        for i in music:
            if songToChange in i["title"]:
                i["genre"] = newGenre
                #Tell the user the change was successful:
                print("\nChange successful.")

    #If the user chooses to change the song's length:
    elif choice.upper() == "L":
        
        #Ask the user what they want the song's new length to be:
        newLength = input("\nWhat do you want to change the song's length to be? (minutes:seconds)\n")

        #Apply the change as specified by the user:
        for i in music:
            if songToChange in i["title"]:
                i["length"] = newLength
                #Tell the user the change was successful:
                print("\nChange successful.")

    #If the user does not choose any of the valid options:
    else:
        #Tell the user they chose an invalid option:
        print("\nINVALID OPTION\n\nPlease try again.")
        #Return the user to the main menu:
        main()

#Main function to run the program:
def main():

    #Aske the user what they want the program to do:
    function = input("\nWhat function would you like me to perform?\n1: Add a song to your list\n2: Search for a song on your list\n3: Remove a song from your list\n4: Show every song on your list\n5: Modify a song on your list\n6: exit\n")
    
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

    #If the user chose to modify a song on their music list:
    elif function == 5:
        #Run the function to modify a song on the music list:
        change()

    #If the user chose to exit the program:
    elif function == 6:
        #Exit the program(and make it look nice):
        print("")
        exit()

    #If the user entered a number that isn't a valid option:
    else:
        print("\nThat isn't an option.\n\nPlease try again.")
        main()

    #Keep the program running in a loop:
    main()

#Start the program:
main()