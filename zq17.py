#write a program that asks user for an integer n and creates and prints as n*n
# array whose entries alternate between 1 and 2 in a checkboard pattern, starting 
#with 1 in the upper left corner
# m = [[1,2],[2,1]]
n = int(input("enter : "))
m = []
for i in range(n):
    v = []
    for j in range(n):
        r = i+j
        if r%2==0:
            v.append(1)
        else:
            v.append(2)
    m.append(v)        
for i in range(n):
    for j in range(n):
        print(m[i][j], end=" ")
    print()
