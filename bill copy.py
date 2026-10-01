units=150
if units<=100:
    bill=units*5
elif units<=20:
    bill=units*7
else:
    bill=units*10
print("total electricity bill:{bill}")



units=int(input("enter total units"))
if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+(units-100)*7
else:
    bill=(100*5)+(100*7)+(units-200)*10
    print("total electricity bill=$",bill)





    units=5
    if units<=100:
        bill=units*5
    elif units<=200:
        bill=units*7
    else:
        bill=units*10
        print("total electricity bill: ",bill)

