# input by the user and check whether tht number is leap year or not
year = int(input("enter year : "))
if (year%4==0)and (year%100!=0) or (year%400==0):
    print("true")
else:
    print("false")
    