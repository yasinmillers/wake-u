#Find all even numbers in tuple
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = tuple(x for x in t if x % 2 == 0)
print("Even numbers in tuple:", even_numbers)