
import random
import turtle
import time


#Skapar nya ormsegment (ormblock)
def new_block():
    newblock = turtle.Turtle()
    newblock.speed(0)
    newblock.penup()
    newblock.shape("square")
    newblock.color(0,1,0)
    Snake_block.append(newblock)

#Svänger men låter inte ormen göra 180
def turn_left():
    """global turning
    if Snake_block[0].heading() != 0 and (not turning):
        Snake_block[0].seth(180)
        turning = True"""
    #Gammal kod
    if len(Snake_block)>1:   
        if not round(Snake_block[0].xcor()) > round(Snake_block[1].xcor()):
            Snake_block[0].seth(180)
        else:
            print("x", Snake_block[0].xcor(), Snake_block[1].xcor())
    else:
        Snake_block[0].seth(180)
def turn_right():
    if len(Snake_block)>1: 
        if not round(Snake_block[0].xcor()) < round(Snake_block[1].xcor()):
            Snake_block[0].seth(0)
        else:
            print("x", Snake_block[0].xcor(), Snake_block[1].xcor())
    else:
        Snake_block[0].seth(0)
def turn_up():
    if len(Snake_block)>1: 
        if not round(Snake_block[0].ycor()) < round(Snake_block[1].ycor()):
            Snake_block[0].seth(90)
        else:
            print("y", Snake_block[0].ycor(), Snake_block[1].ycor())
    else:
        Snake_block[0].seth(90)
def turn_down():
    if len(Snake_block)>1: 
        if not round(Snake_block[0].ycor()) > round(Snake_block[1].ycor()):
            Snake_block[0].seth(270)
        else:
            print("y", Snake_block[0].ycor(), Snake_block[1].ycor())
    else:
        Snake_block[0].seth(270)
#Problem: Det går att svänga tillbaka precis när ändan flyttar sig/// ormen låser upp ibland
#Lösning avrunda talen för det blev en decimalutveckling. Går fortfarande att göra 180 i början

""" Byter ordning på objekt i en lista. Används fr att byta ordning på ormblocken. 
[1,2,3,4,5] --> [1,5,2,3,4]--> [1,4,5,2,3]-->[1,3,4,5,2]-->[1,2,3,4,5] 
Första blocket stannar längst fram för att det är huvudet och sista blocket flyttas till näst längts fram och måste då byta plats i listan också
"""
def snake_list_shuffle(x):
    funklist = []
    funklist.append(x[0])
    if len(x) >= 2:
        funklist.append(x[-1])
    if len(x) > 2:
        for i in range(2,len(x)):
            funklist.append(x[i-1])
    return funklist


#turning = False
running = True
fps = 24
time_delta = 1/fps

Score = 0

#Listan på ormsegment
Snake_block = []


#skärmen
win = turtle.Screen()
win.setup(800,800)
win.bgcolor(0, 0.5, 0.1)
win.title("Snake")

#äpplet
apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("Red")
apple.penup()
apple.goto(random.randrange(-380,380,20), random.randrange(-380,380,20))

#skapar första blocket
new_block()

#lyssnar efter inputs
win.listen()
win.onkeypress(turn_left, "Left")
win.onkeypress(turn_right, "Right")
win.onkeypress(turn_up, "Up")
win.onkeypress(turn_down, "Down")
win.onkeypress(new_block, "space")
win.onkeypress(turn_left, "a")
win.onkeypress(turn_right, "d")
win.onkeypress(turn_up, "w")
win.onkeypress(turn_down, "s")

#Main loop
while running:
    #Kollar huvudets position för att kunna flytta svansändan dit
    crawl_x = Snake_block[0].xcor()
    crawl_y = Snake_block[0].ycor()

    #Flyttar ändan 
    if len(Snake_block) > 1:
        Snake_block[-1].setx(crawl_x)    
        Snake_block[-1].sety(crawl_y)
        Snake_block = snake_list_shuffle(Snake_block)
    #Flyttar huvudet
    Snake_block[0].forward(20)
    #Kollar kollision med sig själv
    for tail in Snake_block[1:]:
        if ((tail.xcor()-10) < Snake_block[0].xcor() < (tail.xcor()+10)) and ((tail.ycor()-10) < Snake_block[0].ycor() < (tail.ycor()+10)):
            running = False


    #Kollar kollision med äpplet
    if ((apple.xcor()-10) < Snake_block[0].xcor() < (apple.xcor() +10)) and ((apple.ycor()-10) < Snake_block[0].ycor() < (apple.ycor() +10)):
        Score += 1
        apple.goto(random.randrange(-380,380,20), random.randrange(-380,380,20))
        new_block()
    #Kollar kollision med väggen
    if Snake_block[0].xcor() > 390 or Snake_block[0].xcor() < -390 or Snake_block[0].ycor() > 390 or Snake_block[0].ycor() < -390:
        running = False
   
    #väntar

    #turning = False
    time.sleep(time_delta)
    win.update()
print(Score)