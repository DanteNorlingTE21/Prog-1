from datetime import timedelta
import turtle
import time
import random

ds = 0
dv = 0

k = 0

fps = 60
delta_t = 1/fps
running = True
enemies = []
shot = []

win = turtle.Screen()
win.setup(800,800)
win.bgcolor("black")
win.title("Asteroid")
win.mode("logo")

ship = turtle.Turtle()
ship.shape("classic")
ship.goto(0,0)
ship.color('white')
ship.penup()
ship.speed(0)

def fram():
    global ds
    ds = 15
def stopp_fram():
    global ds
    ds = 0
def left():
    global dv
    dv = 20
def right():
    global dv
    dv = -20
def stopp_left():
    global dv
    if dv > 0:
        dv = 0
def stopp_right():
    global dv
    if dv < 0:
        dv = 0
def shoot():
    global k
    print(k)
    if k >= 3:
        k = 0

    shoot_turtle = shot[k]
    shoot_turtle.clear()
    shoot_turtle.penup()
    shoot_turtle.goto(ship.xcor(),ship.ycor())
    shoot_turtle.pendown()
    shoot_turtle.setheading(ship.heading())
    k += 1

for _ in range(4):
    asteroid_turtle = turtle.Turtle()
    asteroid_turtle.speed(0)
    asteroid_turtle.penup()
    asteroid_turtle.shape('circle')
    asteroid_turtle.shapesize(2,2)
    asteroid_turtle.color('red')
    asteroid_turtle.goto(random.randrange(-400,400,1), random.randrange(-400,400,1))
    asteroid_turtle.dx = random.randint(-15,15)
    asteroid_turtle.dy = random.randint(-15,15)
    enemies.append(asteroid_turtle)

for _ in range(3):
    shot_turtle = turtle.Turtle()
    shot_turtle.speed(0)
    shot_turtle.penup()
    shot_turtle.shape("classic")
    shot_turtle.color("white")
    shot_turtle.goto(500,500)
    shot.append(shot_turtle)

win.listen()
win.onkeypress(fram, "Up")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")

win.onkey(shoot, "space")

win.onkeyrelease(stopp_fram, "Up")
win.onkeyrelease(stopp_left, "Left")
win.onkeyrelease(stopp_right, "Right")




while running:


    ship.left(dv)
    ship.forward(ds)


    for rock in enemies:
        if ((rock.xcor()-20)< ship.xcor() < (rock.xcor()+20)) and ((rock.ycor()-20)< ship.ycor() < (rock.ycor()+20)):
            running = False

        if (-400 < rock.xcor() < 400) and (-400 < rock.ycor() < 400):
            rock.setx(rock.xcor()+rock.dx)
            rock.sety(rock.ycor()+rock.dy)

        else:
            rock.goto(random.randint(-400,400), random.randint(-400,400))
            rock.dx = random.randint(-15,15)
            rock.dy = random.randint(-15,15)
            
       


    for bullet in shot:
        if (-400 < bullet.xcor() < 400) and (-400 < bullet.ycor() < 400):
            for i in range(4):
                bullet.forward(6)
            #print(bullet.xcor(),bullet.ycor())
        elif(bullet.xcor()> 400) or (bullet.xcor()< -400) or (bullet.ycor() > 400) or (bullet.ycor() < -400):
            bullet.hideturtle()
            bullet.clear()
        for rock in enemies:
            if ((rock.xcor()-20)< bullet.xcor() < (rock.xcor()+20)) and ((rock.ycor()-20)< bullet.ycor() < (rock.ycor()+20)):
                bullet.hideturtle()
                rock.goto(random.randint(-400,400), random.randint(-400,400))
                rock.dx = random.randint(-15,15)
                rock.dy = random.randint(-15,15)



    #time.sleep(delta_t)
    win.update()
