from file_handler import *
from input_validation import *

# Function to Search books by Name, Author or Year
def search_books():
    books = load_json(LIBRARY_FILE)
    print("Search by:")
    print("1. Name")
    print("2. Author")
    print("3. Year")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = validate_non_empty_string(input("Enter book name: "), "Book Name")
        results = [book for book in books if name.lower() in book['title'].lower()]
    elif choice == "2":
        author = validate_non_empty_string(input("Enter author name: "), "Author Name")
        results = [book for book in books if author.lower() in book['author'].lower()]
    elif choice == "3":
        year = validate_positive_int(input("Enter year: "), "Year")
        results = [book for book in books if book['year'] == year]
    else:
        print("Invalid choice.")
        return

    if results:
        print(f"{'Title':<30}{'Author':<30}{'ISBN':<15}{'Year':<10}{'Quantity':<10}")
        print("-" * 95)
        for book in results:
            print(f"{book['title']:<30}{book['author']:<30}{book['isbn']:<15}{book['year']:<10}{book['quantity']:<10}{book.get('timestamp', 'N/A'):<20}")
    else:
        print("No matching books found.")

# Function to View books
def view_books():
    books = load_json(LIBRARY_FILE)
    if not books:
        print("No books in the library.")
        return

    print(f"| {'Title':<30} | {'Author':<30} | {'ISBN':<15} | {'Year':<10} | {'Quantity':<10} | {'Timestamp':<20} |")
    print("-" * 110)
    for book in books:
        print(f"| {book['title']:<30} | {book['author']:<30} | {book['isbn']:<15} | {book['year']:<10} | {book['quantity']:<10} | {book.get('timestamp', 'N/A'):<20} |")

# Function to display Lend books
def display_lent_books():
    lent_books = load_json(LEND_FILE)
    if not lent_books:
        print("No books have been lent.")
    else:
        # Table headers
        print("-" * 95)
        print(f"| {'Book Title':<25} | {'Borrower Name':<20} | {'Phone':<15} | {'Lend Date':<20} | {'Return Date':<15} |")
        print("-" * 95)

        for lent_book in lent_books:
            # Safely access keys using get() method
            borrower_name = lent_book.get('borrower_name', 'Unknown Borrower')
            borrower_phone = lent_book.get('borrower_phone', 'Unknown Phone')
            book_title = lent_book.get('book_title', 'Unknown Title')
            lend_date = lent_book.get('lend_date', 'Unknown Date')
            return_date = lent_book.get('return_date', 'Not returned yet')

            # Print the details of the lent book
            print(f"| {book_title:<25} | {borrower_name:<20} | {borrower_phone:<15} | {lend_date:<20} | {return_date:<15} |")

        # End table border
        print("-" * 95)