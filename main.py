from tkinter import *

student_window = None  # Global variable to store the student_window

def create_middle_frame():
    def open_admin_window():
        root.withdraw()
        admin_window = Toplevel(root)
        admin_window.title("Admin Window")
        admin_window.geometry('1000x600')
        admin_window.configure(bg='#333333')
        label_admin = Label(admin_window, text="Welcome to Admin Window", bg='#333333', fg='white', font=("Arial", 16, "bold"))
        label_admin.pack(expand=True)
        admin_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(admin_window))

    def open_student_window():
        global student_window
        root.withdraw()
        student_window = Toplevel(root)
        student_window.title("Student Window")
        student_window.geometry('1000x600')
        student_window.configure(bg='#333333')

        # Center the buttons horizontally and vertically in the window
        student_window.grid_rowconfigure(0, weight=1)
        student_window.grid_columnconfigure(0, weight=1)

        frame_buttons = Frame(student_window, bg='#333333')
        frame_buttons.pack(expand=True)

        # Create the "BORROW BOOK" button and associate it with the open_borrow_window function
        button1 = Button(frame_buttons, text="BORROW BOOK", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=20, height=7, anchor="center", command=open_borrow_window)
        button1.grid(row=0, column=0, padx=5, pady=5)

        # Create the "RETURN BOOK" button and associate it with the open_return_window function
        button2 = Button(frame_buttons, text="RETURN BOOK", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=20, height=7, anchor="center", command=open_return_window)
        button2.grid(row=0, column=1, padx=5, pady=5)

        # Create the "EXIT" button and associate it with the close_windows function
        button3 = Button(frame_buttons, text="EXIT", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=20, height=7, anchor="center", command=lambda: close_windows(student_window))
        button3.grid(row=0, column=2, padx=5, pady=5)

        student_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(student_window))

    def open_borrow_window():
        student_window.withdraw()
        borrow_window = Toplevel(student_window)
        borrow_window.title("BORROW BOOK Window")
        borrow_window.geometry('800x400')
        borrow_window.configure(bg='#333333')
        label_borrow = Label(borrow_window, text="BORROW BOOK Window", bg='#333333', fg='white', font=("Arial", 16, "bold"))
        label_borrow.pack(expand=True)
        borrow_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(borrow_window, student_window))

    def open_return_window():
        student_window.withdraw()
        return_window = Toplevel(student_window)
        return_window.title("RETURN BOOK Window")
        return_window.geometry('800x400')
        return_window.configure(bg='#333333')
        label_return = Label(return_window, text="RETURN BOOK Window", bg='#333333', fg='white', font=("Arial", 16, "bold"))
        label_return.pack(expand=True)
        return_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(return_window, student_window))

    def close_windows(new_window, prev_window=None):
        new_window.destroy()
        if prev_window:
            prev_window.deiconify()

    middle_frame = Frame(root, bg='#333333', width=500, height=150)
    middle_frame.grid(row=0, column=0, padx=50, pady=200)  # Center the middle_frame in the main window

    # Configure row and column weights to center the middle_frame vertically and horizontally
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create the "Admin" button and associate it with the open_admin_window function
    frame_admin = Frame(middle_frame, bg='#333333')
    frame_admin.pack(expand=True, pady=10)
    button_admin = Button(frame_admin, text="Admin", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=10, height=2, command=open_admin_window)
    button_admin.pack(expand=True)

    # Create the "Student" button and associate it with the open_student_window function
    frame_student = Frame(middle_frame, bg='#333333')
    frame_student.pack(expand=True, pady=10)
    button_student = Button(frame_student, text="Student", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=10, height=2, command=open_student_window)
    button_student.pack(expand=True)

# Create the main window
root = Tk()
root.title("Library Check-out")
root.geometry('1000x600')
root.configure(bg='#333333')

# Call the function to create the middle frame with two buttons inside white frames
create_middle_frame()

root.mainloop()
