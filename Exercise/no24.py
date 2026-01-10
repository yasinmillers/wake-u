#Check whether two strings are anagrams
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1.lower()) == sorted(str2.lower()):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")