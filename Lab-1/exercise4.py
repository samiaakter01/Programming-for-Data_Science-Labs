# Problem 4. Input a student’s name and five course marks. 
# Calculate the total, average, highest mark, lowest mark, and number of passed courses. 
# Display all results. A mark of 50 or higher is considered a pass.



student_name = input("Enter student name: ")
programming_ds = float(input("Enter your Programming for Data Science mark: "))
data_visualization = float(input("Enter your Data Visualization mark: "))
data_processing = float(input("Enter your Data Processing mark: "))
data_science = float(input("Enter your Data Science mark: "))
java = float(input("Enter your Java mark: "))


marks = [programming_ds, data_visualization, data_processing, data_science, java]


total = 0
maximum = marks[0]
minimum = marks[0]
passed_count = 0


for mark in marks:
    
    total = total + mark

    average = total / len(marks)
   
    if mark > maximum:
        maximum = mark

    
    if mark < minimum:
        minimum = mark

    
    if mark >= 50:
        passed_count = passed_count + 1


print("Student Name:", student_name)
print("Total marks:", total)
print("Average mark:", average)
print("Highest mark:", maximum)
print("Lowest mark:", minimum)
print("Number of courses passed:", passed_count)
