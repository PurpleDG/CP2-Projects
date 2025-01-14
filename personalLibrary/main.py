#Evan McCabe Personal Library Program

print("\nHello! I am the personal library manager. I can manage a list of your favorite songs.")

music = {""}

def addItem():
    song = input("\nWhat song would you like to add? (song - artist)\n")
    music.add(song)
    print("\nSong added.")

def search():

    artistOrSong = input("\nDo you want to search by artist, or title? (a = artist, t = title)\n")
    
    if artistOrSong == "t" or "T":

        song = input("\nWhat song would you like to search for?\n")
        
        for i in music:
            if song in i:
                print("\nThat song is on your list.")
            else:
                print("\nThat song is not on your list.")

    elif artistOrSong == "a" or "A":

        artist = input("\nWhat artist would you like to search for?\n")
        
        print("\nHere are the songs in your list created by that artist:")

        for i in music:
            if artist in i:
                print(i)

    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

def removeItem():
    song = input("\nWhat song would you like to remove?\n")
    if song in music:
        music.remove(song)
        print("\nSong removed.")
    else:
        print("\nThat song is not on your list.")

def printItems():
    for i in music:
        print(i)

def main():
    function = input("\nWhat function would you like me to perform?\n1: Add song\n2: Search for a song on your list\n3: Remove song\n4: Print list\n")
    try:
        function = int(function)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

    if function == 1:
        addItem()

    elif function == 2:
        search()

    elif function == 3:
        removeItem()

    elif function == 4:
        printItems()

    else:
        print("\nThat isn't an option.\n\nPlease try again.")
        main()

    main()

main()