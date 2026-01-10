#Rotate list by k positions
numbers = [1, 2, 3, 4, 5]
k = 2
rotated_numbers = numbers[k:] + numbers[:k]
print("Rotated list:", rotated_numbers)