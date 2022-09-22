import turtle
import random
turtle.bgcolor("sky blue")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)       # change the width of the pen
pen.color("Black")
pen.hideturtle()
pen.speed(0)
turtle.colormode(255)
style = ("Arial", 12, "normal")

# ask the user for their name
user_name = turtle.textinput("Name Program", "Name: ")

# Ask the user how many times they want to see their name.
num_display = int(turtle.numinput("Name Program", "How many names", 10, 1, 100))

# loop through and display their name the given number of times
# Initially they will all be ontop of each other.
for i in range(num_display):
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    pen.color(r, g, b)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write(user_name)

    turtle.done()

