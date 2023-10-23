import tkinter as tk
from tkinter import ttk
import re

def check_password_strength():
    password = password_entry.get()
    strength_label.config(text="")
    strength_bar["value"] = 0
    
    if len(password) == 0:
        return
    
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
    
    # Check uppercase, lowercase, numbers, and special characters
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*().,?":{}|<>]', password):
        score += 1
        
    strength_bar["value"] = (score / 4) * 100
    
    if score == 4:
        strength_label.config(text="Password is strong!", foreground="green")
    else:
        strength_label.config(text="Password is weak. Please make sure it includes uppercase, lowercase, numbers, and special characters.",
foreground="red")
        
# Create GUI Window
root = tk.Tk()
root.title("Password Strength Checker")

# Set width and length of the GUI window
window_width = 600
window_height = 250
root.geometry(f"{window_width}x{window_height}")

# Password entry
password_label = tk.Label(root, text="Enter your password:")
password_label.pack()
password_entry = tk.Entry(root, show="")
password_entry.pack()

# Password strength barS
strength_label = tk.Label(root, text="")
strength_label.pack()
strength_bar = ttk.Progressbar(root, length=200, mode="determinate")
strength_bar.pack()

# Check button
check_button = tk.Button(root, text="Check Password Strength", command=check_password_strength)
check_button.pack()

# Run the GUI loop
root.mainloop()