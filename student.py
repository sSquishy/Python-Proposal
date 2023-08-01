from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime

def create_middle_frame():
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

    def close_windows(new_window, prev_window=None):
        new_window.destroy()
        if prev_window:
            prev_window.deiconify()

    def open_borrow_window():
        def update_database(selected_type, isbn_issn_id, book_id):
            try:
                conn = sqlite3.connect('sample.db')
                cursor = conn.cursor()

                # Check if the given book exists and has available copies
                cursor.execute("SELECT Copies FROM BookID WHERE BookID = ? AND [Literature type] = ? AND ID = ?",
                               (book_id, selected_type, isbn_issn_id))
                result = cursor.fetchone()

                if result:
                    copies = result[0]
                    if copies > 0:
                        # If there are available copies, reduce the count by one and update the database
                        new_copies = copies - 1
                        cursor.execute(
                            "UPDATE BookID SET Copies = ? WHERE BookID = ? AND [Literature type] = ? AND ID = ?",
                            (new_copies, book_id, selected_type, isbn_issn_id))
                        conn.commit()
                        messagebox.showinfo("Success", "Book has been successfully registered as borrowed!")
                    else:
                        # If no available copies, show a message
                        messagebox.showinfo("Out of Stock", "Out of Stock")
                else:
                    # If the book is not found, show an error message
                    messagebox.showerror("Error", "Book not found.")

                cursor.close()
                conn.close()
            except Exception as e:
                print("Error:", str(e))
                messagebox.showerror("Error", "An error occurred. Please try again.")

        def process_borrow():
            selected_type = literature_type_var.get()
            isbn_issn_id = isbn_issn_id_entry.get()
            book_id = book_id_entry.get()

            if selected_type and isbn_issn_id and book_id:
                # Add the item to the checkout list and update the database
                update_database(selected_type, isbn_issn_id, book_id)

                # Clear the input fields for the next item
                literature_type_var.set("ISBN")  # Reset the radio button selection
                isbn_issn_id_entry.delete(0, 'end')  # Clear the ISBN/ISSN ID Entry
                book_id_entry.delete(0, 'end')  # Clear the Book ID Entry
            else:
                # Show an error message if any field is empty
                messagebox.showerror("Error", "Please fill in all the fields.")


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


        # Create the "CANCEL" button to cancel the borrow action
        cancel_button = Button(input_frame,
                               text = "Cancel",
                               bg = 'red',
                               fg = '#FFFFFF',
                               font = ("Arial", 12),
                               width = 7,
                               height = 1,
                               command = lambda: close_windows(borrow_window, student_window))
        cancel_button.grid(row=4, column=1)

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

    def open_return_window():
        def update_database(selected_type, isbn_issn_id, book_id):
            try:
                conn = sqlite3.connect('sample.db')
                cursor = conn.cursor()

                # Check if the given book exists in the database
                cursor.execute("SELECT Copies FROM BookID WHERE BookID = ? AND [Literature type] = ? AND ID = ?",
                               (book_id, selected_type, isbn_issn_id))
                result = cursor.fetchone()

                if result:
                    copies = result[0]
                    # Increase the count by one and update the database
                    new_copies = copies + 1
                    cursor.execute("UPDATE BookID SET Copies = ? WHERE BookID = ? AND [Literature type] = ? AND ID = ?",
                                   (new_copies, book_id, selected_type, isbn_issn_id))
                    conn.commit()
                    messagebox.showinfo("Success", "Book has been successfully registered as returned!")
                else:
                    # If the book is not found, show an error message
                    messagebox.showerror("Error", "Book not found.")

                cursor.close()
                conn.close()
            except Exception as e:
                print("Error:", str(e))
                messagebox.showerror("Error", "An error occurred. Please try again.")

        def process_return():
            selected_type = literature_type_var.get()
            isbn_issn_id = isbn_issn_id_entry.get()
            book_id = book_id_entry.get()

            if selected_type and isbn_issn_id and book_id:
                # Update the item's information in the database
                update_database(selected_type, isbn_issn_id, book_id)

                # Clear the input fields for the next item
                literature_type_var.set("ISBN")  # Reset the radio button selection
                isbn_issn_id_entry.delete(0, 'end')  # Clear the ISBN/ISSN ID Entry
                book_id_entry.delete(0, 'end')  # Clear the Book ID Entry
            else:
                # Show an error message if any field is empty
                messagebox.showerror("Error", "Please fill in all the fields.")

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
                                command=process_return,
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

    middle_frame = Frame(root,
                         bg='#333333',
                         width=500,
                         height=150)
    middle_frame.grid(row=0, column=0, padx=50, pady=200)  # Center the middle_frame in the main window

    # Configure row and column weights to center the middle_frame vertically and horizontally
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


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