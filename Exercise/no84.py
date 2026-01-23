#Write a function that takes a username and a list of "Banned Users." Return True if
#the user is safe and False if they are banned, using the in keyword.
def is_user_safe(username, banned_users):
    return username not in banned_users


banned_users = input("Enter banned users separated by space: ").split()
username = input("Enter a username: ")
print(is_user_safe(username, banned_users))