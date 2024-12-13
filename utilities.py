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

    print(f"{'Title':<30}{'Author':<30}{'ISBN':<15}{'Year':<10}{'Quantity':<10}{'Timestamp':<20}")
    print("-" * 110)
    for book in books:
        print(f"{book['title']:<30}{book['author']:<30}{book['isbn']:<15}{book['year']:<10}{book['quantity']:<10}{book.get('timestamp', 'N/A'):<20}")

# Function to display Lend books
def display_lend_info():
    lend_info = load_json(LEND_FILE)
    if not lend_info:
        print("No books have been lent.")
    else:
        print("List of lent books:")
        for lend_info in lend_info:
            # Safely access keys using get() method
            borrower_name = lend_info.get('borrower_name', 'Unknown Borrower')
            borrower_phone = lend_info.get('borrower_phone', 'Unknown Phone')
            book_title = lend_info.get('book_title', 'Unknown Title')
            lend_date = lend_info.get('lend_date', 'Unknown Date')
            return_date = lend_info.get('return_date', 'Not returned yet')

            # Print the details of the lent book
            print(f"Title: {lend_info['title']}, Borrower: {lend_info['borrower']}, "
                  f"Lent Date: {lend_info['lent_date']}, Return Date: {lend_info['return_date'] if lend_info.get('return_date') else 'Not returned yet'}")
            


# "borrower_name": borrower_name,
#                     "borrower_phone": borrower_phone,
#                     "book_title": book['title'],
#                     "lend_date": lend_date,
#                     "return_date": return_date