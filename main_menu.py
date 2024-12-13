from core_operations import *
from utilities import *


def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Remove Book")
        print("5. Search Books")
        print("6. Lend Book")
        print("7. Display lend info")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            search_books()
        elif choice == "6":
            lend_book()
        elif choice == "7":
            display_lend_info()
        elif choice == "0":
            if confirm_action("Are you sure you want to exit?"):
                print("Exiting program. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()