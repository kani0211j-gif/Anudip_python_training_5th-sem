''' Write a program to count the frequency of each character in a given string and store the result in a dictionary.'''
# to split the words
#-----------------------------------------
# to make a dictionary
string = input("Enter a string: ")

freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:")
for key in freq:
    print(key, ":", freq[key])       


