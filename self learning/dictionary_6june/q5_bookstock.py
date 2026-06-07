books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# show books out of stock
print("--- Out of Stock Books ---")
for book, copies in books.items():
    if copies == 0:
        print(book)

# count available unique titles
available_types = 0
for copies in books.values():
    if copies > 0:
        available_types += 1
print("\nAvailable book categories:", available_types)

# find book with maximum stock
most_copied_book = ""
max_copies = 0
for book, copies in books.items():
    if copies > max_copies:
        max_copies = copies
        most_copied_book = book
print("\nBook with maximum stock:", most_copied_book, "Copies:", max_copies)

# list books with less than 3 copies
low_stock_books = []
for book, copies in books.items():
    if copies < 3:
        low_stock_books.append(book)
print("\nBooks with less than 3 copies:", low_stock_books)

# count total actual books available
total_books = 0
for copies in books.values():
    total_books += copies
print("\nTotal books available:", total_books)

