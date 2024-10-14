a=int(input ('Enter the First Number: '))
b=int(input ('Enter the Second Number: '))
c=[a,]
i=0
while c[i]<=a*b:
    c.append(c[i]+a)
    i+=1
for x in c:
    if x%b==0:
        print('LCM is: ',x)
        break
else:
    print('No LCM Found')