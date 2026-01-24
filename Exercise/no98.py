'''The "Ghost" Guest List (Sets & Logic)
Definition: A security check to see who attended a party but wasn't on the original invite
list.
Task: You have two lists: invited_guests and actual_attendees. Convert both to Sets and
use set subtraction to find the "Crashers" (people who attended but weren't invited).'''

def find_crashers(invited_guests, actual_attendees):
    invited_set = set(invited_guests)
    attendees_set = set(actual_attendees)
    crashers = attendees_set - invited_set
    return crashers     
# User input
invited_input = input("Enter the invited guests (comma-separated): ")
actual_input = input("Enter the actual attendees (comma-separated): ")
# Convert input strings to lists
invited_guests = [guest.strip() for guest in invited_input.split(",")]
actual_attendees = [attendee.strip() for attendee in actual_input.split(",")]
# Find crashers
crashers = find_crashers(invited_guests, actual_attendees)
if crashers:
    print("Crashers detected:", ", ".join(crashers))
else:
    print("No crashers detected.")  
    
