#Check whether list is palindrome
numbers = [1, 2, 3, 2, 1]
is_palindrome = numbers == numbers[::-1]
print("Is palindrome:", is_palindrome)