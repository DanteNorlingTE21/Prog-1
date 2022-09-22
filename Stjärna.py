import turtle
import math

corner = int(input("?"))
len = int(input("?"))
star = turtle.Turtle()
star.speed(0)
star.penup()
star.goto(-(len/2),0)
star.pendown()

if corner % 2 == 0:
    star.penup()
    star.goto((corner*len)/(2*math.pi), 0)
    star.pendown()
    star.left(180-(((90*corner) -360)/corner))
    for i in range(corner):

        star.forward(len)
        star.right(360/corner)
        star.forward(len)
        star.left(720/corner)
else:
    for i in range(corner):
        star.forward(len)
        star.left(180 -(180/corner))


turtle.done()