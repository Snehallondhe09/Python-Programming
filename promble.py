'''word="hello"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
'''
'''word="Hello"
for i in range(len(word)):
    print(word[i])'''

'''def fruits():
    fruits=["Orange","Apple","Mango","Apple","Apple"]
    print(fruits)
    fruits.append("kiwi")
    fruits.insert(1,"watermelon")
    last=fruits.pop()
    count=fruits.count("Apple")
    print(count)
    print(fruits.reverse())
    print(fruits)
fruits()'''


'''list=[1,2,3,4,5,6],[7,8],[9,10]

print(list)
print(list[-1])
print(list[0::2])'''

'''
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class B(A):
    def __init__(self,name,age):
        self.age=age
        self.name=name
b=B("snehal",19)
print(b.name)
print(b.age)'''
'''

birth_year=int(input("Enter your birth year:"))
current_year=2026
age=current_year-birth_year
print("your age is:",age)'''

'''
name="snehal"
print(name,type(name))
a=10
print(a,type(a))
b=20.8
print(b,type(b))
is_pass=True
print(is_pass,type(is_pass))'''


'''course={
    "course1":"puyhon",
    "course2":"Java",
    "course3":"C++"
}
print(course)
print(course["course1"])
'''


num=eval(input("enter a number:"))
if num%2==0:
    print("even")
else:
    print("odd")

