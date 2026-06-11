'''News Article Text Analyzer
Problem Statement
A news agency wants to analyze the content of an article.
Use a paragraph containing at least 300 words.
Requirements
1. Count total characters.
2. Count total words.
3. Count total sentences.
4. Count vowels and consonants.
5. Find longest word.
6. Find shortest word.
7. Find the most frequent word.
8. Create a dictionary of word frequencies.
9. Display words appearing only once.
10. Display words appearing more than 5 times.
11. Count words starting with each alphabet.
12. Display all unique words.
Challenge
Generate a complete text summary:
Total Words
Total Sentences
Average Word Length
Most Frequent Word
Vocabulary Size'''
#---------------------------------------------------------------
# a paragraph using 300 words 
article = """
The rapid growth of technology has changed the world significantly. In recent years, digital transformation has become a key focus for organizations across the globe. News agencies report that artificial intelligence, machine learning, and data science are shaping the future of industries. Technology is improving communication, transportation, healthcare, and education systems. Many experts believe that automation will increase efficiency and reduce human effort in repetitive tasks.

The internet has made information easily accessible to people worldwide. Social media platforms are now major sources of news and communication. However, the spread of misinformation has also become a serious concern. Governments and tech companies are working together to ensure safe and reliable information sharing.

Economic growth is also influenced by technological advancements. Businesses are adopting new tools to improve productivity and customer experience. Startups are emerging in large numbers, contributing to innovation and job creation. The demand for skilled professionals in technology-related fields is increasing rapidly.

Education systems are also evolving with online learning platforms. Students can now access courses from anywhere in the world. This has made education more flexible and inclusive. Despite challenges, the future of technology looks promising and full of opportunities.The growth of artificial intelligence continues to expand globally. Many industries are now relying on automated systems for better performance and accuracy. Cloud computing is also playing a major role in data storage and processing. Cybersecurity has become an important concern due to increasing online threats.
The impact of technology is not limited to large industries only. Even small businesses are now using digital tools for marketing and customer engagement. Mobile applications have made services faster and more convenient for users. People can now shop, learn, and communicate with just a few clicks.

In addition, research and development in science have accelerated due to advanced computing systems. Data analysis helps organizations make better decisions based on real-time insights. Many countries are investing heavily in digital infrastructure to support future growth.

Despite all these advantages, technology also brings challenges such as data privacy issues and dependency on machines. Therefore, it is important to use technology responsibly and ensure proper regulations are in place."""
#----------------------------------------------------------------------------------
# to count total character

print("total_character = ",len(article))
#---------------------------------------------------------------------
#to count total words 
word_list = article.split()
print("Total words = ", len(word_list))
#-----------------------------------------------------------------------------
#to count total sentence
sentences = article.split(".")
total_sentences = len(sentences) - 1 
print("Total Sentences :", total_sentences)
#----------------------------------------------------------------------
# 4. Vowels & Consonants
# -----------------------------------------------------------------------
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in article:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels :", vowel_count)
print("Consonants :", consonant_count)
# ------------------------------------------------------------------------------------
#to count longest nd shortest word
words = article.split()
longest_word = words[0]
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word
print("Longest Word :", longest_word)
print("Shortest Word :", shortest_word)
#--------------------------------------------------------------------
# to find most frequest word 
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
#-------------------------------------------------------
# Words appearing once
once_words = []

for word in freq:
    if freq[word] == 1:
        once_words.append(word)
#---------------------------------------------------------
 #Words > 5 times
# ------------------------------------------------------
more_than_5 = []

for word in freq:
    if freq[word] > 5:
        more_than_5.append(word)

# -------------------------------------------------------------------
# 11 Words starting with each alphabet
# -------------------------------------------------------------
alpha_count = {}

for word in words:
    first = word[0]
    if first in alpha_count:
        alpha_count[first] += 1
    else:
        alpha_count[first] = 1

# ---------------------------------------------------------------------
# 12 Unique words
# --------------------------------------------------------------
unique_words = list(freq.keys())

# ------------------------------------------------------------------
# REPORT
# --------------------------------------------------------------------

most_frequent_word = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        most_frequent_word = word

print("TEST ANALYSIS REPORT")
print("Total Characters :",len(article))
print("Total Words :", len(words))
print("Total Sentences :", total_sentences)
print("Vowels :", vowel_count)
print("Consonants :", consonant_count)

print("Longest Word :", longest_word)
print("Shortest Word :", shortest_word)

print("Most Frequent Word :", most_frequent_word)

print("\nVocabulary Size :", len(unique_words))
print("\nWords appearing only once :", once_words)
print("\nWords appearing more than 5 times :", more_than_5)

print("\nAlphabet-wise Word Count :", alpha_count)
#---------------------------------------------------------------------------
#output will be
'''total_character =  2514
Total words =  354
Total Sentences : 30
Vowels : 814
Consonants : 1295
Longest Word : technology-related
Shortest Word : a
TEST ANALYSIS REPORT
Total Characters : 2514
Total Words : 354
Total Sentences : 30
Vowels : 814
Consonants : 1295
Longest Word : technology-related
Shortest Word : a
Most Frequent Word : and

Vocabulary Size : 226

Words appearing only once : ['rapid', 'changed', 'world', 'significantly.', 'recent', 'years,', 'transformation', 'key', 'focus', 'across', 'globe.', 'News', 'agencies', 'report', 'intelligence,', 'machine',
                             
                           'learning,', 'shaping', 'industries.', 'Technology', 'improving', 'communication,', 'transportation,', 'healthcare,', 'experts', 'believe', 'automation', 'will', 'increase', 'efficiency',
                           'reduce', 'human', 'effort', 'repetitive', 'tasks.', 'internet', 'easily', 'accessible', 'people', 'worldwide.', 'Social', 'media', 'platforms', 'sources', 'news', 'communication.', 
                           'However,', 'spread', 'misinformation', 'serious', 'concern.', 'Governments', 'tech', 'companies', 'working', 'together', 'safe', 'reliable', 'sharing.', 'Economic', 'influenced', 'by',
                           'technological', 'advancements.', 'Businesses', 'adopting', 'new', 'improve', 'productivity', 'experience.', 'Startups', 'emerging', 'numbers,', 'contributing', 'innovation', 'job',
                           'creation.', 'demand', 'skilled', 'professionals', 'technology-related', 'fields', 'rapidly.', 'Education', 'evolving', 'learning', 'platforms.', 'Students', 'access', 'courses', 'from',
                           'anywhere', 'world.', 'This', 'flexible', 'inclusive.', 'challenges,', 'looks', 'promising', 'full', 'opportunities.The', 'intelligence', 'continues', 'expand', 'globally.', 'relying',
                           'automated', 'performance', 'accuracy.', 'Cloud', 'playing', 'role', 'storage', 'processing.', 'Cybersecurity', 'an', 'concern', 'threats.', 'impact', 'not', 'limited', 'only.', 'Even',
                           'small', 'businesses', 'using', 'marketing', 'engagement.', 'Mobile', 'applications', 'services', 'faster', 'convenient', 'users.', 'People', 'shop,', 'learn,', 'communicate', 'just', 'few',
                           'clicks.', 'addition,', 'research', 'development', 'accelerated', 'advanced', 'Data', 'analysis', 'helps', 'make', 'decisions', 'based', 'real-time', 'insights.', 'countries', 'investing',
                           'heavily', 'infrastructure', 'support', 'growth.', 'all', 'these', 'advantages,', 'brings', 'challenges', 'such', 'as', 'privacy', 'issues', 'dependency', 'machines.', 'Therefore,', 'it',
                           'use', 'responsibly', 'proper', 'regulations', 'place.']

Words appearing more than 5 times : ['of', 'has', 'the', 'and', 'are', 'is', 'in', 'to']

Alphabet-wise Word Count : {'T': 7, 'r': 13, 'g': 6, 'o': 17, 't': 34, 'h': 12, 'c': 22, 
                            
                'w': 7, 's': 20, 'I': 2, 'y': 1, 'd': 12, 'b': 10, 'a': 58, 'k': 1, 'f': 15, 'N': 1,
                'i': 38, 'm': 13, 'l': 7, 'e': 13, 'M': 4, 'p': 12, 'S': 3, 'n': 9, 'H': 1, 'G': 1, 'E': 3, 
                
                'B': 1, 'j': 2, 'D': 3, 'C': 2, 'u': 3, 'P': 1}'''


 
    

    

