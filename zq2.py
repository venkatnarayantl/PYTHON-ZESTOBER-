#let n be the input given by the user program to add the 1st number and the 
#last number 
n = int(input("enter a number : "))
c = 0
while n!=0:
    if c ==0:
        l = n%10
        c = c+1
    r = n%10
    n = int(n/10)
sum = r+l
print("\n sum of 1st and last digit is : ", sum)