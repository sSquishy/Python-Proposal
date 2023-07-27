import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry('1000x600')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333', padx=50, pady=50)

# Creating widgets
login_label = tkinter.Label(frame, text="Hello Student!", bg='#333333', fg="#ffffff", font=("Arial", 30))

# Function to handle placeholder text behavior for the username entry field
def on_username_click(event):
    if username_entry.get() == "Fullname":
        username_entry.delete(0, "end")
        username_entry.config(fg="#ffffff")

def on_username_exit(event):
    if username_entry.get() == "":
        username_entry.insert(0, "Fullname")
        username_entry.config(fg="#b3b3b3")

# Username Entry Field
username_entry = tkinter.Entry(frame, bg='#333333', fg="#b3b3b3", font=("Arial", 16))
username_entry.insert(0, "Fullname")
username_entry.bind("<FocusIn>", on_username_click)
username_entry.bind("<FocusOut>", on_username_exit)

# Password Entry Field
password_entry = tkinter.Entry(frame, show="*", bg='#333333', fg="#ffffff", font=("Arial", 16))
password_entry.insert(0, "Student Number")

login_button = tkinter.Button(frame, text="Login", bg="#771e1e", fg="#FFFFFF", font=("Arial", 16))

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_entry.grid(row=1, column=1, pady=20)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack(padx=50, pady=50)

window.mainloop()
