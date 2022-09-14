import turtle
import random
import math

running = True

win = turtle.Screen()
win.setup(800,800)
win.bgcolor("white")
win.title("Crash")

text = turtle.Turtle()
text.speed(0)
text.penup()
text.goto(-400,350)

text.write("Multiplier 0", font =("Arial",20,"normal"))

mult = 0

arrow = turtle.Turtle()
arrow.shape("classic")
arrow.speed(0)



def print_out(x):
    text.clear()
    stringish = "Multiplier" + str(x)
    text.write(stringish, font =("Arial",20,"normal"))

def shutdown():
    global running
    running = False

win.listen()
win.onkey(shutdown, 'x')


while running:
    mult = arrow.ycor()/100

    arrow.forward(1)
    arrow.seth((180/math.pi) * math.atan(math.log(2)* (2 ** ((arrow.xcor())/100))))
    print_out(mult)

    win.update()