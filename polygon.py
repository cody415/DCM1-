import turtle

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("lightgrey")
screen.title("Turtle Graphics - Polygons")

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(5)

pen.color("blue", "lightblue")
pen.begin_fill()
for _ in range(3):
    pen.forward(150)
    pen.left(120)
pen.end_fill()

pen.penup()
pen.goto(-200, -200)
pen.pendown()

pen.color("green", "lightgreen")
pen.begin_fill()
for _ in range(2):
    pen.forward(200)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(200, -200)
pen.pendown()

pen.color("red", "pink")
pen.begin_fill()
for _ in range(6):
    pen.forward(100)
    pen.left(60)
pen.end_fill()

screen.mainloop()
