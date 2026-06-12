''' Write a program to count the frequency of each character in a given string and store the result in a dictionary.'''
string = " hello , how are you "
words = string.split()# to split the words
#-----------------------------------------
# to make a dictionary
count = 0
freq = {} # empty dictionary
list1 = list(words)
print("list of words :", list1) 
for ch in list1:
    if ch in words:
       count +=1
    else:
        count = 1

        


