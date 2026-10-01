from random import randint,choice
from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Maths Quiz")
headingLabel=Label(root,text="Maths Quiz",font=('arial,20'))

headingLabel.grid(row=0 ,column=0)
number1=randint(1,10)
number2=randint(1,10)
operator=choice(['+','-','*','/'])
question=str(number1)+ operator +str(number2)
answer=eval(question)
def generateQuestion():
   global question ,answer
   number1=randint(1,10)
   number2=randint(1,10)
def checkAnswer():
    if str(answer)==givenAnswer.get():
     print("Correct")
     resultLabel=Label(root,text="corect",font=('arial',20))
     resultLabel.grid(row=3,column=0)
    else:
       print("Your answer is incorect")


givenAnswer=StringVar()



#User interface
questionLabel=Label(root,text=question,font=('arial',20))
questionLabel.grid(row=1,column=0)
answerEntery=Entry(root,textvariable=givenAnswer, font=('arial',20))
answerEntery.grid(row=2,column=0)
submitButton=Button(root,text="Submit",font=('arial',20),command=checkAnswer)
submitButton.grid(row=2,column=1)
                    

print(question)
print(answer)
root.mainloop()