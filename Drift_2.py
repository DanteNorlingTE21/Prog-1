from datetime import timedelta
import time
import turtle
import random
enemies = []
fps = 100
delta_t = 1/fps

win = turtle.Screen()
win.setup(800,800)
win.bgcolor("blue")
win.title("Drift")
win.colormode(255)

car = turtle.Turtle()
car.shape("turtle")
car.speed(0)
car.color('yellow')
#car.penup()
n = 1
score = 0
dv = 0
ds = 10
Kne = 0


#def left():
    
#def right(x):

def stop_left():
    global dv
    if dv >= 10:
        dv = 0

def stop_right():
    global dv
    if dv <= -10:
        dv = 0

def left():
    global dv
    global n
    #dv = 10 * 1.001**n
    dv = 10 

def right():
    global dv
    global n
    #dv = -10 * 1.001**n
    dv = -10 



win.listen()

win.onkeypress(left, "Left")
win.onkeypress(right, "Right")

win.onkeyrelease(stop_left, "Left")
win.onkeyrelease(stop_right, "Right")
gameover = False
while not gameover:


    car.left(dv)
    car.forward(ds)

    #ds = ds*1.003

    Kne += 1
    if(Kne >= 20):
        Kne = 0
        new_turtle = turtle.Turtle()
        new_turtle.speed(0)
        new_turtle.penup()
        new_turtle.shape('square')
        new_turtle.color(random.randrange(0,255,1), random.randrange(0,255,1), random.randrange(0,255,1))
        x = random.randrange(-390,390,1)
        y = random.randrange(-390,390,1)
        new_turtle.goto(x,y)


        enemies.append(new_turtle)


    for enemy in enemies:
        if (enemy.xcor() -10 < car.xcor() < enemy.xcor() + 10) and (enemy.ycor()-10 < car.ycor() < enemy.ycor() + 10):
            gameover = True


    n += 1
    score += 1

    if car.ycor() > 400 or car.ycor() < -400 or car.xcor() >400 or car.xcor() < -400:
        break


    win.update()
    time.sleep(delta_t)

print(score)