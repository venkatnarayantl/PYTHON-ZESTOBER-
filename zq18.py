#ask the user for an integer n. then create n*n character array that consists of 
# spaces everywhere except that the 1st ,last row,first column and last column
#,main diagonal and off diagonal should all be # symbols. print out the array
# remember that you are creating an array, not just printing characters

n = int(input("n = "))
print()
m = []
for i in range(n):
    v = []
    for j in range(n):
        r = i+j
        t = n-1
        if i==0 or j==0 or i==t or j==t or i==j or r==t:
            v.append("#")
        else:
            v.append(" ")
    m.append(v)        
for i in range(n):
    for j in range(n):
        print(m[i][j], end=" ")
    print()    