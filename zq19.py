'''create and print a n*n array that consists of random integers from 1 through 5 .
then print a count ofhow many fives are in array........constraint: n<=100'''

import random
n = int(input("enter a number to form matrix : "))
print()
m = []
r = []
if n<=100:
    for i in range(n):
        v = []
        for j in range(n):
                v.append(random.randint(1,5))
        m.append(v)
        f = v.count(5)
        r.append(f)
        
    for i in range(n):
        for j in range(n):
            print(m[i][j], end=" ")
        print()    
    t = 0
    for e in range(0,len(r)):
        t = t + r[e]    
    print(t)
else:
    print("given number should not exceed more than 100")