#atendance of students
present_student = 0
absent_student = 0
student_count = 0 
while(student_count<30):
    student_count = student_count+1
    attendance=input("Enter p or a :p ")
    if(attendance == 'p'):
       present_student+=1 
       print("STUDENT:",student_count) 
       print("Attendance : Present")
    else:
        absent_student+=1
        print("STUDENT:",student_count) 
        print("Attendance : Absent")
print(" No. of present students :",present_student)
print(" No.of absent students : ",absent_student)




