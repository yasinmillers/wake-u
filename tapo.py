x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)  # This will raise an error because tuples are immutable


print(x)
print(y)