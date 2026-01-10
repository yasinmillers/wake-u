#Check whether a string is palindrome
s = input("Enter a string: ")
reversed_string = ""
for char in s:
    reversed_string = char + reversed_string
if s == reversed_string:
    print("Palindrome")
else:
    print("Not Palindrome") 