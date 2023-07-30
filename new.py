import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import calendar


def validate_integer(entry):
    try:
        int(entry.get())
        return True
    except ValueError:
        return False


def create_main_window():
    global window
    window = tk.Tk()
    window.title("Library System")
    window.geometry("800x300")

    # LabelFrame to group Full Name, Student ID, and Confirm Button
    input_frame = tk.LabelFrame(window, text="Personal Information")
    input_frame.pack(padx=10, pady=10)

    # Input for Full Name
    full_name_label = tk.Label(input_frame, text="Full Name:")
    full_name_label.grid(row=0, column=0, padx=5, pady=5)

    global full_name_entry
    full_name_entry = tk.Entry(input_frame)
    full_name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Input for Student ID
    student_id_label = tk.Label(input_frame, text="Student ID:")
    student_id_label.grid(row=1, column=0, padx=5, pady=5)

    global student_id_entry
    student_id_entry = tk.Entry(input_frame)
    student_id_entry.grid(row=1, column=1, padx=5, pady=5)

    # Confirm Button
    confirm_button = tk.Button(input_frame, text="Confirm", command=on_confirm_button_click)
    confirm_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Header Label to display the Full Name
    global header_label
    header_label = tk.Label(window, text="", font=("Helvetica", 16, "bold"))
    header_label.pack(padx=10, pady=10)


def on_confirm_button_click():
    full_name = full_name_entry.get()
    if not full_name.strip():
        messagebox.showerror("Error", "Full Name cannot be empty.")
        return

    student_id = student_id_entry.get()
    if not validate_integer(student_id_entry):
        messagebox.showerror("Error", "Invalid input! Please enter a valid Student ID.")
        return

    # Display Full Name as a header
    header_label.config(text=f"Welcome, {full_name}!")

    # Here you can perform any necessary actions with the entered student ID
    # For example, you can check if the student ID exists in the database, etc.

    # After processing the student ID, show the client and admin buttons
    client_button = tk.Button(window, text="CLIENT", command=show_client_options)
    client_button.pack(side=tk.LEFT, padx=10, pady=10)

    admin_button = tk.Button(window, text="ADMIN", command=show_admin_options)
    admin_button.pack(side=tk.RIGHT, padx=10, pady=10)


def show_client_options():
    global client_window
    client_window = tk.Tk()
    client_window.title("Client Options")
    client_window.geometry("1920x1080")

    borrow_button = tk.Button(client_window, text="BORROW BOOK", command=show_borrow_book_window)
    borrow_button.pack(side=tk.LEFT, padx=10, pady=10)

    return_button = tk.Button(client_window, text="RETURN BOOK",
                              command=show_return_book_window)  # Add the "RETURN BOOK" button to the client window
    return_button.pack(side=tk.LEFT, padx=10, pady=10)

    exit_button = tk.Button(client_window, text="EXIT", command=client_window_quit)
    exit_button.pack(side=tk.LEFT, padx=10, pady=10)
    window.destroy()  # Close the main window
    client_window.mainloop()


def show_admin_options():
    global admin_window
    admin_window = tk.Tk()
    admin_window.title("ADMIN Options")
    admin_window.geometry("1920x1080")

    borrow_button = tk.Button(admin_window, text="ADD LITERATURE", command=show_add_literature_window)
    borrow_button.pack(side=tk.LEFT, padx=10, pady=10)

    return_button = tk.Button(admin_window, text="REMOVE LITERATURE", command=show_remove_literature_window)
    return_button.pack(side=tk.LEFT, padx=10, pady=10)

    return_button = tk.Button(admin_window, text="SEARCH LITERATURE", command=show_search_literature_window)
    return_button.pack(side=tk.LEFT, padx=10, pady=10)

    exit_button = tk.Button(admin_window, text="EXIT", command=admin_window_quit)
    exit_button.pack(side=tk.LEFT, padx=10, pady=10)
    window.destroy()  # Close the main window
    admin_window.mainloop()


def show_borrow_book_window():
    client_window.destroy()  # Close the main window

    borrow_book_window = tk.Tk()
    borrow_book_window.title("Borrow Book")
    borrow_book_window.geometry("1920x1080")

    literature_type_frame = tk.LabelFrame(borrow_book_window, text="Book Checkout")
    literature_type_frame.pack(padx=15, pady=15)

    literature_type_var = tk.StringVar()
    literature_type_var.set("")

    isbn_radio_button = tk.Radiobutton(literature_type_frame, text="ISBN (For books)", variable=literature_type_var,
                                       value="ISBN")
    isbn_radio_button.pack()
    isbn_radio_button.deselect()

    issn_radio_button = tk.Radiobutton(literature_type_frame, text="ISSN (For Journals and Magazines)",
                                       variable=literature_type_var, value="ISSN")
    issn_radio_button.pack()

    input_id_frame = tk.LabelFrame(borrow_book_window, text="Input ID")
    input_id_frame.pack(padx=15, pady=15)

    book_id_label = tk.Label(input_id_frame, text="BOOK ID")
    book_id_label.pack()

    book_id_entry = tk.Entry(input_id_frame)
    book_id_entry.pack()

    isbn_issn_label = tk.Label(input_id_frame, text="ISBN/ISSN ID")
    isbn_issn_label.pack()

    isbn_issn_entry = tk.Entry(input_id_frame)
    isbn_issn_entry.pack()

    checkout_list_frame = tk.LabelFrame(borrow_book_window, text="Checkout List")
    checkout_list_frame.pack(padx=15, pady=15)

    # Listbox to display the ISBN/ISSN IDs
    isbn_issn_listbox = tk.Listbox(checkout_list_frame, selectmode=tk.SINGLE)
    isbn_issn_listbox.pack(padx=5, pady=5)

    def add_to_checkout_list():
        isbn_issn_id = int(isbn_issn_entry.get())
        isbn_issn_listbox.insert(tk.END, isbn_issn_id)
        isbn_issn_entry.delete(0, tk.END)

    def back_to_client():
        borrow_book_window.destroy()  # Close the borrow book window
        show_client_options()

    def confirm_borrow(isbn_issn_listbox):
        if validate_integer(book_id_entry) and validate_integer(isbn_issn_entry):
            book_id = int(book_id_entry.get())
            isbn_issn_id = int(isbn_issn_entry.get())
            literature_type = literature_type_var.get()

            # Perform the necessary actions with the borrowed book information
            # ...

            messagebox.showinfo("Borrow Book", f"You borrowed Book ID: {book_id}, {literature_type} ID: {isbn_issn_id}")

            # Add the ISBN/ISSN ID to the Checkout List
            isbn_issn_listbox.insert(tk.END, isbn_issn_id)

        else:
            messagebox.showerror("Error", "Invalid input! Please enter only integers.")

    confirm_button = tk.Button(input_id_frame, text="Confirm", command=confirm_borrow)
    confirm_button.pack(side=tk.LEFT, padx=10, pady=10)

    confirm_checkout_button = tk.Button(checkout_list_frame, text="Confirm Checkout", command=show_checkout_receipt)
    confirm_checkout_button.pack(padx=5, pady=5)

    back_button = tk.Button(input_id_frame, text="Back", command=back_to_client)
    back_button.pack(side=tk.LEFT, padx=10, pady=10)

    borrow_book_window.mainloop()


def show_checkout_receipt():
    #   Retrieve the selected ISBN/ISSN IDs from the Listbox

    # selected_indices = isbn_issn_listbox.curselection()
    # selected_ids = [isbn_issn_listbox.get(index) for index in selected_indices]

    #  Create a new window for the Checkout Receipt
    # receipt_window = tk.Toplevel()
    # receipt_window.title("Checkout Receipt")

    #  Display the ISBN/ISSN IDs in a Listbox in the Receipt Window
    # receipt_listbox = tk.Listbox(receipt_window, selectmode=tk.NONE)
    # for id in selected_ids:
    #     receipt_listbox.insert(tk.END, id)
    # receipt_listbox.pack(padx=10, pady=10)

    # receipt_window.mainloop()
    # Create a new window for the Checkout Receipt

    # Create a new window for the Checkout Receipt
    receipt_window = tk.Toplevel()
    receipt_window.title("Checkout Receipt")
    receipt_window.geometry("600x400")

    # Header Label
    header_label = tk.Label(receipt_window, text="Check out Receipt", font=("Helvetica", 16, "bold"))
    header_label.pack(padx=10, pady=10)

    # Check out ID Label
    checkout_id_label = tk.Label(receipt_window, text="Check out ID:")
    checkout_id_label.pack(padx=10, pady=5)

    # Current Date Label
    current_date_label = tk.Label(receipt_window, text="Current Date:")
    current_date_label.pack(padx=10, pady=5)

    # Multi-column Treeview for Receipt List
    receipt_listbox = ttk.Treeview(receipt_window, columns=("Book Title", "Author/s", "Date Published"),
                                   show="headings")
    receipt_listbox.heading("Book Title", text="Book Title")
    receipt_listbox.heading("Author/s", text="Author/s")
    receipt_listbox.heading("Date Published", text="Date Published")

    # Insert sample data (filler strings) for demonstration purposes
    # For each book, the authors' names are stored as a comma-separated string
    receipt_listbox.insert("", "end", values=("Sample Book 1", "Author 1, Author 2", "2023-07-22"))
    receipt_listbox.insert("", "end", values=("Sample Book 2", "Author 3", "2023-07-23"))
    receipt_listbox.insert("", "end", values=("Sample Book 3", "Author 4, Author 5", "2023-07-24"))

    receipt_listbox.pack(padx=10, pady=10)

    receipt_window.mainloop()


def show_return_book_window():
    client_window.destroy()  # Close the main window

    borrow_book_window = tk.Tk()
    borrow_book_window.title("Return Book")
    borrow_book_window.geometry("1920x1080")

    literature_type_frame = tk.LabelFrame(borrow_book_window, text="Book Check-in")
    literature_type_frame.pack(padx=15, pady=15)

    literature_type_var = tk.StringVar()
    literature_type_var.set("")

    isbn_radio_button = tk.Radiobutton(literature_type_frame, text="ISBN (For books)", variable=literature_type_var,
                                       value="ISBN")
    isbn_radio_button.pack()
    isbn_radio_button.deselect()

    issn_radio_button = tk.Radiobutton(literature_type_frame, text="ISSN (For Journals and Magazines)",
                                       variable=literature_type_var, value="ISSN")
    issn_radio_button.pack()

    input_id_frame = tk.LabelFrame(borrow_book_window, text="Input ID")
    input_id_frame.pack(padx=15, pady=15)

    book_id_label = tk.Label(input_id_frame, text="BOOK ID")
    book_id_label.pack()

    book_id_entry = tk.Entry(input_id_frame)
    book_id_entry.pack()

    isbn_issn_label = tk.Label(input_id_frame, text="ISBN/ISSN ID")
    isbn_issn_label.pack()

    isbn_issn_entry = tk.Entry(input_id_frame)
    isbn_issn_entry.pack()

    # New LabelFrame to group Checkout List components

    def back_to_client():
        borrow_book_window.destroy()  # Close the borrow book window
        show_client_options()

    def confirm_borrow():
        if validate_integer(book_id_entry) and validate_integer(isbn_issn_entry):
            book_id = int(book_id_entry.get())
            isbn_issn_id = int(isbn_issn_entry.get())
            literature_type = literature_type_var.get()

            # Perform the necessary actions with the borrowed book information
            # ...

            messagebox.showinfo("Borrow Book", f"You borrowed Book ID: {book_id}, {literature_type} ID: {isbn_issn_id}")
        else:
            messagebox.showerror("Error", "Invalid input! Please enter only integers.")

    confirm_button = tk.Button(input_id_frame, text="Confirm", command=confirm_borrow)
    confirm_button.pack(side=tk.LEFT, padx=10, pady=10)

    back_button = tk.Button(input_id_frame, text="Back", command=back_to_client)
    back_button.pack(side=tk.LEFT, padx=10, pady=10)

    borrow_book_window.mainloop()


def show_add_literature_window():
    admin_window.destroy()  # Close the previous ADMIN window

    add_literature_window = tk.Tk()
    add_literature_window.title("Add Literature")
    add_literature_window.geometry("1920x1080")

    literature_types_frame = tk.LabelFrame(add_literature_window, text="Select Literature Types")
    literature_types_frame.pack(padx=15, pady=15)

    literature_type_var = tk.StringVar()

    isbn_radio_button = tk.Radiobutton(literature_types_frame, text="ISBN (For Books)", variable=literature_type_var,
                                       value="ISBN")
    isbn_radio_button.pack()

    issn_radio_button = tk.Radiobutton(literature_types_frame, text="ISSN (For Journals and Magazines)",
                                       variable=literature_type_var, value="ISSN")
    issn_radio_button.pack()

    literature_info_frame = tk.LabelFrame(add_literature_window, text="Literature Information")
    literature_info_frame.pack(padx=15, pady=15)

    title_label = tk.Label(literature_info_frame, text="Literature Title")
    title_label.pack()

    title_entry = tk.Entry(literature_info_frame)
    title_entry.pack()

    copies_label = tk.Label(literature_info_frame, text="No. Of Copies")
    copies_label.pack()

    copies_entry = tk.Entry(literature_info_frame)
    copies_entry.pack()

    literature_info_frame = tk.LabelFrame(add_literature_window, text="Literature Information")
    literature_info_frame.pack(padx=15, pady=15)

    title_label = tk.Label(literature_info_frame, text="Literature Title")
    title_label.pack()

    title_entry = tk.Entry(literature_info_frame)
    title_entry.pack()

    copies_label = tk.Label(literature_info_frame, text="No. Of Copies")
    copies_label.pack()

    copies_entry = tk.Entry(literature_info_frame)
    copies_entry.pack()

    def validate_copies():
        if not validate_integer(copies_entry):
            messagebox.showerror("Error", "Invalid input! Please enter a non-negative integer for No. Of Copies.")

    copies_entry.bind("<FocusOut>", lambda event: validate_copies())

    def show_calendar():
        def select_date():
            selected_date = cal.get_date()
            date_entry.delete(0, tk.END)
            date_entry.insert(tk.END, selected_date)
            top.destroy()

        top = tk.Toplevel(add_literature_window)
        top.title("Select Date")
        cal = calendar.Calendar(firstweekday=0)
        year = tk.IntVar()
        month = tk.IntVar()
        year.set(calendar.datetime.datetime.now().year)
        month.set(calendar.datetime.datetime.now().month)

        year_spinbox = tk.Spinbox(top, from_=1900, to=9999, textvariable=year)
        year_spinbox.pack()

        month_spinbox = tk.Spinbox(top, from_=1, to=12, textvariable=month)
        month_spinbox.pack()

        calendar_frame = tk.Frame(top)
        calendar_frame.pack()

        def update_calendar():
            month_calendar = cal.monthdayscalendar(year.get(), month.get())
            for i in range(6):
                for j in range(7):
                    day = month_calendar[i][j]
                    day_button = tk.Button(calendar_frame, text=str(day) if day != 0 else "", width=4)
                    day_button.grid(row=i, column=j)
                    if day != 0:
                        day_button.config(command=select_date)

        update_calendar()

    date_label = tk.Label(literature_info_frame, text="Date Published")
    date_label.pack()

    date_entry = tk.Entry(literature_info_frame)
    date_entry.pack()

    date_button = tk.Button(literature_info_frame, text="Select Date", command=show_calendar)
    date_button.pack()

    authors_frame = tk.LabelFrame(add_literature_window, text="Authors")
    authors_frame.pack(padx=15, pady=15)

    first_name_label = tk.Label(authors_frame, text="First Name")
    first_name_label.pack()

    first_name_entry = tk.Entry(authors_frame)
    first_name_entry.pack()

    last_name_label = tk.Label(authors_frame, text="Last Name")
    last_name_label.pack()

    last_name_entry = tk.Entry(authors_frame)
    last_name_entry.pack()

    authors_listbox = tk.Listbox(authors_frame, selectmode=tk.NONE)
    authors_listbox.pack()

    def confirm_literature():
        if validate_integer(copies_entry):
            literature_title = title_entry.get()
            num_copies = int(copies_entry.get())
            date_published = date_entry.get()

            # Perform necessary actions with the literature information
            # ...

            messagebox.showinfo("Add Literature", "Literature added successfully!")
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a non-negative integer for No. Of Copies.")

    confirm_button = tk.Button(literature_info_frame, text="Confirm", command=confirm_literature)
    confirm_button.pack(side=tk.LEFT, padx=10, pady=10)

    def confirm_author():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        author_name = f"{first_name} {last_name}"
        authors_listbox.insert(tk.END, author_name)
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)

    confirm_button = tk.Button(authors_frame, text="Confirm", command=confirm_author)
    confirm_button.pack(side=tk.LEFT, padx=10, pady=10)
    add_literature_window.mainloop()


def show_remove_literature_window():
    pass


def show_search_literature_window():
    pass


def client_window_quit():
    client_window.destroy()  # Close the borrow book window
    create_main_window()


def admin_window_quit():
    admin_window.destroy()  # Close the borrow book window
    create_main_window()


create_main_window()
window.mainloop()