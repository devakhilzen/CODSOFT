import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity):
    characters = ''
    if 'uppercase' in complexity:
        characters += string.ascii_uppercase
    if 'lowercase' in complexity:
        characters += string.ascii_lowercase
    if 'digits' in complexity:
        characters += string.digits
    if 'symbols' in complexity:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    if len(password) >= 5 and len(password) <= 12:
        strength = "Strong"
    else:
        strength = "Weak"

    return password, strength

def generate_button_clicked():
    length = int(length_entry.get())
    complexity = []
    if uppercase_var.get():
        complexity.append('uppercase')
    if lowercase_var.get():
        complexity.append('lowercase')
    if digits_var.get():
        complexity.append('digits')
    if symbols_var.get():
        complexity.append('symbols')

    password, strength = generate_password(length, complexity)
    if password:
         password_font = ("Georgia", 14, "bold")  
         strength_font = ("Georgia", 10)  
         result_label.config(text=f"{password}", font=password_font)
         strength_label.config(text=f"Strength: {strength}", font=strength_font)



window = tk.Tk()
window.configure(bg="#DE3163")
window.title("Password Generator")
window.geometry("400x300")  


font_style = ("Georgia", 10)
internal_padding = 5

length_label = tk.Label(window, text="Password Length :", font=font_style,bg="#DFFF00")
length_label.pack(padx=internal_padding, pady=internal_padding)
length_entry = tk.Entry(window, font=font_style,bg="#9FE2BF",width=5)
length_entry.pack(ipadx=internal_padding, ipady=internal_padding)

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Upper case", variable=uppercase_var, font=font_style,bg="#40E0D0")
uppercase_check.pack(padx=internal_padding, pady=internal_padding)

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(window, text="Lower case", variable=lowercase_var, font=font_style,bg="#40E0D0")
lowercase_check.pack(padx=internal_padding, pady=internal_padding)

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(window, text="Digits", variable=digits_var, font=font_style,bg="#40E0D0")
digits_check.pack(padx=internal_padding, pady=internal_padding)

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(window, text="Symbols", variable=symbols_var, font=font_style,bg="#40E0D0")
symbols_check.pack(padx=internal_padding, pady=internal_padding)

generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked, font=("Georgia",12),bg="#32CD32")
generate_button.pack(padx=internal_padding, pady=internal_padding)

result_label = tk.Label(window, text="", font=("Times New Roman",10))
result_label.pack(padx=internal_padding, pady=internal_padding)

strength_label = tk.Label(window, font=font_style, padx=internal_padding,bg="#40E0D0")
strength_label.pack()

window.mainloop()
