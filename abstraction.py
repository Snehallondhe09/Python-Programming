'''from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
d=Dog()
d.sound()'''

'''
from abc import ABC,abstractmethod
class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehical):
    def start(self):
        print("Car start with a key")
car=Car()
car.start()'''


'''class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
m1=Mobile("Samsang",40000)
m2=Mobile("Apple",90000)
m1.display()
m2.display()'''

'''class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
b1=Book("wings of fire","A.P.J abdul kalam")
b1.display()'''

'''class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of circle:",3.14*self.radius*self.radius)
c1=Circle(5)
c1.area()'''


'''class movie:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating
    def check_rating(self):
        if self.rating>=7:
            print("Movie rating is good")
        else:
            print("Movie rating is not good")
m1=movie("3 idiots",8.5)
m1.check_rating()
'''


'''class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposited:",amount)
        print("Balance:",self.balance)
    def withdraw(self,amount):
        if  amount <=self.balance:
         self.balance=self.balance-amount
         print("withdrawn:",amount)
         print("Balance:",self.balance)
a1=BankAccount("snehal",5000)
a1.deposit(2000)
a1.withdraw(1000)'''


'''class Person:
    def introduce(self):
        print("I am a person")
class Student(Person):
    def study(self):
        print("I am studying")
s1=Student()
s1.introduce()
s1.study()'''


'''class Password:
    def __init__(self,password):
        self.password=password
    def check_password(self,password):
        if self._password==password:
            print("password is correct")
        else:
            print("password is incorrect")
p1=Password("12345")
p1.check_password("12345")'''


'''class Vehicle:
    def start(self):
        print("vehicle is starting")
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
c1=Car()
b1=Bike()
c1.start()
b1.start()'''

'''class Circle:
    def __init__(self,radius):
        self.radius=radius
        def area(self):
            return 3.14*self.radius*self.radius
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
c=Circle(5)
r=Rectangle(10,4)
print("Circle Area:",c.area())
print("Rectangle Area:",r.area())'''



from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FulltimeEmployee(Employee):
    def __init__(self,salary):
        self.salary=salary
emp=FulltimeEmployee(5000)
print("Salary:",emp.calculate_salary())
