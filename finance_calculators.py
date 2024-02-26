import math

#Print the menu and ask the user which calculation they would like to choose
#Check if decision matches menu options
#Depending on what input they choose from the menu, ask the user for the quantity of the necessary variables e.g. "How much money are you depositing?" needed to execute the relevant formula
#Use the user's input of these relevant variables to calculate their investment or bond
#Print the user's final amount

print("\ninvestment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan\n")
decision = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if decision == "investment":
    money_for_investment = input("How much money are you depositing?: ")
    interest_rate_investment = input("What is the interest rate? (please enter this value as a percentage): ")
    years_investment = input("How many years do you plan on investing?: ")
    interest = input("Do you want to use 'simple' or 'compound' interest?: ").lower()

    if interest == "simple":
        simple = float(money_for_investment) * (1 + (float(interest_rate_investment)/100) * float(years_investment))
        formatted_simple = f"{simple:.2f}"
        print(f"\nYour Simple Interest is: {formatted_simple}\n")
    elif interest == "compound":
        compound = float(money_for_investment) * math.pow((1 + (float(interest_rate_investment)/100)),float(years_investment))
        formatted_compound = f"{compound:.2f}"
        print(f"\nYour Compound Interest is: {formatted_compound}\n")
    
elif decision == "bond":
    money_for_bond = input("What is the present value of the house. e.g. 100000: ")
    interest_rate_bond = input("What is the interest rate? (please enter this value as a percentage): ")
    months_bond = input("How many months do you plan to take to repay the bond. e.g. 120: ")
    repayment = (((float(interest_rate_bond)/100)/12) * float(money_for_bond))/(1 - (1 + ((float(interest_rate_bond)/100)/12))**(-float(months_bond)))
    formatted_repayment = f"{repayment:.2f}"
    print(f"\nYou will have to repay {formatted_repayment} each month.\n")

else:
    print("\nERROR! You have not chosen an option from the MENU.\n")

