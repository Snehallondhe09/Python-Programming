'''name={"name":"snehal","age":1}
if "age" in name:
    print("key exists")
else:
    print("key does not exists")'''

'''num={1,2,3,4,5,6,7}
print(len(num))'''
'''
data={
    "a":10,
    "b":20,
    "c":30
}
print(data)
total=sum(data.values())
print(total)'''



'''marks={
    "snehal":90,
    "payal":80,
    "sakshi":70
}
print(marks)
highest=max(marks.values())
print(highest)'''

'''def welcome():
    print("welcome snehal")
welcome()'''


'''def welcome(name):
    print("welcome",name)
student=input("enter student name:")
welcome(student)'''


'''add=lambda x,y:x+y
print(add(5,6))'''

'''square=lambda n:n*n
print("square:",square(4))
'''


'''name="snehal navnath londhe"
print(name)
print("upper():",name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.strip())
print(name.split())
print(name.replace("snehal","adity"))

'''


'''number=-5
if number>0:
    print("the number is positive")
elif number<0:
    print("the number is negative")
else:
    print("the number is zero")'''


'''number=9
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")'''


'''num1=10
num2=20
if num1>num2:
    print("the num1 is greater")
elif num1<num2:
    print("num2 greater")
else:
    print("both equal")'''

'''
for i in range(1,11):
    print(i)'''

'''
for i in range(10,0,-1):
    print(i)
'''


'''name="snehal"
num=1
while num<11:
    print(name)
    num+=1'''

'''
number=[1,2,3,4,5]
print(number)
print(len(number))
number.append(6)
number.remove(1)'''


'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
s1=student("snehal",19)
print(s1.name)
print(s1.age)'''


'''class student:
    def __init__(self,name,marks,city):
        self.name=name
        self.marks=marks
        self.city=city
    def display(self):
        print(self.name)
        print(self.marks)
        print(self.city)
s=student("snehal",90,"pune")
s.display()
'''

'''
for i in range(5):
    for j in range(4):
        print("*",end=" ")
    print()'''


'''rows=4
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()'''

'''
class A:
    def m1(self):
        print("class A")
class B:
    def m1(self):
        print("class B")
a=A()
b=B()
a.m1()
b.m1()'''


'''class A:
    def m1(self):
        print("class A")
class B(A):
    def m2(self):
        print("class B")
b=B()
b.m1()
b.m2()'''
'''
class A:
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
    def m2(self):
        print("class B")
class C(B):
    def m3(self):
        print("class C")
b=B()
b.m1()
b.m2()
c=C()
c.m2()
c.m3()'''


'''from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("salary is 3000")
e=FullTimeEmployee()
e.calculate_salary()'''

'''from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog bark")
d=Dog()
d.sound()'''

