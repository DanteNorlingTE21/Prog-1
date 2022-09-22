
import random
import turtle
import time



def new_block():
    newblock = turtle.Turtle()
    newblock.speed(0)
    newblock.penup()
    newblock.shape("square")
    newblock.color(0,1,0)
    Snake_block.append(newblock)

def turn_left():
    if Snake_block[0].heading() != 0:
        Snake_block[0].seth(180)
def turn_right():
    if Snake_block[0].heading() != 180:
        Snake_block[0].seth(0)
def turn_up():
    if Snake_block[0].heading() != 270:
        Snake_block[0].seth(90)
def turn_down():
    if Snake_block[0].heading() != 90:
        Snake_block[0].seth(270)
def snake_list_shuffle(x):
    funklist = []
    funklist.append(x[0])
    if len(x) >= 2:
        funklist.append(x[len(x)-1])
    if len(x) > 2:
        for i in range(2,len(x)):
            funklist.append(x[i-1])
    return funklist



running = True
fps = 12
time_delta = 1/fps

Score = 0

Snake_block = []



win = turtle.Screen()
win.setup(800,800)
win.bgcolor(0, 0.5, 0.1)
win.title("Snake")

apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("Red")
apple.penup()
apple.goto(random.randrange(-400,400,20),random.randrange(-400,400,20))

new_block()

win.listen()
win.onkeypress(turn_left, "Left")
win.onkeypress(turn_right, "Right")
win.onkeypress(turn_up, "Up")
win.onkeypress(turn_down, "Down")
win.onkeypress(new_block, "space")



while running:
    crawl_x = Snake_block[0].xcor()
    crawl_y = Snake_block[0].ycor()


    Snake_block[0].forward(20)
    if len(Snake_block) > 1:
        Snake_block[-1].setx(crawl_x)    
        Snake_block[-1].sety(crawl_y)
        Snake_block = snake_list_shuffle(Snake_block)
    
    for tail in range(1,len(Snake_block)):
        if (Snake_block[0].xcor() == Snake_block[tail].xcor()) and (Snake_block[0].ycor() == Snake_block[tail].ycor()):
            running = False
    if ((apple.xcor()-10) < Snake_block[0].xcor() < (apple.xcor() +10)) and ((apple.ycor()-10) < Snake_block[0].ycor() < (apple.ycor() +10)):
        Score += 1
        apple.goto(random.randrange(-400,400,20),random.randrange(-400,400,20))
        new_block()
    if Snake_block[0].xcor() > 400 or Snake_block[0].xcor() < -400 or Snake_block[0].ycor() > 400 or Snake_block[0].ycor() < -400:
        running = False

    time.sleep(time_delta)
    win.update()
print(Score)