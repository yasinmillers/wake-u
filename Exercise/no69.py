#Find highest scoring student
n=int(input("Enter number of students: "))
student_marks = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    student_marks[name] = marks
highest_student = max(student_marks, key=student_marks.get)
print("Highest Scoring Student:", highest_student)
print("With highest of Marks:", student_marks[highest_student])
