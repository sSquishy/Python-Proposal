import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


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
    window.geometry("300x150")

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
    student_id_label = tk.Label(input_frame, text="Admin ID:")
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
    # Set default name and student ID for confirmation
    default_full_name = "john"
    default_student_id = "00197"

    full_name = full_name_entry.get()
    student_id = student_id_entry.get()

    # Check if the input fields are blank
    if not full_name.strip() or not student_id.strip():
        messagebox.showerror("Error", "Full Name and Student ID cannot be empty.")
        return

    # Check if the entered name and student ID match the default values
    if full_name == default_full_name and student_id == default_student_id:
        # Display Full Name as a header
        header_label.config(text=f"Welcome, {full_name}!")

        # Show a successful login message
        messagebox.showinfo("Success", "Login Successful!")

        # Proceed to admin options
        show_admin_options()
    else:
        messagebox.showerror("Error", "Invalid Full Name or Student ID. Please enter the correct values.")
        return
def fetch_library_collection_data():
    try:
        conn = sqlite3.connect("sample.db")
        c = conn.cursor()

        # Fetch data from both BookID and AuthorID tables based on common BookID
        c.execute("""
            SELECT b.Title, b.ID, GROUP_CONCAT(a.Firstname || ' ' || a.Lastname) as Authors, b.Datepublished, b.Copies
            FROM BookID b
            LEFT JOIN AuthorID a ON b.BookID = a.ID
            GROUP BY b.BookID
            ORDER BY b.BookID
        """)
        data = c.fetchall()

        conn.close()

        return data
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def show_admin_options():
    global admin_window
    admin_window = tk.Tk()
    admin_window.title("ADMIN Options")
    admin_window.geometry("400x300")

    # Create a frame to hold all the buttons
    button_frame = tk.Frame(admin_window)
    button_frame.pack(pady=50, anchor=tk.CENTER)

    # Set a blue background and white font for the buttons
    button_style = {"bg": "blue", "fg": "white"}

    # ADD LITERATURE button
    borrow_button = tk.Button(button_frame, text="ADD LITERATURE", command=show_add_literature_window, **button_style)
    borrow_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    # REMOVE LITERATURE button
    return_button = tk.Button(button_frame, text="REMOVE LITERATURE", command=show_remove_literature_window,
                              **button_style)
    return_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    show_library_collection_button = tk.Button(button_frame, text="SHOW LIBRARY COLLECTION",
                                               command=show_library_collection, **button_style)
    show_library_collection_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    # EXIT button
    exit_button = tk.Button(button_frame, text="EXIT", command=admin_window_quit, **button_style)
    exit_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    window.destroy()  # Close the main window
    admin_window.mainloop()

def show_library_collection():
    library_collection_data = fetch_library_collection_data()

    if library_collection_data:
        # Hide the main window temporarily
        admin_window.withdraw()

        # Create a new window for the Library Collection Listbox
        library_collection_window = tk.Tk()
        library_collection_window.title("Library Collection")
        library_collection_window.geometry("1100x300")

        # Create a Multi-column Treeview for Library Collection Listbox
        library_collection_listbox = ttk.Treeview(library_collection_window, columns=(
            "Title", "Literature ID", "Author", "Date Published", "No. Of Copies"), show="headings")

        library_collection_listbox.heading("Title", text="Title")
        library_collection_listbox.heading("Literature ID", text="Literature ID")
        library_collection_listbox.heading("Author", text="Author")
        library_collection_listbox.heading("Date Published", text="Date Published")
        library_collection_listbox.heading("No. Of Copies", text="No. Of Copies")

        for row in library_collection_data:
            # Insert the fetched data into the Treeview/Listbox
            library_collection_listbox.insert("", "end", values=row)

        library_collection_listbox.pack(padx=10, pady=10)

        # Function to go back to the admin options window
        def go_back_to_admin():
            library_collection_window.destroy()  # Close the "Library Collection" window
            admin_window.deiconify()  # Show the admin options window again

        # Button to go back to admin options
        back_button = tk.Button(library_collection_window, text="Back", command=go_back_to_admin)
        back_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    else:
        messagebox.showinfo("No Data", "No data found in the Library Collection.")

def insert_literature(literature_type, id, title, date_published, copies):
    try:
        # Connect to the database (create it if it doesn't exist)
        conn = sqlite3.connect("sample.db")
        c = conn.cursor()

        # Insert data into BookID table
        c.execute("INSERT INTO BookID ([Literature type], ID, Title, Datepublished, Copies) "
                  "VALUES (?, ?, ?, ?, ?)",
                  (literature_type, id, title, date_published, copies))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Literature added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert literature: {str(e)}")

def insert_author(book_id, first_name, last_name, gender):
    try:
        # Connect to the database (create it if it doesn't exist)
        conn = sqlite3.connect("sample.db")
        c = conn.cursor()

        # Insert data into AuthorID table
        c.execute("INSERT INTO AuthorID (ID, Firstname, Lastname, Gender) VALUES (?, ?, ?, ?)",
                  (book_id, first_name, last_name, gender))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Author added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert author: {str(e)}")


def get_book_id(literature_id):
    try:
        conn = sqlite3.connect("sample.db")
        c = conn.cursor()

        # Get the BookID primary key for the given literature_id
        c.execute("SELECT BookID FROM BookID WHERE ID = ?", (literature_id,))
        book_id = c.fetchone()[0]

        conn.close()

        return book_id
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def show_add_literature_window():
    admin_window.destroy()  # Close the previous ADMIN window

    add_literature_window = tk.Tk()
    add_literature_window.title("Add Literature")
    add_literature_window.geometry("320x440")

    literature_types_frame = tk.LabelFrame(add_literature_window, text="Select Literature Types")
    literature_types_frame.grid(row=0, column=1, columnspan=5,padx=15, pady=15)

    literature_type_var = tk.StringVar()

    isbn_radio_button = tk.Radiobutton(literature_types_frame,
                                       text="ISBN (For Books)",
                                       variable=literature_type_var,
                                       value="ISBN")
    isbn_radio_button.pack()

    issn_radio_button = tk.Radiobutton(literature_types_frame,
                                       text="ISSN (For Journals and Magazines)",
                                       variable=literature_type_var,
                                       value="ISSN")
    issn_radio_button.pack()

    issn_isbn_ID_entry = tk.Entry(literature_types_frame)
    issn_isbn_ID_entry.pack()

    issn_isbn_ID_label = tk.Label(literature_types_frame, text="Insert ISBN/ISSN ID")
    issn_isbn_ID_label.pack()

    literature_info_frame = tk.LabelFrame(add_literature_window, text="Literature Information")
    literature_info_frame.grid(row=1, column=1, padx=15, pady=15)

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

        # Check if the literature_id (ISBN/ISSN ID) is provided
        literature_id = issn_isbn_ID_entry.get()
        if not literature_id:
                messagebox.showerror("Error", "ISBN/ISSN ID cannot be blank.")
                return

        # Check if the literature_title is provided
        literature_title = title_entry.get()
        if not literature_title:
            messagebox.showerror("Error", "Literature Title cannot be blank.")
            return

    copies_entry.bind("<FocusOut>", lambda event: validate_copies())

    date_label = tk.Label(literature_info_frame, text="Date Published")
    date_label.pack()

    date_entry = tk.Entry(literature_info_frame)
    date_entry.pack()

    authors_frame = tk.LabelFrame(add_literature_window, text="Authors")
    authors_frame.grid(row=1, column=2, padx=15, pady=15)

    gender_type_var = tk.StringVar()

    male_button = tk.Radiobutton(authors_frame, text="(Male)", variable=gender_type_var,
                                 value="MALE")
    male_button.pack()

    female_button = tk.Radiobutton(authors_frame, text="(Female)",
                                   variable=gender_type_var, value="FEMALE")
    female_button.pack()

    NA_button = tk.Radiobutton(authors_frame, text="(Unspecified)",
                               variable=gender_type_var, value="UNSPECIFIED")
    NA_button.pack()

    first_name_label = tk.Label(authors_frame, text="First Name")
    first_name_label.pack()

    first_name_entry = tk.Entry(authors_frame)
    first_name_entry.pack()

    last_name_label = tk.Label(authors_frame, text="Last Name")
    last_name_label.pack()

    last_name_entry = tk.Entry(authors_frame)
    last_name_entry.pack()

    def confirm_literature():
        literature_type = literature_type_var.get()
        literature_id = issn_isbn_ID_entry.get()
        literature_title = title_entry.get()
        literature_date_published = date_entry.get()
        num_copies = copies_entry.get()

        # Check if literature type is blank
        if not literature_type:
            messagebox.showerror("Error", "Please choose a literature type.")
            return

        # Check if ID is blank
        elif not literature_id:
            messagebox.showerror("Error", "Please input an ID.")
            return

        # Check if title is blank
        elif not literature_title:
            messagebox.showerror("Error", "Please input a title.")
            return

        # Check if the number of copies is a non-negative integer
        if not num_copies.isdigit() or int(num_copies) < 0:
            messagebox.showerror("Error", "Invalid input! Please enter a non-negative integer for No. Of Copies.")
            return

        # If the published date is not provided, set it to None
        if not literature_date_published:
            literature_date_published = None

        # Perform necessary actions with the literature information
        insert_literature(literature_type, literature_id, literature_title, literature_date_published, int(num_copies))

        # Fetch the BookID primary key after inserting the literature
        book_id = get_book_id(literature_id)

        # After inserting literature, also insert the author information
        gender = gender_type_var.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        # If first name or last name is blank, set them to "Unspecified"
        if not first_name:
            first_name = "   "
        if not last_name:
            last_name = "    "

        # Perform necessary actions with the author information
        insert_author(book_id, first_name, last_name, gender)

        # Reset all the input fields after confirming the literature
        literature_type_var.set("")
        issn_isbn_ID_entry.delete(0, "end")
        title_entry.delete(0, "end")
        date_entry.delete(0, "end")
        copies_entry.delete(0, "end")
        gender_type_var.set("MALE")  # Set gender to "MALE" by default
        first_name_entry.delete(0, "end")
        last_name_entry.delete(0, "end")

    confirm_button = tk.Button(add_literature_window, text="Confirm", command=confirm_literature)
    confirm_button.grid(row=3, column=1, padx=10, pady=10)

    def go_back_to_admin():
        add_literature_window.destroy()  # Close the add literature window
        show_admin_options()  # Show the admin options window again

    cancel_button = tk.Button(add_literature_window, text="Cancel", command=go_back_to_admin)
    cancel_button.grid(row=3, column=2, padx=10, pady=10)
    add_literature_window.mainloop()


def show_remove_literature_window():
    admin_window.destroy()  # Close the main window

    remove_lit_window = tk.Tk()
    remove_lit_window.title("Remove Book")
    remove_lit_window.geometry("300x300")

    # Frame for selecting the literature type (ISBN or ISSN)
    literature_type_frame = tk.LabelFrame(remove_lit_window, text="Remove Literature")
    literature_type_frame.pack(padx=15, pady=15)

    literature_type_var = tk.StringVar()

    isbn_radio_button = tk.Radiobutton(literature_type_frame,
                                       text="ISBN (For books)",
                                       variable=literature_type_var,
                                       value="ISBN")
    isbn_radio_button.pack()
    isbn_radio_button.deselect()

    issn_radio_button = tk.Radiobutton(literature_type_frame,
                                       text="ISSN (For Journals and Magazines)",
                                       variable=literature_type_var,
                                       value="ISSN")
    issn_radio_button.pack()

    # Frame for inputting literature information (title and ISBN/ISSN ID)
    input_id_frame = tk.LabelFrame(remove_lit_window, text="Input Information")
    input_id_frame.pack(padx=15, pady=15)

    book_name_label = tk.Label(input_id_frame, text="Input Title")
    book_name_label.pack()

    book_name_entry = tk.Entry(input_id_frame)
    book_name_entry.pack()

    isbn_issn_label = tk.Label(input_id_frame, text="ISBN/ISSN ID")
    isbn_issn_label.pack()

    isbn_issn_entry = tk.Entry(input_id_frame)
    isbn_issn_entry.pack()

    # Function to confirm the removal of literature
    def confirm_removal():
        title = book_name_entry.get()
        isbn_issn_id = isbn_issn_entry.get()

        # Check if all inputs are blank
        if not title.strip() and not isbn_issn_id.strip() and not literature_type_var.get():
            messagebox.showerror("Error", "Please enter the Title and ISBN/ISSN ID and Choose Literature type.")
            return

        # Check if Literature type is not chosen but it has data Title and ID
        if not literature_type_var.get() and title.strip() and isbn_issn_id.strip():
            messagebox.showerror("Error", "Please choose a literature type.")
            return

        # Check if Title is blank but it has literature type and ID
        if literature_type_var.get() and not title.strip() and isbn_issn_id.strip():
            messagebox.showerror("Error", "Please fill in the Title to be removed.")
            return

        # Check if ID is blank but it has literature type and Title
        if literature_type_var.get() and title.strip() and not isbn_issn_id.strip():
            messagebox.showerror("Error", "Please fill in the ISBN/ISSN ID to be removed.")
            return

        # Validate inputs
        if not title.strip() or not validate_integer(isbn_issn_entry):
            messagebox.showerror("Error", "Invalid input! Please enter a valid Title and ISBN/ISSN ID.")
            return



        try:
            conn = sqlite3.connect("sample.db")
            c = conn.cursor()

            # Check if the record exists in the BookID table
            c.execute("SELECT BookID FROM BookID WHERE Title = ? AND ID = ?", (title, int(isbn_issn_id)))
            book_id = c.fetchone()

            if book_id:
                # Remove the record from the BookID table
                c.execute("DELETE FROM BookID WHERE BookID = ?", (book_id[0],))

                # Remove the corresponding author record from the AuthorID table using the matching ID
                c.execute("DELETE FROM AuthorID WHERE ID = ?", (book_id[0],))

                # Commit changes and close connection
                conn.commit()
                conn.close()

                messagebox.showinfo("Success",
                                    f"The literature with Title: {title} and ID: {isbn_issn_id} has been removed.")
            else:
                messagebox.showerror("Error",
                                     f"No matching literature found with Title: {title} and ID: {isbn_issn_id}.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove literature: {str(e)}")

    # Frame for the buttons
    button_frame = tk.Frame(remove_lit_window)
    button_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

    # Button to confirm the removal
    confirm_button = tk.Button(button_frame, text="Confirm", command=confirm_removal)
    confirm_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Function to go back to the admin options window
    def go_back_to_adminn():
        remove_lit_window.destroy()  # Close the "Remove Literature" window
        show_admin_options()  # Show the admin options window again

    # Button to cancel and go back to admin options
    cancel_button = tk.Button(button_frame, text="Cancel", command=go_back_to_adminn)
    cancel_button.pack(side=tk.LEFT, padx=10, pady=10)

    remove_lit_window.mainloop()

def admin_window_quit():
    admin_window.destroy()  # Close the borrow book window
    create_main_window()



create_main_window()

window.mainloop()