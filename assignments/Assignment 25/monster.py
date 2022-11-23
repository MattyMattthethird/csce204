import turtle
import random

class monster:
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, pen):
        self.pen = pen
        self.pen.color(self.color)
        self.draw_body()
        self.draw_eyes()
        self.draw_mouth()
        self.draw_nose()
        self.pen.setheading(0)

    def draw_body(self):
        self.pen.penup()
        self.pen.setposition(self.x,self.y)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.right(70)
        self.pen.forward(self.width/2)
        self.pen.left(90)
        self.pen.forward(self.width/2)
        self.pen.left(90)
        self.pen.forward(self.width)
        self.pen.left(90)
        self.pen.forward(self.width)
        self.pen.left(90)
        self.pen.forward(self.width)
        self.pen.left(90)
        self.pen.forward(self.width/2)
        self.pen.end_fill()

        #Draw arms
        self.pen.penup()
        self.pen.setposition(self.x,self.y)
        self.pen.left(20)
        self.pen.pendown()
        self.pen.width(6)
        self.pen.forward(self.width)
        self.pen.back(self.width*2+self.width*0.5)
        
        #Draw legs
        self.pen.penup()
        self.pen.setposition(self.x,self.y)
        self.pen.width(12)
        self.pen.left(50)
        self.pen.pendown()
        self.pen.back(self.width)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.width*0.3)
        self.pen.right(90)
        self.pen.forward(self.width)

    def draw_eyes(self):
        self.pen.penup()
        self.pen.setheading(20)
        self.pen.width(1)
        self.pen.setposition(self.x,self.y)
        self.pen.color('white')
        self.pen.left(20)
        self.pen.forward(self.width/4)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(self.width/8)
        self.pen.end_fill()

        self.pen.penup()
        self.pen.left(90)
        self.pen.forward(self.width/48)
        self.pen.pendown()
        self.pen.color('black')
        self.pen.right(90)
        self.pen.begin_fill()
        self.pen.circle(self.width/16)
        self.pen.end_fill()

        self.pen.penup()
        self.pen.setposition(self.x,self.y)
        self.pen.color('white')
        self.pen.right(40)
        self.pen.back(self.width/4)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(self.width/8)
        self.pen.end_fill()

        self.pen.penup()
        self.pen.left(90)
        self.pen.forward(self.width/48)
        self.pen.pendown()
        self.pen.color('black')
        self.pen.right(90)
        self.pen.begin_fill()
        self.pen.circle(self.width/16)
        self.pen.end_fill()

    def draw_mouth(self):
        self.pen.penup()
        self.pen.width(5)
        self.pen.setposition(self.x,self.y-self.width/4)
        self.pen.right(20)
        self.pen.color('black')
        self.pen.pendown()
        self.pen.circle(self.width/4, 110)
        self.pen.width(1)

    def draw_nose(self):

        colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow', 'black', 'white']

        #choose how many noses he will have from 5 - 15
        iterations = random.randint(3, 15)

        for i in range(iterations):
            self.pen.color(colors[random.randint(0,len(colors)-1)])
            self.pen.penup()
            self.pen.setposition(self.x,self.y)
            self.pen.setheading(0)
            self.pen.right(70)
            self.pen.pendown()
            self.pen.begin_fill()
            self.pen.forward(((iterations-i)/iterations)*self.width/6)
            self.pen.left(90)
            self.pen.forward(((iterations-i)/iterations)*self.width/4)
            self.pen.left(120)
            self.pen.forward(((iterations-i)/iterations)*self.width/2)
            self.pen.left(120)
            self.pen.forward(((iterations-i)/iterations)*self.width/2)
            self.pen.left(120)
            self.pen.forward(((iterations-i)/iterations)*self.width/4)
            self.pen.end_fill()
