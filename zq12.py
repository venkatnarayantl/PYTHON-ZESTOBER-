# write a program that determines whether a word is palindrome or not. 
#A palindrome is word that reads the same backwards as forwards

l = input("enter a word : ")
if l == l[::-1]:
    print(l,"--->","true")
else:
    print(l,"--->","false")
    