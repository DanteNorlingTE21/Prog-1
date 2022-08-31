from datetime import timedelta
from msilib.schema import Class
import turtle
import time
import random

Win = turtle.Screen()
Win.bgcolor("blue")
Win.title("Hampus")
Win.setup(800,800)

running = True
FPS = 60
delta_t = 1/FPS


bird = turtle.Turtle()
bird.shape('classic')
bird.color('yellow')
bird.goto(0,0)
bird.penup()
bird.speed(0)
bird.dy = 0
min_dy = -10



pipe = turtle.Turtle()
pipe.shape('square')
pipe.color('green')
pipe.penup()
pipe.shapesize(40,3)
pipe.speed(0)
pipe.goto(370,0)
pipe.dx = -5


gap = turtle.Turtle()
gap.shape('square')
gap.color('blue')
gap.penup
gap.shapesize(3,4)
gap.speed(0)
gap.goto(370,0)



def jump():
    bird.dy = 5


Win.listen()
Win.onkey(jump, "Up")
while True:




    

    if bird.ycor() <= -400:
        break

    if -30 < pipe.xcor() <= 30 and (bird.ycor() < (gap.ycor() -30) or bird.ycor() > (gap.ycor() + 30)):
        break
    if pipe.xcor() <= -370:
        pipe.setx(370)
        gap.setx(370)
        gap.sety(random.randrange(-370,370,1))

    bird.sety(bird.ycor()+ bird.dy)
    pipe.setx(pipe.xcor()+ pipe.dx)
    gap.setx(pipe.xcor())

    if (bird.dy > min_dy):
        bird.dy = bird.dy -0.3 
    elif(bird.dy < min_dy):
        bird.dy = min_dy

    timedelta(delta_t)
    Win.update()
    