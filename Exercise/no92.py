"""The Coffee Shop Loyalty Bot (Ternary & Assignment)
Definition: A POS system that applies discounts to "Gold Member" customers.
Task: Use a ternary operator to calculate a final_price. If the variable is_member is True,
subtract 15% from the bill_total; otherwise, keep the bill_total as is. Print the result
formatted to 2 decimal places."""


bill_total = float(input("Enter the bill total: "))
is_member = input("Is the customer a Gold Member? (yes/no): ").strip().lower() == 'yes'
final_price = bill_total * 0.85 if is_member else bill_total
print(f"Final Price: ${final_price:.2f}")   