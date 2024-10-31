class person:
    def __init__(self,a,b):
        print("Person Constructor")
        self.fname=a
        self.lname=b
    def display(self):
        print("Person Name: ",self.fname,self.lname)

class student(person):
    def __init__(self,a,b,c):
        print("Student Constructor")
        person.__init__(self,a,b)
        self.graduation=c
    def display(self):
        print("Student Name: ",self.fname,self.lname)
        print("Graduation Year: ", self.graduation)

class alumni(student):
    def __init__(self,a,b,c,d):
        print("Alumni Constructor")
        student.__init__(self,a,b,c)
        self.id=d
    def display(self):
        print("Student Name: ",self.fname,self.lname)
        print("Graduation Year: ", self.graduation)
        print("ID: ",self.id)

class graduated(student):
    def __init__(self,a,b,c,d):
        print("Graduated Constructor")
        student.__init__(self,a,b,c)
        self.id=d
    def display(self):
        print("Student Name: ",self.fname,self.lname)
        print("Graduation Year: ", self.graduation)
        print("ID: ",self.id)

class teacher(person):
    def __init__(self, a, b, c):
        print("Teacher Constructor")
        person.__init__(self,a, b)
        self.joining = c
    def display(self):
        print("Teacher Name: ", self.fname, self.lname)
        print("Joining Year: ", self.joining)

class admin(person):
    def __init__(self, a, b, c):
        print("Admin Constructor")
        person.__init__(self,a, b)
        self.joining = c
    def display(self):
        print("Admin Name: ", self.fname, self.lname)
        print("Joining Year: ", self.joining)

class employee(teacher,admin):
    def __init__(self,a,b,c,d):
        print("Employee Constructor")
        super().__init__(a,b,c)
        self.id=d
    def display(self):
        print("Employee Name: ",self.fname,self.lname)
        print("Joining Year: ", self.joining)
        print("ID: ",self.id)

p1=person("Mahtab","Khan")
p1.display()
print()
s1=student("Mahtab","Khan", 2026)
s1.display()
print()
t1=teacher("Mahtab","Khan", 2022)
t1.display()
print()
a1=admin("Mahtab","Khan", 2024)
a1.display()
print()
al1=alumni("Mahtab","Khan", 2026, "0242220005101608")
al1.display()
print()
g1=graduated("Mahtab","Khan", 2026, "0242220005101608")
g1.display()
print()
e1=employee("Mahtab","Khan", 2026, "0242220005101608")
e1.display()