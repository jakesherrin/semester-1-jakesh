"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

# Function that takes in a value and returns the interager form of that value if its interager, returning False otherwise
def is_interager (value) :
    # Attemps to cast the functions input to interager and returns false if an error occurs
    try :
        value = int(value)
    except ValueError:
         return False
    
    return value

# Gets the users name and welcomes the user
name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

# Sets savings initially as a string to begin the loop
savings_amount = "temp"

# Repeats until an appropriate value is entered
while type(savings_amount) != int or savings_amount < 0 :
    savings_amount = input("How much do you want to save each month?")

    # Checks that the data type and size of savings_amount is valid - making it False otherwise
    savings_amount = is_interager (savings_amount)
    if savings_amount < 0 :
        savings_amount = False

    if savings_amount == False :
        print("*** Warning: Savings amount must be a positive whole number ***")


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
print(f"You will have saved £{savings_amount * 12} by the end of this year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
annual_savings = (savings_amount * 12) + (savings_amount * 12 * (0.8/100))
print(f"With interest you will have saved £{(annual_savings):.2f} (assuming 0.8% interest) {name}!")
