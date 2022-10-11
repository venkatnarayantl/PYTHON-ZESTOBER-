# program to reeverse a number without converting it to a string
n = int(input("enter any number : "))
t = n
r = 0
while t>0:
    d = t % 10
    r = (r*10)+d
    t = t//10
print(r)