#write a program that asks the user to enter a sequence of integers separated 
#by semincolons. your program should print the sum of all the integers. 
#for instance, if the user enters 4;20;3;9 the program should print out 36

n = input("enter : ")
a = n.split(';')
print(a)
r =[int(i) for i in a]
print(r)
t = 0 
for e in range(0,len(r)):
    t = t + r[e]
print(t)