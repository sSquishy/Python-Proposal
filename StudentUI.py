import sqlite3
from tkinter import *
from tkinter import messagebox

def open_student_window():
    global student_window

    student_window = Toplevel()
    student_window.title("Student Window")
    student_window.geometry('500x800')
    student_window.configure(bg='#333333')

    # Center the buttons horizontally and vertically in the window
    student_window.grid_rowconfigure(0, weight=1)
    student_window.grid_columnconfigure(0, weight=1)

    frame_buttons = Frame(student_window, bg='#333333')
    frame_buttons.pack(expand=True)

    # Create the "BORROW BOOK" button and associate it with the open_borrow_window function
    BORROWbutton = Button(frame_buttons,
                          text="BORROW BOOK",
                          bg='red',
                          fg='#FFFFFF',
                          font=("Arial", 16, "bold"),
                          width=20,
                          height=7,
                          anchor="center")  # Placeholder for open_borrow_window function
    BORROWbutton.grid(row=0, column=0, padx=5, pady=5)

    # Create the "RETURN BOOK" button and associate it with the open_return_window function
    RETURNbutton = Button(frame_buttons,
                          text="RETURN BOOK",
                          bg='red',
                          fg='#FFFFFF',
                          font=("Arial", 16, "bold"),
                          width=20,
                          height=7,
                          anchor="center")  # Placeholder for open_return_window function
    RETURNbutton.grid(row=1, column=0, padx=5, pady=5)

    # Create the "EXIT" button and associate it with the close_windows function
    EXITbutton = Button(frame_buttons,
                        text="EXIT",
                        bg='red',
                        fg='#FFFFFF',
                        font=("Arial", 16, "bold"),
                        width=20,
                        height=7,
                        anchor="center",
                        command=lambda: close_windows(student_window))
    EXITbutton.grid(row=2, column=0, padx=5, pady=5)

    student_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(student_window))

def close_windows(new_window, prev_window=None):
    new_window.destroy()
    if prev_window:
        prev_window.deiconify()





# Call the function to welcome the student
open_student_window()
