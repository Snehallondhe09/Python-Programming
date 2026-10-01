'''def welcome():
    print("welcome to Python programming")
welcome()


def collage():
    print("SIET (poly) paniv")
collage()


def print_numbers():
    for i in range(1,11):
        print(i)
print_numbers()
'''

'''def print_numbers():
    for i in range(2,21,2):
        print(i)
print_numbers()'''


'''def star_pattern():
    for i in range(5):
        print("***")
star_pattern()'''

#paramiterized functions
'''def welcome(name):
    print("Welcome",name)
student=input("enter student name:")
welcome(student)'''

'''def sum(a,b):
    return a+b
result=sum(10,20)
print(result)'''


'''def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
number=int(input("enter a number:"))
table(number)'''

'''def area(length,width):
    print("area of rectangle=",length*width)
l=float(input("enter length:"))
w=float(input("enter width:"))
area(l,w)'''

'''def calculate_marks(m1,m2,m3,m4,m5):
    total=m1+m2+m3+m4+m5
    percentage=total/5
    print("total marks=",total)
    print("percentage=",percentage,"%")
a=float(input("enter marks of subject 1:")) 
b=float(input("enter marks of subject 2:")) 
c=float(input("enter marks of subject 3:")) 
d=float(input("enter marks of subject 4:")) 
e=float(input("enter marks of subject 5:"))  
calculate_marks(a,b,c,d,e)
'''


'''def celsius_to_fahrenheit(c):
    f=(c*9/5)+32
    print("temperature in fahrenheit=",f)
celsius=float(input("Enter tenperature in celsius:")) 
celsius_to_fahrenheit(celsius)   '''

'''def to_uppercase(text):
    print("Uppercase string:",text.upper())
string=input("Enter a string:")    
to_uppercase(string)'''


'''def check_even_odd(num):
    if num%2==0:
        print(num,"is Even:")
    else:
       print(num,"is odd:")
number=int(input("enter a number:"))
check_even_odd(number)'''

#return type function

'''def square(n):
    return n*n
num=int(input("enter  a number:"))
print("square=",square(num))'''


'''def largest(a,b,c):
    return max(a,b,c)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
print("Largest=",largest(a,b,c))
'''


'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
num=int(input("Enter a number:"))
print("Factorial=",factorial(num))'''

'''
def reverse_string(text):
    return text[::-1]
string=input("Enter a string:")
print("Reversed string=",reverse_string(string))'''

'''
def count_vowels(text):
    count=0
    vowels="aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count+=1
    return count
string=input("Enter a string:")
print("number of vowels=",count_vowels(string))'''

'''def area_circle(radius):
    return 3.14*radius*radius
r=float(input("enter radius:"))
print("area od circle=",area_circle(r))'''




'''def is_prime(num):
    if num % 2==0:
        return "Not prime"
    else:
        return"prime"
n=int(input("enter a number:"))
print(is_prime(n))'''
'''
def average(numbers):
    return sum (numbers)/ len (numbers)
nums=[10,20,30,40,50]
print("avearge=",average(nums))'''


'''def maximum(numbers):
    return max(numbers)
nums=[10,25,15,40,30]
print("maximum=",maximum(nums))'''



'''add=lambda x,y:x+y
print(add(5,3))'''



'''square=lambda n:n*n
print("square:",square(4))'''


'''cube=lambda n:n*n*n
print("cube:",cube(3))'''

'''even_odd=lambda n:"Even" if n%2==0 else"Odd"
print("4 is:",even_odd(4))'''

'''greater=lambda a,b:a if a>b else b
print("Greater:",greater(10,20))'''


'''Area=lambda l,w:l*w
print("Area:",Area(5,4))'''



'''c_to_f=lambda c:(c*9/5)+32
print("25C to f:",c_to_f(25))'''


'''s=input("Enter a string:")
print("you entered:",s)
print("length:",len(s))
print("uppercase:",s.upper())
print("Lowercase:",s.lower())
print("charcters without spaces:",len(s.replace(" ","")))
print("Reversed:",s[::-1])

vowels="aeiouAEIOU"
V=sum(1 for ch in s if ch in vowels)
C=sum (1 for ch in s if ch.isalpha()and ch not in vowels)
print("vowels:",V,"consonants:",C)


words=s.split()
print("Number of words:",len(words))

print("First:",s[0],"Last:",s[-1])

'''


s="Hello world 123"
print("upper():",s.upper())
print("lower():",s.lower())
print("strip():",s.strip())
print("replace():",s.replace("World","python"))
words=s.split()
print("split():",words)
print("join():","-".join(words))
print("find():",s.find("world"))
print("count():",s.count("l"))
print("stratswith():",s.strip().startswith("hello"))
print("endwith():",s.strip().endswith("!23"))
print("isalpha():","hello".isalpha())
print("isdigit():","123".isdigit())
print("isalnum():","Hello123".isalnum())
print("capitalize():","Hello world".capitalize())
print("title():","hello world".title())
