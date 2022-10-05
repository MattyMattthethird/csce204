import turtle 
import random
turtle.bgcolor("sky blue")
turtle.title("Biking Party Fun Time")

bike_names = []
bike_color = []

def drawBike(x, y, color, name):
    turtle.color(color)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(60)
    turtle.pendown()
    turtle.forward(120/3)
    turtle.right(60)
    turtle.forward(35/6)
    turtle.back(35/3)
    turtle.forward(35/6)
    turtle.right(120)
    turtle.forward(20/3)
    turtle.left(60)
    turtle.forward(100/3)

    #First wheel
    turtle.right(30)
    turtle.penup()
    turtle.forward(45/3)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(45/3)
    turtle.penup()
    turtle.right(90)
    turtle.back(45/3)
    turtle.left(30)
    turtle.pendown()

    turtle.right(120)
    turtle.forward(100/3)
    turtle.right(60)
    turtle.forward(100/3)
    turtle.right(120)
    turtle.forward(100/3)
    turtle.back(100/3)
    turtle.left(60)
    turtle.back(100/3)

    #Second wheel
    turtle.right(150)
    turtle.penup()
    turtle.forward(45/3)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(45/3)
    turtle.penup()
    turtle.right(90)
    turtle.back(45/3)
    turtle.left(150)
    turtle.pendown()

    turtle.forward(160/3)
    turtle.right(60)
    turtle.forward(35/3)
    
    turtle.penup()
    turtle.setposition(x, y-50)
    turtle.write(name, align='center', font=('Arial', 25, 'normal'))
def setup():
    turtle.pen(speed=0)
    turtle.pensize(4)
    turtle.hideturtle()
    turtle.color('brown')
    turtle.penup()
    turtle.setposition(-1000, -300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(2000)
    turtle.left(90)
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(2000)
    turtle.left(90)
    turtle.forward(600)
    turtle.end_fill()

setup()
count = int(turtle.numinput("# of Bikes", "Bikes(0-10)", minval=0, maxval=10))

for i in range(count):
    bike_names.append(turtle.textinput("Bike Properties", "Name of bike "+str(i)))
    bike_color.append(turtle.textinput("Bike Properties", "Color of bike "+str(i)))
for i in range(count):
    drawBike(-550+(100*i), random.randint(-300, 300), bike_color[i], bike_names[i])




turtle.done()