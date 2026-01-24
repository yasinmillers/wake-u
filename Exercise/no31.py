#Find sum of list elements
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]     
total = sum(numbers)
print("Sum of list elements:", total)