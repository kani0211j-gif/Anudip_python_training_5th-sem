'''
3. Chat Message Analytics
Problem Statement
A chat application stores a message:
Python is awesome and Python is easy to learn
Tasks
Write a program to:
1. Count total characters.
2. Count total words.
3. Find the longest word.
4. Find the shortest word.
5. Count how many times the word "Python" appears.
6. Create a list of words having more than 4 characters.
7. Display all words starting with a vowel.
8. Count the number of vowels and consonants.
Sample Output
Message:
Python is awesome and Python is easy to learn
Total Characters: 45
Total Words: 8
Longest Word: awesome
Shortest Word: is
Occurrences of Python: 2
Words Longer Than 4 Characters:
['Python', 'awesome', 'Python', 'learn']
Vowels: 16
Consonants: 22
'''
#-----------------------------------------------------
#Taking input from user
Message = input("enter your message:").strip() 
#------------------------------------------------------
#count of total character
print("total_character = ",len(Message))
#------------------------------------------------------
#count total words
word_list=Message.split()
print("Total words: ",len(word_list))
#--------------------------------------------------------
#to find the longest word
longest_word = word_list[0]

for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word:", longest_word)
#---------------------------------------------------------
#to find the shortest word
shortest_word=word_list[0]
for word in word_list:
    if len(word)<len(shortest_word):
        shortest_word=word
print("shortest word: ",shortest_word)
#--------------------------------------------------------
# 5. Count how many times the word "Python" appears
python_count = word_list.count("python")

print("Occurrences of Python:", python_count)

# ------------------------------------------------

# 6. Create a list of words having more than 4 characters
long_words = [] #empty list initialized by none

for word in word_list:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:", long_words)

# ------------------------------------------------
# 7. Display all words starting with a vowel
vowel_words = [] #empty list initialized by none

for word in word_list:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words Starting With Vowel:", vowel_words)

# ------------------------------------------------

# 8. Count the number of vowels and consonants
vowels = 0
consonants = 0

for ch in Message.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)






