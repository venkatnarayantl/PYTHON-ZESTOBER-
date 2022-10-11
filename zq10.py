#write a program that asks the user to input a word with an odd number of letters 
#and theen prints out the string where the middle letters is printed once, the
# letter next to the  middle are printed twice, the letters next to them printed 
#3 times. eg: red ==> rredd
#CONCEPT
inp = input("enter the word which has odd numbers of letters : ")
middle = inp[(len(inp)-1)//2:(len(inp)+2)//2]
ind = inp.index(middle)
n1 = 1
l1 = []
while ind > 0:
    ind = ind-1
    n1 = n1 + 1
    h = inp[ind]*(n1)    
    l1.append(h)
ind2 = inp.index(middle)
l = []
n = 1
while ind2 < len(inp)-1:
    ind2 = ind2+1
    n = n+1
    v = inp[ind2]*(n)    
    l.append(v)
mid = []
mid.append(middle)
rev = l1[::-1]
arr = []
arr.append(rev)
arr.append(mid)
arr.append(l)
print(arr)
str1 = " "
for i in arr:
    for j in i:
        str1 += j
print(str1)
    