import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Viral Neon Spiral Annimation" )

t=turtle.Turtle()
t.goto(300,50)
t.speed(0)
t.color("cyan")

b=200

while b > 0:
    t.left(b)
    t.forward(b * 3)
    b-=1
t.hideturtle()
turtle.done()
