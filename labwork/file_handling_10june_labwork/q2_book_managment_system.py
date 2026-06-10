''' Library Book Issue System Problem Statement
A library stores book information in books.txt.
File Format
B101,Python Basics,5
B102,Java Programming,2
B103,Data Science,0
B104,DBMS,3
B105,Machine Learning,1
B106,Operating Systems,4
B107,Networking,2
B108,Cyber Security,6
B109,Cloud Computing,0
B110,Web Development,3
Requirements
Develop a program to:
1. Display all books.
2. Search a book using Book ID.
3. Issue a book (decrease quantity by 1).
4. Return a book (increase quantity by 1).
5. Display unavailable books.
6. Display books requiring restocking (copies < 2).
7. Update the file after every issue/return operation'''
#-----------------------------------------------------------------------------------------
# Function to display all books
def display_books():
    filev = open('books.txt', 'r')
    if not filev: #to check file is open or not
        exit("Error opening the file.")

    content = filev.read()

    if not content: #to check file is empty or not
        print("The file is empty.")
    else:
        print("Book ID, Book Name, Quantity")
        print(content)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to search a book using Book ID
def search_book():
    book_id = input("Enter the Book ID to search: ")

    filev = open('books.txt', 'r')
    if not filev: #to check file is open or not
        exit("Error opening the file.")

    found = False

    lines = filev.readlines()

    for line in lines:

        data = line.strip().split(',')

        if data[0] == book_id:

            print("Book Found")
            print("Book ID :", data[0])
            print("Book Name :", data[1])
            print("Quantity :", data[2])

            found = True
            break

    if found == False:
        print("Book not found.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to issue a book (decrease quantity by 1)
def issue_book():

    book_id = input("Enter the Book ID to issue: ")

    filev = open('books.txt', 'r')
    if not filev: #to check file is open or not
        exit("Error opening the file.")

    lines = filev.readlines()
    filev.close()

    found = False

    for i in range(len(lines)):

        data = lines[i].strip().split(',')

        if data[0] == book_id:

            found = True

            qty = int(data[2])

            if qty > 0:

                qty = qty - 1

                lines[i] = data[0] + "," + data[1] + "," + str(qty) + "\n"

                print("Book issued successfully.")

            else:

                print("Book is unavailable.")

    if found == False:
        print("Book not found.")

    filev = open('books.txt', 'w')

    for line in lines:
        filev.write(line)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to return a book (increase quantity by 1)
def return_book():

    book_id = input("Enter the Book ID to return: ")

    filev = open('books.txt', 'r')
    if not filev: #to check file is open or not
        exit("Error opening the file.")

    lines = filev.readlines()
    filev.close()

    found = False

    for i in range(len(lines)):

        data = lines[i].strip().split(',')

        if data[0] == book_id:

            found = True

            qty = int(data[2])

            qty = qty + 1

            lines[i] = data[0] + "," + data[1] + "," + str(qty) + "\n"

            print("Book returned successfully.")

    if found == False:
        print("Book not found.")

    filev = open('books.txt', 'w')

    for line in lines:
        filev.write(line)

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to display unavailable books
def unavailable_books():

    filev = open('books.txt', 'r')
    if not filev: #to check file is open or not
        exit("Error opening the file.")

    found = False

    lines = filev.readlines()

    print("Unavailable Books")

    for line in lines:

        data = line.strip().split(',')
        if len(data) != 3:
           continue

        if int(data[2]) == 0:

            print(line.strip())

            found = True

    if found == False:
        print("No unavailable books found.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Function to display books requiring restocking
def restocking_books():

    filev = open('books.txt', 'r')
    if not filev: #to check file is open or not
        exit("Error opening the file.")

    found = False

    lines = filev.readlines()

    print("Books Requiring Restocking")

    for line in lines:

        data = line.strip().split(',')
        if len(data) != 3:
           continue


        if int(data[2]) < 2:

            print(line.strip())

            found = True

    if found == False:
        print("No books require restocking.")

    filev.close()
#-----------------------------------------------------------------------------------------
# Main Menu
while True:

    print("\n===== LIBRARY BOOK ISSUE SYSTEM =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    #-------------------------------------------------------------------------------------

    if choice == 1:
        display_books()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")

#-----------------------------------------------------------------------------------------
