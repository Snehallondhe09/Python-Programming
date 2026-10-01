'''numbers={1,2,3,4,5,6}
print(numbers)

numbers.add(7)
print(numbers)

numbers.remove(1)
print(numbers)

for i in numbers:
    print(i)'''


'''name={"snehal","payal","komal"}
print(name)

for i in name:
    print(i)

name.add("sneha")
print(name)

name.remove("komal")
print(name)

print(len(name))


if "snehal" in name:
    print("snehal is present")
else:
    print("not present")'''



'''num={1,2,3,4,5,6,7}
print(num)
for i in num:
    print(i)

    total=0
    for i in num :
     total=total+i

     print(total)'''


'''number={1,2,3,4,5,6,7}
total=0
for i in number:
    total=total-i

    print(total)'''



student={
    "name":"snehal",
    "Age":19,
    "address":"solapur",
    "number":1234567893

}
print(student)
print(student["Age"])


student["rollno"]=22
print(student)

student["Age"]=23
print(student)

for key in student :
    print(key)

    for val in student.values():
        print(val)


    for k,v in student.items():
            print(k,"  :",v)

    del student["Age"]
    print(student)






    