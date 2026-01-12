import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")
screen.title("Turtle Graphics - Square")

pen = turtle.Turtle()
pen.pensize(3)
pen.color("darkblue")

for _ in range(4):
    pen.forward(100)
    pen.right(90)

screen.mainloop()
