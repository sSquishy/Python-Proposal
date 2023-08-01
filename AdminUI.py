def borrow_book(library, book_title):
    if book_title in library and library[book_title] > 0:
        library[book_title] -= 1
        print(f"You have successfully borrowed '{book_title}'.")
    elif book_title in library and library[book_title] == 0:
        print(f"Sorry, all copies of '{book_title}' are currently borrowed.")
    else:
        print(f"Sorry, '{book_title}' is not available in the library.")

def return_book(library, book_title):
    if book_title in library:
        library[book_title] += 1
        print(f"You have successfully returned '{book_title}'.")
    else:
        print(f"Sorry, '{book_title}' was not borrowed from the library.")

def main():
    library = {
        "Book A": 2,  # Replace the book titles and available copies with your own library data
        "Book B": 1,
        "Book C": 3,
    }

    while True:
        print("\nLibrary Catalog:")
        for book, copies in library.items():
            print(f"{book} - Copies available: {copies}")

        print("\n1. Borrow a book")
        print("2. Return a book")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_to_borrow = input("Enter the title of the book you want to borrow: ")
            borrow_book(library, book_to_borrow)
        elif choice == 2:
            book_to_return = input("Enter the title of the book you want to return: ")
            return_book(library, book_to_return)
        elif choice == 3:
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
