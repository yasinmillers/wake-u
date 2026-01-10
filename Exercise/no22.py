#Replace spaces with underscores in a string
s = input("Enter a string: ")
modified_string = ""
for char in s:
    if char == " ":
        modified_string += "_"
    else:
        modified_string += char
print("Modified string:", modified_string)