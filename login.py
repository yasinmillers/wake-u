import tkinter as tk
from tkinter import messagebox

# Dummy user credentials
USER_CREDENTIALS = {
    "admin": "12345",
    "user": "password"
}

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("800x600")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

# Password label and entry
tk.Label(root, text="Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=40)

# Run the GUI
root.mainloop()
