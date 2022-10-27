'''string bitflip(string s) - takes a string of 0s and 1s and flips all the 0s to
1s and all 1s to 0s.
for instance, bitflip("00010") would return "11101"
'''
def bitflip(s):
    l = list(s)
    for i in range(len(l)):
        if l[i] == '0':
            l[i] = '1'
        elif l[i] == '1':
            l[i] ='0'
    print('"',"".join(l),'"')
s = input("enter a string containing 0s and 1s : ")
bitflip(s)