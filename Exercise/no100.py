'''The "Eco-tax" Calculator (Lambda & Dictionaries)
• Definition: A shipping company that adds a "carbon tax" based on the weight of a
package and the vehicle type.
• Task: 1. Create a dictionary called vehicles where keys are types (e.g., "Electric", "Gas")
and values are their tax multipliers (e.g., 1.0, 1.5).
2. Write a lambda function that takes weight and vehicle_type as inputs.
3. The lambda should look up the multiplier in the dictionary and return weight * times .
4. Bonus: If the vehicle type isn't in the dictionary, use the .get() method to provide a
default multiplier of 2.0.'''
 
# Get vehicle types and multipliers from the user
vehicles = {}
n = int(input("How many vehicle types do you want to enter? "))

for _ in range(n):
    vehicle = input("Enter vehicle type: ").strip()
    multiplier = float(input(f"Enter tax multiplier for {vehicle}: "))
    vehicles[vehicle] = multiplier

# Lambda function to calculate eco-tax
eco_tax = lambda weight, vehicle_type: weight * vehicles.get(vehicle_type, 2.0)

# Example usage
weight = float(input("Enter package weight: "))
vehicle_type = input("Enter vehicle type: ").strip()

print("Eco-tax:", eco_tax(weight, vehicle_type))


        











'''
# 1. Vehicle tax multipliers
vehicles = {
    "Electric": 1.0,
    "Gas": 1.5
}

# 2. Lambda function: takes weight and vehicle_type
# 3. Looks up multiplier and returns weight * multiplier
eco_tax = lambda weight, vehicle_type: weight * vehicles.get(vehicle_type, 2.0)

# Example usage
weight = 10
vehicle_type = "Electric"
print("Eco-tax:", eco_tax(weight, vehicle_type))  # 10.0

vehicle_type = "Gas"
print("Eco-tax:", eco_tax(weight, vehicle_type))  # 15.0

vehicle_type = "Diesel"  # not in dictionary
print("Eco-tax:", eco_tax(weight, vehicle_type))  # 20.0 (default)
'''
