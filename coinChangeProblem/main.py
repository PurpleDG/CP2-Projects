#Evan McCabe Coin Change Problem

#Introduce the program to the user:
print("\nHello! I am the coin change program. I can take a money amount and tell you what dollars and coins you need to distribute the money into the least amount of dollars and coins possible.")

#Main function to run the program:
def main():

    #Ask the user what country they want to coin change money from:
    country = input("\nWhat country do you want to coin change money from?\n1. America\n2. Japan\n")

    #Make sure that the user entered a number:
    try:
        country = int(country)
    except:
        print("\nHey! That's not a valid number!\n\nPlease try again.")
        main()

    

#Start the program:
main()