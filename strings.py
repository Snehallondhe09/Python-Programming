'''name="snehal navanth londhe"
print("uppercase:",name .upper())
print("Lowercase:",name.lower())
print("Title:",name.title())
print("Capitalize:",name.capitalize())
print("Replace:",name.replace("snehal","adity"))
print("find:",name.find("snehal"))
print("count:",name.count("a"))
print("split:",name.split())
print("strip:",name.strip())

'''

'''
student="sai bapu gaikwad"
print("Uppercase:",student.upper())
print("Lowercase:",student.lower())
print("find:",student.find("sai"))
print("count:",student.count("i"))
print("replace:",student.replace("sai","saee"))
print("strip:",student.strip())
print("split:",student.split())
print("title:",student.title())
print("Capitalize:",student.capitalize())'''

'''

#non parameterized
def welcome():
    print("welcome to python programming.")
welcome()


def collage():
    print("SIET poly paniv")
collage()


def numbers():
    for i in range(1,11):
        print(i)
numbers()



def even():
    for i in range(2,21,2):
        print(i)
even()


def star():
    for i in range(5):
        print("* * *")
star()'''


#parameterized


'''def welcome(name):
    print("Welcome:",name)
student=input("enter student name:")
welcome(student)
'''
'''

def sum(a,b):
    return a+b
result=sum(11,12)
print(result)'''

'''
def table(n):
    for i in range(1,11):
         print(n,"*",i,"=",n * i)
number=int(input("enter a number:"))'''


'''
def square(n):
    return n*n
num=int(input("enter a number:"))
print("square=",square(num))
'''


add=lambda x,y:x+y
print(add(5,6))

square=lambda n:n*n
print("square:",square(4))

cube=lambda n:n*n*n
print("cube:",cube(3))


even_odd=lambda n:"Even"if n%2==0 else "odd"
print("4 is :",even_odd(4))


greater=lambda a,b: a if a>b else b
print("greater:",greater(12,13))


area=lambda l,w:l*w
print("Area:",area(5,4))




