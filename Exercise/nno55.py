#Convert tuple of digits into a number
t = (1, 2, 3, 4, 5)
number=0
for digit in t:
    number = number * 10 + digit
print("Number:", number)