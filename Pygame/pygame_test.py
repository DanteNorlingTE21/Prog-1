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


pygame.init()

win = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()  # Skapar en klocka

tile = pygame.image.load("tileface.gif")

test_tile = Tiles(0, 0)

print(test_tile)

tile_list = []


def draw(tile_pos):  # Gör allt ritande för varje frame
    win.fill((255, 0, 0))

    win.blit(tile, tile_pos)


running = True

while running:

    clock.tick(60)  # sätter framerate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw((200, 150))
    pygame.display.update()
