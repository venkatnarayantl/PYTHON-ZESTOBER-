#program that ask for user for their name and prints out the numerical value of
#their name where a = 1,b=2,c=3....z=26 and add up the numerical value of each 
#letter in the name. for ex: dave => 4+1+22+5 = 32. assume the name is in lowercase 

s = input("enter your name in lowercase : ")
n = [ord(c)-96 for c in s.lower()]
print(n)
c = 0
for j in range(0,len(n)):
    c = c+n[j]
print(c)