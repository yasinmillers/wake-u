#Convert tuple of digits into a number
t = (1, 2, 3, 4, 5)
number = int(''.join(map(str, t)))
print("Number:", number)    