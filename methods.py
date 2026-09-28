#string method
'''name="Snehal Navnath Londhe"
print(name)
print(name[0])
print(name[1])
for i in name:
    print(i)
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.split())
print(name.find("a"))
print(name.replace("snehal","Adity"))
print(name.count("a"))
print(name.capitalize())'''
'''

s=input("Enter a string:")
print("You entered:",s)
print(len(s))
print(s.upper())
print(s.lower())
print("Revesed:",s[::-1])
def palindrome(s):
    if s==s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
'''
'''
word="komal"
print(word.split())
print(len(word))'''

'''
word="banana"
print(word.count("a"))'''

'''
word="welcome to python"
new_word=word.replace("python","Java")
print(new_word)'''
'''
a="hello"
b="world"
result=a+""+b
print(result)'''

'''
a="snehal"
b=19
c=19.8
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))'''

'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
         print("Name=",self.name)
         print("Age=",self.age)
s1=student("Snehal",19)
s1.display()'''

'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name=",self.name)
        print("Salary=",self.salary)
s1=Employee("Adity",250000)
s1.display()
'''


'''class car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand=",self.brand)
        print("Price=",self.price)
c=car("Tata",100000)
c.display()
'''


'''class employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
e1=employee("Snehal",20000,"IT")
e2=employee("Sneha",25000,"CM")
e3=employee("Sonal",28000,"HR")
for emp in [e1,e2,e3]:
 emp.display()
'''

'''class product:
    def __init__(self,product_name,price,quality):
        self.product_name=product_name
        self.price=price
        self.quality=quality
    def total_price(self):
        return self.price*self.quality
    def display(self):
        print("Product:",self.product_name)
        print("Price:",self.price)
        print("quality:",self.quality)
        print("Total:",self.total_price())
p1=product("Laptop",50000,2)
p1.display()

'''

    
'''class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def display(self):
        print("Bank Account Details")
        print("Account_holder:",self.account_holder)
        print("Balance:",self.balance)
a=BankAccount("Snehal",20000)
a.display()
'''

'''
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def display(self):
        print("Length:",self.length)
        print("Widht:",self.width)
        print("Area:",self.area())
        
c=rectangle(10,5)
c.display()'''


''''class student:
    def __init__(self,name,roll_no,m1,m2,m3):
        self.name=name
        self.roll_no=roll_no
        self.marks=[m1,m2,m3]
    def total(self):
        return sum(self.marks)
    def percentage(self):
        return self.total()
    def result(self):
        if min (self.marks)>=40:
            return "Pass"
        else:
            return "fail"
    def display(self):
        print("student REport")
        print(self.name)
        print(self.roll_no)
        print(self.marks)
        print(self.total())
        print(self.percentage())
        print(self.result())
s1=student("snehal",22,90,70,60)
s1.display()
'''


'''#single level inheritance
class Animal:
    def eat(Self):
        print("animal eats")

class Dog(Animal):
    def bark(self):
        print("dogs barking")
d=Dog()
d.eat()
d.bark()'''

'''
class parent:
    def show(self):
        print("this is a parent class")
class child(parent):
    def display(self):
        print("this is child class")
c=child()
c.show()
c.display()'''

'''class A:
    def showA(self):
        print("this is a class A")
class B:
    def showB(self):
        print("this is a class B")
class C (A,B):
    def showC(self):
        print("this is a class C ")
c=C()
c.showA()
c.showB()
c.showC()'''



'''class grandfather:
    def show1(self):
        print("this is a grandfather ")
class father(grandfather):
    def show2(self):
        print("this is a father ")
class son(father):
    def show3(self):
        print("this is a son")
s=son()
s.show1()
s.show2()
s.show3()'''


'''class animal:
    def show1(self):
        print("this is a animal")
class Dog(animal):
    def bark(self):
        print("this is dog")
class cat(animal):
    def meow(self):
        print("this is a cat")
c=cat()
d=Dog()
c.meow()
c.show1()
d.bark()
d.show1()
'''


'''class A:
    def show1(self):
        print("class A")
class B(A):
    def show2(self):
        print("Class B")
class C(A):
    def show3(self):
        print("Class C")
class D(B,C):
    def show4(self):
        print("class D")
obg=D()
obg.show1()
obg.show2()
obg.show3()
obg.show4()'''
'''


class dog:
    def m1(self):
        print("this is a dog")
class cat(dog):
    def m2(self):
        print("this is a cat")
class ox(dog):
    def m3(self):
        print("this is ox")
class rabbit(cat):
    def m4(self):
        print("this is a rabbit")
class parrot(cat):
    def m5(self):
        print("this is a parrot")
c=cat()
c.m2()
c.m1()
o=ox()
o.m3()
o.m1()
r=rabbit()
r.m4()
r.m2()
p=parrot()
p.m5()
p.m2()'''

