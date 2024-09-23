a=int(input ('Enter the First Number: '))
b=int(input ('Enter the Second Number: '))
c=[]
for x in range(2,a):
    if a%x==0:
        c.append(x)
c.append(a)
c.reverse()
for x in c:
    if b%x==0:
        print('HCF is: ',x)
        break
else:
    print('No HCF Found')