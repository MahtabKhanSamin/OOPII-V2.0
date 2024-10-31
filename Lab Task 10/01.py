class person:
    def __init__(self,a,b):
        self.fname=a
        self.lname=b
    def display(self):
        print("Person Name: ",self.fname,self.lname)
class student(person):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.graduation=c
    def display(self):
        print("Student Name: ",self.fname,self.lname)
        print("Graduation Year: ", self.graduation)
s1=student("Mahtab","Khan", 2026)
s1.display()
p1=person("Mahtab","Khan")
p1.display()