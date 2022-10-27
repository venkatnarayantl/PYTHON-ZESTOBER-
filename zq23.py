''' rules....
boolean isBinary(string s) - takes a string s and returns true if the string 
consists only of 0s and 1s and returns false otherwise.
for instance it would return true for "00101" and "00" while it would return false
for "01z" and "abc" '''


def isBinary(string):
    s1 = list(string)
    c = 0
    for i in range(len(s1)):
        if s1[i] == '0' or s1[i] == '1':
                c = c+1
    if c == len(string):
        return True
    return False
s = input("enter the string : ")
print(isBinary(s))