''' rules
boolean OneAway(string s, string t) - returns true if strings s and t are the same 
length and differ in exactly one character, like draw and drab or water and wafer.
'''

def OneAway(s,t):
    if len(s) == len(t):
        i = 0
        for a,b in zip(s,t):
            if a != b:
                i += 1
        if i == 1:
            return True
        else:
            return False
    else:
        return False
s = input("enter stirng s : ")
t = input("enter string t : ")
print(OneAway(s, t))

