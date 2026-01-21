#Count frequency of characters using dictionary
text = "hello"
freq_dict = {}
for char in text:
    freq_dict[char] = freq_dict.get(char, 0) + 1
print("Frequency dictionary:", freq_dict)