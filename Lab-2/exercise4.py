# Problem 4 – Grade Calculator. 
# Write a function named calculate_grade(marks) that receives a 
# list of marks, calculates the average, and returns the corresponding grade.
# Average Grade
# 80 or higher A
# 70 to below 80 B
# 60 to below 70 C
# 50 to below 60 D
# Below 50 F
# Call the function using a list of five marks.



def calculate_grade(marks):

    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)


    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    
    return grade



marks = [75, 82, 68, 91, 55]

grade = calculate_grade(marks)


print("Marks:", marks)
print("Grade:", grade)
