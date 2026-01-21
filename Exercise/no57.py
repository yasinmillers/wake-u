#Count frequency of characters using dictionary
text = input("Enter a string: ")
freq_dict = {}
for char in text:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
        
print("Character frequency dictionary:", freq_dict)