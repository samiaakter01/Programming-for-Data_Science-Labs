# Problem 7 – Student Record Analyzer. 
# Using the student records above, display each student’s name and marks. 
# Count the students who passed (marks ≥50), calculate the class average, 
# and identify the student with the highest mark.


students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

total = 0
passed_count = 0
highest_mark = students[0]["marks"]
highest_student = students[0]["name"]


for student in students:

    
    print("Student name:", student["name"])
    print("Student marks:", student["marks"])


    total = total + student["marks"]

    
    if student["marks"] >= 50:
        passed_count = passed_count + 1


    if student["marks"] > highest_mark:
        highest_mark = student["marks"]
        highest_student = student["name"]


average = total / len(students)


print("Total marks:", total)
print("Class average:", average)
print("Number of students passed:", passed_count)
print("Highest mark:", highest_mark)
print("Student with the highest mark:", highest_student)
