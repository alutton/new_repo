l=[0]*99
for i in [ord(x.upper()) for x in input('? ') if x.isalpha()]:l[i]+=1
print([chr(x) for x in range(65,91) if l[x]==max(l)])

print(''.join(['9' if x in 'Zz' else str(int((ord(x.upper()) - ord('A'))/3) + 2) if x.isalpha() else x for x in input("phone#: ")]))

y=[0]*4
for c in open(input('fn? '),'r').read():
 y[0]+=c.isupper()
 y[1]+=c.islower()
 y[2]+=c.isdigit() 
 y[3]+=c.isspace()
print(y)
