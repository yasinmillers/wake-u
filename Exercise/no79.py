#Lambda with map() to square list elements
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)