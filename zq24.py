''' rules....
int digitalRoot(int n) - returns the digital root of the +ve integer n. 
The digital root of n is obtained as follows : 
    add up the digit n to get a new number. add up the digits of tht to get
    a new number. keep doing that until u get a no. that has only one digit.
    the number is the digital root.'''
    

def digitalRoot(n):
    while n>=10:
        n = sum(int(i) for i in str(n))
    return n
n1 = int(input("enter number : "))
print(digitalRoot(n1))