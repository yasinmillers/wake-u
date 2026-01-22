# Electricity bill calculation
units = float(input("Enter number of units consumed in ugandan settings : "))
if units < 0:
    print("Invalid input")
            
fixed_charge = 5000
bill=0
if units <= 100:
    bill = units * 600
elif units <= 200:
    bill = 100 * 600 + (units - 100) * 750
else:
    bill = 100 * 600 + 100 * 750 + (units - 200) * 1000

print("Electricity Bill:", bill + fixed_charge)