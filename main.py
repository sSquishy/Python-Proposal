from tkinter import *

student_window = None  # Global variable to store the student_window

def create_middle_frame():
    def open_add_literature_window():
        add_window = Toplevel(student_window)
        add_window.title("ADD Literature Window")
        add_window.geometry('1000x600')
        add_window.configure(bg='#333333')


        # Create a frame for literature type selection
        literature_type_frame = Frame(add_window, bg='#333333')
        literature_type_frame.pack()

        # Create title for literature type selection
        literature_type_title = Label(literature_type_frame, text="Select Type of Literature",
                                      bg='#333333',
                                      fg='white',
                                      font=("Arial", 12, "bold"))
        literature_type_title.pack(anchor="w")

        # Create radio buttons for literature type selection
        literature_type_var = StringVar()
        literature_type_var.set("ISBN")  # Set the default selection
        isbn_radio = Radiobutton(literature_type_frame,
                                 text="ISBN",
                                 variable=literature_type_var,
                                 value="ISBN",
                                 bg='#333333',
                                 fg='white',
                                 font=("Arial", 12, "bold"),
                                 activebackground='#444444',
                                 selectcolor='red')
        isbn_radio.pack(anchor="w", pady=2)
        issn_radio = Radiobutton(literature_type_frame,
                                 text="ISSN",
                                 variable=literature_type_var,
                                 value="ISSN",
                                 bg='#333333',
                                 fg='white',
                                 font=("Arial", 12, "bold"),
                                 activebackground='#444444',
                                 selectcolor='red')
        issn_radio.pack(anchor="w", pady=2)

        # Create a frame for text fields
        text_fields_frame = Frame(add_window, bg='#333333')
        text_fields_frame.pack()


        # Labels and Entry widgets for input details
        input_labels = ["Input ID Type:", "Input Title:", "Input Date:", "Input Copies:"]
        for i, label_text in enumerate(input_labels):
            label = Label(text_fields_frame,
                          text=label_text,
                          bg='#333333',
                          fg='white',
                          font=("Arial", 12))
            label.grid(row=i, column=0, sticky='w', padx=5, pady=5)

            text_entry = Entry(text_fields_frame, font=("Arial", 12), bg='white', fg='black')
            text_entry.grid(row=i, column=1, padx=5, pady=5, sticky='we')
            text_entry.config(state='normal')


        # Create a frame for text fields
        AuthorFrame = Frame(add_window, bg='#333333')
        AuthorFrame.pack()  # 'ne' for top-right

        # Create radio buttons for author gender selection
        Author_gender = StringVar()
        male_radio = Radiobutton(AuthorFrame,
                                 text = "Male",
                                 variable = Author_gender,
                                 value = "Male",
                                 bg = '#333333',
                                 fg = 'white',
                                 font = ("Arial", 12, "bold"),
                                 activebackground = '#444444',
                                 selectcolor = 'red')
        male_radio.pack(anchor="w", pady=2)
        female_radio = Radiobutton(AuthorFrame,
                                   text = "Female",
                                   variable = Author_gender,
                                   value = "Female",
                                   bg = '#333333',
                                   fg = 'white',
                                   font = ("Arial", 12, "bold"),
                                   activebackground = '#444444',
                                   selectcolor = 'red')
        female_radio.pack(anchor="w", pady=2)
        unspecified_radio = Radiobutton(AuthorFrame,
                                    text = "Unspecified",
                                    variable = Author_gender,
                                    value = "Unspecified",
                                    bg = '#333333',
                                    fg = 'white',
                                    font = ("Arial", 12, "bold"),
                                    activebackground = '#444444',
                                    selectcolor = 'red')
        unspecified_radio.pack(anchor="w", pady=2)

        add_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(add_window))

    def open_remove_literature_window():
        admin_window.withdraw()  # Hide the current window
        remove_window = Toplevel()
        remove_window.title("Remove Literature Window")
        admin_window.geometry('1000x600')
        remove_window.configure(bg='#333333')

        # Add your code for the Remove Literature Window here...
        # Don't forget to handle closing this window and restoring the admin_window when necessary.

    def open_admin_window():
        root.withdraw()
        global admin_window
        admin_window = Toplevel(root)
        admin_window.title("Admin Window")
        admin_window.geometry('1000x600')
        admin_window.configure(bg='#333333')

        def close_admin_window():
            admin_window.destroy()
            root.deiconify()

        # Create a frame to hold the buttons on the left side
        button_frame = Frame(admin_window, bg='#333333')
        button_frame.pack(side='left', padx=50)

        # Create three buttons on the left side
        ADDLITbutton = Button(button_frame, text="ADD LITERATURE", bg='#0D3C7B', fg='White', font=("Arial", 16, "bold"),
                              width=20, height=2, command=open_add_literature_window)
        ADDLITbutton.pack(pady=10)

        REMOVELITbutton = Button(button_frame, text="REMOVE LITERATURE", bg='#0D3C7B', fg='White',
                                 font=("Arial", 16, "bold"), width=20, height=2, command=open_remove_literature_window)
        REMOVELITbutton.pack(pady=10)

        EXITLITbutton = Button(button_frame, text="EXIT", bg='#0D3C7B', fg='white', font=("Arial", 16, "bold"),
                               width=20, height=2, command=close_admin_window)
        EXITLITbutton.pack(pady=10)

        admin_window.protocol('WM_DELETE_WINDOW', close_admin_window)

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
        BORROWbutton = Button(frame_buttons, text="BORROW BOOK", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=20, height=7, anchor="center", command=open_borrow_window)
        BORROWbutton.grid(row=0, column=0, padx=5, pady=5)

        # Create the "RETURN BOOK" button and associate it with the open_return_window function
        RETURNbutton = Button(frame_buttons, text="RETURN BOOK", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=20, height=7, anchor="center", command=open_return_window)
        RETURNbutton.grid(row=0, column=1, padx=5, pady=5)

        # Create the "EXIT" button and associate it with the close_windows function
        EXITbutton = Button(frame_buttons, text="EXIT", bg='red', fg='#FFFFFF', font=("Arial", 16, "bold"), width=20, height=7, anchor="center", command=lambda: close_windows(student_window))
        EXITbutton.grid(row=0, column=2, padx=5, pady=5)

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


        borrow_window = Toplevel(student_window)
        borrow_window.title("BORROW BOOK Window")
        borrow_window.geometry('1000x600')
        borrow_window.configure(bg='#333333')
        label_borrow = Label(borrow_window, text="BORROW BOOK Window",
                             bg='#333333',
                             fg='white',
                             font=("Arial", 16, "bold"))
        label_borrow.pack(expand=True)

        # Create a frame for literature type selection
        literature_type_frame = Frame(borrow_window, bg='#333333')
        literature_type_frame.pack(anchor="w", padx=80, pady=0)

        # Create title for literature type selection
        literature_type_title = Label(literature_type_frame, text="Select Type of Literature", bg='#333333', fg='white',
                                      font=("Arial", 12, "bold"))
        literature_type_title.pack(anchor="w")

        # Create radio buttons for literature type selection
        literature_type_var = StringVar()
        literature_type_var.set("ISBN")  # Set the default selection
        isbn_radio = Radiobutton(literature_type_frame, text="ISBN", variable=literature_type_var, value="ISBN",
                                 bg='#333333',
                                 fg='white',
                                 font=("Arial", 12, "bold"),
                                 activebackground='#444444',
                                 selectcolor='red')
        isbn_radio.pack(anchor="w", pady=2)
        issn_radio = Radiobutton(literature_type_frame, text="ISSN", variable=literature_type_var, value="ISSN",
                                 bg='#333333',
                                 fg='white',
                                 font=("Arial", 12, "bold"),
                                 activebackground='#444444',
                                 selectcolor='red')
        issn_radio.pack(anchor="w", pady=2)

        # Frame for inputting ISBN/ISSN Id and Book ID
        input_frame = Frame(borrow_window, bg='#333333')
        input_frame.pack(pady=20, padx=10, side='left')

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
        borrow_button = Button(input_frame, text="Confirm", bg='red', fg='#FFFFFF', font=("Arial", 9, "bold"),
                               width=7, height=1, command=process_borrow)
        borrow_button.grid(row=3, column=0, pady=10)

        # Create the "CANCEL" button to cancel the borrow action
        cancel_button = Button(input_frame, text="Cancel", bg='red', fg='#FFFFFF', font=("Arial", 9, "bold"),
                               width=7, height=1, command=lambda: close_windows(borrow_window, student_window))
        cancel_button.grid(row=3, column=1, pady=10)


        borrow_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(borrow_window, student_window))

    def open_return_window():

        return_window = Toplevel(student_window)
        return_window.title("RETURN BOOK Window")
        return_window.geometry('1000x600')
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
