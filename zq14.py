# write a program that uses a loop to generate the 26 line block of letters
#, partially shown below :
# abcd...z to zabcde.....y
import string
l = string.ascii_lowercase
l1 = list(l)
str(l1) [1:-1]
print(" ".join(l1))
o = 0
for i in range(0,len(l1)-1):
    o += 0
    l1.append(l1.pop(o))
    str(l1) [1: -1]
    print(" ".join(l1))