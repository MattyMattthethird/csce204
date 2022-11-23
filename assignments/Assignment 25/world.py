import turtle
import monster
import random

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
turtle.bgcolor('sky blue')


xwidth, yheight = 600, 400
colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow', 'black', 'white']
maxSize = 400

#Loop it ten times
for i in range(10):
    m = monster.monster(random.randint(-xwidth, xwidth), random.randint(-yheight, yheight), random.randint(10, maxSize), colors[random.randint(0,len(colors)-1)])
    m.draw(pen)
turtle.done()