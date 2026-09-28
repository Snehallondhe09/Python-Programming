cal=input("Enter  an character ; ")
match cal:
   case "+":
     print("addition")
   case "-":
     print("substraction")
   case "*":
     print("multification")
   case "/":
      print("division")
   case _:
      print("invalid choice")