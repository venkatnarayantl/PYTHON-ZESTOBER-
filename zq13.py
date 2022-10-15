#add 1 to each and every element in the list

def addone(arr):
    t = []
    for j in range(len(arr)):
        r = arr[j] + 1
        t.append(r)
    print(t)
    
arr = input("enter : ")
s = arr.split(",")
a = []

for i in range(len(s)):
        b = int(s[i])
        a.append(b)    
print(a)    
addone(a)