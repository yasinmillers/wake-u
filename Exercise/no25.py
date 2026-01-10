# Remove duplicate characters from string
s = input("Enter a string: ")
unique_chars = ""
for char in s:
    if char not in unique_chars:
        unique_chars += char
print("String with duplicates removed:", unique_chars)