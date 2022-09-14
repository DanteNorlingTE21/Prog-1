import turtle

corner = int(input("?"))
len = int(input("?"))
star = turtle.Turtle()
star.speed(0)
star.penup()
star.goto(-(len/2),0)
star.pendown()

if corner % 2 == 0:

    for i in range(corner):
            star.forward(200)
            star.left(180-(180/corner))
            star.forward(200)
            star.right(360/(corner))
else:
    for i in range(corner):
        star.forward(len)
        star.left(180 -(180/corner))


turtle.done()