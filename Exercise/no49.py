#Check whether an element exists in tuple
t = (1, 2, 3, 4, 5)
element = int(input("Enter an element to check: "))
if element in t:
    print("Element exists in tuple")
else:
    print("Element does not exist in tuple")