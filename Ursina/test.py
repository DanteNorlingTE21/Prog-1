from ursina import *

# https://www.youtube.com/watch?v=DHSRaVeQxIk


class Test_Block(Entity):
    def __init__(self):
        super().__init__(model="cube", color=color.white, rotation=Vec3(20, 20, 20))

    def lol(self):
        destroy(self)


def update():
    pass


app = Ursina()

B = Test_Block()

app.run()
