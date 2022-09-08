import turtle
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)     # change the width of the pen
pen.color("black")
pen.hideturtle()
pen.speed(0)

grade = turtle.numinput ("Grades", "Enter Grade", 80, 0, 100)

radius = turtle.window_width()//6
eye_radius = radius // 4
mouth_radius = radius // 2

#draw head
pen.up()
pen.setpos(0, -radius)
pen.down()
pen.color("gold")
pen.begin_fill()
pen.circle(radius)
pen.end_fill()

#draw left eye
pen.up()
pen.setpos(-radius//3,0)
pen.down()
pen.color("gray")
pen.begin_fill()
pen.circle(eye_radius)
pen.end_fill()

#draw right eye
pen.up()
pen.setpos(radius//3,0)
pen.down()
pen.color("gray")
pen.begin_fill()
pen.circle(eye_radius)
pen.end_fill()

# based on grade draw smile
pen.color("red")
pen.pensize(5)
if grade >= 89.5:
    pen.up()
    pen.setpos(-mouth_radius, -radius//3)
    pen.down()

    #happy face 
    pen.setheading(-60)
    pen.circle(mouth_radius, 120)

# straight face
elif grade >= 79.5: 
    pen.up()
    pen.setpos(-mouth_radius, -radius//3)
    pen.down()

    pen.forward(mouth_radius * 2)

else:
    pen.up()
    pen.setpos(-mouth_radius, -radius//2)
    pen.down()

    #sad face 
    pen.setheading(60)
    pen.circle(-mouth_radius, 120)
    
turtle.done()
