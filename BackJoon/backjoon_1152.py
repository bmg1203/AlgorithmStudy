m = input()
l = len(m.split(' '))
if(m[0] == ' '):
    l -= 1
if(m[-1] == ' '):
    l -= 1
print(l)