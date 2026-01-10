#Count frequency of each character in a string
s = input("Enter a string: ")
frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequencies:")
for char, freq in frequency.items():
    print(f"{char}: {freq}")