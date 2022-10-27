'''rules.......
int firstDiff(string s, string t) - returns thr 1st index in which the strings 
s and t differ.
fro instance if s = abc and t = abd then the function should return 2. if s = ab 
and t = abcde the function should also return 2.'''

s = input("enter String s  : ")
t = input("enter String t : ")
def firstDiff(s,t):
    i = 0
    for a,b in zip(s,t):
        if a != b:
            break
        i += 1
    return i
print(firstDiff(s, t))