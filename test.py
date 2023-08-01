import sqlite3

def create_connection(database_name):
    try:
        conn = sqlite3.connect('testt.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def create_table(conn):
    try:
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_date TEXT
        )
        '''
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(e)

def insert_data(conn, title, author, published_date):
    try:
        insert_data_query = '''
        INSERT INTO books (title, author, published_date)
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(insert_data_query, (title, author, published_date))
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(e)

def main():
    database_name = "library.db"
    conn = create_connection(database_name)
    if conn is not None:
        create_table(conn)

        print("Enter book details:")
        title = input("Title: ")
        author = input("Author: ")
        published_date = input("Published Date: ")

        insert_data(conn, title, author, published_date)

        conn.close()

if __name__ == "__main__":
    main()
