#write a program to input the sentence nd display the frequency fo vowels which are present in that sentence ignoring the case
# ---------------------------------
#taking the input ofor taking input sentence
sentence = input("enter your sentence : ")
#making of loop
countA=0
countE=0
countI=0
countO=0
countU=0
for ch in sentence:
    if ch=='A' or ch=='a':
        countA=countA+1
        
    elif ch=='E' or ch=='e':
        countE=countE+1
        
    elif ch=='I' or ch=='i':
        countI=countI+1
        
    elif ch=='O' or ch=='o':
        countO=countO+1
        
    elif ch=='U' or ch=='u':
        countU=countU+1
        
if(countA>0):
       print("Frequency of vowel a/A is:",countA )
if( countE>0):
       print("Frequency of vowel e/E is:", countE)
if( countI>0):
       print("Frequency of vowel i/I is:",countI )
if(countO>0):
       print("Frequency of vowel o/O is:",countO )
if( countU>0):
       print("Frequency of vowel u/U is:", countU)
 
    
        
        



