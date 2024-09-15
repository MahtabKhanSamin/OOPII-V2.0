Courses = {'CSE101':{'Course name': "Introduction to Programming",
                     'Credits': 3,
                     'Instructor':'Dr. Alice'
                     },
           'CSE102':{'Course name': 'Data Structures',
                     'Credits': 4,
                     'Instructor': 'Dr. Bob'
                     },
           'CSE103':{'Course name': 'Database Systems',
                     'Credits': 3,
                     'Instructor': 'Dr. Carol'}
           }
print(Courses)
Courses['CSE102']['Instructor']='Dr. Bob Jr.'
print(Courses)
Courses.update({'CSE104':{'Course name': 'Algorithms',
                     'Credits': 4,
                     'Instructor': 'Dr. Dave'}})
print(Courses)
Courses.pop('CSE101')
print(Courses)
for x,y in Courses.items():
    print(x)
    for z in y:
        print(z,':',y[z])
