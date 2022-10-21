'''rules:.....using recursion
boolean has consecutiverepeat(string s) - returns true if the string s has 2 
consecutive equal characters and false otherwise
for instance, has ConsecutiveRepeat("bcddef") would return true because of the 
consecutive dd in the string '''

def ConsecutiveRepeat(str1):
    d = False
    for i in range(len(str1)):
            u = i+1
            if u <= len(str1)-1:
                if str1[i] == str1[u]:
                    d = True
    return d
str = input("enter a string : ")
r = ConsecutiveRepeat(str)
print(r)