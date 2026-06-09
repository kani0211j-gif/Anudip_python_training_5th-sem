'''Problem Statement
A customer submits a review:
This product is excellent excellent excellent and very useful
Tasks
1. Count total words.
2. Create a dictionary containing word frequencies.
3. Find the most frequently used word.
4. Find all words appearing only once.
5. Count words having more than 5 characters.
6. Display words in reverse order.
7. Create a list of unique words.
----------------------------------------------------------
'''
# to ask user to enter review
review = input("Enter Review: ").strip()

# validating review
if review == "":
    exit("Review cannot be empty.")

print("-----------------------------------------")

# convert review into list of words
word_list = review.split()

# ------------------------------------------------

# 1. Count total words
print("Total Words:", len(word_list))
# ------------------------------------------------
# 2. Create a dictionary containing word frequencies
frequency = {}

for word in word_list:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print("Word Frequencies:")

for word in frequency:
    print(word, "->", frequency[word])
# ------------------------------------------------
# 3. Find the most frequently used word
most_frequent_word = ""

highest_count = 0

for word in frequency:

    if frequency[word] > highest_count:

        highest_count = frequency[word]

        most_frequent_word = word

print("Most Frequent Word:", most_frequent_word)
# ------------------------------------------------
# 4. Find all words appearing only once

single_words = []

for word in frequency:

    if frequency[word] == 1:

        single_words.append(word)

print("Words Appearing Once:", single_words)
# ------------------------------------------------
# 5. Count words having more than 5 characters

count_long_words = 0

for word in word_list:

    if len(word) > 5:

        count_long_words += 1
print("Words Having More Than 5 Characters:", count_long_words)
# ------------------------------------------------
# 6. Display words in reverse order
reverse_words = word_list[::-1]
print("Words In Reverse Order:", reverse_words)
# ------------------------------------------------
# 7. Create a list of unique words
unique_words = []

for word in word_list:

    if word not in unique_words:

        unique_words.append(word)

print("Unique Words:", unique_words)
#output will be
'''
Total Words: 9
Word Frequencies:
This -> 1
product -> 1
is -> 1
excellent -> 3
and -> 1
very -> 1
useful -> 1
Most Frequent Word: excellent
Words Appearing Once: ['This', 'product', 'is', 'and', 'very', 'useful']
Words Having More Than 5 Characters: 5
Words In Reverse Order: ['useful', 'very', 'and', 'excellent', 'excellent', 'excellent', 'is', 'product', 'This']
Unique Words: ['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']'''

