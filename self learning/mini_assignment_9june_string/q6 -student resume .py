''' Student Resume Analyzer
Problem Statement
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements).
The system should:
1. Count total words.
2. Count total characters.
3. Extract email IDs.
4. Extract phone numbers.
5. Count skills mentioned.
6. Find repeated keywords.
7. Identify the most frequently used word.
8. Generate a skill frequency report.
9. Detect duplicate skills.
10. Create a summary dashboard.'''
#--------------------------------------------------------------------------------------------
# students input
resume = """
Name: Rahul Sharma
Email: rahul.sharma@gmail.com
Phone: 9876543210
Skills: Python, C, Java, Python, HTML, CSS, Java
Education: BTech Computer Science
Projects: Chatbot using Python, Resume Analyzer tool
Achievements: Won coding competition, Python certification completed
"""
#-----------------------------------------------------------------------------------------
#to count total words
words = resume.split()
total_words = len(words)

# -----------------------------------
# to Total Characters
# -----------------------------------
total_characters = len(resume)

# -----------------------------------
# 3. Extract Email IDs
# -----------------------------------
emails = []

for word in words:
    if "@" in word:
        emails.append(word)

# -----------------------------------
# to  Extract Phone Numbers
# -----------------------------------
phones = []

for word in words:
    if word.isdigit() and len(word) == 10:
        phones.append(word)

# -----------------------------------
# to find  Skill Analysis
# -----------------------------------
skills = ["python", "c", "java", "html", "css"]

skill_count = {}
all_words = []

for word in words:
    all_words.append(word)

    if word in skills:
        if word in skill_count:
            skill_count[word] += 1
        else:
            skill_count[word] = 1

# -----------------------------------
# to find Repeated Keywords
# -----------------------------------
repeated = []

for word in skill_count:
    if skill_count[word] > 1:
        repeated.append(word)

# -----------------------------------
# to find  Most Frequent Word
# -----------------------------------
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

most_word = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        most_word = word

# -----------------------------------
# 9 Duplicate Skills
# -----------------------------------
duplicate_skills = repeated

# -----------------------------------
# 10 Summary Dashboard
# -----------------------------------
print("\n---------------------- RESUME ANALYZER ----------------------")

print("Total Words :", total_words)
print("Total Characters :", total_characters)

print("\nEmails Found :", emails)
print("Phone Numbers :", phones)

print("\nSkill Frequency Report :")
print(skill_count)

print("\nDuplicate Skills :", duplicate_skills)
#_----------------------------------------------------------------------------
#output will be
'''Total Words : 33
Total Characters : 273

Emails Found : ['rahul.sharma@gmail.com']
Phone Numbers : ['9876543210']

Skill Frequency Report :
{}

Duplicate Skills : []'''



