'''The "Ghost" Guest List (Sets & Logic)
Definition: A security check to see who attended a party but wasn't on the original invite
list.
Task: You have two lists: invited_guests and actual_attendees. Convert both to Sets and
use set subtraction to find the "Crashers" (people who attended but weren't invited).'''

# Get invited guests from user
invited_guests = input("Enter invited guests (separate names with commas): ").split(",")

# Get actual attendees from user
actual_attendees = input("Enter actual attendees (separate names with commas): ").split(",")

# Convert to sets (strip spaces to avoid errors)
invited_set = {name.strip() for name in invited_guests}
attendees_set = {name.strip() for name in actual_attendees}

# Find crashers using set subtraction
crashers = attendees_set - invited_set

print("Crashers:", crashers)

