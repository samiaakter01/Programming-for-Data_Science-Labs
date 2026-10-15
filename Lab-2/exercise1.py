# Problem 1 – Course Marks. 
# Create a list containing the marks of five courses. 
# Display the total, average, highest mark, and lowest mark. 
# Count the number of passed courses, using 50 as the pass mark.

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


print("Total marks:", total)
print("Average mark:", average)
print("Highest mark:", maximum)
print("Lowest mark:", minimum)
print("Number of courses passed:", passed_count)
