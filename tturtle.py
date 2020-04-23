import turtle
def move(a):
    turtle.forward(a)
    turtle.left(90)

def drawSquare(a):
    for i in range(4):
        move(a)

def drawSquareColor(a,color):
    turtle.color(color)
    turtle.begin_fill()
    drawSquare(a)
    turtle.end_fill()


turtle.speed(1)

drawSquareColor(60,'red')
turtle.goto(150,150)
drawSquareColor(120,'blue')