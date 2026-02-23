numbers = [1, 2, 3, 4, 5]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[-2])
else:
    print("Not enough unique numbers")