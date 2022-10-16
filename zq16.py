#write a program that asks user for weight in ounces and returns the weight
#in pounds and ounces. for instance, 43 ounces becomes 2 pounds , 11 ounces

n = int(input("enter the weight (in ounces) : "))
lb = n//16
oz = n%16
print(n,"ounces","---->",lb,"pounds",oz,"ounces")