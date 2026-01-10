#Count even and odd numbers in list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)