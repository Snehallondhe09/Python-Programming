import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Mandala")
screen.tracer(5)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_heart(size, color):
    t.color(color)
    t.pendown()

    t.left(50)
    t.forward(size)
    t.circle(size * 0.375, 200)
    t.right(140)
    t.circle(size * 0.375, 200)
    t.forward(size)

    t.penup()

def draw_mandala():
    size = 100

    for i in range(36):
        hue = i / 36
        color = colorsys.hsv_to_rgb(hue, 1, 1)

        t.goto(0, -40)
        t.setheading(i * 10)

        draw_heart(size, color)

draw_mandala()

screen.update()
screen.mainloop()