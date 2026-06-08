'''Program to input a sentence from user and count the number of special characters in it'''
sentence = input("Enter a sentence: ")
alphanumeric_count = 0
#counting number fo alphanumeric characters in the sentence
for char in sentence:
    if char.isalnum():
        alphanumeric_count += 1
#total number of characters in the sentence
total_characters = len(sentence)
#number of special characters in the sentence
special_characters_count = total_characters - alphanumeric_count
print("Number of special characters in the sentence:", special_characters_count)

