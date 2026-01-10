#Convert string to title case
s = input("Enter a string: ")
title_case = ""
words = s.split()
for word in words:
    title_case += word.capitalize() + " "
print("Title case:", title_case.strip())