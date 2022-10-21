'''rules.....
boolean contains(string s, char ch) - returns whether the string s contains char ch
ex :
    contains("Hello",'o') -->true
    contains("Tharun",'h') --> true
    contains("Yellow",'u') --> false
    contains("Tower",'W') --> false'''
    
def contains(s,ch):
    if(s.find(ch)==-1):
        print(False)
    else:
        print(True)
s = input("enter the string : ")
ch = input("enter the letter : ")
print("contains(",s,",",ch,")")
contains(s, ch)