import turtle
import random

def drawBike(x, y, color):
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
    #turtle.write(name, align='center', font=('Arial', 25, 'normal'))

def setup():
    turtle.bgcolor("sky blue")
    turtle.pen(speed=0)
    turtle.pensize(4)
    turtle.hideturtle()
    turtle.color('tan')
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
def clicked(x, y): #Click handler

    #Print location of the click
    print("Clicked ", x, " ", y)

    #Draw a bike at the location 
    colors = [ 'blue', 'red', 'green', 'cyan', 'purple', 'orange', 'black', 'white', 'yellow', 'pink']
    print(len(colors))
    drawBike(x, y, colors[random.randint(0, len(colors)-1)])





#Setup the screen and the turtle
setup()

#Start listening for left-clicks and call clicked(x, y)
turtle.onscreenclick(clicked)
turtle.done()