def boost_grades(grade):
    return grade+grade*.05;
grades=[85, 78, 92, 45, 33, 67, 88, 41]
print('Grade Categories:')
for x in grades:
    if x >80:
        print('Score:',x,'- Grade: A')
    elif x>60 and x<=80:
        print('Score:',x,'- Grade: B')
    elif x>=40 and x<=60:
        print('Score:',x,'- Grade: C')
    elif x<40:
        print('Score:',x,'- Grade: F')
grades=list(map(boost_grades,grades))
print()
print('Boosted Grades:')
print(grades)
print()
print('Boosted Grades Above 90:')
grades90=list(filter(lambda x:x>90,grades))
print(grades90)