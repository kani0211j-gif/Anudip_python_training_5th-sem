'''Classwork : To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file.'''
#----------------------------------------------------------------------
# Open the file in read mode
filev = open('apple.txt', 'r')
#to check file is open or not
if not filev:
    exit("Error opening the file.")
# Read the entire content of the file
content = filev.read()
#to check file is empty or not
if not content:
    print("The file is empty.")
else:
    # Initialize counters
    vowel_count = 0
    char_count = 0
    line_count = 0
    # Define vowels
    vowels = 'AEIOUaeiou'
    # Loop through each character in the content
    for char in content:
        char_count += 1  # Increment character count
        if char in vowels:
            vowel_count += 1  # Increment vowel count
        if char == '\n':
            line_count = content.count('\n')  # Increment line count
    # Print the results
    print(f"Number of Vowels in file: {vowel_count}")
    print(f"Number of characters in the file: {char_count}")
    print(f"Number of lines in the file: {line_count}")
#-----------------------------------------------------------------------
#output will be
Number of Vowels in file: 13
Number of characters in the file: 39
Number of lines in the file: 3

