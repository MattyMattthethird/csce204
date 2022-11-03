import turtle
turtle.bgcolor("white")

#setup pen
pen = turtle.Turtle()
pen.pensize(2)
pen.hideturtle()
pen.speed(0)

#returns a list of colors from text file
def get_colors(): 
    colors = []

    try:
    # read in the movie file and add each movie to the list 
        with open("exercises/Nov 1/colors.txt") as file:
            for line in file: 
                if line.strip() != "":
                    colors.append(line.strip())
    except FileNotFoundError:
        print("Invalid File Name ")

    return colors

def draw_color_strip(y, height, color):
    x = - turtle.window_width()//2
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()

    # draw rectangle 
    for i in range(4):
        if i % 2 == 0:
            pen.forward(turtle.window_width())
        else: 
            pen.forward(height)
        pen.left(90)

    pen.end_fill()

# main program 
colors = get_colors()
y = - turtle.window_height()//2
height = turtle.window_height()/len(colors)

for color in colors: 
    draw_color_strip(y, height, color)
    y+= height 

turtle.done()