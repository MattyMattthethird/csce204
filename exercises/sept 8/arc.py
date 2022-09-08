import turtle
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)    # change the width of the pen
pen.color("black")
pen.hideturtle()
pen.speed(0)

arc_radius = 100

pen.up()
pen.setpos(-arc_radius, 0)
pen.down()

#happy face
pen.setheading(-60)
pen.circle(arc_radius, 120)

#frown
pen.up()
pen.setpos(0,0)
pen.down()
pen.setheading(60)
pen.circle(-arc_radius, 120)


turtle.done()