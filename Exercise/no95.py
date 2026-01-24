'''he Movie Age-Gate (Nested Logic & Types)
Definition: A cinema booking system that checks both age and ticket type.
Task: Write a function book_ticket(age, ticket_type). If ticket_type is "R-Rated" and age <
18, return "Denied". If the age input is not an integer, use type() to detect it and return
"Invalid Input Type".'''

def book_ticket(age, ticket_type):
    if type(age) is not int:
        return "Invalid Input Type"

    if ticket_type == "R-Rated" and age < 18:
        return "Denied"

    return "Booking Successful"


# User input
age_input = input("Enter your age: ")
ticket_type = input("Enter ticket type (Regular / R-Rated): ")

# Convert age safely
if age_input.isdigit():
    age = int(age_input)
else:
    age = age_input  # keeps it non-int to trigger type check

# Call function
result = book_ticket(age, ticket_type)
print(result)
