import turtle

number_of_bombs =int(input("NUMBER OF MINES:"))
gridsize = int(input("GRIDSIZE:"))

tiles ={}



def startup(mines,grid):
    win = turtle.Screen()
    win.setup((20*grid+grid-1),(20*grid+grid-1))
    win.bgcolor("grey")
    win.title("Minesweeper")
    linedrawer = turtle.Turtle()
    linedrawer.color("black")
    linedrawer.penup()
    linedrawer.speed(0)
    linedrawer.goto((-1/2)*(20*grid+grid-1),(-1/2)*(20*grid+grid-1))

    """"
    for i in range(grid+1):
        linedrawer.pendown()
        linedrawer.forward(20*grid+grid-1)
    """


    return win
def rightclick(x,y):
    print(x)
    print(y)
def leftclick(x,y):
    pass

app = startup(number_of_bombs,gridsize)
app.listen()
app.onclick(rightclick, btn=3, add=None)

while True:
    app.update()