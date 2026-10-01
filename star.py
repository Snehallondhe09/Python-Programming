'''rows=4
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''


'''rows=10
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2 * i - 1):
     print("*",end=" ")
    print()'''



'''rows=5
for i in range(1,rows+1):
    for j in range(rows - i):
        print(" ",end=" ")
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == rows:
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print()'''





'''rows = 5  

for i in range(1, rows + 1):  
    for j in range(rows - i):  # Print spaces
        print(" ", end=" ")  
    for k in range(2 * i - 1):  
        if k == 0 or k == 2 * i - 2 or i == rows:  # Print stars at borders
            print("*", end=" ")  
        else:  
            print(" ", end=" ")  # Print spaces inside
    print()'''



rows=5
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2 * (rows - i)):
        print(" ",end=" ")
    for j in range(i):
       print("*",end=" ")
print()



for i in range(rows-1,0,-1):
   for j in range(i):
       print("*",end=" ")
   for k in range(2 * (rows - i)):
       print(" ",end=" ")
   for j in range(i):
       print("*",end=" ")
print()
