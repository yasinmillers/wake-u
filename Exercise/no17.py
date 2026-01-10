#Reverse a string
s = input("Enter a string: ")
reversed_string = ""
for char in s:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)  