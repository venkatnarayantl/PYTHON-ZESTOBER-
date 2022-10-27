''' write  a program that asks user to enter a number n and displays the 
multipliation  table of the numeber 1 through n-1 with the arithmethic done 
modulo n. for instance,if n = 5 to compute 3x3 we do 3x3 = 9 and then mod that by 
5 to get 4. Use printf to right-justify table entries
show below are the tables you shld get for n = 5 and n = 11

for n = 5                            
1 2 3 4                              
2 4 1 3                              
3 1 4 2                              
4 3 2 1'''         

n = int(input("enter a number : "))
x = range(1,n)
p = range(1,n)

m = [[(i*j) % n for j in x] for i in p]
s = n-1
for i in range(s):
    for j in range(s):
        print(m[i][j], end=" ")
    print()    

#t = (c*d) % n'''

