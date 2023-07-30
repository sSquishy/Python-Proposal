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
        def process_borrow():
            # Function to process the borrow action based on the selected literature type
            selected_type = literature_type_var.get()
            isbn_issn_id = isbn_issn_id_entry.get()
            book_id = book_id_entry.get()

            if selected_type == "ISBN":
                # Process borrow with ISBN
                print("Borrowing with ISBN")
                print("ISBN/ISSN Id:", isbn_issn_id)
                print("Book ID:", book_id)
            elif selected_type == "ISSN":
                # Process borrow with ISSN
                print("Borrowing with ISSN")
                print("ISBN/ISSN Id:", isbn_issn_id)
                print("Book ID:", book_id)
            else:
                # Handle the case when no literature type is selected
                print("Please select a literature type.")

        student_window.withdraw()
        borrow_window = Toplevel(student_window)
        borrow_window.title("BORROW BOOK Window")
        borrow_window.geometry('800x400')
        borrow_window.configure(bg='#333333')
        label_borrow = Label(borrow_window, text="BORROW BOOK Window", bg='#333333', fg='white', font=("Arial", 16, "bold"))
        label_borrow.pack(expand=True)

        # Create title for literature type selection
        literature_type_title = Label(borrow_window, text="Select Type of Literature", bg='#333333', fg='white', font=("Arial", 12, "bold"))
        literature_type_title.pack(anchor="w", padx=10, pady=5)

        # Create radio buttons for literature type selection
        literature_type_var = StringVar()
        literature_type_var.set("ISBN")  # Set the default selection
        isbn_radio = Radiobutton(borrow_window, text="ISBN", variable=literature_type_var, value="ISBN", bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444', selectcolor='red')
        isbn_radio.pack(anchor="w", padx=10, pady=2)
        issn_radio = Radiobutton(borrow_window, text="ISSN", variable=literature_type_var, value="ISSN", bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444', selectcolor='red')
        issn_radio.pack(anchor="w", padx=10, pady=2)

        # Frame for inputting ISBN/ISSN Id and Book ID
        input_frame = Frame(borrow_window, bg='#333333')
        input_frame.pack(pady=20)

        # Create title for input section
        input_title = Label(input_frame, text="Input ID", bg='#333333', fg='white', font=("Arial", 12, "bold"))
        input_title.grid(row=0, columnspan=2, padx=10, pady=5)

        # Labels and Entry widgets for ISBN/ISSN Id and Book ID
        isbn_issn_id_label = Label(input_frame, text="ISBN/ISSN ID:", bg='#333333', fg='white',
                                   font=("Arial", 12, "bold"))
        isbn_issn_id_label.grid(row=1, column=0, padx=5, pady=5)
        isbn_issn_id_entry = Entry(input_frame, bg='white', fg='black', font=("Arial", 12))
        isbn_issn_id_entry.grid(row=1, column=1, padx=5, pady=5)

        book_id_label = Label(input_frame, text="Book ID:", bg='#333333', fg='white', font=("Arial", 12, "bold"))
        book_id_label.grid(row=2, column=0, padx=5, pady=5)
        book_id_entry = Entry(input_frame, bg='white', fg='black', font=("Arial", 12))
        book_id_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create the "BORROW" button to process the borrow action
        borrow_button = Button(borrow_window, text="BORROW", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"),
                               width=20, height=2, command=process_borrow)
        borrow_button.pack(pady=10)

        # Create the "BACK" button to go back to the student window
        back_button = Button(borrow_window, text="BACK", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=20,
                             height=2, command=lambda: close_windows(borrow_window, student_window))
        back_button.pack()

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
