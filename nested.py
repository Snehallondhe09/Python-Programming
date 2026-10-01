'''for i in range(3):
    for j in range(4):
        print("*" ,end ="  ")
    print()'''


'''rows=5
for i in range(1,rows+1):
    for j in range(i):
        print("*" ,end=" ")
    print()'''


'''i=1
while i<=5:
    print(" * " * i)
    i+=1'''


rows=5
for i in range( 1,rows+1):
    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(i-1):
     print(" * ",end=" ")
    print()
