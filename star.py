import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Graphics - Star")

pen = turtle.Turtle()
pen.color("yellow")
pen.pensize(2)

for _ in range(5):
    pen.forward(200)
    pen.right(144)

screen.mainloop()
