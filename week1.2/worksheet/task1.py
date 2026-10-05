# Worksheet 1.2: Task 1 Solution
import sys

grade = input("Enter your grade (0 - 100)")

grade_is_int = True

try :
    grade_int = int(grade)
except :
    grade_is_int = False

if grade_int < 0 or grade_int > 100 or grade_is_int == False:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade_int < 40:
    grade_str = "Fail"
elif grade_int < 70 :
    grade_str = "Pass"
else :
    grade_str = "Distinction"

print(f"{grade_int} is a {grade_str}")