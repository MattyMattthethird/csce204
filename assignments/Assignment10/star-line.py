import turtle

num = int(input("How many turtles do u want?: "))

t = turtle.Turtle()
gap = 120

def drawStar(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.setheading(90)
    for n in range(8):
        t.forward(50)
        t.right(135)

for n in range(num):
    drawStar(n * gap, 0)


turtle.done()