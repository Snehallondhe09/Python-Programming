book={
    1:"math",
    2:"english",
    3:"science",
    4:"marathi",
    5:"history"
}
print(book)
book[2]="C++"
print(book)
for key in book:
    print(key)
for val in book.values():
     print(val)
for k,v in book.items():
     print(k," : ",v) 
print(book)
print(len(book))
if 2 in book:
     print("2 is present")
else:
     print("not present")