import turtle 
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)          # change the width of the pen
pen.color("red")
pen.hideturtle()
pen.speed(0)

# default, min, max 
scale = turtle.numinput("U-haul", "Size (1-10)", 3, 1, 10)

width = turtle.window_width()//12 * scale
height = width // 3
cab_width = width //6
cab_height = height //2 
dwheel = width//4

# set initial position
pen.up()
pen.setpos(-width //2, 0)
pen.down()

# draw the frame
pen.begin_fill()
pen.forward(width)
pen.left(90)
pen.forward(cab_height)
pen.left(90)
pen.forward(cab_width)
pen.right(90)
pen.forward(height - cab_width)
pen.setheading(-180)
pen.forward(width - cab_width)
pen.left(90)
pen.forward(height)
pen.end_fill()

# set position for left wheel
pen.setheading(0)
pen.up()
pen.setpos(-width//4, -dwheel//2)
pen.down()

# draw left wheel
pen.color("Black")
pen.begin_fill()
pen.circle(dwheel//2)
pen.end_fill()

# set position for right wheel
pen.up()
pen.setpos(width//4, -dwheel//2)
pen.down()

# draw right wheel
pen.color("Black")
pen.begin_fill()
pen.circle(dwheel//2)
pen.end_fill()


turtle.done()