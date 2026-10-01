units=150
if units <=100:
    bill=units*5
elif units<=200:
    bill=units*7
else:
    bill=units*10
    print("total electricity bil:${bill}")




    year=2024
    if year%4==0:
        print("leap year")
    else:
        print("not a leap year")