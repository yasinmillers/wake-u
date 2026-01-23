#Given a day of the week (1-7), use a ternary operator to return "Rest" if the day is 6
#or 7, and "Work" for 1-5.
day = int(input("Enter a day of the week (1-7): "))
print("Rest") if day == 6 or day == 7 else print("Work")