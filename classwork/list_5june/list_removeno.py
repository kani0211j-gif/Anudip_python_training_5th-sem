numbers = []

# Input 20 numbers
for i in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Display original list
print("Original List:", numbers)

# Input the number whose duplicates are to be removed
target = int(input("Enter the number: "))
#----------------------------------------------
#finding the frequency of given number
frequency = numbers.count(target)
if frequency == 0:
    print("element not found")
elif frequency == 1:
    print("no duplicate found")
else:
    #reversing the list 
    numbers.reverse()
    for i in range(1,frequency):
        #removing element
        numbers.remove(target)
    #reversing thelist again
    numbers.reverse()
    print("After removing duplicates")
    print(numbers)
    