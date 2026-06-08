
#--------------------------------------------------------
#write a program to input a string and input a sentence from user and count the number of character present in it without using len fucntion 
sentence = input("enter your sentence : ")
#count
count = 0
for ch in sentence:
    count=count+1
print("no. of characters are : ",count)