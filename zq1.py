# check the number of occurrences of number 4 in the input given by the user
o = 4
n = int(input("enter the number : "))
c  = 0
while n>0:
    if n%10==o:
        c = c+1
    n = n//10
print(c)