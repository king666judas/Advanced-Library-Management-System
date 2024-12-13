from file_handler import *
from input_validation import *
from datetime import datetime

# Function to Add book information
def add_book():
    books = load_json(LIBRARY_FILE)

    while True:
        title = validate_non_empty_string(input("Enter book title: "), "Title")
        if title:
            break

    while True:
        author = validate_non_empty_string(input("Enter author(s): "), "Author")
        if author:
            break

    while True:
        isbn = validate_non_empty_string(input("Enter ISBN: "), "ISBN")
        if isbn:
            break
    
    # Check if the book already exists by title or ISBN
    for book in books:
        if book['title'] == title:
            print("A book with this title already exists.")
            return  # Stop adding the book
        if book['isbn'] == isbn:
            print("A book with this ISBN already exists.")
            return  # Stop adding the book

    while True:
        year = validate_positive_int(input("Enter publishing year: "), "Year")
        if year is not None:
            break

    while True:
        quantity = validate_positive_int(input("Enter quantity: "), "Quantity")
        if quantity is not None:
            break
    
    while True:
        try:
            price = float(input("Enter price: "))
            if price <= 0:
                raise ValueError
            break
        except ValueError:
            print("Price must be a positive number.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    books.append({
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "quantity": quantity,
        "price": price,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_json(LIBRARY_FILE, books)
    print("Book added successfully on {timestamp}!")

# Function to Update book information
def update_book():
    books = load_json(LIBRARY_FILE)
    search_title = validate_non_empty_string(input("Enter the title of the book to update: "), "Title")
    if not search_title:
        return

    for book in books:
        if book["title"].lower() == search_title.lower():
            if confirm_action("Do you want to update this book?"):
                print("Leave a field blank to keep the current value.")
                book['title'] = input(f"Enter new title ({book['title']}): ").strip() or book['title']
                book['author'] = input(f"Enter new author(s) ({book['author']}): ").strip() or book['author']
                book['isbn'] = input(f"Enter new ISBN ({book['isbn']}): ").strip() or book['isbn']
                new_year = input(f"Enter new publishing year ({book['year']}): ").strip()
                book['year'] = int(new_year) if new_year else book['year']
                new_quantity = input(f"Enter new quantity ({book['quantity']}): ").strip()
                book['quantity'] = int(new_quantity) if new_quantity else book['quantity']
                new_price = input(f"Enter new price ({book['price']}): ").strip()
                book['price'] = float(new_price) if new_price else book['price']
                book['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                save_json(LIBRARY_FILE, books)
                print(f"Book updated successfully on {book['timestamp']}!")
            return

    print("Book not found.")

# Function to Remove books
def remove_book():
    books = load_json(LIBRARY_FILE)
    search_title = validate_non_empty_string(input("Enter the title of the book to remove: "), "Title")
    if not search_title:
        return

    for book in books:
        if book["title"].lower() == search_title.lower():
            if confirm_action("Do you want to remove this book?"):
                books.remove(book)
                save_json(LIBRARY_FILE, books)
                print("Book removed successfully!")
            return

    print("Book not found.")

# Function to Lend books
def lend_book():
    books = load_json(LIBRARY_FILE)
    lend_info = load_json(LEND_FILE)

    search_title = validate_non_empty_string(input("Enter the title of the book to lend: "), "Title")
    if not search_title:
        return

    for book in books:
        if book["title"].lower() == search_title.lower():
            if book['quantity'] > 0:
                borrower_name = validate_non_empty_string(input("Enter borrower's name: "), "Borrower's Name")
                borrower_phone = validate_non_empty_string(input("Enter borrower's phone: "), "Borrower's Phone")
                lend_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return_date = input("Enter return date (YYYY-MM-DD): ")

                lend_info.append({
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book['title'],
                    "lend_date": lend_date,
                    "return_date": return_date
                })

                book['quantity'] -= 1
                save_json(LIBRARY_FILE, books)
                save_json(LEND_FILE, lend_info)
                print("Book lent successfully!")
            else:
                print("There are not enough books available to lend.")
            return

    print("Book not found.")