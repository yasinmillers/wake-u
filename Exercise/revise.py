numbers = []

# Take at least 5 inputs
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find min and max
minimum = min(numbers)
maximum = max(numbers)
even_count=0
odd_count=0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1  

print("List:", numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)