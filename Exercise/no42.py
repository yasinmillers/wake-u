#Find frequency of elements in list
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print("Frequency of elements:", frequency)