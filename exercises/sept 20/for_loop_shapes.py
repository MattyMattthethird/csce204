import turtle
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)       # change the width of the pen
pen.color("Black")
pen.hideturtle()
pen.speed(0)

shape = turtle.textinput("Shape", "Enter Shape").lower().strip()
shape_width = turtle.window_width()//5

pen.up()
pen.setpos(-shape_width//2, -shape_width//2)
pen.down()

if shape == "circle":
    pen.up()
    pen.setx(0)
    pen.down()
    pen.circle(shape_width//2)
elif shape == "square":
    pen.color("cyan")
    pen.begin_fill()
    for i in range(4):
        pen.forward(shape_width)
        pen.left(90)
    pen.end_fill()
elif shape == "triangle":
    for i in range(3):
        pen.forward(shape_width)
        pen.left(120)
else:
    print("sorry, invalid shape")

