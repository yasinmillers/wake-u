'''The "Infinite" Grocery Cart (*args)
Definition: A checkout counter that doesn't know how many items a customer will buy.
Task: Define a function calculate_total(*items) that uses *args to accept any number of
price inputs. Inside the function, use a loop to sum them up and return the total.'''


def calculate_total(*items):
    total = 0
    for price in items:
        total += price
    return total        

total_price = calculate_total(5.99, 12.49, 3.50, 7.25)
print(f"Total Price: ${total_price:.2f}")         