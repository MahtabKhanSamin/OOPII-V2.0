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
for x in range(c):
    for y in range(r):
        print(m1[y][x], end=' ')
    print()