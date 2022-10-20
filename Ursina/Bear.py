from ursina import *
win = Ursina()

player = Entity(model='sphere', color=color.red, scale_y = 2)


def update():
    player.x += held_keys['d'] *2* time.dt
    player.x -= held_keys['a'] *2* time.dt

win.run()