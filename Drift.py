from datetime import timedelta
import time
import turtle
import random

fps = 30
delta_t = 1/fps

win = turtle.Screen()
win.setup(800,800)
win.bgcolor("blue")
win.title("Drift")

car = turtle.Turtle()
car.shape("turtle")
car.speed(0)
car.color('yellow')
#car.penup()
n = 1
score = 0
dv = 0
ds = 1

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
while True:


    car.left(dv)
    car.forward(ds)

    ds = ds*1.003

    n += 1
    score += 1

    if car.ycor() > 400 or car.ycor() < -400 or car.xcor() >400 or car.xcor() < -400:
        break


    win.update()
    timedelta(delta_t)

print(score)