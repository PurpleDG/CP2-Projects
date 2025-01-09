#Evan McCabe Financial Calculator

import time

#Introduction to the user:
print("\nHello! I am a financial calculator.")

def savingGoal():
    weekOrMonth = int(input("\nWeekly or monthly deposit? (1 = weekly, 2 = month)\n"))

    if weekOrMonth == 1 or 2:
        print("")
    else:
        print("\nINVALID INPUT\n\nPlease try again.")
        savingGoal()

    goalCost = float(input("How much does your goal item cost? (whole number or decimal number)\n"))

    if weekOrMonth == 1:
        deposit = float(input("\nWhat is your weekly deposit? (whole number or decimal number)\n"))
        timeTaken = str(int(goalCost / deposit))
        print("It will take around " + timeTaken + " weeks for you to reach your goal.")
        time.sleep(3)
        main()


    if weekOrMonth == 2:
        deposit = float(input("\nWhat is your monthly deposit? (whole number or decimal number)\n"))
        timeTaken = str(int(goalCost / deposit))
        print("It will take around " + timeTaken + " months for you to reach your goal.")
        time.sleep(3)
        main()

#The main function that runs the program:
def main():
    #Ask the user what function they would like the calculator to perform:
    print("\nWhat function would you like me to perform?")
    #Tell the user what their options are on the calculator:
    function = int(input("1: Saving Goal Calculator\n2: Coumpound Interest Calculator\n3: Budget Allocator\n4: Sale Price Calculator\n5: Tip Calculator\n"))
   
    if function == 1 or 2 or 3 or 4 or 5:
        if function == 1:
            savingGoal()
        if function == 2:
            coumpoundInterest()
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