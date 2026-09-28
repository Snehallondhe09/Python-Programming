'''class friend:
    def m1(self):
        print("my friend sneha")
class bestfriend(friend):
    def m1(self):
        print("my bestfriend pragati")
b=bestfriend()
b.m1()'''

'''class College:
    def A(self):
        print("collage name SIET")
class Department(College):
    def A(self):
        print("department name COMPUTER")

class Student(College):
    def A(self):
        print("student name snehal")
d=Department()
d.A()
s=Student()
s.A()
''''''
class student:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def display(self):
       print("Name=",self.name)
       print("Age=",self.age)
s1=student("Snehal",20)
s1.display()'''
'''
class student:
    def __init__(self,name="snehal",age=19):
        self.name=name
        self.age=age
s1=student()
s2=student("sakshi",29)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)'''

'''
class student:
    name="Snehal"
    age=18
    def display(self):
      print("name:",self.name)
      print("age:",self.age)
s1=student()
s1.display()'''


'''#single level 
class company:
    def skill(self):
        print("company skills")
class Employee(company):
    def salary(self):
        print("Employee salary")
e=Employee()
e.skill()
e.salary()
'''

#mutiple 
'''class department:
    def m1(self):
        print("department")
class teacher:
    def m2(self):
        print("teacher")
class student(department,teacher):
    def m3(self):
       print("student")


s=student()
s.m1()
s.m2()
s.m3()

'''

#multilevel

'''class grandfather:
    def A(self):
        print("grandfather")
class father(grandfather):
    def B(self):
        print("father")
class child(father):
    def C(self):
        print("child")
c=child()
c.A()
c.B()
c.C()
'''
'''
class friend:
    def m1(self):
        print("my friend Sneha")
class Bestfriend(friend):
    def m1(self):
          super().m1()
          print("pragati")
        
b=Bestfriend()
b.m1()'''


