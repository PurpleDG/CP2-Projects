#Evan McCabe Financial Calculator

import time

#Introduction to the user:
print("\nHello! I am a financial calculator.")

def savingGoal():
    weekOrMonth = input("\nWeekly or monthly deposit? (1 = weekly, 2 = month)\n")
    try:
        weekOrMonth = int(weekOrMonth)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        savingGoal()

    if weekOrMonth == 1 or 2:
        print("")
    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        savingGoal()

    goalCost = input("How much does your goal item cost? (whole number or decimal number)\n")
    try:
        goalCost = float(goalCost)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        savingGoal()


    if weekOrMonth == 1:
        deposit = input("\nWhat is your weekly deposit? (whole number or decimal number)\n")
        try:
            deposit = float(deposit)
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingGoal()

        timeTaken = str(int(goalCost / deposit))
        print("\nIt will take around " + timeTaken + " weeks for you to reach your goal.")
        time.sleep(3)
        main()


    if weekOrMonth == 2:
        deposit = input("\nWhat is your monthly deposit? (whole number or decimal number)\n")
        try:
            deposit = float(deposit)
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingGoal()

        timeTaken = str(int(goalCost / deposit))
        print("\nIt will take around " + timeTaken + " months for you to reach your goal.")
        time.sleep(3)
        main()

def compoundInterest():

    deposit = input("What is your monthly deposit? (whole number or decimal number)\n")
    try:
        deposit = float(deposit)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        compoundInterest()

    rate = input("What is the interest rate? (whole number or decimal number)\n")
    try:
        rate = float(rate)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        compoundInterest()

    years = 

    amount = deposit * ((1 + (rate / 12)) ** (12 * years))

#The main function that runs the program:
def main():
    #Ask the user what function they would like the calculator to perform:
    print("\nWhat function would you like me to perform?")
    #Tell the user what their options are on the calculator:
    function = input("1: Saving Goal Calculator\n2: Coumpound Interest Calculator\n3: Budget Allocator\n4: Sale Price Calculator\n5: Tip Calculator\n")
    try:
        function = int(function)
    except ValueError:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()

    if function == 1 or 2 or 3 or 4 or 5:
        if function == 1:
            savingGoal()
        if function == 2:
            compoundInterest()
        if function == 3:
            budgetAllocator()
        if function == 4:
            salePrice()
        if function == 5:
            tip()
    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        main()
    main()

main()