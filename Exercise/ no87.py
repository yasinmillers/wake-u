#Take a Celsius value. Use a ternary operator within a print statement to label it
#"Boiling" if it’s <100, and "Normal" otherwise
celsius = float(input("Enter temperature in Celsius: "))
print("Boiling") if celsius < 100 else print("Normal")  