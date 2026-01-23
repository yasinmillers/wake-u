'''The Alchemist’s Ingredient Filter (Lambda & Filter)
Definition: A potion-making script that removes "toxic" ingredients from a list.
Task: Given a list of ingredient names, use the filter() function and a lambda to create a
new list containing only ingredients that have more than 5 letters.'''

ingredients = ["eye of newt", "bat wing", "mandrake root", "unicorn hair", "dragon scale"]
filtered_ingredients = list(filter(lambda x: len(x) > 5, ingredients))
print(filtered_ingredients)  # Output: ['mandrake root', 'unicorn hair', 'dragon scale']            
