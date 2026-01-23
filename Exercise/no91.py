'''The "Smart Home" Mood Lighting (Ternary Operator)
Definition: An automated system that sets the house lighting based on the time of day.
Task: Create a variable hour (0–23). Use a ternary operator to assign the value "Warm
Orange" to a variable light_color if hour is between 18 and 22; otherwise, assign
"Daylight White"'''
hour = int(input("Enter the hour (0-23): "))
light_color = "Warm Orange" if 18 <= hour <= 22 else "Daylight White"
print(light_color)