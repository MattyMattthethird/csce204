import turtle
turtle.bgcolor("sky blue")

#Create new turtle
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(-300, 20)
turtle.pendown()

#Draw conductor box
turtle.color("red")
turtle.begin_fill()
turtle.forward(500)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(60)
turtle.end_fill()
turtle.left(90)

turtle.begin_fill()
turtle.penup()
turtle.goto(-300, 80)
turtle.pendown()
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(140)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.right(180)

#Draw First wheel
turtle.penup()
turtle.goto(-300, 0)
turtle.color("black")
turtle.pendown()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.forward(120)
turtle.pendown()

#Draw second wheel
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.forward(200)
turtle.pendown()

#Draw first small wheel
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.forward(120)
turtle.pendown()

#Draw second small wheel
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()


