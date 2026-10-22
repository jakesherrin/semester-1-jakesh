# Worksheet 1.3: Task 3

# Your code for the overall grade classification
grade_equivolent = {"F": 40, "3": 50, "2:2": 60, "2:1": 70, "1": 100}
student_grades = []

# ask for filename of the student file
file_name = input("Which student file would you like to open?")
# open the file
with open(str('/workspaces/semester-1-jakesh/week1.3/worksheet/task3/' + file_name +".csv"), 'r') as student_file :
    # read in the data, and for each student calculate their average grade and classification
    for line in student_file :
        if line[:10] != "student_id" :
            scores = [int(score) for score in line if score.isdigit() == True]
            average = sum(scores) / len(scores)

            for grade, upper_bound in grade_equivolent.items() :
                if average <= upper_bound :
                    classification = grade

            student_grades.append((line[:5], average, classification))

student_file.close()

print(student_grades)

    # write out this calculated data in the format without a header:
    #      student_id,average_grade,classification - replace this with actual value
    #      The average grade should be given to 2 decimal places
    #      this can be achieved by using the following in an fstring: {variable_name:.2f}
with open('/workspaces/semester-1-jakesh/week1.3/worksheet/task3/' + file_name +"_out.csv", "a") as out_file :
    for entry in student_grades :
        out_file.write(f"{entry[0]},{entry[1]:.2f},{entry[2]}\n")

    

    # write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

    # You can compare your output files with the 4 example files in example_outfiles folder