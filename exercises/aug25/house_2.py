import turtle
turtle.bgcolor("light pink")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)          # change the width of the pen
pen.color("peru")
pen.hideturtle()        # hides the cursor
pen.speed(0)

house_size = 100

pen.up()
pen.setpos(-house_size//2, -house_size//2)
pen.down()
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.left(90)

# roof
pen.up()
pen.setpos(-house_size * .6 , house_size//2)
pen.down()
pen.forward(house_size * 1.2)
pen.left(120)
pen.forward(house_size * 1.2)
pen.left(120)
pen.forward(house_size * 1.2)
pen.left(120)

turtle.done()  # must be the last line of the file.