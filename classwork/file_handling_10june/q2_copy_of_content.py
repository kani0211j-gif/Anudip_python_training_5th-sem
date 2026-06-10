#------------------------------------------------------
# Program to copy content from one file into another

# Open source file in read mode
file1 = open("apple.txt", "r")

# To check file is open or not
if not file1:
    exit("Error opening the file.")

# Read entire content
content = file1.read()

# To check file is empty or not
if not content:
    print("The file is empty.")
else:

    # Open destination file in write mode
    file2 = open("orange.txt", "w")

    # Write content into second file
    file2.write(content)

    print("File copied successfully.")

    # Close destination file
    file2.close()

# Close source file
file1.close()

