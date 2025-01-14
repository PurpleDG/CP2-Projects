#Evan McCabe Financial Calculator

#I tried to make a function to check if an input is the corrects variable type, as that needs to happen a lot in the program, but I was not able to.

#Introduction to the user:
print("\nHello! I am a financial calculator.")

#Function to save money for a purchasing goal:
def savingGoal():
    #Ask the user if they are depositing money weekly or monthly:
    weekOrMonth = input("\nWeekly or monthly deposit? (1 = weekly, 2 = month)\n")
    #Check if the user inputted a valid value:
    try:
        weekOrMonth = int(weekOrMonth)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        savingGoal()

    #Check if the user inputted a 1 or a 2:
    if weekOrMonth == 1 or 2:
        print("")
    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        savingGoal()

    #Ask the user how much their goal is:
    goalCost = input("How much does your goal item cost? (whole number or decimal number)\n")
    #Check to make sure the user inputted a valid value:
    try:
        goalCost = float(goalCost)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        savingGoal()

    #If the user chose weekly deposit:
    if weekOrMonth == 1:
        #Ask the user how much their weekly deposit is:
        deposit = input("\nWhat is your weekly deposit? (whole number or decimal number)\n")
        #Check if the user inputted a valid value:
        try:
            deposit = float(deposit)
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingGoal()

        #Calculate how many weeks it will take for the user to reach their goal:
        timeTaken = str(int(goalCost / deposit))
        #Tell the user how many weeks it will take them to reach their goal:
        print("\nIt will take around " + timeTaken + " weeks for you to reach your goal.")
        #Keep the program running:
        main()

    #If the user chose months:
    if weekOrMonth == 2:
        #Ask the user how much their monthly deposit is:
        deposit = input("\nWhat is your monthly deposit? (whole number or decimal number)\n")
        #Make sure the user inputted a valid value:
        try:
            deposit = float(deposit)
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingGoal()

        #Calculate how many months it will take the user to reach their goal:
        timeTaken = str(int(goalCost / deposit))
        #Tell the user how many months it will take them to reach their goal:
        print("\nIt will take around " + timeTaken + " months for you to reach your goal.")
        #Keep the program running:
        main()

#Function to calculate compound interest based on user input values:
def compoundInterest():

    #Ask the user how much money is in the account:
    deposit = input("\nWhat is the starting amount of money? (whole number or decimal number)\n")
    #Make sure the inputted a valid value:
    try:
        deposit = float(deposit)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        compoundInterest()
    
    #Ask the user what the interest rate on the account is:
    rate = input("\nWhat is the interest rate? (whole number or decimal number)\n")
    #Make sure the user inputted a valid value:
    try:
        rate = float(rate)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        compoundInterest()

    #Ask the user how many years the account is being compounded over:
    years = input("\nOver how many years is interest being compunded? (whole number or decimal number)\n")
    #Make sure the user inputted a valid value:
    try:
        years = float(years)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        compoundInterest()

    #Calculate the total amount of money in the account after being compounded over the inputted amount of years:
    rate = rate / 100
    a = rate / 12
    b = a + 1
    years = years * 12
    b = b ** years
    amount = deposit * b
    amount = round(amount, 2)
    amount = str(amount)

    #Tell the user the total amount of money in the account after being compounded over the inputted amount of years:
    print("\nYou will end up with $" + amount + ".")

#Function to make general budget reccomendations to the user based on their monthly income:
def budgetAllocator():
    #Ask the user what their monthly income is:
    income = input("\nWhat is your monthly income?\n")
    #Make sure the user inputted a valid value:
    try:
        income = float(income)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        budgetAllocator()

    #Fractions of monthly income portioned to each category:
    savings = 0.5
    spending = 0.1
    food = 0.4

    #Reccomendations for each category based on the user's monthly income specifically:
    savings = savings * income
    spending = spending * income
    food = food * income

    #Reccomendations rounded to adjust for possible large decimal numbers:
    savings = round(savings, 2)
    spending = round(spending, 2)
    food = round(food, 2)

    #Print monthly budget reccomendations to the user:
    print("\nHere is a good GENERAL budget for your income, not including monthly expenses:")
    print("savings: $" + str(savings) + " a month")
    print("spending: $" + str(spending) + " a month")
    print("food: $" + str(food) + " a month")

#Function to find the paid price of an item based on its original price and a discount:
def salePrice():
    #Ask the user what the original price of the item is:
    price = input("\nWhat is the normal price of the item? (whole number or decimal number)\n")
    #Make sure the user inputted a valid value:
    try:
        price = float(price)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        salePrice()

    #Ask the user what the discount on the item is:
    discount = input("\nWhat is the percent discount being taken from the price of the item? (whole number)\n")
    #Make sure the user inputted a valid value:
    try:
        discount = int(discount)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        salePrice()

    #Adjust the discount percentage to be calculated:    
    discount = ("0." + str(discount))
    discount = float(discount)

    #Calculate the amount of money taken away from the total price of the item:
    discount = price * discount

    #Find the final price of the item after being lowered by the discount:
    finalPrice = price - discount

    #Tell the user the total cost of the item after the discount:
    print("\nThe total cost of the item is $" + str(finalPrice) + ".")

#Function to calculate how much money the user should tip based on their check and what percent they would like to tip:
def tipCalculator():
    #Ask the user how much money they are being charged on their check in total:
    check = input("\nHow much is your check? (whole number or decimal number)\n")

    #Make sure the user inputted a valid value:
    try:
        check = float(check)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        tipCalculator()

    #Ask the user what percent of their check they would like to tip to the employees:
    tip = input("\nWhat percent would you like to tip? (whole number)\n")
    try:
        tip = int(tip)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        tipCalculator()

    #Adjust the tip percentage to be calculated:
    tip = str(tip)
    tip = tip.replace(".", "")
    tip = ("0." + str(tip))
    tip = float(tip)

    #Calculate how much money the user should tip:
    tip = tip * check
    tip = round(tip, 2)

    #Ask the user how much money they should tip:
    print("\nYou should tip $" + str(tip) + ".")

#The main function that runs the program:
def main():
    #Ask the user what function they would like the calculator to perform:
    print("\nWhat function would you like me to perform?")
    #Tell the user what their options are on the calculator:
    function = input("1: Saving Goal Calculator\n2: Coumpound Interest Calculator\n3: Budget Allocator\n4: Sale Price Calculator\n5: Tip Calculator\n")
    #Make sure the user inputted a valid value:
    try:
        function = int(function)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

    #Make sure the user inputted one of the five valid number options:
    if function == 1 or 2 or 3 or 4 or 5:
        #If the user chose option 1:
        if function == 1:
            #Run the Saving Goal Function:
            savingGoal()
        #If the user chose option 2:
        if function == 2:
            #Run the compound interest calculator function:
            compoundInterest()
        #If the user chose option 3:
        if function == 3:
            #Run the budget allocator function:
            budgetAllocator()
        #If the user chose option 4:
        if function == 4:
            #Run the sale price calculator function:
            salePrice()
        #If the user chose option 5:
        if function == 5:
            #Run the tip calculator function:
            tipCalculator()
    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()
    #Keep the program running once the user's desired function has been completed:
    main()

#Start running the program:
main()
