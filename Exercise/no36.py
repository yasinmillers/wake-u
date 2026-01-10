#Sort a list without using sort()
numbers = [5, 2, 8, 1, 9]
sorted_numbers = []
while numbers:
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    sorted_numbers.append(min_val)
    numbers.remove(min_val)
print("Sorted list:", sorted_numbers)