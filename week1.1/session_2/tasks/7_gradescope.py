# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# multiply those numbers together
try :
    out = int(num1) * int(num2)
    # print out the result
    print(out)
except :
    print("That is not a number")
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!