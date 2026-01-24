''''''


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
