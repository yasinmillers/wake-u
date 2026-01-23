#Lambda with reduce() to find sum of list elements
from functools import reduce
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)    