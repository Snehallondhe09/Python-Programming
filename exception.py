'''class Exception():
    try:
        number=int(input("Enter value:"))
        result=10/number
        print(result)

    except ZeroDivisionError:
        print("You can not divide by zero")


    except ValueError:
        print("Provide only Integer value")

    finally:
        print("hello")
obj=Exception()'''


'''
class Exception():
    try:
       a=10
       b=2
       
       print(a/b)
    except ZeroDivisionError:
        print("You can not divide by Zero")
    except TypeError:
        print("please enter a number")
    finally:
        print("snehal")
obj=Exception()    '''



'''class LowBalanceError(Exception):
    "'raised when an acount Balance'"
    pass

balance=20
if balance<50:
    raise LowBalanceError("balance is to low ")
'''

'''
class Excpetion():
    try:
        number=int(input("Enter a number:"))
        result=10/number
        print(result)
    except ZeroDivisionError:
        print("You can not divide by Zero...!")
    else:
        print("program run ")
obj=Exception()'''
''
   
'''age=15
if age <18:
    raise AgeError('minimise age is 18')
'''''


'''class Exception():

  num=int(input("enter a number:"))
  if num<100:
    raise ValueError("Provide only integer value")


obj=Exception()'''

class EXception:
    try:
        name=str(input("Enter a value:"))
        result=10/name
        print(result)
    except TypeError:
        print("print only name")
    except ValueError:
        print("can not print the name")
    except ZeroDivisionError:
        print("You can not divide by Zero")
    finally:
        print("end program")

obj=Exception()
