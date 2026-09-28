import re
text="my mobile number is 9245357989"
result=re.findall(r"\D+",text)
print(result)

'''import re
name="my age is 19"
result=re.findall(r"\D+",name)
print(result)'''


'''import re
text="python_123"
res=re.findall(r"\W",text)
print(res)
'''

'''import re
text="snehal navnath londhe"
res=re.findall(r"\S",text)
print(res)
'''
'''
text="snehal"
res=re.findall(r"s.e",text)
print(res)'''
'''
text="cat bat rat"
rest=re.findall(r"[cbr]at",text)
print(rest)


res=re.findall(r"[a-z]+","Python123")
print(res)

text="python is easy" 
res=re.search(r"python$",text)
print(res)


text="I am learning Python"
result=re.search(r"ok",text)
print(result)
res=re.search(r"\d+","age 25").group()
print(res)'''

'''text="Python is easy"
res=re.match(r"Python","I love Python")
print(res)'''

'''
mobile="723456789"
res=re.fullmatch(r"[6-9]\d{9}",mobile)
print(res)
'''

import re
text="my name is snehal navnath londhe and my number is 123456789"
res=re.findall(r"\d+",text)
print(res)

'''#\w
text="python_123#"
res=re.findall(r"\W",text)
print(res)'''
'''
#\s
text="my name is snehal"
res=re.findall(r"\S",text)
print(res)'''

#\.

'''text="Snehal"
res=re.findall(r"\S.e",text)
print(res)


#\[]
text="cat "
'''