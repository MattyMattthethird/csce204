import turtle
turtle.bgcolor("sky blue")
turtle.speed(0)
turtle.hideturtle()
def get_candies():
    candies = []
    file = open("scene.txt", "r")
    length = len(file.readlines())
    file = open("scene.txt", "r")
    for i in range(length):
        line = file.readline().rstrip()
        candies.append(line)
    return candies
def draw_concentric_circles(x, y, size, color):
    turtle.penup()
    turtle.setposition(x, y)
    #Draw concentric circles
    for i in range(10):
        if((i+1)%2 == 1): turtle.color("white")
        else: turtle.color(color)
        turtle.right(90)
        turtle.forward((1-(i/9))*size)
        turtle.left(90)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle((1-(i/9))*size)
        turtle.end_fill()
        turtle.penup()
        turtle.setposition(x, y)
def draw_mint(x, y, size):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.color("white")
    
    #Draw two side triangles
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(26.566)
    turtle.forward(2.236*size)
    turtle.left(63.4384)
    turtle.back(2*size)
    turtle.left(63.4384)
    turtle.forward(2.236*size*2)
    turtle.right(63.4384)
    turtle.back(2*size)
    turtle.right(63.4384)
    turtle.forward(2.236*size)
    turtle.end_fill()
    turtle.penup()
    turtle.right(26.566)

    #Draw concentric circles
    draw_concentric_circles(x, y, size, 'red')
def draw_lollipop(x, y, size):
    #Draw base stick
    turtle.penup()
    turtle.setposition(x, y)
    turtle.right(90)
    turtle.width(5)
    turtle.pendown()
    turtle.color('brown')
    turtle.forward(size)

    #Draw conecntric circles
    draw_concentric_circles(x, y + size, size, 'pink')
size = 50
x = -600
for i in range(len(get_candies())):
    if(get_candies()[i] == 'mint'):
        draw_mint(x, 0, size)
    if(get_candies()[i] == 'lollipop'):
        draw_lollipop(x, 0, size)
    x += 4*size + size/4
turtle.done()