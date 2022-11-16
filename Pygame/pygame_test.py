import pygame


class Tiles:
    def __init__(
        self,
        xcor,
        ycor,
        mine_status=False,
        flag_status=False,
        texture="tileface.gif",
        clicked_on=False,
    ):
        self.xcor = xcor
        self.ycor = ycor
        self.mine_status = mine_status
        self.flag_status = flag_status
        self.texture = texture
        self.clicked_on = clicked_on

    def __str__(self):
        return f"""
        X:{self.xcor}
        Y:{self.ycor}
        CLICKED:{self.clicked_on}
        FLAG:{self.flag_status}
        TEXTURE{self.texture}"""

    def surface_return(self):
        local_tile = pygame.image.load(self.texture)
        return local_tile


pygame.init()

win = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()  # Skapar en klocka

tile = pygame.image.load("tileface.gif")

test_tile = Tiles(0, 0)

print(test_tile)

tile_list = []
tile_1 = Tiles(xcor=0, ycor=0)
tile_2 = Tiles(xcor=20, ycor=20)
tile_list.append(tile_1)
tile_list.append(tile_2)


def draw(tile_pos):  # Gör allt ritande för varje frame
    win.fill((255, 0, 0))

    win.blit(tile, tile_pos)
    for i in tile_list:
        win.blit(i.surface_return(), (i.xcor, i.ycor))


running = True

while running:

    clock.tick(60)  # sätter framerate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw((200, 150))
    pygame.display.update()
