a='hello'
b='b2b2b2'
c='3g3g          '
d=a+' '+b+' '+c
print(d)
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(d[:-3])
print(d[::-1])
print(d.upper())
print(d.lower())
print(d.title())
print(d.find('3g'))
print(d.capitalize())
print(d.isalnum())
print(d.count('b2'))
print(d.split())
print(d.count('a2'))
print(d.replace('hello','python'))
print(d.swapcase())
e=len(d)
# for x,y in range(0,e):
#     if d[x]+d[y]=='a2':
#         print('a2 is there')
# else:
#     print('No a2 spotted+')
if 'a2' in d:
    print('a2 is present')
else:
    print('a2 is not there')