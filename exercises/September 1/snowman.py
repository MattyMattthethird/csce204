import turtle 
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)          # change the width of the pen
pen.color("white")
pen.hideturtle()

# default, min, max
scale = turtle.numinput("Snowman", "Size (1-5)", 3, 1, 5)

ldiameter = turtle.window_height()//12 * scale
mdiameter = ldiameter * 2 // 3
sdiameter = mdiameter * 2 // 3

# draw large snowball fill it white
pen.up()
pen.setpos(0, - ldiameter)
pen.down()
pen.begin_fill()
pen.circle(ldiameter//2)
pen.end_fill()

# draw medium snowball fill it white
pen.up()
pen.setpos(0, 0)
pen.down()
pen.begin_fill()
pen.circle(mdiameter//2)
pen.end_fill()

# draw small snowball fill it white 
pen.up()
pen.setpos(0, mdiameter)
pen.down()
pen.begin_fill()
pen.circle(sdiameter//2)
pen.end_fill()

turtle.done()
