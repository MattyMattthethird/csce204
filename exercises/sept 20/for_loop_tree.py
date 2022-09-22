import turtle
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)       # change the width of the pen
pen.color("Black")
pen.hideturtle()
pen.speed(0)

trunk_width = turtle.window_width()//8
bottom_width = trunk_width *3
middle_width = bottom_width *2/3
top_width = middle_width *2/3

# draw a brown trunk
pen.up()
pen.setpos(-trunk_width, -trunk_width)
pen.down()
pen.color("sienna")
pen.begin_fill()
for i in range(4):
    pen.forward(trunk_width)
    pen.left(90)
pen.end_fill()

# draw big triangle
pen.up()
pen.setpos(-bottom_width//2, 0)
pen.down()
pen.color("forest green")
pen.begin_fill()
for i in range(3):
    pen.forward(bottom_width)
    pen.left(120)
pen.end_fill()



# draw middle triangle
pen.up()
pen.setpos(-middle_width//2, middle_width)
pen.down()

pen.color("forest green")
pen.begin_fill()
for i in range(3):
    pen.forward(middle_width)
    pen.left(120)
pen.end_fill()

# draw top triangle 
pen.up()
pen.setpos(-top_width//2, (bottom_width + middle_width) *1/2)
pen.down()

pen.color("forest green")
pen.begin_fill()
for i in range(3):
    pen.forward(top_width)
    pen.left(120)
pen.end_fill()


turtle.done()