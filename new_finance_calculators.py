
# import the math module at the beninning of the code to access math functions          
import math

# create menu options using triple quatation marks to inform the user 
menu = """
investment - to calculate the amonut of interest you'll earn on the investment
bond - to calculate the amount you'll have to pay on a home loan
"""
print(menu)

# request choice from user and use the lowewr function to get the answer in lower case letters
# to manage any possible invalid input
choice = input("Enter either 'investment' or 'bond' from the menu presented to start : ").lower()
print(f"You have selected {choice}!")

if choice == 'investment':

    deposit = float(input("Please enter the amonut you would like to deposit : "))
    # the input is divided by 100 to change it to a decimal number
    interest = float(input("Please enter the rate of interest (exclude the % symbol) : ")) / 100
    years = int(input("Please enter the years for your investment : "))
    calculation_answer = input("Please select either 'simple' or 'compound' interest :").lower()

    if calculation_answer == 'simple':
        simple = deposit * (1 + interest * years)
        # to round the calculation number to two decimel places
        simple_rounded = round(simple, 2)
        print(f"The total amount when simple interest is applied is £{simple_rounded}.")

    elif calculation_answer == 'compound':
        compound_interest = deposit * math.pow((1 + interest), years)
        compound_rounded = round(compound_interest, 2)
        print(f"The total amount when compound interest is applied is £{compound_rounded}.")

elif choice == 'bond':
    house_value = float(input("Please enter the present value of your house : "))
    # the input is divided by 100 to change it to a decimal number
    # then the value is divided by the number 12 (number of months in a year)
    bond_interest = (float(input(("Please enter the rate of interest (exclude the % symbol) : "))) /100) / 12
    months = int(input("Please enter the number of months over which the bond will be repaid "))
    repayment_bond = (bond_interest * house_value) / (1 - (1 + bond_interest) ** (- months))
    bond_rounded = round(repayment_bond, 2)
    print(f"The total amount to be repaid is £{bond_rounded}.")
    
else:
    print("We have entered a wrong option. Please try again!")
    print(menu)
    choice = input("Enter either 'investment' or 'bond' from the menu presented to start : ").lower()
    