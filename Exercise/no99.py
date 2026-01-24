'''The "Time Traveler" Validator (Type Checking & Ternary)
• Definition: A control panel for a time machine that only accepts specific "Chronal
Coordinates."
• Task: Write a function launch_machine(year).
1. First, use type(year) to check if the input is an integer. If it is a string or float,
return "Error: Coordinate Type Mismatch."
2. If the type is correct, use a ternary operator to return "Heading to the Future" if
year > 2026, and "Heading to the Past" if year < 2026.'''

def launch_machine(year):
    if type(year) is not int:
        return "Error: Coordinate Type Mismatch."
    
    return "Heading to the Future" if year > 2026 else "Heading to the Past"    


# User input
year_input = input("Enter the Chronal Coordinate (year): ") 
# Convert year safely
if year_input.isdigit():
    year = int(year_input)
else:
    try:
        year = float(year_input)
    except ValueError:
        year = year_input  # keeps it non-int to trigger type check
# Call function
result = launch_machine(year)
print(result)   