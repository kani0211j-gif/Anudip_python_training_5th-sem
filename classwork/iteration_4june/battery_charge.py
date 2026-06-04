#program for displaying battery charging level
charging_level = 20
electricity_status = True
while(charging_level<=100):
    if(electricity_status):
      print(" Battery charging level:",charging_level,"%")
      charging_level = charging_level + 10
    else:
        break
#------------
print("Full charged")

