#fuction without parameters 
def greet() :
    print("hello")
greet ()


#function with parameters

def greet(name) :
    print(name)

greet ("snehal")


#function with return value
def add(a,b):
    return a+b
result=add(10,5)
print(result)


#lambda function (anonymous)
square=lambda a:a*a
print(square(5))
