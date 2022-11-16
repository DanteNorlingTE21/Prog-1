import pygame
import random

""" TODO:
cooldown for click functions
left and middle click

"""


class Tiles:
    def __init__(
        self,
        xcor=0,
        ycor=0,
        texture="tileface.gif",
        clicked_on=False,
        mine=False,
        flag=False,
    ):
        self.xcor = xcor
        self.ycor = ycor
        self.texture = texture
        self.clicked_on = clicked_on
        self.mine = mine
        self.flag = flag

    # sets required attributes for each tile

    def __str__(self):
        """Makes the tiles attributes printable for troubleshooting purposes"""
        return f"""
        X:{self.xcor}
        Y:{self.ycor}
        TEXTURE:{self.texture}
        Clicked:{self.clicked_on}
        MINE:{self.mine}
        FLAG:{self.flag}
        """

    def coord_tuple(self):
        """Gives the cords of a tile in a tuple because pygame wants tuples: also multiplies by twenty because the textures are 20x20 pixels"""
        return (20 * self.xcor, 20 * self.ycor)

    def surface(self):
        """Returns a surface with the tiles texture"""
        local_tile = pygame.image.load(self.texture)
        return local_tile


def startup(x=3, y=3, number_of_mines=int):
    """returns a list(x cord list) with y_lists that contain the tiles. Also makes some of them mines"""

    x_list = []
    for x_entry in range(x):
        y_list = []
        for y_entry in range(y):
            local_tile = Tiles(xcor=x_entry, ycor=y_entry)
            y_list.append(local_tile)
            # print(*y_list)
        x_list.append(y_list)
        # print(*x_list)
    mine_counter = 0
    while mine_counter < number_of_mines:
        local_tile = random.choice(random.choice(x_list))
        if not local_tile.mine:
            local_tile.mine = True
            mine_counter += 1
    return x_list


# cords[0] = x cords[1] = y


def left_click(cords=tuple):
    print(cords)


def middle_click(cords=tuple):
    pass


def right_click(cords=tuple):
    mouse_x = cords[0]
    mouse_y = cords[1]

    for lists in list_of_tiles:
        for local_tile in lists:
            local_tuple = local_tile.coord_tuple()
            local_x = local_tuple[0]
            local_y = local_tuple[1]
            if (local_x + 20 > mouse_x >= local_x) and (
                local_y + 20 > mouse_y >= local_y
            ):

                if not local_tile.clicked_on:
                    if not local_tile.flag:
                        local_tile.flag = True
                        local_tile.texture = "tileflag.gif"

                    elif local_tile.flag:
                        local_tile.flag = False
                        local_tile.texture = "tileface.gif"


def draw():
    win.fill((160, 160, 160))
    for x in list_of_tiles:
        for y in x:
            win.blit(y.surface(), y.coord_tuple())


dimensions = input("X * Y?:").split()  # takes two dimension inputs x by y
mines = int(input("NUMBER OF MINES:"))


pygame.init()
win = pygame.display.set_mode((20 * int(dimensions[0]), 20 * int(dimensions[1])))

list_of_tiles = startup(int(dimensions[0]), int(dimensions[1]), mines)

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    mouse_status = pygame.mouse.get_pressed()
    if mouse_status[0]:
        left_click(pygame.mouse.get_pos())
        draw()
        # pygame.time.delay(200)
    if mouse_status[2]:
        right_click(pygame.mouse.get_pos())
        draw()
        # pygame.time.delay(200)

    # print(pygame.mouse.get_pos())
    # print(pygame.mouse.get_pressed())
    pygame.display.update()
