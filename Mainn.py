from tkinter import *
from tkinter import messagebox
import sqlite3



student_window = None  # Global variable to store the student_window
checkout_list = []

def create_middle_frame():

    def open_admin_window():
        root.withdraw()
        global admin_window
        admin_window = Toplevel(root)
        admin_window.title("Admin Window")
        admin_window.geometry('500x800')
        admin_window.configure(bg='#333333')

        def close_admin_window():
            admin_window.destroy()
            root.deiconify()

        # Create a frame to hold the buttons on the left side
        button_frame = Frame(admin_window, bg='#333333')
        button_frame.pack(side='left', padx=50)

        # Create three buttons on the left side
        ADDLITbutton = Button(button_frame,
                              text="ADD LITERATURE",
                              bg='#0D3C7B',
                              fg='White',
                              font=("Arial", 16, "bold"),
                              width=20,
                              height=2,
                              # command = open_add_literature_window
                              )
        ADDLITbutton.pack(pady=10)

        REMOVELITbutton = Button(button_frame,
                                 text="REMOVE LITERATURE",
                                 bg='#0D3C7B',
                                 fg='White',
                                 font=("Arial", 16, "bold"),
                                 width=20,
                                 height=2,
                                 # command = remove_literature_window
                                 )
        REMOVELITbutton.pack(pady=10)

        EXITLITbutton = Button(button_frame,
                               text = "EXIT",
                               bg = '#0D3C7B',
                               fg = 'white',
                               font = ("Arial", 16, "bold"),
                               width = 20,
                               height = 2)
        EXITLITbutton.pack(pady=10)

        admin_window.protocol('WM_DELETE_WINDOW', close_admin_window)

    # def open_add_literature_window():
    #     def addbook():
    #         selected_type = literature_type_var.get()
    #         ID_label = Book_ID_entry.get()
    #         title = Title_entry.get()
    #
    #         date = Date_entry.get()
    #         copies = text_entry4.get()
    #         author_gender = Author_gender.get()
    #         first_name = first_name_entry.get()
    #         last_name = last_name_entry.get()
    #
    #         # Check if any of the fields are blank
    #         if not all(
    #                 [selected_type, ID_label, title, date, copies, author_gender, first_name, last_name]):
    #             messagebox.showerror("Error", "Please fill in all the fields.")
    #             return
    #
    #
    #         # Process the data (For demonstration, we'll just print the data)
    #
    #         print("Selected Type:", selected_type)
    #         print("ISBN/ISSN ID:", ID_label)
    #         print("Title:", title)
    #         print("Date:", date)
    #         print("Copies:", copies)
    #         print("Author Gender:", author_gender)
    #         print("First Name:", first_name)
    #         print("Last Name:", last_name)
    #
    #         # Clear the input fields for the next item
    #
    #         Book_ID_entry.delete(0, 'end')  # Clear the Title Entry
    #         Title_entry.delete(0, 'end')  # Clear the Title Entry
    #         Date_entry.delete(0, 'end')  # Clear the Date Entry
    #         text_entry4.delete(0, 'end')  # Clear the Copies Entry
    #         first_name_entry.delete(0, 'end')  # Clear the First Name Entry
    #         last_name_entry.delete(0, 'end')  # Clear the Last Name Entry
    #
    #     add_window = Toplevel(student_window)
    #     add_window.title("ADD Literature Window")
    #     add_window.geometry('500x800')
    #     add_window.configure(bg='#333333')
    #
    #     # Create a frame for literature type selection
    #     literature_type_frame = Frame(add_window, bg='#333333', highlightbackground="white", highlightthickness=2)
    #     literature_type_frame.pack(pady=20, padx=20)
    #
    #
    #     # Create title for literature type selection
    #     literature_type_title = Label(literature_type_frame, text="Select Type of Literature", bg='#333333',
    #                                   fg='white', font=("Arial", 12, "bold"))
    #     literature_type_title.pack(anchor="w")
    #
    #     # Create radio buttons for literature type selection
    #     literature_type_var = StringVar()
    #     isbn_radio = Radiobutton(literature_type_frame, text="ISBN", variable=literature_type_var, value="ISBN",
    #                              bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444',
    #                              selectcolor='red')
    #     isbn_radio.pack(anchor="w", pady=5)
    #     issn_radio = Radiobutton(literature_type_frame, text="ISSN", variable=literature_type_var, value="ISSN",
    #                              bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444',
    #                              selectcolor='red')
    #     issn_radio.pack(anchor="w", pady=5)
    #
    #     # Frame for inputting text fields
    #     text_fields_frame = Frame(add_window, bg='#333333', highlightbackground="white", highlightthickness=2)
    #     text_fields_frame.pack(pady=20, padx=20)
    #
    #     # Label and Entry widget for "Input Book ID Type"
    #     Book_ID_label = Label(text_fields_frame, text="Input Book ID Type:", bg='#333333', fg='white', font=("Arial", 12))
    #     Book_ID_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    #
    #     Book_ID_entry = Entry(text_fields_frame, font=("Arial", 12), bg='white', fg='black')
    #     Book_ID_entry.grid(row=0, column=1, padx=5, pady=5, sticky='we')
    #     Book_ID_entry.config(state='normal')
    #
    #     # Label and Entry widget for "Input Title"
    #     Title_label = Label(text_fields_frame, text="Input Title:", bg='#333333', fg='white', font=("Arial", 12))
    #     Title_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    #
    #     Title_entry = Entry(text_fields_frame, font=("Arial", 12), bg='white', fg='black')
    #     Title_entry.grid(row=1, column=1, padx=5, pady=5, sticky='we')
    #     Title_entry.config(state='normal')
    #
    #     # Label and Entry widget for "Input Date"
    #     Date_label = Label(text_fields_frame, text="Input Date:", bg='#333333', fg='white', font=("Arial", 12))
    #     Date_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
    #
    #     Date_entry = Entry(text_fields_frame, font=("Arial", 12), bg='white', fg='black')
    #     Date_entry.grid(row=2, column=1, padx=5, pady=5, sticky='we')
    #     Date_entry.config(state='normal')
    #
    #     # Label and Entry widget for "Input Copies"
    #     label4 = Label(text_fields_frame, text="Input Copies:", bg='#333333', fg='white', font=("Arial", 12))
    #     label4.grid(row=3, column=0, sticky='w', padx=5, pady=5)
    #
    #     text_entry4 = Entry(text_fields_frame, font=("Arial", 12), bg='white', fg='black')
    #     text_entry4.grid(row=3, column=1, padx=5, pady=5, sticky='we')
    #     text_entry4.config(state='normal')
    #
    #     # Create a frame for author info and buttons
    #     author_frame = Frame(add_window, bg='#333333', highlightbackground="white", highlightthickness=2)
    #     author_frame.pack(pady=20, padx=20)
    #
    #     author_type_title = Label(author_frame, text="Author Info:", bg='#333333', fg='white',
    #                               font=("Arial", 12, "bold"))
    #     author_type_title.pack(anchor="w", pady=5)
    #
    #     # Create radio buttons for author gender selection
    #     Author_gender = StringVar()
    #     male_radio = Radiobutton(author_frame, text="Male", variable=Author_gender, value="Male",
    #                              bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444',
    #                              selectcolor='red')
    #     male_radio.pack(anchor="w", pady=2)
    #     female_radio = Radiobutton(author_frame, text="Female", variable=Author_gender, value="Female",
    #                                bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444',
    #                                selectcolor='red')
    #     female_radio.pack(anchor="w", pady=2)
    #     unspecified_radio = Radiobutton(author_frame, text="Unspecified", variable=Author_gender, value="Unspecified",
    #                                     bg='#333333', fg='white', font=("Arial", 12, "bold"),
    #                                     activebackground='#444444',
    #                                     selectcolor='red')
    #     unspecified_radio.pack(anchor="w", pady=2)
    #
    #     # Text fields for first name and last name
    #     first_name_label = Label(author_frame, text="First Name:", bg='#333333', fg='white', font=("Arial", 12))
    #     first_name_label.pack(anchor="w", pady=5)
    #     first_name_entry = Entry(author_frame, font=("Arial", 12), bg='white', fg='black')
    #     first_name_entry.pack(anchor="w", pady=5)
    #
    #     last_name_label = Label(author_frame, text="Last Name:", bg='#333333', fg='white', font=("Arial", 12))
    #     last_name_label.pack(anchor="w", pady=5)
    #     last_name_entry = Entry(author_frame, font=("Arial", 12), bg='white', fg='black')
    #     last_name_entry.pack(anchor="w", pady=5)
    #
    #     # Confirm button
    #     confirm_button = Button(author_frame, text="Confirm", bg='#0D3C7B', fg='#FFFFFF', font=("Arial", 12),
    #                             width=10, height=1, command = addbook)
    #     confirm_button.pack(anchor="e", padx=5, pady=10)
    #
    #     add_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(add_window))
    #
    # def remove_literature_window():
    #     admin_window.withdraw()  # Hide the current window
    #     remove_window = Toplevel()
    #     remove_window.title("Remove Literature Window")
    #     remove_window.geometry('500x700')
    #     remove_window.configure(bg='#333333')
    #
    #     # Create a frame for literature type selection
    #     literature_type_frame = Frame(remove_window, bg='#333333', highlightbackground="white", highlightthickness=2)
    #     literature_type_frame.pack(pady=50, anchor="center")
    #
    #     # Create title for literature type selection
    #     literature_type_title = Label(literature_type_frame, text="Select Type of Literature", bg='#333333',
    #                                   fg='white', font=("Arial", 12, "bold"))
    #     literature_type_title.pack()
    #
    #     # Create radio buttons for literature type selection
    #     literature_type_var = StringVar()
    #     isbn_radio = Radiobutton(literature_type_frame, text="ISBN", variable=literature_type_var, value="ISBN",
    #                              bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444',
    #                              selectcolor='red')
    #     isbn_radio.pack(anchor="w", pady=2)
    #     issn_radio = Radiobutton(literature_type_frame, text="ISSN", variable=literature_type_var, value="ISSN",
    #                              bg='#333333', fg='white', font=("Arial", 12, "bold"), activebackground='#444444',
    #                              selectcolor='red')
    #     issn_radio.pack(anchor="w", pady=2)
    #
    #     # Frame for inputting book ID, ISBN/ISSN, and Title/Published data
    #     input_frame = Frame(remove_window, bg='#333333', highlightbackground="white", highlightthickness=2)
    #     input_frame.pack(pady=10, padx=10, anchor="center")
    #
    #     # Create title for input section
    #     input_title = Label(input_frame, text="Input Details", bg='#333333', fg='white', font=("Arial", 18))
    #     input_title.grid(row=0, columnspan=2, padx=10, pady=5)
    #
    #     # Labels and Entry widgets for input details
    #     input_labels = ["Book ID:", "ISBN/ISSN:", "Title/Published Data:"]
    #     for i, label_text in enumerate(input_labels):
    #         label = Label(input_frame, text=label_text, bg='#333333', fg='white', font=("Arial", 12))
    #         label.grid(row=i + 1, column=0, sticky='w', padx=5, pady=5)
    #
    #         text_entry = Entry(input_frame, font=("Arial", 12), bg='white', fg='black')
    #         text_entry.grid(row=i + 1, column=1, padx=5, pady=5, sticky='we')
    #         text_entry.config(state='normal')
    #
    #     # Create a frame for buttons
    #     button_frame = Frame(remove_window, bg='#333333')
    #     button_frame.pack(pady=20)
    #
    #     # Create the "Remove Literature" button
    #     remove_button = Button(button_frame, text="Remove Literature", bg='#0D3C7B', fg='#FFFFFF', font=("Arial", 12),
    #                            width=20, height=2)
    #     remove_button.pack(side='left', padx=10)
    #
    #     # Create the "EXIT" button to close the window
    #     exit_button = Button(button_frame, text="EXIT", bg='0D3C7B', fg='#FFFFFF', font=("Arial", 12), width=20, height=2,
    #                          command=lambda: close_windows(remove_window, admin_window))
    #     exit_button.pack(side='right', padx=10)
    #
    #     # Close the remove_window and show the admin_window when the remove_window is closed
    #     remove_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(remove_window, admin_window))

    def open_student_window():
        global student_window
        root.withdraw()
        student_window = Toplevel(root)
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
                              bg = 'red',
                              fg = '#FFFFFF',
                              font = ("Arial", 16, "bold"),
                              width = 20,
                              height = 7,
                              anchor = "center",
                              command = open_borrow_window)
        BORROWbutton.grid(row=0, column=0, padx=5, pady=5)

        # Create the "RETURN BOOK" button and associate it with the open_return_window function
        RETURNbutton = Button(frame_buttons,
                              text = "RETURN BOOK",
                              bg = 'red',
                              fg = '#FFFFFF',
                              font = ("Arial", 16, "bold"),
                              width = 20,
                              height = 7,
                              anchor = "center",
                              command=open_return_window)
        RETURNbutton.grid(row=1, column=0, padx=5, pady=5)

        # Create the "EXIT" button and associate it with the close_windows function
        EXITbutton = Button(frame_buttons,
                            text = "EXIT",
                            bg = 'red',
                            fg = '#FFFFFF',
                            font = ("Arial", 16, "bold"),
                            width = 20,
                            height = 7,
                            anchor = "center",
                            command = lambda: close_windows(student_window))
        EXITbutton.grid(row=2, column=0, padx=5, pady=5)

        student_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(student_window))

    def open_borrow_window():
        def add_to_list():
            global checkout_list

            selected_type = literature_type_var.get()
            isbn_issn_id = isbn_issn_id_entry.get()
            book_id = book_id_entry.get()

            if selected_type and isbn_issn_id and book_id:
                # Add the item to the checkout list
                item = f"{selected_type} - ISBN/ISSN ID: {isbn_issn_id}, Book ID: {book_id}"
                checkout_list.append(item)
                messagebox.showinfo("Success", "Item added to the list for checkout.")

                # Clear the input fields for the next item
                literature_type_var.set("ISBN")  # Reset the radio button selection
                isbn_issn_id_entry.delete(0, 'end')  # Clear the ISBN/ISSN ID Entry
                book_id_entry.delete(0, 'end')  # Clear the Book ID Entry
            else:
                # Show an error message if any field is empty
                messagebox.showerror("Error", "Please fill in all the fields.")

        def process_borrow():
            global checkout_list
            if not checkout_list:
                # Show an error message if the list is empty
                messagebox.showerror("Error", "Please add items to the list for checkout.")
                return

            # Create a receipt window
            receipt_window = Toplevel(borrow_window)
            receipt_window.title("Checkout Receipt")
            receipt_window.geometry('400x300')
            receipt_window.configure(bg='#333333')

            receipt_label = Label(receipt_window, text="Checkout Receipt",
                                  bg='#333333',
                                  fg='white',
                                  font=("Arial", 16, "bold"))
            receipt_label.pack()

        student_window.withdraw()  # Hide the student_window
        borrow_window = Toplevel(student_window)
        borrow_window.title("BORROW BOOK Window")
        borrow_window.geometry('500x600')
        borrow_window.configure(bg='#333333')

        label_borrow = Label(borrow_window, text="BORROW BOOK Window",
                             bg='#333333',
                             fg='white',
                             font=("Arial", 16, "bold")
                             )
        label_borrow.pack()

        # Create a frame for literature type selection
        literature_type_frame = Frame(borrow_window,
                                      bg='#333333',
                                      highlightbackground="white",
                                      highlightthickness=1)
        literature_type_frame.pack(pady=50, anchor="center")

        # Create title for literature type selection
        literature_type_title = Label(literature_type_frame,
                                      text="Select Type of Literature",
                                      bg='#333333',
                                      fg='white',
                                      font=("Arial", 12, "bold"))
        literature_type_title.pack()

        # Create radio buttons for literature type selection
        literature_type_var = StringVar()
        isbn_radio = Radiobutton(literature_type_frame,
                                 text = "ISBN",
                                 variable = literature_type_var,
                                 value = "ISBN",
                                 bg = '#333333',
                                 fg = 'white',
                                 font = ("Arial", 12, "bold"),
                                 activebackground = '#444444',
                                 selectcolor = 'red')
        isbn_radio.pack(anchor = "w", pady = 2)
        issn_radio = Radiobutton(literature_type_frame,
                                 text = "ISSN",
                                 variable = literature_type_var,
                                 value = "ISSN",
                                 bg = '#333333',
                                 fg = 'white',
                                 font = ("Arial", 12, "bold"),
                                 activebackground = '#444444',
                                 selectcolor = 'red')
        issn_radio.pack(anchor="w", pady=2)

        # Frame for inputting ISBN/ISSN Id and Book ID
        input_frame = Frame(borrow_window,
                            bg='#333333',
                            highlightbackground="white",
                            highlightthickness=2,)
        input_frame.pack(pady=10, padx=10, anchor="center")

        # Create title for input section
        input_title = Label(input_frame, text = "Input ID", bg = '#333333', fg = 'white', font = ("Arial", 18))
        input_title.grid(row=0, columnspan=2, padx=10, pady=5)

        # Labels and Entry widgets for ISBN/ISSN Id and Book ID
        isbn_issn_id_label = Label(input_frame,
                                   text = "ISBN/ISSN ID:",
                                   bg = '#333333',
                                   fg = 'white',
                                   font = ("Arial", 12, "bold"))
        isbn_issn_id_label.grid(row=1, column=0, padx=5, pady=5)
        isbn_issn_id_entry = Entry(input_frame,
                                   bg = 'white',
                                   fg = 'black',
                                   font = ("Arial", 12))
        isbn_issn_id_entry.grid(row=1, column=1, padx=5, pady=5)

        book_id_label = Label(input_frame,
                              text = "Book ID:",
                              bg = '#333333',
                              fg = 'white',
                              font = ("Arial", 12, "bold"))
        book_id_label.grid(row=2, column=0, padx=5, pady=5)
        book_id_entry = Entry(input_frame,
                              bg = 'white',
                              fg = 'black',
                              font = ("Arial", 12))
        book_id_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create the "ADD" button to cancel the borrow action
        Add_button = Button(input_frame,
                            text = "Add to List",
                            bg = 'red',
                            fg = '#FFFFFF',
                            font = ("Arial", 12),
                            width = 9,
                            height = 1,
                            command = add_to_list)
        Add_button.grid(row=3, column=1)

        # Create the "CANCEL" button to cancel the borrow action
        cancel_button = Button(input_frame,
                               text = "Cancel",
                               bg = 'red',
                               fg = '#FFFFFF',
                               font = ("Arial", 12),
                               width = 7,
                               height = 1,
                               command = lambda: close_windows(borrow_window, student_window))
        cancel_button.grid(row=4, column=2)

        # Create the "BORROW" button to process the borrow action
        borrow_button = Button(input_frame,
                               text = "Confirm",
                               bg = 'red',
                               fg = '#FFFFFF',
                               font = ("Arial", 12),
                               width = 7,
                               height = 1,
                               command = process_borrow)
        borrow_button.grid(row=4, column=0)

        borrow_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(borrow_window, student_window))

    def open_return_window():
        student_window.withdraw()  # Hide the student_window
        return_window = Toplevel(student_window)
        return_window.title("RETURN BOOK Window")
        return_window.geometry('500x800')
        return_window.configure(bg='#333333')
        label_return = Label(return_window,
                             text="RETURN BOOK Window",
                             bg='#333333',
                             fg='white',
                             font=("Arial", 16, "bold"))
        label_return.pack()

        # Frame for selecting type of literature
        literature_type_frame = Frame(return_window, bg='#333333', highlightbackground="white",
                                      highlightthickness=2)
        literature_type_frame.pack(pady=20)

        # Create title for literature type selection
        literature_type_title = Label(literature_type_frame, text="Select Type of Literature",
                                      bg='#333333',
                                      fg='white',
                                      font=("Arial", 12, "bold"))
        literature_type_title.pack(anchor="w")

        # Create radio buttons for literature type selection
        literature_type_var = StringVar()
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

        # Frame for inputting ISBN/ISSN Id and Book ID
        input_frame = Frame(return_window, bg='#333333', highlightbackground="white",
                            highlightthickness=2)
        input_frame.pack(pady=20, padx=20)

        # Create title for input section
        input_title = Label(input_frame, text="Input ID", bg='#333333', fg='white', font=("Arial", 18))
        input_title.grid(row=0, columnspan=2, padx=10, pady=5)

        # Labels and Entry widgets for ISBN/ISSN Id and Book ID
        isbn_issn_id_label = Label(input_frame,
                                   text="ISBN/ISSN ID:",
                                   bg='#333333',
                                   fg='white',
                                   font=("Arial", 12, "bold"))
        isbn_issn_id_label.grid(row=1, column=0, padx=5, pady=5)
        isbn_issn_id_entry = Entry(input_frame, font=("Arial", 12), bg='white', fg='black')
        isbn_issn_id_entry.grid(row=1, column=1, padx=5, pady=5)

        book_id_label = Label(input_frame,
                              text="Book ID:",
                              bg='#333333',
                              fg='white',
                              font=("Arial", 12, "bold"))
        book_id_label.grid(row=2, column=0, padx=5, pady=5)
        book_id_entry = Entry(input_frame, font=("Arial", 12), bg='white', fg='black')
        book_id_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create the "CONFIRM" button to process the return action
        confirm_button = Button(input_frame,
                                text="CONFIRM",
                                bg='red',
                                fg='#FFFFFF',
                                font=("Arial", 12),
                                width=10,
                                height=1)
        confirm_button.grid(row=3, column=0, padx=5, pady=10)

        # Create the "CANCEL" button to cancel the return action
        cancel_button = Button(input_frame,
                               text="CANCEL",
                               bg='red',
                               fg='#FFFFFF',
                               font=("Arial", 12),
                               width=10,
                               height=1,
                               command=lambda: close_windows(return_window, student_window))
        cancel_button.grid(row=3, column=1, padx=5, pady=10)

        return_window.protocol('WM_DELETE_WINDOW', lambda: close_windows(return_window, student_window))

    def close_windows(new_window, prev_window=None):
        new_window.destroy()
        if prev_window:
            prev_window.deiconify()

    middle_frame = Frame(root,
                         bg='#333333',
                         width=500,
                         height=150)
    middle_frame.grid(row=0, column=0, padx=50, pady=200)  # Center the middle_frame in the main window

    # Configure row and column weights to center the middle_frame vertically and horizontally
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create the "Admin" button and associate it with the open_admin_window function
    frame_admin = Frame(middle_frame, bg='#333333')
    frame_admin.pack(expand=True, pady=10)
    button_admin = Button(frame_admin,
                          text="Admin",
                          bg='red',
                          fg='#FFFFFF',
                          font=("Arial", 16, "bold"),
                          width=10,
                          height=2,
                          command= open_admin_window)
    button_admin.pack(expand=True)

    # Create the "Student" button and associate it with the open_student_window function
    frame_student = Frame(middle_frame, bg='#333333')
    frame_student.pack(expand=True, pady=10)
    button_student = Button(frame_student,
                            text="Student",
                            bg='red',
                            fg='#FFFFFF',
                            font=("Arial", 16, "bold"),
                            width=10,
                            height=2,
                            command=open_student_window)
    button_student.pack(expand=True)



# Create the main window
root = Tk()
root.title("Library Check-out")
root.geometry('500x800')
root.configure(bg='#333333')



# Call the function to create the middle frame with two buttons inside white frames
create_middle_frame()

root.mainloop()