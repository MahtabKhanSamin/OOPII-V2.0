class person:
    def __init__(self,a,b):
        self.fname=a
        self.lname=b
    def display(self):
        print("Person Name: ",self.fname,self.lname)

class student(person):
    def __init__(self,a,b,c):
        print("Student Constructor")
        super().__init__(a,b)
        self.graduation=c
    def display(self):
        print("Student Name: ",self.fname,self.lname)
        print("Graduation Year: ", self.graduation)

class teacher(person):
    def __init__(self, a, b, c):
        print("Teacher Constructor")
        super().__init__(a, b)
        self.joining = c
    def display(self):
        print("Teacher Name: ", self.fname, self.lname)
        print("Joining Year: ", self.joining)

class admin(person):
    def __init__(self, a, b, c):
        print("Admin Constructor")
        super().__init__(a, b)
        self.joining = c
    def display(self):
        print("Admin Name: ", self.fname, self.lname)
        print("Joining Year: ", self.joining)

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