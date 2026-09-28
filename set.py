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



for val in student.values():
        print(val)


for k,v in student.items():
            print(k,"  :",v)

del student["Age"]
print(student)






    