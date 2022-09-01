import time
import math
import turtle

running = True
hz = 4 *int(input("hertz: "))
fps = int(input("fps: "))
r = int(input("radie: "))

dv = 360 * hz/fps
ds = (r*math.pi*dv)/(180)

win = turtle.Screen()
win.setup(800,800)
win.bgcolor("black")
win.title("sin")

circle = turtle.Turtle()
circle.penup()
circle.speed(0)
circle.color("white")
circle.shape("classic")
circle.goto(0,-r)
circle.pendown()
circle.left(dv/2)

sin = turtle.Turtle()
sin.shape("square")
sin.color("red")
sin.goto(0,0)
sin.speed(0)

cos = turtle.Turtle()
cos.shape("square")
cos.color("blue")
cos.goto(0,0)
cos.speed(0)



while running: 

    circle.forward(ds)
    circle.left(dv)
    sin.sety(circle.ycor())
    cos.setx(circle.xcor())

    time.sleep(1/fps)
    win.update()