# Find first non-repeating character in a string
s = input("Enter a string: ")
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1        
first_non_repeating = None
for char in s:
    if char_count[char] == 1:
        first_non_repeating = char
        break
if first_non_repeating is not None:
    print("First non-repeating character:", first_non_repeating)
else:
    print("No non-repeating character found.")