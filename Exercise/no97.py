'''The RPG Stat Multiplier (High-Order Functions)
Definition: A game engine that doubles or triples player stats based on a "Power-Up."
Task: Create a function power_up(n) that returns a lambda function. The returned
lambda should take a stat value and multiply it by n. (e.g., double = power_up(2), then
double(10) should give 20).'''
def power_up(n):
    return lambda stat: stat * n        
# User input
multiplier = int(input("Enter the power-up multiplier (e.g., 2 for double, 3 for triple): "))
stat_value = int(input("Enter the player's stat value: "))
# Get the power-up function
power_up_function = power_up(multiplier)
# Calculate the new stat value
new_stat_value = power_up_function(stat_value)
print(f"New stat value after power-up: {new_stat_value}")       