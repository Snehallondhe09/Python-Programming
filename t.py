'''class snehal:
    name="snehal"
    age=19
    def display(self):
     print("name",self.name)
     print("age",self.age)
s1=snehal()
s1.display()'''

'''#single
class A:
    def show(self):
        print("my name is snehal")
class B(A):
    def display(self):
        print("my age is 19")
s1=B()
s1.show()
s1.display()'''

'''#mutiple
class A:
    def m1(self):
        print("snehal")
class B:
    def m2(self):
        print("navnath")
class C(A,B):
    def m3(self):
        print("londhe")
s1=C()
s1.m1()
s1.m2()
s1.m3()'''

#mutilevel 


'''class A:
    def m1(self):
        print("snehal")
class B(A):
    def m2(self):
        print("navnath")
class C(B):
    def m3(self):
        print("londhe")
s1=C()
s1.m1()
s1.m2()
s1.m3()'''


#herarchical''''
'''class A:
    def m1(self):
        print("father")
class B(A):
    def m2(self):
        print("child1")
class C(A):
    def m3(self):
        print("child 2")
class D(B):
    def m4(self):
        print("child 3")
b=B()
b.m1()
b.m2()
c=C()
c.m1()
c.m3()
d=D()
d.m2()
d.m4()
'''


#polymarphism

'''class friend:
    def m1(self):
        print("friend")
class bestfriend(friend):
    def m1(self):
        super().m1()
        print("bestfriend")
s1=bestfriend()
s1.m1()'''