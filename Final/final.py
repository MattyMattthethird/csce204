import turtle
import random
import time

turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("sky blue")
row_0 = [ "", "", "" ]
row_1 = [ "", "", "" ]
row_2 = [ "", "", "" ]
rows = [ row_2, row_1, row_0 ]

board_center = [ 0, 0 ]
gridWidth = 100
lineWidth = 15

if(random.randrange(0, 1) == 0): player = "X"
else: player = "O"

def RandomizeColor():
    colors = ["blue", "red", "green", "gold", "purple", "orange", "yellow", "black", "grey"]
    turtle.color(colors[random.randrange(0, len(colors)-1)])


def draw_board(x, y, widthSquare, widthLine):
    turtle.penup()
    turtle.setposition(x + widthLine/2 + widthSquare/2, y + (3*widthSquare)/2 + widthLine)
    turtle.setheading(90)
    turtle.width(widthLine)
    turtle.pendown()
    RandomizeColor()
    turtle.back(3*widthSquare + 2 * widthLine)
    turtle.penup()
    turtle.setposition(x - widthLine/2 - widthSquare/2, y + (3*widthSquare)/2 + widthLine)
    turtle.pendown()
    RandomizeColor()
    turtle.back(3*widthSquare + 2 * widthLine)
    turtle.penup()
    turtle.setposition(x + (3*widthSquare)/2 + widthLine, y - widthLine/2 - widthSquare/2)
    turtle.right(90)
    turtle.pendown()
    RandomizeColor()
    turtle.back(3*widthSquare + 2 * widthLine)
    turtle.penup()
    turtle.setposition(x + (3*widthSquare)/2 + widthLine, y + widthLine/2 + widthSquare/2)
    turtle.pendown()
    RandomizeColor()
    turtle.back(3*widthSquare + 2 * widthLine)


def draw_letter(gridX, gridY, isX):
    RandomizeColor()
    x = gridX * (lineWidth + gridWidth) + board_center[0]
    y = gridY * (lineWidth + gridWidth) + board_center[1]
    y -= gridWidth / 2

    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    if (isX): char = 'X'
    else: char = 'O'
    turtle.write(char, align="center", font=("Verdana", gridWidth, "normal"))

def clicked(x, y):
    global player
    if(get_grid_coord(x, y) == None): return
    if(rows[get_grid_coord(x, y)[1]+1][get_grid_coord(x, y)[0]+1] != ""): return

    
    if(player == "X"): isX = True
    else: isX = False

    gridX = get_grid_coord(x, y)[0]
    gridY = get_grid_coord(x, y)[1]

    draw_letter(gridX, gridY, isX)
    rows[gridY+1][gridX+1] = player

    result = checkBoard()
    if(result == None): 
        DisplayWinner("Tie game")
        Reset()
        return
    elif (result == "ongoing"): pass
    elif (result == "X"): 
        DisplayWinner("X won!")
        Reset()
        return
    elif (result == "O"): 
        DisplayWinner("O won!")
        Reset()
        return
    
    if(player == "X"): player = "O"
    else: player = "X"
    

def get_grid_coord(absoluteX, absoluteY):
    if(absoluteX > board_center[0] + (3*gridWidth)/2 + lineWidth or
       absoluteX < board_center[0] -(3*gridWidth)/2 - lineWidth or
       absoluteY > board_center[1] + (3*gridWidth)/2 + lineWidth or
       absoluteY < board_center[1] -(3*gridWidth)/2 - lineWidth):
        return None
    if(absoluteX > board_center[0] + gridWidth/2 + lineWidth/2): 
        gridX = 1
    elif(absoluteX < board_center[0] - gridWidth/2 - lineWidth/2): 
        gridX = -1
    else: gridX = 0 

    if(absoluteY > board_center[1] + gridWidth/2 + lineWidth/2): 
        gridY = 1
    elif(absoluteY < board_center[1] - gridWidth/2 - lineWidth/2): 
        gridY = -1
    else: gridY = 0 

    return [gridX, gridY]

def checkBoard():
    global rows

    for i in range(3): 
        

        check = rows[i][0]
        if(check == ""): continue

        if ( rows[i][1] == check and rows[i][2] == check):
            return check

    for i in range(3): 
        

        check = rows[0][i]
        if(check == ""): continue

        if ( rows[1][i] == check and rows[2][i] == check):
            return check

    
    check = rows[0][0]

    if ( rows[1][1] == check and rows[2][2] == check and check != ""):
        return check

    check = rows[2][0]

    if ( rows[1][1] == check and rows[0][2] == check and check != ""):
        return check

    freeSpace = False
    for i in range(3):
        for j in range(3):
            if(rows[i][j] == ""): freeSpace = True
    if(not freeSpace): return None
    else: return "ongoing"


turtle.clear()
draw_board(board_center[0], board_center[1], gridWidth, lineWidth)

def Reset():
    turtle.clear()
    draw_board(board_center[0], board_center[1], gridWidth, lineWidth)

    for i in range(3):
        for j in range(3):
            rows[i][j] = ""
    if(random.randrange(0, 1) == 0): player = "X"
    else: player = "O"

def DisplayWinner(winner):
    turtle.penup()
    turtle.setposition(board_center[0], board_center[1]+(3*gridWidth)/2+lineWidth)
    turtle.write(winner, align="center", font=("Verdana", gridWidth, "normal"))
    time.sleep(3)



turtle.onscreenclick(clicked)
turtle.done()