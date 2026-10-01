class A:
    def m1(self):
        print("m1 of A")

class B(A):
    def m2(self):
        print("m2 of B")

b=B()
b.m2()
b.m1()

'''
class collage:
    def m1 (self):
        print("m1 of collage")
class student(collage):
    def m2 (self):
        print("m2 of student")

s=student()
s.m1()
s.m2()'''
'''
class parent:
    def show(self):
        print("this is a parent class")

class child(parent):
    def display(self):
        print("this is a child class")
c=child()
c.show()
c.display()'''


'''
class A:
    def __init__(self,name):
        self.name=name
class B(A):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
b=B("Snehal",19)
print(b.name)
print(b.age)'''



'''class Animal:
    def sound(self):
        print("animal sounds")
class Dog(Animal):
    def Bark(self):
        super().sound()
        print("Dog Barks")
d=Dog()
d.Bark()'''



'''class student:
    def mark(self):
        print("student pass")
class girls(student):
    def marks(self):
     super().mark()
    print("student fail")
g=girls()
g.marks()
'''



'''num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    num=num%10
    if num%i==0:
        count=count+1
if count==2:
         print("prime")
else:
     print("not prime")'''


'''num=int(input("enter a number:"))
t=num
r=0
while num>0:
    r=r*10+num%10
    num=num//10
if t==r:
     print("palindrome")
else:
    print("not palindrome")'''

'''for n in range(2,101):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
      print(n)
'''


'''num=int(input("enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
    print(sum)
'''


'''num=int(input("enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial=",fact)'''

'''num=int(input("enter a number:"))
even=0
odd=0
while num>0:
    digit=num%10
    if digit % 2==0:
         even=even+1
    else:
        odd=odd+1
    num=num//10
print("Even=",even)
print("Odd=",odd)
'''

'''num=int(input("enter a number:"))
count=0
while num>0:
    count=count+1
    num=num//10
print(count)'''


'''num=int(input("enter a number:"))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)'''