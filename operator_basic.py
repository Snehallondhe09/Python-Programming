a=10
b=20
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a%b=",a%b)
print("a/b=",a/b)



#relatonal 
a=20
b=30
print("a==b=",a==b)
print("a!=b=",a!=b)
print("a>b=",a>b)
print("a<b=",a<b)
print("a>=b=",a>=b)
print("a<=b=",a<=b)



#logical
a=20
b=10
c=30
print(a>b and c>a)
print(a<b or c<a)
print(not(a>b))





#assignment 
a=30
print(a)
a=a+2
print(a)
a=a-2
print(a)
a=a*2
print(a)
a=a%2
print(a)
a=a/b
print(a)




year=2024
if year% 400==0:
        print("year is a leap year")
elif year%100==0 :
        print("year is not a leap year")
elif year%4==0:
        print("year is a leap year")
else:
        print("year is not leap year")


        correct_username="snehal"
        correct_password=123456789
        username_input=input("enter name")
        password_input=input("enter password")
if username_input==correct_username and password_input==correct_password:
             print("login successful")
else:
        print("invalid credentials")