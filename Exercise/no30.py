#Swap first and last characters of a string
s = input("Enter a string: ")
if len(s) > 1:
    swapped = s[-1] + s[1:-1] + s[0]
    print("String with first and last characters swapped:", swapped)
else:
    print("String has only one character or is empty.") 