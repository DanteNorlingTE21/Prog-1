from ursina import*
import random


def update():
    isak_object_1.rotation_y += time.dt * 100
    if held_keys['q']:                               # If q is pressed
        camera.position += (0, time.dt, 0)           # (X,Y,Z) movement
    if held_keys['a']:                               # If a is pressed
        camera.position -= (0, time.dt, 0) 
    if held_keys['o']:
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue =random.randint(0,255)
        isak_object_1.color=color.rgb(red,green,blue) #entities verkar vara objekt och color verkar vara ett library

win = Ursina()  # Fönster/app funktion som skapar fönster

window.title = 'Test 1'    # Ursina() funktionen används inte i fönster setup tydligen
window.borderless = False        #Borderless
window.fullscreen = False       #Fullscreen
window.exit_button.visible = False          #Kryss i hörnet
window.fps_counter.enabled = True           #fps


isak_object_1 = Entity(model = 'cube', color = color.orange, scale=(2,2,2) )

win.run()