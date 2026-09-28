'''import re 
text="I am learning Python Programming"
if re.search(r"\bPython\b",text):
    print("Python is present")
else:
    print("Python does not present")'''
'''
import re
text="My age is 20"
res=re.findall(r"\d+",text)
print(res)'''


'''import re
text="My Name is snehal"
res=re.findall(r"\D+",text)
print(res)'''

'''import re
text="12345"
if re.fullmatch(r"\d+",text):
    print("String contains only numbers")
else:
    print("strings does not contains only numbers")
'''


'''import re
text="Python"
if re.fullmatch(r"[A-Za-z]+",text):
    print("String contain only alphabets")
else:
    print("String does not contain only aplhabets")'''



'''import re
text="Apple is an Amazing and Awesome fruit"
result=re.findall(r"\b[Aa]\w",text)
print(result)'''

'''
import re
text="This is a class of students and books"
result=re.findall(r"\b\w*s\b",text)
print(result)'''


'''import re
text="My number are 12,123,4567 and 789"
result=re.findall(r"b\d{3}\b",text)
print(result)'''


'''import re
text="Hello Python World"
result=re.sub(r"\s+","-",text)
print(result)'''

'''
import re
text="My email is abc@gmail.com"
result=re.findall(r"[A-Za-Z0-9._%+-]+@[A-Za-Z0-9.-]+\.[A-Za-z]{2}",text)
print(result)'''

'''
import re
mobile="8999612077"
if re.fullmatch(r"\d{10}",mobile):
    print("valid mobile number")
else:
    print("Invalid mobile number")'''


'''import re
text="Python 123 is easy 456"
result=re.findall(r"\d",text)
print(result)'''


'''import re
text="Python is Powerful and Popular"
result=re.findall(r"\bP\w*",text)
print(result)'''


'''import re
text="Python123"
result=re.sub(r"\d","",text)
print(result)'''
'''
import re
text="Hello Python "
if re.match(r"^Hello",text):
    print("string starts with hello")
else:
    print("string does not  start with hello")'''