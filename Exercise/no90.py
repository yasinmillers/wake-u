#The Cyberpunk Bounty Hunter (Lambda & Sorting)
Definition: A futuristic bounty board needs to be sorted by risk level.
Task: You have a list of tuples representing bounties: [("Cyber-Thief", 500), ("Data-Ghost",
1200), ("Neon-Raider", 800)]. Write a lambda function to sort this list by the reward
amount (the second element in the tuple) in descending order.
bounties = [("Cyber-Thief", 500), ("Data-Ghost", 1200), ("Neon-Raider", 800)]
sorted_bounties = sorted(bounties, key=lambda x: x[1], reverse=True)
print(sorted_bounties) # Output: [('Data-Ghost', 1200), ('Neon-Raider', 800), ('Cyber-Thief', 500)]
