# Create a function that accepts two parameters (width, height). If only one
# parameter is provided, use a default parameter value to treat it as a square.
def rectangle_area(width, height=None):
    if height is None:
        height = width
    return width * height

# Get user input
values = input("Enter width and optionally height (separated by space): ").split()

width = float(values[0])

if len(values) > 1:
    height = float(values[1])
    print("Area:", rectangle_area(width, height))
else:
    print("Area:", rectangle_area(width))