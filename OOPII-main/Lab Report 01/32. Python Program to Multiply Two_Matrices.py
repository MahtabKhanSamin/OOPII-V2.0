r=int(input("Enter the Number of Rows: "))
c=int(input("Enter the Number of Columns: "))
m1=[]
m2=[]
print("Input for Matrix 1: ")
for x in range(r):
    a=[]
    for y in range(c):
        print('Enter the Value for R',x,'C',y,':',end=" ")
        t=int(input())
        a.append(t)
    m1.append(a)
print("Input for Matrix 2: ")    
for x in range(r):
    a=[]
    for y in range(c):
        print('Enter the Value for R',x,'C',y,':',end=" ")
        t=int(input())
        a.append(t)
    m2.append(a)
m3=[]    
for x in range(r):
    a=[]
    for y in range(r):
        t=0
        for z in range(c):
            t=t+(m1[x][z]*m2[z][y])
        a.append(t)    
    m3.append(a)
print("Added Matrix: ")    
for x in m3:
    print(x)