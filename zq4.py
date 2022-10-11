# finding the 2nd largest number without converting it to string
a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))

if a>b and a>c:
    if b>c:
        print("2nd largest no. is : ",b)
    else:
        print("largest no. is : ",c)
elif b>a and b>c:
    if a>c:
        print("2nd largest no. is : ",a)
    else:
        print("2nd largest no. is : ",c)
        
else:
    if a>b:
        print("2nd largest no. is : ",a)
    else:
        print("2nd largest no. is : ",b)