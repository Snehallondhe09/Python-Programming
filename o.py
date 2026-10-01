'''class Employee:
    name="snehal"
    age=19
    def display(self):
     print("name:",self.name)
     print("age:",self.age)
s1=Employee()
s1.display()'''


'''
class Manager:
    name="Adity"
    salary=25000
    def display(self):
        print(self.name)
        print(self.salary)
s1=Manager()
s1.display()'''


''''class Department:
    def __init__(self,name,course,teacher_name,student_name):
        self.name=name
        self.course=course
        self.teacher_name=teacher_name
        self.student_name=student_name
    
s1=Department("snehal","Engineering","shitole","payal")
s2=Department("Sakshi","IT","nikita","sonal")
print(s1.name)
print(s1.course)
print(s1.teacher_name)
print(s1.student_name)
'''


'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("snehal",19)
print(s1.name)
print(s1.age)'''

'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
s1=Employee("snehal",12000)
print(s1.name)
print(s1.salary)'''


'''class car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
s1=car("Tata",100000)
print(s1.brand)
print(s1.price)
'''     
'''
class Student:
    def __init__(self,name,marks,city):
        self.name=name
        self.marks=marks
        self.city=city
    def display(self):
        print(self.name)
        print(self.marks)
        print(self.city)
s1=Student("snehal",90,"pune")
s1.display()'''

'''class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print("name=",self.name)
        print("salary=",self.salary)
        print("department=",self.department)
s1=Employee("snehal",25000,"CM")
s2=Employee("adity",30000,"IT")
s3=Employee("sagar",40000,"CIVIL")
for emp in[s1,s2,s3]:
   emp. display()
'''   

'''
class Product:
    def __init__(self,product_name,price,quality):
        self.product_name=product_name
        self.price=price
        self.quality=quality
    def total_price(self):
        return self.price*self.quality
    def display(self):
        print(self.product_name)
        print(self.price)
        print(self.quality)
        print(self.total_price())
p1=Product("laptop",10000,2)
p1.display()'''


'''class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def display(self):
        print(self.length)
        print(self.width)
        print(self.area())
r=Rectangle(10,30)
r.display()'''

'''class animal:
    def info(self):
        print("animal info")
class dog(animal):
    def sound(self):
        print("dog sounds" )
d=dog()
d.sound()
d.info()'''
'''
class parent:
    def info1(self):
        print("parent info")
class child(parent):
    def info2(self):

        print("child info  ")
p=parent()
p.info1()
p.info2()'''
'''
class A:
    def show(self):
        print("class A")
class B(A):
    def display(self):
        print("class B")
s1=B()
s1.display()
s1.show()'''
'''
class A:
    def m1(self):
        print("class A")
class B(A):
    def m2(self):
        print("class B")
class C(B):
    def m3(self):
        print("class C")
c=C()
c.m1()
c.m2()
c.m3()
'''
'''class A:
    def m1(self):
        print("class A")
class B:
    def m2(self):
        print("class B")
class C(A,B):
    def m3(self):
        print("class C")
c=C()
c.m1()
c.m2()
c.m3()'''


'''class A:
    def m1(self):
        print("class A")
class B(A):
    def m2(Self):
        print("Class B")
class C(A):
    def m3(self):
        print("Class C")
b=B()
b.m2()
b.m1()
c=C()
c.m3()
c.m1()'''

'''
class friend:
    def m1(self):
        print("my friend")
class bestfriend(friend):
    def m1(self):
        super().m1()
        print("my bestfriend")
b=bestfriend()
b.m1()'''

'''class A:
    def m1(self):
        print("class A")
class B(A):
    def m2(self):
        print("class B")
class C(A):
    def m3(self):
        print("class C")
class D(B,C):
    def m4(self):
        print("class D")
b=B()
b.m1()
b.m2()
c=C()
c.m1()
c.m3()
d=D()
d.m1()
d.m2()
d.m3()
d.m4()'''

'''
class snehal:
    age=18
    salary=25000
    def display(self):
     print(self.age)
     print(self.salary)
s1=snehal()
s1.display()'''

'''class car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(self.brand)
        print(self.price)
s1=car("Tata",25000)
print(s1.brand)
print(s1.price)
'''
'''
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(self.title)
        print(self.author)
b=Book("shyamchi aai","sane guruji")
print(b.title)
print(b.author)'''

