number=-5
if number>0:
    print("the number is positive")
elif number<0:
    print("the number is negative ")
else:
    print("the number is zero")


    #check whether a number is even or odd
    num=5
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")

        #find the greater number between two numbers
        num1=12
        num2=10
        if num1>num2:
            print("the num1 is greater")
        elif num2>num1:
            print(" the num2 is greater")
        else:
            print(" both numbers are equal")

            #check if a person is eligible to vote (age>_18)
age=20
if age>=10:
    print("eligible to vote")
else:
    print("not eligible to vote")

    #check whether a student is pass or fail(passing marks=35)
    mark=45
    if mark>=35:
        print("pass")
    else:
        print("fail")

        #find the largest among three numbers
num1=20
num2=40
num3=50
if num1>=num2 and num2>=num3:
    print("num1 is largest")
elif num1>=num3 and num2>=num3:
    print("num2 is largest")
else:
    print("num3 is largest")

    #calculate grade
    #marks>=90-A
    #marks>=75-b
    #marks>=60-c
    #marks>=35-d
    #otherwise-fail
mark=85
if mark>=90:
    print("grade A")
elif mark>=75:
    print("grade B")
elif mark>=75:
    print("grade C")
elif mark>=60:
    print("grade D")
else:
    print("fail")



    #check wheather a year is a leap year
    year=2024
    if year% 400==0:
        print("year is a leap year")
    elif year%100==0 :
        print("year is not a leap year")
    elif year%4==0:
        print("year is a leap year")
    else:
        print("year is not leap year")


        #create a simple calculator using +,-,*,/
        a=20
        b=30
        print(a+b)
        print(a-b)
        print(a*b)
        print(a/b)

        #display the day of the week based on a number(1-7)
day=7
print(day)
day1="sunday"
print(day1)
day2="monday"
print(day2)
day3="thuesday"
print(day3)
day4="wednesday"
print(day4)
day5="thursday"
print(day5)
day6="friday"
print(day6)
day7="saturday"
print(day7)



#check whether a character is :alphabet ,digit,special character 
char="@"
if char.isalpha():
    print("is an alphabet")
elif char.isdigit():
    print("is a digit")
else:
    print("is a special character")


    #calculate BMI and display:underweight,normal,overweight,obese
    weight=45
    height=5.5
    bmi=weight/(height**2)
    print("your bmi is :(bmi.1f)")
    if bmi<18.5:
        print("underweight")
    elif bmi >= 18.5 and bmi < 25.0:
        print("Category: Normal weight")
    elif bmi >= 25.0 and bmi < 30.0:
        print("Category: Overweight")
    else:
        print("Category: Obese")




#calculate movie ticket price:age<12-$100,age12-60-$200,age>60$150
age=25
if age<12:
    price=100
elif age<=60:
    price=200
else:
    price=150
    print("price:${price}")


    #create a login system:check username & password ,dispaly "login successful or invalid credentials"
    username="snehal"
    password=123456789
    if username=="snehal"and password==123456789:
        print("login successful")
    else:
        print("invalid credentials")


    bill_amount=0
if units<=100:
    bill_amount=units*5
elif units<=200:
    bill_amount=(100*5)+((units-100)*7)
else:
    bill_amount=(100*5)+(100*7)+((units-200)*100)
    print("total electricity bill:{bill amount}")
