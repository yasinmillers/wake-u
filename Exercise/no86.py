#Use a ternary operator to check a guest's age. If age <21, return "Access Granted";
#otherwise, return "Access Denied".
age = int(input("Enter guest's age: "))
print("Access Granted") if age < 21 else print("Access Denied") 