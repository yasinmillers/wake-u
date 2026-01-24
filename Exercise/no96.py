'''The Digital Thermostat (Void Functions)
Definition: A system that triggers a physical action (simulated) without returning a value.'''
def set_thermostat(temperature):
    if temperature < 60:
        action = "Heating On"
    elif temperature > 75:
        action = "Cooling On"
    else:
        action = "Thermostat is Optimal"

    print(f"Thermostat set to {temperature}°F. {action}.")  
# User input
temp_input = input("Enter desired temperature (°F): ")  