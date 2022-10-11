# check whether inputs given by user is triangle or not sum of all sides 180 and 
# side shld not be measured in 0

a = int(input("enter the 1st side : "))
b= int(input("enter the 2nd side : "))
c = int(input("enter the 3rd side : "))
s = a+b+c
if (s == 180) and a!=0 and b!=0 and c!=0:
    print(True)
else:
    print(False)
