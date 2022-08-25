import turtle 
turtle.bgcolor("LightPink")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)   #change the width of the pen
pen.color("royal blue")
pen.hideturtle()  #hides the cursor 

# Let's draw!!!
pen.begin_fill()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.end_fill()

pen.up()
pen.setposition(-200,-200)
pen.down()

#draw a different colored triangle
#use right instead of left 
pen.color("gold")
pen.setheading(0)
pen.forward(100)
pen.right(-120)
pen.forward(100)
pen.right(-120)
pen.forward(100)


turtle.done()  #must be the last line of code 

