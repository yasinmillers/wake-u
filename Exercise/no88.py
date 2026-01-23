#Write a single line of code using a ternary operator that assigns the string "Even" or
#"Odd" to a variable result based on a user's input number.
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(result)