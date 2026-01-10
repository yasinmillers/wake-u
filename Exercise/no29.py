#Find number of occurrences of a substring
s = input("Enter a string: ")
substring = input("Enter a substring: ")
count = 0
start = 0
while True:
    pos = s.find(substring, start)
    if pos != -1:
        count += 1
        start = pos + 1
    else:
        break
print("Number of occurrences:", count)  