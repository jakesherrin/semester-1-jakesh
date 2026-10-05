# Worksheet 1.2: Task 2 Solution
import sys

def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

float_values = read_numbers()

try :
    float_values_length = len(float_values)
    print(f"The average is {sum(float_values) / float_values_length}")
    print(f"The maxium is {max(float_values)}")
    print(f"The minimum is {min(float_values)}")
    print(f"The median is {sorted(float_values)[float_values_length // 2]}")
except :
    sys.exit("Error: no numbers provided")
