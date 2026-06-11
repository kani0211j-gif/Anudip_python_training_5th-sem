'''Chat Message Analytics Dashboard
Problem Statement
A messaging application wants to analyze chat messages.
Store at least 20 chat messages in a list.
Requirements
For each message:
1. Count total words.
2. Count total characters.
3. Count vowels and consonants.
4. Find longest word.
5. Find shortest word.
6. Count occurrence of each word.
7. Display repeated words.
8. Display words starting with vowels.
9. Display words longer than 5 characters.
10. Create a dictionary containing word frequencies.
Challenge
Generate a report showing:
Most Frequently Used Word
Longest Message
Shortest Message
Average Words Per Message'''
#----------------------------------------------------------------------------
#to store msg in list
messages = [
    "hello how are you",
    "i am doing great today",
    "python is very interesting",
    "hello everyone welcome",
    "coding makes life easier",
    "practice makes perfect",
    "data science is amazing",
    "hello python learners",
    "machine learning is powerful",
    "keep learning every day",
    "python programming is fun",
    "chat applications are useful",
    "communication is important",
    "hello friends good morning",
    "coding improves problem solving",
    "technology changes rapidly",
    "artificial intelligence is growing",
    "welcome to python class",
    "hard work brings success",
    "hello coding enthusiasts"
    
]
#-------------------------------------------------------
#to count total words
total_count=0
for msg in messages:
    words = msg.split()
    total_count += len(words)
print("total count = ", total_count)
#-----------------------------------------
#to count total character
total_character = 0
for msg in messages:
    total_character += len(msg)
print("Total_character : ", total_character)
#-------------------------------------------------
#to count vowels nd consonents
vowels = "aeiouAEIOU"
vowel_count=0
consonent_count = 0
for msg in messages:
    for ch in msg:
        if ch.isalpha():
            if ch in vowels:
               vowel_count += 1
            else:
                 consonent_count += 1
print("vowel count : ",vowel_count)
print("consonent : ",consonent_count)
#-----------------------------------------------------
#to find the longest word
longest_word = ""
for msg in messages:
    words = msg.split()
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word
print("longest word is : ", longest_word)
#----------------------------------------------------
#to find shortest word 
first_word= messages[0].split()[0]
shortest_word = first_word
for msg in messages:
    words = msg.split()
    for word in words:
        if len(word)<len(shortest_word):
            shortest_word=word
print("longest word is : ", shortest_word)
#-------------------------------------------------------
# to find word frequency dictionary
word_frequency = {} # empty dictionary 
for msg in messages:
    words = msg.split()
    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1
print("\nWord Frequency Dictionary")
print(word_frequency)
#----------------------------------------------------------------
# Occurrence of Each Word
# ------------------------------------------
print("\nOccurrence of Each Word")

for word in word_frequency:
    print(word, ":", word_frequency[word])

# ------------------------------------------
# Repeated Words
# ------------------------------------------
print("\nRepeated Words")

for word in word_frequency:

    if word_frequency[word] > 1:
        print(word)

# ------------------------------------------
# Words Starting With Vowel
# ------------------------------------------
print("\nWords Starting With Vowel")

for word in word_frequency:

    if word[0].lower() in "aeiou":
        print(word)

# ------------------------------------------
# Words Longer Than 5 Characters
# ------------------------------------------
print("\nWords Longer Than 5 Characters")

for word in word_frequency:

    if len(word) > 5:
        print(word)
#------------------------------------------------------
# REPORT SECTION
# ==========================================

# Most Frequently Used Word
most_word = ""
highest_count = 0

for word in word_frequency:

    if word_frequency[word] > highest_count:
        highest_count = word_frequency[word]
        most_word = word

# Longest Message
longest_message = messages[0]

for msg in messages:

    if len(msg) > len(longest_message):
        longest_message = msg

# Shortest Message
shortest_message = messages[0]

for msg in messages:

    if len(msg) < len(shortest_message):
        shortest_message = msg

# Average Words Per Message
average_count = total_count / len(messages)
print("CHAT ANALYTICS REPORT")
#-------------------------------------------------

print("Most Frequently Used Word :", most_word)

print("Frequency :", highest_count)

print("\nLongest Message :")
print(longest_message)

print("\nShortest Message :")
print(shortest_message)

print("\nAverage Words Per Message :", average_count)
#-------------------------------------------------------------
#output will be 
'''
total count =  75
Total_character :  495
vowel count :  164
consonent :  276
longest word is :  communication
longest word is :  i

Word Frequency Dictionary
{'hello': 5, 'how': 1, 'are': 2, 'you': 1, 'i': 1, 'am': 1, 'doing': 1, 'great': 1, 'today': 1, 'python': 4, 'is': 6, 'very': 1, 'interesting': 1, 'everyone': 1, 'welcome': 2, 'coding': 3, 'makes': 2, 'life': 1, 'easier': 1, 'practice': 1, 'perfect': 1, 'data': 1, 'science': 1, 'amazing': 1, 'learners': 1, 'machine': 1, 'learning': 2, 'powerful': 1, 'keep': 1, 'every': 1, 'day': 1, 'programming': 1, 'fun': 1, 'chat': 1, 'applications': 1, 'useful': 1, 'communication': 1, 'important': 1, 'friends': 1, 'good': 1, 'morning': 1, 'improves': 1, 'problem': 1, 'solving': 1, 'technology': 1, 'changes': 1, 'rapidly': 1, 'artificial': 1, 'intelligence': 1, 'growing': 1, 'to': 1, 'class': 1, 'hard': 1, 'work': 1, 'brings': 1, 'success': 1, 'enthusiasts': 1}

Occurrence of Each Word
hello : 5
how : 1
are : 2
you : 1
i : 1
am : 1
doing : 1
great : 1
today : 1
python : 4
is : 6
very : 1
interesting : 1
everyone : 1
welcome : 2
coding : 3
makes : 2
life : 1
easier : 1
practice : 1
perfect : 1
data : 1
science : 1
amazing : 1
learners : 1
machine : 1
learning : 2
powerful : 1
keep : 1
every : 1
day : 1
programming : 1
fun : 1
chat : 1
applications : 1
useful : 1
communication : 1
important : 1
friends : 1
good : 1
morning : 1
improves : 1
problem : 1
solving : 1
technology : 1
changes : 1
rapidly : 1
artificial : 1
intelligence : 1
growing : 1
to : 1
class : 1
hard : 1
work : 1
brings : 1
success : 1
enthusiasts : 1

Repeated Words
hello
are
python
is
welcome
coding
makes
learning

Words Starting With Vowel
are
i
am
is
interesting
everyone
easier
amazing
every
applications
useful
important
improves
artificial
intelligence
enthusiasts

Words Longer Than 5 Characters
python
interesting
everyone
welcome
coding
easier
practice
perfect
science
amazing
learners
machine
learning
powerful
programming
applications
useful
communication
important
friends
morning
improves
problem
solving
technology
changes
rapidly
artificial
intelligence
growing
brings
success
enthusiasts
CHAT ANALYTICS REPORT
Most Frequently Used Word : is
Frequency : 6

Longest Message :
artificial intelligence is growing

Shortest Message :
hello how are you

Average Words Per Message : 3.75'''
    
    
    
