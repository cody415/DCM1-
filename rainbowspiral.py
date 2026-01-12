import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral Web")

pen = turtle.Turtle()
pen.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(360):
    pen.color(colors[i % 7])
    pen.forward(i * 2)
    pen.right(59)

screen.mainloop()
