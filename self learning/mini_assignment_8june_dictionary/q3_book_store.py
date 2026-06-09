'''3. Smart Library Management System
Problem Statement
Create a digital library management system.
Example Structure
library = {
 "B101": {
 "title": "Python Basics",
 "author": "ABC",
 "copies": 5
 }
}
Maintain records of at least 30 books.
Requirements
1. Add a book.
2. Remove a book.
3. Search a book by ID.
4. Search by title.
5. Update available copies.
6. Issue a book.
7. Return a book.
8. Display books with fewer than 3 copies.
9. Display books that are unavailable.
10. Find the most available book.
11. Generate a restocking report.
12. Create a separate dictionary of books requiring immediate purchase.
Challenge
Generate a complete library summary report.'''
#----------------------------------------------------------------------------------------
# to create a menu-driven program for inventory management
#----------------------------------------------------------------------------------------
#database of books
library = {
 "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
 "B102": {"title": "Data Structures", "author": "DEF", "copies": 3},
 "B103": {"title": "Algorithms", "author": "GHI", "copies": 0},
 "B104": {"title": "Machine Learning", "author": "JKL", "copies": 2},
 "B105": {"title": "Artificial Intelligence", "author": "MNO", "copies": 4},
 "B106": {"title": "Deep Learning", "author": "PQR", "copies": 1},
    "B107": {"title": "Natural Language Processing", "author": "STU", "copies": 0},
    "B108": {"title": "Computer Vision", "author": "VWX", "copies": 6},
    "B109": {"title": "Data Science", "author": "YZA", "copies": 3},
    "B110": {"title": "Big Data", "author": "BCD", "copies": 2},
    "B111": {"title": "Cloud Computing", "author": "EFG", "copies": 5},
    "B112": {"title": "Cybersecurity", "author": "HIJ", "copies": 0},
    "B113": {"title": "Blockchain", "author": "KLM", "copies": 4},
    "B114": {"title": "Internet of Things", "author": "NOP", "copies": 1},
    "B115": {"title": "Quantum Computing", "author": "QRS", "copies": 0},
    "B116": {"title": "Augmented Reality", "author": "TUV", "copies": 3},
    "B117": {"title": "Virtual Reality", "author": "WXY", "copies": 2},
    "B118": {"title": "5G Technology", "author": "ZAB", "copies": 4},
    "B119": {"title": "Edge Computing", "author": "CDE", "copies": 0},
    "B120": {"title": "Robotics", "author": "FGH", "copies": 5},
    "B121": {"title": "Autonomous Vehicles", "author": "IJK", "copies": 1},
    "B122": {"title": "Wearable Technology", "author": "LMN", "copies": 0},
    "B123": {"title": "3D Printing", "author": "OPQ", "copies": 2},
    "B124": {"title": "Nanotechnology", "author": "RST", "copies": 3},
    "B125": {"title": "Biotechnology", "author": "UVW", "copies": 0},
    "B126": {"title": "Genomics", "author": "XYZ", "copies": 4},
    "B127": {"title": "Proteomics", "author": "ABC", "copies": 1},
    "B128": {"title": "Metabolomics", "author": "DEF", "copies": 0},
    "B129": {"title": "Systems Biology", "author": "GHI", "copies": 2},
    "B130": {"title": "Synthetic Biology", "author": "JKL", "copies": 3}
}
#----------------------------------------------------------------------------------------
# to maintain the menu driven program
#----------------------------------------------------------------------------------------
while True:
    print("\nMenu:")
    print("1. Display all books")
    print("2. Add a new book")
    print("3. Remove a book")
    print("4. Search a book by ID")
    print("5. Search a book by title")
    print("6. Update available copies")
    print("7. Issue a book")
    print("8. Return a book")
    print("9. Display books with fewer than 3 copies")
    print("10. Display unavailable books")
    print("11. Find the most available book")
    print("12. Generate a restocking report")
    print("13. Create a dictionary of books requiring immediate purchase")
    print("14. Library Summary Report")
    print("15. Exit")
    #----------------------------------------------------------------------------------------
    # to take input from the user
    choice = int(input("Enter your choice (1-15): "))
    #----------------------------------------------------------------------------------------
    # to display all books
    if choice == 1:
        print("\nAll Books:")
        for bid in library:
            print(bid, ":", library[bid])
    #----------------------------------------------------------------------------------------
    # to add a new book
    elif choice == 2:
        bid = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        copies = int(input("Enter number of copies: "))
        library[bid] = {"title": title, "author": author, "copies": copies}
        print("Book added successfully.")
    #----------------------------------------------------------------------------------------
    # to remove a book
    elif choice == 3:
        bid = input("Enter book ID to remove: ")
        if bid in library:
            del library[bid]
            print("Book removed successfully.")
        else:
            print("Book not found.")
    #----------------------------------------------------------------------------------------
    # to search a book by ID
    elif choice == 4:
        bid = input("Enter book ID to search: ")
        if bid in library:
            print("Book found:", library[bid])
        else:
            print("Book not found.")
    #----------------------------------------------------------------------------------------
    # to search a book by title
    elif choice == 5:
        title = input("Enter book title to search: ")
        title_found = False
        for bid in library:
            if library[bid]["title"].lower() == title.lower():
                print("Book found:", library[bid])
                title_found = True
                break
        if not title_found:
            print("Book not found.")
    #----------------------------------------------------------------------------------------
    # to update available copies
    elif choice == 6:
        bid = input("ENTER BOOK ID: ")
        copies = int(input("Enter new number of copies: "))
        if bid in library:
            library[bid]["copies"] = copies
            print("Copies updated successfully.")
        else:
            print("Book not found.")
    #----------------------------------------------------------------------------------------
    # to issue a book
    elif choice == 7:
        bid = input("enter the book id you want to issue: ")
        if bid in library:
            if library[bid]["copies"] > 0:
                library[bid]["copies"] -= 1
                print("Book issued successfully.")
            else:
                print("Book is currently unavailable.")
        else:
            print("Book not found.")
    #----------------------------------------------------------------------------------------
    # to return a book
    elif choice == 8:
        bid = input("enter the book id you want to return:")
        if bid in library:
            library[bid]["copies"] += 1
            print("Book returned successfully.")
        else:
            print("Book not found.")
    #----------------------------------------------------------------------------------------
    # to display books with fewer than 3 copies
    elif choice == 9:

         found = False

         print("\nBooks with fewer than 3 copies:")

         for bid in library:
             if library[bid]["copies"] < 3:
                print(bid, ":", library[bid])
                found = True

         if not found:
            print("No books with fewer than 3 copies.")
    #----------------------------------------------------------------------------------------
    # to display unavailable books 
    elif choice == 10:
        print("\nUnavailable Books:")
        for bid in library:
            if library[bid]["copies"]==0:
                print(bid, ":", library[bid])
    #----------------------------------------------------------------------------------------
    # to find the most available book
    elif choice == 11:
        dict1 = list(library.items())
        most_id = dict1[0][0]
        most_copies = dict1[0][1]["copies"]
        for bid in library:
            if library[bid]["copies"] > most_copies:
                most_id = bid
                most_copies = library[bid]["copies"]
        print("Most Available Book:", most_id, ":", library[most_id])
    #----------------------------------------------------------------------------------------
    # to generate a restocking report
    elif choice == 12:
        print("\nRestocking Report:")
        for bid in library:
            if library[bid]["copies"] < 3:
                print(bid, ":", library[bid])
    #----------------------------------------------------------------------------------------
    # to create a dictionary of books requiring immediate purchase
    elif choice == 13:
        restock_books = {} # empty dictionary to store books requiring immediate purchase(62 bytes)
        for bid in library:
            if library[bid]["copies"] == 0:
                restock_books[bid] = library[bid]
        print("\nBooks Requiring Immediate Purchase:")
        for bid in restock_books:
            print(bid, ":", restock_books[bid])     
    #----------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
# to generate complete library summary report
    elif choice == 14:

    # most available book
         dict1 = list(library.items())

         most_id = dict1[0][0]
         most_copies = dict1[0][1]["copies"]

         unavailable_count = 0
         restocking_count = 0
         immediate_purchase_count = 0

         for bid in library:

            if library[bid]["copies"] > most_copies:
                most_id = bid
                most_copies = library[bid]["copies"]

            if library[bid]["copies"] == 0:
               unavailable_count += 1

            if library[bid]["copies"] < 3:
               restocking_count += 1

            if library[bid]["copies"] == 0:
               immediate_purchase_count += 1

         print("\n====================================")
         print("      LIBRARY SUMMARY REPORT")
         print("Total Books :", len(library))

         print("Most Available Book :", most_id)
         print("Title :", library[most_id]["title"])
         print("Author :", library[most_id]["author"])
         print("Copies :", most_copies)

         print("Unavailable Books :", unavailable_count)

         print("Books Needing Restocking :", restocking_count)

         print("Books Requiring Immediate Purchase :", immediate_purchase_count)

         print("====================================")

#---------------------------------------------------------------------------------------
    # to exit the program
    elif choice == 15:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 15.")
    #----------------------------------------------------------------------------------------
    

