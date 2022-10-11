# wrrite a program that asks tthe user to enter a string and then prints out the
#first letter, then the 1st 2 letters, then the 1st 3 letters, etc and so on 
#on the same line. for instance, if the user enter abcde , the program would 
#print out a ab abc abcd abcde 

i = input("enter a word : ")
for j in range(len(i)):
         print(i[0:j+1],end = " ")
print()            