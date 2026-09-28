'''number=-5
if number>0:
    print("the number is positive")
elif number<0:
    print("the number is negative")
else:
    print("the number is zero")
'''
'''
number=4
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")'''


'''number=int(input("Enter a numbr:"))
if number%5==0 and number%10==0:
    print("divisible by both 5 and 10")
else:
    print("Not divisible by both 5 and 10")'''


'''marks=int(input("Enter a marks:"))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Grade D")
else:
    print("fail")'''


'''num=int(input("enter a number:"))
for i in range(1,11):
    print(num*i)'''



'''for i in range(1,101):
    if i%7==0:
        print(i)'''



'''for i in range(2,51,2):
    print(i)'''

'''for i in range(1,51,2):
    print(i)'''


'''num=int(input("enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
    print("Sum=",sum)'''



'''num=int(input("enter a number:"))
fact=1
for i in range(1,num+1):
  fact=fact*i
  print("Factorial=",fact)'''


'''num=int(input("enter a number:"))
count=0
while num>0:
    count=count+1
    num=num//10
print(count)
'''

'''num=int(input("enter a number:"))
sum=0
while num>0:
    sum=sum+num%10
    num=num//10
print(sum)'''

'''num=int(input("Enter a number:"))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)'''


'''num=int(input("Enter number:"))
t=num
r=0
while num>0:
    r=r*10+num%10
    num=num//10
if t==r:
     print("palindrome")
else:
     print("Not palindrome")
'''


'''num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num %i==0:
      count=count+1
if count==2:
    print("prime")
else:
    print("not prime")'''


'''for n in range(2,101):
    count=0
    for i in range(1,n+1):
       if n%i==0:
          count=count+1
    if count==2:
       print(n)
'''


'''n=int(input("enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)'''

'''
num=int(input("enter a number:"))
largest=0
while num>0:
    digit=num%10
    if digit > largest:
        largest=digit
    num=num//10
print(largest)'''

'''num=int(input("enter a number:"))
smallest=9
while num >0:
    digit=num%10
    if digit <smallest:
        smallest=digit
    num=num//10
print(smallest)
'''
'''

num=int(input("enter a number:"))
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
print("odd=",odd)
    '''


'''num=int(input("enter a number:"))
count=0
while num>0:
    count=count+1
    num=num//10
print(count)'''

'''
num=int(input("enter a number:"))
sum=0
while num >0:
    sum=sum+num%10
    num=num//10
print(sum)'''


'''num=int(input("enter a number:"))
sum=0
while num >0:
    sum=sum+num%10
    num=num//10
print(sum)
'''
'''num=int(input("Enter  a number:"))
rev=0
while num >0:
    rev=rev*10+num%10
    num=num//10
print(rev)'''

'''
num=int(input("enter a number:"))
t=num
r=0
while num >0:
    r=r*10+num%10
    num=num//10
if t==r:
        print("palindrome")
else:
        print("not palindrome")
'''


'''num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
    if count==2:
     print("prime")
else:
     print("not prime")

'''

'''num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
     print("prime")
else:
     print("not prime")'''

for n in range(2,101):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
if count==2:
      print(n)









