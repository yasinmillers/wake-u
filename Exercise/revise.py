numbers = []

# Take at least 5 inputs
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find min and max
minimum = min(numbers)
maximum = max(numbers)

print("List:", numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)