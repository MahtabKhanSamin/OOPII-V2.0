def convert(num,base):
    b=[]
    while num!=0:
        if (num%base)>=10:
            i=chr((num%base)+55)
        else:
            i=num%base    
        b.append(i)
        num=int(num/base)
        b.reverse()
    return b
        
a=int(input('Enter the Decimal Number: '))
binary=convert(a,2)
octal=convert(a,8)
hexa=convert(a,16)
print('Binary: ',binary, '\nOctal: ', octal, '\nHexadecimal: ', hexa)