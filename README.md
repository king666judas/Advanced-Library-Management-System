Developer's Note: Book Management Program
----------------------------------------------------------
**Overview**

The Book Management Program is a console-based application designed to manage a small library's operations effectively. 
It allows users to perform core functionalities such as adding books, lending books, viewing available books, and tracking lent books. 
The program is built with simplicity and efficiency in mind, using JSON files to store data persistently.

----------------------------------------------------------
**Key Features**

**Add Book:**
Users can add new books to the library.
Validation ensures no duplicate entries by title or ISBN.

----------------------------------------------------------
**Lend Book:**
Facilitates lending books to borrowers.
Records borrower's name, phone number, lend date, and return date.
Prevents lending of the same book title simultaneously.

----------------------------------------------------------
**View Books:**
Displays all books in the library in a structured table format.
Includes book details such as title, author, ISBN, year, quantity, and price.

----------------------------------------------------------
**View Lent Books:**
Displays all currently lent books in an organized table.
Shows borrower details and lending/return dates.

----------------------------------------------------------
**Technical Details:**
Programming Language: Python
Data Storage: JSON files for persistence of library and lending data.

----------------------------------------------------------
**Input Validation:**
Ensures proper data types and formats (e.g., positive numbers for quantity and price).
Prevents entry of duplicate book titles or ISBNs.

----------------------------------------------------------
**Error Handling:**
Handles missing files by initializing empty data structures.
Safely accesses dictionary keys to avoid runtime errors.

----------------------------------------------------------
**Files Used**
library.json:
Stores the list of books with attributes such as title, author, ISBN, year, quantity, and price.

lend_info.json:
Stores details of currently lent books, including borrower information and lending dates.

----------------------------------------------------------
