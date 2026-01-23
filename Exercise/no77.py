#Function to count vowels in string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
string = input("Enter a string: ")
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)