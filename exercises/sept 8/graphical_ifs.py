import turtle
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)    # change the width of the pen
pen.color("black")
pen.hideturtle()
pen.speed(0)

shape = turtle.textinput("Shapes", "Enter Shape").lower().strip()

shape_size = turtle.window_width()//6

if shape =="circle":
    radius = shape_size//2
    pen.up()
    pen.setpos(0, -radius)
    pen.down()
    pen.circle(radius)
elif shape == "square": 
    pen.up()
    pen.setpos(-shape_size, -shape_size//2)
    pen.down()
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
elif shape == "triangle":
    pen.up()
    pen.setpos(-shape_size//2, -shape_size//2)
    pen.down()
    pen.forward(shape_size)
    pen.left(120)
    pen.forward(shape_size)
    pen.left(120)
    

    

turtle.done()