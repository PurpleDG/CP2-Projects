#Evan McCabe Coin Change Problem

import csv

from keepRunning import keepRunning

#Introduce the program to the user:
print("\nHello! I am the coin change program. I can take a money amount and tell you what dollars and coins you need to distribute the money into the least amount of dollars and coins possible.")

#Main function to run the program:
def main():

    #Ask the user what country they want to coin change money from:
    country = input("\nWhat country do you want to coin change money from?\n1. America\n2. Japan\n3. France\n4. Brazil\n")

    #Make sure that the user entered a number:
    try:
        country = int(country)
    except:
        print("\nHey! That's not a number!\n\nPlease try again.")
        main()

    #Inner function to perform a coin change:
    def coinChange(country, money, rownum):

        print("\nThe country is ", country, ", and the amount of money to be coin changed is ", money, ".")

        #Do the coin change thing:

        print("\nYou will need:\n")

        with open("CP2-Projects\coinChangeProblem\coinDenominations.csv") as file:

            coins = csv.reader(file)

            for row in coins:
                if row[0] == country:
                    denominationNum = ((rownum-1)//2)
                    a = 2
                    for i in range(denominationNum):

                        if money / float(row[i+a]) >= 1:
                            numberNeeded = int(money // float(row[i+a]))
                            if numberNeeded != 0:
                                print(numberNeeded, " ", row[i+(a-1)], "(s).")
                                money -= (int(numberNeeded)*float(row[i+a]))

                        a += 1

        #Ask the user if they want to keep using the program:
        keepRunning()
        main()

    #Function to ask the user how much money they want to coin change:
    def howMuchMoney(country):

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

        #Make sure the user didn't input a number with a decimal for a country that doesn't have smaller money units:
        if country == "Japan":
            if money%1 != 0:
                print("\nThat country doesn't do decimal amounts of money!\n\nPlease try again.")
                main()
        
        #Return the user's desired amount of money to be coin changed for the coin change function:
        return money

    #If the user picked America:
    if country == 1:
        
        #Run the coin change function for America after asking the user how much money they want to coin change:
        coinChange("America", howMuchMoney("America"), 25)

    #If the user picked Japan:
    elif country == 2:
        
        #Run the coin change function for Japan after asking the user how much money they want to coin change:
        coinChange("Japan", howMuchMoney("Japan"), 19)

    #If the user picked France:
    elif country == 3:

        #Run the coin change function for France after asking the user how much money they want to coin change:
        coinChange("France", howMuchMoney("France"), 31)

    #If the user picked Brazil:
    elif country == 4:

        #Run the coin change function for Brazil after asking the user how much money they want to coin change:
        coinChange("Brazil", howMuchMoney("Brazil"), 27)

    #If the user did not pick a valid option
    else:

        #Tell the user they didn't choose a valid option and let them try again:
        print("\nNOT A VALID OPTION\n\nPlease try again.")
        main()

#Start the program:
main()