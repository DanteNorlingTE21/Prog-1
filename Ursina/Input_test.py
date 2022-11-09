from turtle import position
from ursina import *
import random
cubes = []



def update():
    #for titties in cubes:
        #titties.rotation_y += time.dt*100
    cube.rotation_y += time.dt*100

    cube.y = cube.y + cube.dy *time.dt
    if cube.y >=4:
        cube.dy *= -1
    if cube.y <= -4:
        cube.dy *= -1
    for titties in cubes:
        if titties.x >=5:
            titties.dx *= -1
        if titties.x <= -5:
            titties.dx *= -1
        if held_keys['p']:
                titties.x = titties.x + titties.dx* time.dt
                print(titties.x)
def input(key):
    if key == "m":
        print("Mor din")

    if key == "c":
        newcube = Entity(parent = cube, model= 'cube', color = color.orange, position=(random.randint(-5,5),random.randint(-5,5),random.randint(-5,5)), scale=(1,1,1), dx =2)
        cubes.append(newcube)
app  = Ursina()

cube = Entity(model= 'cube', color = color.orange, position=(random.randint(-5,5),random.randint(-4,4),random.randint(-5,5)), scale=(1,1,1), dy = 1)



window.title = 'Input test'
window.fullscreen = False
window.borderless = True
window.fps_counter.visible = True

app.run()