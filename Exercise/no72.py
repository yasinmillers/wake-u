#Grade system based on marks
while True:
    try:                                                    
        marks = float(input("Enter marks: "))
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        elif marks >= 0:
            grade = "F"
        else:
            grade = "invalid marks"
        print("Grade:", grade)  
    except ValueError:
        print("Please enter a valid number for marks.") 