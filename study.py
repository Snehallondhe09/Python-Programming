'''animals=["cat","dog","monkey","elephant"]
print(animals)
for i in animals:
    print(i)
    animals[0]="ox"
    print(animals[0])
    print(animals)
    animals.remove("ox")
    print(animals)'''

'''

#tuple
student=("snehal","navnath","londhe")
print(student)
for i in student:
    print(i)

student= {
    "name":"snehal",
    "fathername":"navnath",
    "sarname":"londhe"
}
print(student)

for key in student:
    print(key)
for val in student.values():
        print(val)
for k,v in student.items():
            print(k," ",v)'''


'''name={"snehal","navnath","londhe"}
if "snehal" in  name:
    print("key exits")
else:
    print("key does not exits")
''''''
numbers={1,2,3,4,5,6,7,8}
print(numbers)
print(len(numbers))'''

'''
my_dict={"a":1,"b":2}
del my_dict'''


marks={
    "snehal":86,
    "sneha":90,
    "adity":75,
    "komal":50
}
highest_mark=max(marks.values())
print(highest_mark)


