#Create student marks dictionary and find average
n=int(input("Enter number of subjects: "))
student_marks = {}
total=0
for i in range(n):
    name = input("Enter subject name: ")
    marks = float(input("Enter subject marks: "))
    student_marks[name] = marks 
    total += marks
average = total / n 
print("Student Marks Dictionary:", student_marks)
print("Average Marks:", average)