# =====================================
# |         IMPORT LIBRARIES          |
# =====================================

import tkinter as tk
from tkinter import messagebox

# ======================================
# |     PASSWORD ANALYSIS FUNCTION     |
# ======================================

def check_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Please Enter a Password.")
        return
    
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-+_+{}[]|/,.`~;:'?<>" for c in password)

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    if score <= 2:
        strength = "WEAK🔴"
        color = "red"
        suggestion = (
            "• Use at least 8 characters.\n"
            "• Add uppercase characters.\n"
            "• Add lowercase characters.\n"
            "• Add numbers.\n"
            "• Add special characters."
        )

    elif score <= 4:
        strength = "Medium🟠"
        color = "dark orange"
        suggestion = (
            "✔ Good password.\n"
            "✔ Add a number to make it stronger."
        )

    else:
        strength = "Strong🟢"
        color = "green"
        suggestion = (
    "✔ Excellent!\n"
    "✔ Your password is strong.\n"
    "✔ It follows recommended security practices."
)
        
    result_label.config(
        text = f"""Password Analysis
Length              : {length}
Uppercase           : {'Yes' if has_upper else 'No'}
Lowercase           : {'Yes' if has_lower else 'No'}
Numbers             : {'Yes' if has_digit else 'No'}
Special Characters  : {'Yes' if has_special else 'No'}

Password Strength   : {strength}

Suggestions         : {suggestion}
""",
        fg = color
    )

# ======================================
# |         CLEAR FUNCTION             |
# ======================================

def clear_all():
    password_entry.delete(0, tk.END)
    result_label.config(text = "", fg = "black")

# ======================================
# |        SHOW / HIDE PASSWORD        |
# ======================================

def toggle_password():
    if show_password.get():
        password_entry.config(show = "")
    else:
        password_entry.config(show = "*")


# ======================================
# |         CREATE MAIN WINDOW         |
# ======================================

window = tk.Tk()
window.title("Password Strength Analyzer CyberSecurity Mini Project")
window.geometry("700x610")
window.configure(bg = "#F1F1CC")
window.resizable(False, False)

# =====================================
# |            TITLE LABEL            |
# ===================================== 

title = tk.Label(
    window,
    text = "🔒 Password Strength Analyzer CyberSecurity Mini Project",
    font = ("Arial", 18, "bold"),
    bg = "#04cdbc",
    fg = "darkblue"
)
title.pack(pady = 20)

# ======================================
# |        PASSWORD INPUT SECTION      |
# ======================================

label = tk.Label(
    window,
    text = "Enter Password: ",
    font = ("Arial", 12, "bold"),
    bg = "#EAF4FC"
)

label.pack()

password_entry = tk.Entry(
    window,
    show = "*",
    width = 30, 
    font = ("Arial", 12)
)

password_entry.pack(pady = 10)

# =======================================
# |       SHOW PASSWORD CHECKBOX        |
# =======================================

show_password = tk.BooleanVar()

show_check = tk.Checkbutton(
    window,
    text = "Show Password",
    variable  = show_password,
    command = toggle_password,
    bg = "#1B7ECF",
    font = ("Arial", 11)
)

show_check.pack()

# =======================================
# |        BUTTON SECTION               |
# =======================================

button_frame = tk.Frame(
    window,
    bg = "#571ACA"
    )
button_frame.pack(pady = 15)

analyze_button = tk.Button(
    button_frame,
    text = "Analyze Password",
    command = check_password,
    font = ("Arial", 12, "bold"),
    bg = "#0078D7",
    fg = "white",
    width = 18
)
analyze_button.grid(row = 0, column = 0, padx = 10)

clear_button = tk.Button(
    button_frame,
    text = "Clear",
    command = clear_all,
    font = ("Arial", 12, "bold"),
    bg = "#DC3545",
    fg = "white",
    width = 10
)
clear_button.grid(row = 0, column = 1, padx = 10)

# =======================================
# |        RESULT DISPLAY SECTION       |
# =======================================

result_title = tk.Label(
    window,
    text = "Analysis Result",
    font = ("Arial", 14, "bold"),
    bg = "#d9f99d",
    fg = "#003366"
)

result_title.pack(pady = (20, 5))

result_label = tk.Label(
    window,
    text = "Enter a password and click 'Analyze Password'",
    font = ("Consolas", 11),
    bg = "white",
    fg = "black",
    justify = "left",
    anchor = "nw",
    relief = "solid",
    bd = 1,
    width = 58,
    height = 14,
    padx = 10,
    pady = 10
)

result_label.pack(pady = 10)

# =======================================
# |             FOOTER                  |
# =======================================

footer = tk.Label(
    window,
    text = "CyberSecurity Mini Project | Python + Tkinter",
    font = ("Arial", 9),
    bg = "white",
    fg = "gray"
)

footer.pack(side ="bottom", pady = 10)

# =======================================
# |         START APPLICATION           |
# =======================================

window.mainloop()
