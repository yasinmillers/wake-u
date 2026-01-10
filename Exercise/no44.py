#Replace all negative numbers with zero
numbers = [1, -2, 3, -4, 5]
numbers = [num if num >= 0 else 0 for num in numbers]
print("Numbers after replacing negatives with zeros:", numbers)