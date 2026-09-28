#list
'''student=["Snehal","komal","payal","sonal"]
print(student)
for i in student:
    print(i)
print(student[0])
student[0]="sakshi"
print(student[0])
print(student)
student.append("sejal")
print(student)
student.remove("sejal")
print(student)'''
'''

#create
fruits=["apple","banana","mango","kiwi"]
print(fruits)
for i in fruits:
    print(i)

#read
print("read:",fruits[0])
#update
fruits[1]="graps"
print("update:",fruits)
#delete
fruits.remove("graps")
print("delete:",fruits)'''



'''colors=("red","pink","black")
res=list(colors)
print(colors)
print(res)
print(colors)
for i in colors:
    print(i)
'''

'''num=[1,2,3,4,5]
res=tuple(num)
print(num)
print(res)

'''


'''numbers=(1,2,3,4,5,6)
res=list(numbers)
print(numbers)
print(res)'''


#set
'''numbers={1,2,3,4,5,6}
print(numbers)
for i in numbers:
    print(i)
numbers.add(7)
print(numbers)
numbers.remove(1)
print(numbers)
print(len(numbers))
if 7 in numbers:
    print("7 is present")
else:
    print("not present")'''

'''
num={1,2,3}
total=0
for i in num:
    total=total+i
    print(total)'''


'''student={
    "name":"snehal",
    "age":19,
    "address":"pune"
}
print(student)
print(student["age"])
student["rollno"]=22
print(student)
student["age"]=25
print(student)
for key in student:
    print(key)
for val in student.values():
    print(val)
for k ,v in student.items():
    print(k," : " ,v )
del student["age"]
print(student)'''


'''
fruits={
    "fruits1":"mango",
    "friuts2":"banana",
    "fruits3":"kiwi",
    "Fruits4":"apple"
}
print(fruits)
print(fruits["fruits3"])
fruits["fruits5"]="orange"
print(fruits)
for key in fruits:
    print(key)
for val in fruits.values():
    print(val)
for k,v in fruits.items():
    print(k,":",v)
del fruits["fruits1"]
print(fruits)'''


a=[1,2,3,4,5,6,7,8,9,10,11,12]
print(a[0:13])