import tkinter as tk
import random
import string

def generate_password(length):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = lowercase_chars + uppercase_chars + digits + special_chars

    length = max(length, 6)

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_button_click():
    try:
        password_length = int(entry_length.get())
        password = generate_password(password_length)
        result_label.config(text=f"Generated Password:\n{password}", wraplength=500)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number for password length.")

# Create the main window with increased size
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")  # Width x Height

# Password length label and entry field
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

entry_length = tk.Entry(root)
entry_length.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack()

# Result label
result_label = tk.Label(root, text="", wraplength=500, justify="center", font=("Arial", 12))
result_label.pack()

# Start the GUI main loop
root.mainloop()
