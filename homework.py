##name=input("Enter your name")##
#print("welcome: ",name)##




'''num1=float(input("Enter number1 :"))
num2=float(input("Enter number2 :"))
sum=num1+num2
print(f"the sum of {num1} and {num2} is {sum}")
print(sum)'''




'''number=int(input("enter a number: "))
square=number**2
print(square)'''


'''length=int(input("enter the length of the rectangle: "))
width=int(input("enter the width of the rectangle: "))
area=length*width
print(area)'''



'''number=int(input("enter a number: "))
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")'''



'''current_year=2026
birth_year=int(input("enter your birth year: "))
age=current_year-birth_year
print(age)'''


'''weight=float(input("enter your weight: " ))
height=float(input("enter your height: "))
bmi=weight/(height**2)
print(bmi)
if bmi<18.3:
    print("underweight")
elif bmi <18:
    print("normal")
elif bmi>14:
    print("overweight")
else:
    print("obese")'''



'''num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
if num1>num2 and num3<num2:
    print("the num1 is largest")
elif num2<num1 and num3>num2:
    print("the num2 is largest")
else:
    print("the num3 is largest")'''



'''marks=[]
for i in range(1,6):
    subject_mark=float(input(f"enter marks of subject{i}:"))
    marks.append(subject_mark)
    total_marks=sum(marks)
    average_marks=total_marks/5
    print(average_marks)'''


'''celsius=float(input("enter temperature in celsius: "))
fahrenheit=(celsius*9/5)+32
print(fahrenheit)'''



'''total_minutes=int((input("enter minutes: ")))
hours=int(total_minutes/60)
remaining_minutes=total_minutes-(hours*60)
print("hours: ",hours)
print("minutes:",remaining_minutes)'''


'''principal=float(input("enter the principal amount:"))
rate=float(input("enter the annual interest rate(in%):"))
time=float(input("enter the time period (in years):"))
simple_interest=(principal*rate*time)/100
print(simple_interest)'''




'''name=input("enter your name: ")
age=input("enter your age: ")
city=input("enter your city: ")
print(name)
print(age)
print(city)'''


'''number=int(input("enter a number to print its multification table: "))
for i in range (1,11):
    result=number*i
    print(result)'''


first_name=input("enter the first name: ")
last_name=input("enter the last name: ")
full_name=first_name +"  "+ last_name
print("full name:" ,full_na