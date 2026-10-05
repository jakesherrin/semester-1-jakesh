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

if len(float_values) == 0:
    sys.exit("Error: no numbers provided")

try :
    float_values_length = len(float_values)
    print(f"The average is {sum(float_values) / float_values_length}")
    print(f"The maxium is {max(float_values)}")
    print(f"The minimum is {min(float_values)}")

    # Finds the medium without branching by finding the midpoint value of the sorted and reversed sorted list
    midpoint = float_values_length // 2
    median = (sorted(float_values)[midpoint] + list(reversed(sorted(float_values)))[midpoint]) / 2

    print(f"The median is {median}")
except :
    sys.exit("Error: no numbers provided")
