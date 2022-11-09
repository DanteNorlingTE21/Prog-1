import turtle
import random
from math import sqrt

number_of_bombs =int(input("NUMBER OF MINES:"))
gridsize = int(input("GRIDSIZE:"))

tiles ={}



def startup(grid=int):
    win = turtle.Screen() #Skapar fönstret
    
    #win.setup((20*grid+grid-1),(20*grid+grid-1)) #grid-1 är pixlarna för linjerna : används inte, var del av linedrawer innan jag skapade texturer
   
    win.setup(20*grid,20*grid)
    win.bgcolor("grey")
    win.title("Minesweeper")
    win.addshape("tileface.gif") #Laddar texturer:
    win.addshape("tileflag.gif") #'
    win.addshape("tile0.gif")    #'
    win.addshape("tile1.gif")    #'
    win.addshape("tile2.gif")    #'
    win.addshape("tile3.gif")    #'
    win.addshape("tile4.gif")    #'
    win.addshape("tile5.gif")    #'
    win.addshape("tile6.gif")    #'
    win.addshape("tile7.gif")    #'
    win.addshape("tile8.gif")    #'
    win.addshape("mine.gif")     #'
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
def tile_gen(grid=int,mines=int):
    """ 
        if tile dx = 0 it's not a bomb
        dx = 1 = bomb
        dy = flag status  eller om den har bestämt värde"""
    bombcounter = 0
    titties = []    
    for y in range(0,grid):                #Skapar grid * grid turtles som blir rutorna : 
        for x in range(0, grid):        
            tile_titty = turtle.Turtle()
            tile_titty.shape('tileface.gif')
            tile_titty.penup()
            tile_titty.speed(0)
            tile_titty.goto((-10*grid +10 +x*20),(-10*grid + 10 +y*20))
            tile_titty.dx = 0
            tile_titty.dy = 0
            titties.append(tile_titty)
    while bombcounter < mines:
        potential_bomb =random.choice(titties)
        if potential_bomb.dx == 0:
            potential_bomb.dx = 1
            bombcounter +=1
    return titties

def rightclick(x,y):
    for squares in tiles:
        if (squares.xcor()-10) < x < (squares.xcor()+10) and (squares.ycor()-10) < y < (squares.ycor()+10):#Kollar vilken ruta som klickas
            if squares.dy == 0: #Kollar om rutan ar en flagga
                squares.shape('tileflag.gif') #Byter till ruta med flagga
                squares.dy = 1  #Ändrar flagvärdet till sant(typ)
            elif squares.dy == 1:#Kollar om rutan ar en flagga
                squares.shape('tileface.gif')#Byter från ruta med flagga
                squares.dy = 0  #Ändrar flagvärdet till falskt(typ)



def leftclick(x,y):
    for i in range(len(tiles)):
        if (tiles[i].xcor()-10) < x < (tiles[i].xcor()+10) and (tiles[i].ycor()-10) < y < (tiles[i].ycor()+10): #Kollar vilken ruta som klickas
            if tiles[i].dy == 0:
                if tiles[i].dx == 1: #Kollar om rutan är en bomb
                    tiles[i].shape("mine.gif") #Visar bomb grafiken
                    tiles[i].dy = 2
                else:
                    #print(blocktype(i))
                    tile_determiner(i)
                    tiles[i].dy = 2
"""

måste kolla rutorna runtom för minor
kan använda + - grid för att gå ett steg upp/ner och +- 1 för att gå vänster höger 
måste dock göra undantag för blocken vid kanterna då +- 1 kan antingen göra index fel eller leda till att ett block på nästa rad räknas som att det ligger bredvid

kolla höger/ vänster kant (ruta+1)%grid == 0 eller ruta% grid == 0: Fast inde

12 13 14 15
8  9  10 11
4  5  6  7
0  1  2  3

grid =4

(grid = sqrt(len(tiles)))

Det blir 9 olika typer av block: fyra hörn fyra kanter och mitten block

Det blir olika metoder för att kolla närliggande minor beroende på vad för typ av block det är

Jag skapar en funktion för att identifiera blocktyp/position.

"""

def blocktype(block_index =int):
    """Returnerar värde 1 - 9 vilket motsvarar  vilken typ av ruta det är:
    ,1 = vänstertophörn 2 = toppkant, 3 = högertophörn, 4=vänsterkant, 5=mitten, 6 =högerkant, 7 =vänsterbottenhörn, 8 = bottenkant, 9 = högerbottenhörn"""
    gridside = sqrt(len(tiles))
    leftside = False
    top = False
    bot = False
    rightside = False
    if block_index%gridsize == 0:
        leftside = True
    elif (block_index + 1)%gridside == 0:
        rightside = True
    if block_index < gridside:
        bot = True
    elif block_index > (gridside*(gridside-1) - 1):
        top = True
   
    if leftside and top:
        return 1
    elif rightside and top:
        return 3
    elif leftside and bot:
        return 7
    elif rightside and bot:
        return 9
    elif top:
        return 2
    elif leftside:
        return 4
    elif rightside:
        return 6
    elif bot:
        return 8
    else:
        return 5

def tile_determiner(i=int):
    """Bestämmer siffran på en kvadrat utifrån dess index"""
    neighbour_bombs = 0
    blockpos = blocktype(i)
    if blockpos == 1:
        neighbour_bombs += tiles[i+1].dx #höger
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))].dx #  ner
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))+1].dx# ner + höger
    if blockpos == 2:
        neighbour_bombs += tiles[i-1].dx #vänster
        neighbour_bombs += tiles[i+1].dx #höger
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))].dx #  ner
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))-1].dx #  ner + vänster
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))+1].dx# ner + höger     
    if blockpos == 3:
        neighbour_bombs += tiles[i-1].dx #vänster
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))].dx #  ner
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))-1].dx #  ner + vänster
    if blockpos == 4:
        neighbour_bombs += tiles[i+int((sqrt(len(tiles))))].dx # upp
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) +1].dx # upp +höger
        neighbour_bombs += tiles[i+1].dx #höger
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))].dx #  ner
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))+1].dx# ner + höger  
    if blockpos == 5:
        neighbour_bombs += tiles[i+1].dx #höger 
        neighbour_bombs += tiles[i-1].dx #vänster
        neighbour_bombs += tiles[i+int((sqrt(len(tiles))))].dx # upp
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))].dx #  ner
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))+1].dx# ner + höger
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))-1].dx# ner + vänster
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) +1].dx # upp +höger
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) -1].dx # upp +vänster 
    if blockpos == 6:
        neighbour_bombs += tiles[i+int((sqrt(len(tiles))))].dx # upp   
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) -1].dx # upp +vänster
        neighbour_bombs += tiles[i-1].dx #vänster
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))].dx #  ner
        neighbour_bombs += tiles[i-int((sqrt(len(tiles))))-1].dx# ner + vänster
    if blockpos == 7:
        neighbour_bombs += tiles[i+int((sqrt(len(tiles))))].dx # upp 
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) +1].dx # upp +höger
        neighbour_bombs += tiles[i+1].dx #höger 
    if blockpos == 8:
        neighbour_bombs += tiles[i+int((sqrt(len(tiles))))].dx # upp                    
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) +1].dx # upp +höger
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) -1].dx # upp +vänster
        neighbour_bombs += tiles[i+1].dx #höger  
        neighbour_bombs += tiles[i-1].dx #vänster
    if blockpos == 9:
        neighbour_bombs += tiles[i+int((sqrt(len(tiles))))].dx # upp 
        neighbour_bombs += tiles[i+int((sqrt(len(tiles)))) -1].dx # upp +vänster 
        neighbour_bombs += tiles[i-1].dx #vänster
    tiles[i].shape(f"tile{neighbour_bombs}.gif")

    if neighbour_bombs == 0:
        if blockpos == 1:
            leftclick(tiles[i+1].xcor(),tiles[i+1].ycor())#höger
            leftclick(tiles[i-int((sqrt(len(tiles))))].xcor(),tiles[i-int((sqrt(len(tiles))))].ycor())#ner
            leftclick(tiles[i-int((sqrt(len(tiles))))+1].xcor(),tiles[i-int((sqrt(len(tiles))))+1].ycor())#ner + höger
        if blockpos == 2:
            leftclick(tiles[i+1].xcor(),tiles[i+1].ycor())#höger
            leftclick(tiles[i-1].xcor(),tiles[i-1].ycor())#vänster            
            leftclick(tiles[i-int((sqrt(len(tiles))))].xcor(),tiles[i-int((sqrt(len(tiles))))].ycor())#ner
            leftclick(tiles[i-int((sqrt(len(tiles))))+1].xcor(),tiles[i-int((sqrt(len(tiles))))+1].ycor())#ner + höger
            leftclick(tiles[i-int((sqrt(len(tiles))))-1].xcor(),tiles[i-int((sqrt(len(tiles))))-1].ycor())#ner + vänster
        if blockpos == 3:
            leftclick(tiles[i-1].xcor(),tiles[i-1].ycor())#vänster      
            leftclick(tiles[i-int((sqrt(len(tiles))))].xcor(),tiles[i-int((sqrt(len(tiles))))].ycor())#ner
            leftclick(tiles[i-int((sqrt(len(tiles))))-1].xcor(),tiles[i-int((sqrt(len(tiles))))-1].ycor())#ner + vänster
        if blockpos == 4:
            leftclick(tiles[i+int((sqrt(len(tiles))))].xcor(),tiles[i+int((sqrt(len(tiles))))].ycor())#upp     
            leftclick(tiles[i+int((sqrt(len(tiles))))+1].xcor(),tiles[i+int((sqrt(len(tiles))))+1].ycor())#upp + höger
            leftclick(tiles[i+1].xcor(),tiles[i+1].ycor())#höger
            leftclick(tiles[i-int((sqrt(len(tiles))))].xcor(),tiles[i-int((sqrt(len(tiles))))].ycor())#ner
            leftclick(tiles[i-int((sqrt(len(tiles))))+1].xcor(),tiles[i-int((sqrt(len(tiles))))+1].ycor())#ner + höger    
        if blockpos == 5:
            leftclick(tiles[i+int((sqrt(len(tiles))))].xcor(),tiles[i+int((sqrt(len(tiles))))].ycor())#upp     
            leftclick(tiles[i+int((sqrt(len(tiles))))+1].xcor(),tiles[i+int((sqrt(len(tiles))))+1].ycor())#upp + höger
            leftclick(tiles[i+int((sqrt(len(tiles))))-1].xcor(),tiles[i+int((sqrt(len(tiles))))-1].ycor())#upp + vänster
            leftclick(tiles[i+1].xcor(),tiles[i+1].ycor())#höger
            leftclick(tiles[i-1].xcor(),tiles[i-1].ycor())#vänster  
            leftclick(tiles[i-int((sqrt(len(tiles))))].xcor(),tiles[i-int((sqrt(len(tiles))))].ycor())#ner
            leftclick(tiles[i-int((sqrt(len(tiles))))+1].xcor(),tiles[i-int((sqrt(len(tiles))))+1].ycor())#ner + höger        
            leftclick(tiles[i-int((sqrt(len(tiles))))-1].xcor(),tiles[i-int((sqrt(len(tiles))))-1].ycor())#ner + vänster
        if blockpos == 6:
            leftclick(tiles[i+int((sqrt(len(tiles))))].xcor(),tiles[i+int((sqrt(len(tiles))))].ycor())#upp            
            leftclick(tiles[i+int((sqrt(len(tiles))))-1].xcor(),tiles[i+int((sqrt(len(tiles))))-1].ycor())#upp + vänster
            leftclick(tiles[i-1].xcor(),tiles[i-1].ycor())#vänster
            leftclick(tiles[i-int((sqrt(len(tiles))))-1].xcor(),tiles[i-int((sqrt(len(tiles))))-1].ycor())#ner + vänster
            leftclick(tiles[i-int((sqrt(len(tiles))))].xcor(),tiles[i-int((sqrt(len(tiles))))].ycor())#ner
        if blockpos == 7:
            leftclick(tiles[i+int((sqrt(len(tiles))))].xcor(),tiles[i+int((sqrt(len(tiles))))].ycor())#upp     
            leftclick(tiles[i+int((sqrt(len(tiles))))+1].xcor(),tiles[i+int((sqrt(len(tiles))))+1].ycor())#upp + höger
            leftclick(tiles[i+1].xcor(),tiles[i+1].ycor())#höger
        if blockpos == 8:
            leftclick(tiles[i+int((sqrt(len(tiles))))].xcor(),tiles[i+int((sqrt(len(tiles))))].ycor())#upp     
            leftclick(tiles[i+int((sqrt(len(tiles))))+1].xcor(),tiles[i+int((sqrt(len(tiles))))+1].ycor())#upp + höger
            leftclick(tiles[i+int((sqrt(len(tiles))))-1].xcor(),tiles[i+int((sqrt(len(tiles))))-1].ycor())#upp + vänster
            leftclick(tiles[i+1].xcor(),tiles[i+1].ycor())#höger
            leftclick(tiles[i-1].xcor(),tiles[i-1].ycor())#vänster  
        if blockpos == 9:
            leftclick(tiles[i+int((sqrt(len(tiles))))].xcor(),tiles[i+int((sqrt(len(tiles))))].ycor())#upp
            leftclick(tiles[i+int((sqrt(len(tiles))))-1].xcor(),tiles[i+int((sqrt(len(tiles))))-1].ycor())#upp + vänster
            leftclick(tiles[i-1].xcor(),tiles[i-1].ycor())#vänster  


app = startup(gridsize)

tiles = tile_gen(gridsize,number_of_bombs)


app.listen()
app.onclick(rightclick, btn=3, add=None)
app.onclick(leftclick, btn=1, add=None)
print(len(tiles))
while True:
    app.update()