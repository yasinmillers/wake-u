#Lambda with filter() to get even numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)