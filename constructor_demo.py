'''class student :
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("snehal",19)
s2=student("sai",22)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

'''

'''class student :
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

s1=student("name=snehal","age=19","city=pune")
print(s1.name)
print(s1.age)
print(s1.city)'''


'''class student:
    def __init__(self):
        print("DEFault constructor")
s1=student()        '''


'''class student:
    def __init__(self,name="shreya",age=19):
        self.name=name
        self.age=age
s1=student()
s2=student("snehal",19)
s3=student("komal",20)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)
print(s3.name)
print(s3.age)'''



class teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
s1=teacher("shitole mam","DBS")
s2=teacher("nikita mam","data analysis")
print(s1.name)
print(s1.subject)
print(s2.name)
print(s2.subject)