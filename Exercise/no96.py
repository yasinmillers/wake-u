'''The Digital Thermostat (Void Functions)
Definition: A system that triggers a physical action (simulated) without returning a value.'''


def digital_thermostat(temperature):
    if temperature > 30:
        print("🔥 Cooling system activated")
    elif temperature < 18:
        print("❄️ Heating system activated")
    else:
        print("✅ Temperature is stable")


# User input
temp = int(input("Enter current temperature: "))

# Call the void function
digital_thermostat(temp)
