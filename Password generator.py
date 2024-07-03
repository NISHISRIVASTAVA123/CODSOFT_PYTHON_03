import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    
    char= string.ascii_letters + string.digits
    valid_punctuation = "@#$^&*_"
   
    allowed_char = char + valid_punctuation
    
    
    password = ''.join(random.choices(allowed_char, k=length))

    
    return password

def generate_password_button():
    try:
        len = int(length_entry.get())
        if len <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return
        
        password = generate_password(len)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("460x360")
root.config(bg='pink')
root.resizable(False,False)


length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=(8, 0))

length_entry = tk.Entry(root, width=20)
length_entry.pack()


generate_btn = tk.Button(root, text="Generate Password", command=generate_password_button)
generate_btn.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=(10, 0))

password_entry = tk.Entry(root, textvariable=password_var, width=30, state='readonly')
password_entry.pack()


root.mainloop()
