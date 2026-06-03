#program to check three angles form a triangle or not
#if yes then specify type of triangle
angle1 = float(input("Enter first angle :  "))
#validate angle1
if(angle1 <= 0):
	exit("Angle must be positive")
#---------------------------------------------
angle2 = float(input("Enter second angle :  "))
#validate angle2
if(angle2 <= 0):
	exit("Angle must be positive")
#---------------------------------------------
angle3 = float(input("Enter third angle :  "))
#validate angle3
if(angle3 <= 0):
	exit("Angle must be positive")
#---------------------------------------------
#verifying triangle formation
if(angle1 + angle2 + angle3 == 180):
	#triangle is formed
	#acute angled triangle
	if(angle1 < 90 and angle2 <90 and angle3 < 90):
		print("Above angles form acute angled triangle")
	elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
		print("Above angles form Right Angled triangle")
	else:
		print("Above angles form Obtuse Angled triangle")
else:
	print("Above angles do not form any triangle")

