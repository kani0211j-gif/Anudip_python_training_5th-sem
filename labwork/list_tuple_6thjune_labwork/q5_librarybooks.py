# Given data
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]
# 1. Display unavailable books
for item in books:
    if item[1] == 0:
        print("Unavailable Books:",item[0])

# 2. Find all books with more than 2 copies
print("\nBooks with more than 2 copies:")
for item in books:
    if item[1] > 2:
        print(item[0], "with", item[1], "copies")

# 3. Count available books (books in stock)
available_books_count = 0
for item in books:
    if item[1] > 0:
        available_books_count = available_books_count + 1
print("\nTotal available book titles:", available_books_count)

# 4. Stop searching once a requested book is found
search = "Java Programming"
print("\nSearching database for:", search)
for item in books:
    print("Checking database record:", item[0])
    if item[0] == search:
        print("-> Book Found! Stock available:", item[1], "copies.")
        break
print("\n")

