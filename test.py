def get_next_book_id():
    # Function to get the next book ID by reading the last used book ID from a file and incrementing it
    try:
        with open("book_id.txt", "r") as file:
            last_book_id = int(file.read())
    except FileNotFoundError:
        # If the file is not found (i.e., it's the first time running the program), start with 1
        last_book_id = 0

    next_book_id = last_book_id + 1

    # Save the next book ID to the file for future use
    with open("book_id.txt", "w") as file:
        file.write(str(next_book_id))

    return next_book_id


def main():
    while True:
        input("Press Enter to input a new book:")
        book_id = get_next_book_id()
        print("Book ID:", book_id)


if __name__ == "__main__":
    main()
