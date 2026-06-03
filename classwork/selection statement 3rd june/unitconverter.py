#program to convert time into corresponding hour,minute and second
# input of time in second
second = int(input("enter the time in second"))
#check second is negative
if(second<0):
    exit("Time connot be negative.....Exited")
print("------------------------------")
hour=0
minute=0
#converting numbers of second into hours
if(second >= 3600):
    hours=second//3600
    second = second % 3600
#---------------------------
#converting into minute
if(second>=60):
    minute=second//60
    second=second%60
#--------------------------
print("-------------------------------------")
print("equivalent time : " , hour , "Hour" , minute,"Minute", second,"second")


