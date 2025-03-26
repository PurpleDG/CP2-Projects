#Evan McCabe Coin Change Problem

import csv

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
        print("\nHey! That's not a number!\n\nPlease try again.")
        main()

    #Inner function to perform a coin change:
    def coinChange(country, money):

        print("\nThe country is ", country, ", and the amount of money to be coin changed is ", money, ".")

        #Function to ask the user if they want to keep using the program:
        def keepRunning():

            #Ask the user if they want to keep using the program:
            keepUsing = input("\nDo you want to keep using the program? (y/n)\n")

            #If the user says yes:
            if keepUsing == "y":
                main()

            #If the user says no:
            elif keepUsing == "n":
                print("\nThank you! Goodbye!\n")
                exit()

            #If the user does not input a valid action:
            else:

                #Tell the user they did not input a valid action and let them try again:
                print("\nINVALID OPTION\n\nPlease try again.")
                keepRunning()

        #Do the coin change thing:

        print("\nYou will need:")

        with open("coinChangeProblem\coinDenominations.csv") as file:

            coins = csv.reader(file)

            for row in coins:
                if row[0] == country:

                    if money / float(row[2]) >= 1:
                        numberNeeded = int(money // float(row[2]))
                        print(numberNeeded, " ", row[1], "(s).")
                        

        #Ask the user if they want to keep using the program:
        keepRunning()

    #Function to ask the user how much money they want to coin change:
    def howMuchMoney():

        #Ask the user how much money they want to coin change:
        money = input("\nHow much money do you want to coin change? (number only, up to 2 decimal places)\n")

        #Make sure the user input a number:
        try:
            money = float(money)
        except:
            print("\nNOT A NUMBER\n\nPlease try again.")
            main()

        #Make sure the user entered a float with 2 or less decimal places:
        roundedMoney = round(money, 2)
        if money == roundedMoney:
            pass
        else:
            print("\nTOO MANY DECIMAL PLACES\n\nPlease try again.")
            main()
        
        #Return the user's desired amount of money to be coin changed for the coin change function:
        return money

    #If the user picked America:
    if country == 1:
        
        #Run the coin change function after asking the user how much money they want to coin change:
        coinChange("America", howMuchMoney())

    #If the user picked Japan:
    elif country == 2:
        
        #Run the coin change function after asking the user how much money they want to coin change:
        coinChange("Japan", howMuchMoney())

    #If the user did not pick a valid option
    else:

        #Tell the user they didn't choose a valid option and let them try again:
        print("\nNOT A VALID OPTION\n\nPlease try again.")
        main()

#Start the program:
main()