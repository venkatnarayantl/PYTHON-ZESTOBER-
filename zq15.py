#you are given an integer . your task is to print alphabet rangoli of size.
# alphabet rangoli

import string
n = int(input("enter the size of rangoli : "))
l = string.ascii_lowercase
l1 = []
for i in range(n):
    j = "-".join(l[i:n])
    l1.append((j[::-1] + j[1:]).center((n-1)*4+1, "-"))
print("\n".join(l1[:0:-1] + l1))