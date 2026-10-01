'''num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)
'''


'''def factorial(n):
    fact=1
    for i in range(1,n+1):
         fact=fact*i
    return fact
num=int(input("Enter a number:"))
result=factorial(num)
print("factorial:",result)'''


def palindrome(s):
    if s ==s[::-1]:
        return "palindrome"
    else:
        return"not palindrome"
text=input("Enter a sting:")
print(palindrome(text))