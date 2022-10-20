import turtle
import random
turtle.bgcolor('sky blue')
colors = [ "red", "green", "orange", "blue", "purple", "yellow", "brown", "black", "white" ]
def draw_triangle(x, y, width, color):
    turtle.color(color)
    for i in range(7):
        turtle.penup()
        turtle.setposition((x+width/2) - (i/16)*width, (y-width/2) + (i/16)*width)
        turtle.left(120)
        turtle.pendown()
        turtle.forward(width- (i/8)*width)
        turtle.left(120)
        turtle.forward(width- (i/8)*width)
        turtle.left(120)
        turtle.forward(width- (i/8)*width)
        turtle.color(colors[random.randrange(0, 9)])
for i in range(20):
    draw_triangle(random.randrange(-300, 300), random.randrange(-300, 300), random.randrange(50, 200), 'red')
turtle.done()