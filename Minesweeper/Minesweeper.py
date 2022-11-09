import turtle
import random

number_of_bombs =int(input("NUMBER OF MINES:"))
gridsize = int(input("GRIDSIZE:"))

tiles ={}



def startup(grid):
    win = turtle.Screen()
    #win.setup((20*grid+grid-1),(20*grid+grid-1)) #grid-1 är pixlarna för linjerna
    win.setup(20*grid,20*grid)
    win.bgcolor("grey")
    win.title("Minesweeper")
       
    """
    linedrawer = turtle.Turtle()
    linedrawer.color("black")
    linedrawer.penup()
    linedrawer.speed(0)
    linedrawer.goto((-1/2)*(20*grid+grid-1),(-1/2)*(20*grid+grid-1))

    
    for i in range(grid+1):
        linedrawer.pendown()
        linedrawer.forward(20*grid+grid-1)
        linedrawer.penup()
        linedrawer.setx((-1/2)*(20*grid+grid-1))
        linedrawer.sety(linedrawer.ycor()+20)
        print(linedrawer.ycor())
    """

    return win
def tile_gen(grid,mines):
    """ Titties = list: grid = grid side
        if tile dx = 0 it's not a bomb
        dx = 1 = bomb"""
    bombcounter = 0
    titties = []
    for y in range(0,grid):
        for x in range(0, grid):
            tile_titty = turtle.Turtle()
            tile_titty.shape('Tileface.gif')
            tile_titty.penup()
            tile_titty.speed(0)
            tile_titty.goto((-10*grid +10 +x*20),(-10*grid + 10 +y*20))
            tile_titty.dx = 0
            if bombcounter < mines:
                tile_titty.dx = random.randint(0,1)
                if tile_titty.dx == 1:
                    bombcounter += 1
            titties.append(tile_titty)
    return titties

def rightclick(x,y):
    print(x)
    print(y)
def leftclick(x,y):
    pass

app = startup(gridsize)
app.addshape('Tileface.gif')
tiles = tile_gen(gridsize,number_of_bombs)


app.listen()
app.onclick(rightclick, btn=3, add=None)

while True:
    app.update()