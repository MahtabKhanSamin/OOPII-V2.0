def fact(f,b):
    if b==0:
        print('Your Desired Factorial: ',f)
        return
    else:
        f=f*b
        fact (f,b-1)
a=int(input("Enter the Number: "))
fact(1,a)