#ATM withdrawal logic
balance = 100000
amount = float(input("Enter withdrawal amount: "))
if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient funds")
else:
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)