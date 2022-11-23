import pygame
import random
from math import floor
import time

"""New changes:
removed for loop usage in hit-detecting
made an if-statement that only looped through tiles_to_be_clicked if it was empty
made it so that draw only runs when a tile is clicked on and not every frame
made a lose condition

draw became really slow around the extreme sized boards when it had to redraw 2500 tiles every frame

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


class Button:
    def __init__(self, texture="blank.gif", dx=0, dy=0, xcor=0, ycor=0, restart=False):
        self.texture = texture
        self.dx = dx
        self.dy = dy
        self.xcor = xcor
        self.ycor = ycor
        self.restart = restart

    def coord_tuple(self):
        return (20 * self.xcor, 20 * self.ycor)

    def surface(self):
        """Returns a surface with the buttons texture"""
        local_tile = pygame.image.load(self.texture)
        return local_tile


def coord_round(x):
    return floor(x / 20)


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

    for index, list in enumerate(x_list):
        blank = Button(xcor=index, ycor=y)
        if index == x - 2:
            blank.texture = "minus_x.gif"
            blank.dx = -1
        elif index == x - 1:
            blank.texture = "plus_x.gif"
            blank.dx = 1
        list.append(blank)

    right_row = []
    for i in range(y + 1):
        blank = Button(xcor=x, ycor=i)
        right_row.append(blank)
    right_row[-1].texture = "restart.gif"
    right_row[-1].restart = True
    right_row[-2].texture = "plus_y.gif"
    right_row[-2].dy = 1
    right_row[-3].texture = "minus_y.gif"
    right_row[-3].dy = -1
    x_list.append(right_row)

    return x_list


# cords[0] = x cords[1] = y


def restart():
    global list_of_tiles
    global dimensions
    global mines
    for i in list_of_tiles:
        list_of_tiles.remove(i)
    list_of_tiles = startup(int(dimensions[0]), int(dimensions[1]), mines)
    draw()


def left_click(cords=None, tile_to_be_clicked=None):
    """Cords is tuple, tile_to_be_clicked is Tiles"""
    # print(cords)
    if tile_to_be_clicked is not None:
        cords = tile_to_be_clicked.coord_tuple()
    if cords is None:
        return 0
    mouse_x = cords[0]  # HIT detection \/
    mouse_y = cords[1]  # ______________|
    global now  # ______________________|
    global MOUSE_COOLDOWN  # ___________|
    if (pygame.time.get_ticks() - now) >= MOUSE_COOLDOWN:
        local_tile = list_of_tiles[coord_round(mouse_x)][coord_round(mouse_y)]
        # END OF HIT DETECTION _______
        if isinstance(local_tile, Tiles):
            if not local_tile.clicked_on:  # Check if clicked on
                if not local_tile.flag:
                    if local_tile.mine:
                        local_tile.texture = "mine.gif"
                        local_tile.clicked_on = True
                        for list in list_of_tiles:
                            for tile in list:
                                tile.clicked_on = True

                    else:
                        show_face(local_tile)
        elif isinstance(local_tile, Button):
            if local_tile.restart:
                restart()
            elif (local_tile.dx != 0) or (local_tile.dy != 0):
                resize(local_tile.dx, local_tile.dy)

    elif tile_to_be_clicked is not None:
        local_tile = list_of_tiles[coord_round(mouse_x)][coord_round(mouse_y)]
        # END OF HIT DETECTION _______
        if not local_tile.clicked_on:  # Check if clicked on
            if not local_tile.flag:
                if local_tile.mine:
                    local_tile.texture = "mine.gif"
                    local_tile.clicked_on = True
                    for list in list_of_tiles:
                        for tile in list:
                            tile.clicked_on = True

                else:
                    show_face(local_tile)
        now = pygame.time.get_ticks()


def middle_click(cords=tuple):
    mouse_x = cords[0]  # HIT detection \/
    mouse_y = cords[1]  # ______________|
    local_tile = list_of_tiles[coord_round(mouse_x)][coord_round(mouse_y)]
    # END OF HIT DETECTION _______
    if isinstance(local_tile, Tiles):
        if local_tile.clicked_on:  # Check if clicked on
            print(local_tile.coord_tuple())
            for i in local_tile.texture:
                if i in "012345678":
                    click_around(int(i), local_tile)


def right_click(cords=tuple):
    """Does the right click functionality"""
    mouse_x = cords[0]  # HIT detection \/
    mouse_y = cords[1]  # ______________|
    global now  # ______________________|
    global MOUSE_COOLDOWN  # ___________|
    if (pygame.time.get_ticks() - now) >= MOUSE_COOLDOWN:
        local_tile = list_of_tiles[coord_round(mouse_x)][coord_round(mouse_y)]
        # END OF HIT DETECTION _______
        if isinstance(local_tile, Tiles):
            if not local_tile.clicked_on:  # Check if clicked on
                if not local_tile.flag:  # DO STUFF
                    local_tile.flag = True
                    local_tile.texture = "tileflag.gif"

                elif local_tile.flag:
                    local_tile.flag = False
                    local_tile.texture = "tileface.gif"
            now = pygame.time.get_ticks()


def click_around(number=int, local_tile=Tiles):
    neighbour_flags = 0
    check_left = False
    check_right = False
    check_up = False
    check_down = False
    if local_tile.xcor > 0:
        check_left = True
    if local_tile.xcor + 2 < len(list_of_tiles):
        check_right = True
    if local_tile.ycor > 0:
        check_up = True
    if local_tile.ycor + 2 < len(list_of_tiles[local_tile.xcor]):
        check_down = True

    if check_left:
        if list_of_tiles[local_tile.xcor - 1][local_tile.ycor].flag:
            neighbour_flags += 1
    if check_right:
        if list_of_tiles[local_tile.xcor + 1][local_tile.ycor].flag:
            neighbour_flags += 1
    if check_up:
        if list_of_tiles[local_tile.xcor][local_tile.ycor - 1].flag:
            neighbour_flags += 1
    if check_down:
        if list_of_tiles[local_tile.xcor][local_tile.ycor + 1].flag:
            neighbour_flags += 1
    if check_up and check_left:
        if list_of_tiles[local_tile.xcor - 1][local_tile.ycor - 1].flag:
            neighbour_flags += 1
    if check_up and check_right:
        if list_of_tiles[local_tile.xcor + 1][local_tile.ycor - 1].flag:
            neighbour_flags += 1
    if check_down and check_left:
        if list_of_tiles[local_tile.xcor - 1][local_tile.ycor + 1].flag:
            neighbour_flags += 1
    if check_down and check_right:
        if list_of_tiles[local_tile.xcor + 1][local_tile.ycor + 1].flag:
            neighbour_flags += 1
    print("neighbourflags", neighbour_flags)
    if neighbour_flags == number:
        if check_left:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor - 1][local_tile.ycor]
            )
        if check_right:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor + 1][local_tile.ycor]
            )
        if check_up:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor][local_tile.ycor - 1]
            )
        if check_down:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor][local_tile.ycor + 1]
            )
        if check_left and check_up:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor - 1][local_tile.ycor - 1]
            )
        if check_left and check_down:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor - 1][local_tile.ycor + 1]
            )
        if check_right and check_up:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor + 1][local_tile.ycor - 1]
            )
        if check_right and check_down:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor + 1][local_tile.ycor + 1]
            )


def show_face(local_tile=Tiles):
    """Makes the tile show how many mines surround it, also clicks around empty tiles"""
    neighbour_mines = 0
    check_left = False
    check_right = False
    check_up = False
    check_down = False
    if local_tile.xcor > 0:
        check_left = True
    if local_tile.xcor + 2 < len(list_of_tiles):
        check_right = True
    if local_tile.ycor > 0:
        check_up = True
    if local_tile.ycor + 2 < len(list_of_tiles[local_tile.xcor]):
        check_down = True

    if check_left:
        if list_of_tiles[local_tile.xcor - 1][local_tile.ycor].mine:
            neighbour_mines += 1
    if check_right:
        if list_of_tiles[local_tile.xcor + 1][local_tile.ycor].mine:
            neighbour_mines += 1
    if check_up:
        if list_of_tiles[local_tile.xcor][local_tile.ycor - 1].mine:
            neighbour_mines += 1
    if check_down:
        if list_of_tiles[local_tile.xcor][local_tile.ycor + 1].mine:
            neighbour_mines += 1
    if check_up and check_left:
        if list_of_tiles[local_tile.xcor - 1][local_tile.ycor - 1].mine:
            neighbour_mines += 1
    if check_up and check_right:
        if list_of_tiles[local_tile.xcor + 1][local_tile.ycor - 1].mine:
            neighbour_mines += 1
    if check_down and check_left:
        if list_of_tiles[local_tile.xcor - 1][local_tile.ycor + 1].mine:
            neighbour_mines += 1
    if check_down and check_right:
        if list_of_tiles[local_tile.xcor + 1][local_tile.ycor + 1].mine:
            neighbour_mines += 1
    local_tile.texture = f"tile{neighbour_mines}.gif"
    local_tile.clicked_on = True
    if neighbour_mines == 0:
        if check_left:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor - 1][local_tile.ycor]
            )
        if check_right:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor + 1][local_tile.ycor]
            )
        if check_up:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor][local_tile.ycor - 1]
            )
        if check_down:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor][local_tile.ycor + 1]
            )
        if check_left and check_up:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor - 1][local_tile.ycor - 1]
            )
        if check_left and check_down:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor - 1][local_tile.ycor + 1]
            )
        if check_right and check_up:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor + 1][local_tile.ycor - 1]
            )
        if check_right and check_down:
            tiles_to_be_clicked.append(
                list_of_tiles[local_tile.xcor + 1][local_tile.ycor + 1]
            )


def resize(dx, dy):
    global dimensions
    global win
    dimensions[0] = int(dimensions[0]) + dx
    dimensions[1] = int(dimensions[1]) + dy
    win = pygame.display.set_mode(
        (20 * dimensions[0] + 20, 20 * dimensions[1] + 20), pygame.RESIZABLE
    )
    restart()
    time.sleep(1)


def draw():
    """updates the screen (is laggy and is thus only ran when events happen that would change the look of the screen)"""
    win.fill((160, 160, 160))
    for x in list_of_tiles:
        for y in x:
            win.blit(y.surface(), y.coord_tuple())


dimensions = input("X * Y?:").split()  # takes two dimension inputs x by y
mines = int(input("NUMBER OF MINES:"))


if (int(dimensions[0]) < 5) or (int(dimensions[1]) < 5):
    dimensions[0] = 5
    dimensions[1] = 5

if mines > int(dimensions[0]) * int(dimensions[1]):
    mines = int(dimensions[0]) * int(dimensions[1])

pygame.init()
win = pygame.display.set_mode(
    (20 * int(dimensions[0]) + 20, 20 * int(dimensions[1]) + 20), pygame.RESIZABLE
)

MOUSE_COOLDOWN = 500

now = pygame.time.get_ticks()

list_of_tiles = startup(int(dimensions[0]), int(dimensions[1]), mines)
tiles_to_be_clicked = []


draw()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    mouse_status = pygame.mouse.get_pressed()
    if mouse_status[0] and not mouse_status[2]:
        left_click(pygame.mouse.get_pos())
        draw()
        # pygame.time.delay(200)
    if mouse_status[1] or (mouse_status[0] and mouse_status[2]):
        middle_click(pygame.mouse.get_pos())
        draw()
    if mouse_status[2] and not mouse_status[0]:
        right_click(pygame.mouse.get_pos())
        draw()
        # pygame.time.delay(200)
    if len(tiles_to_be_clicked) > 0:
        for local_tile in tiles_to_be_clicked:
            left_click(tile_to_be_clicked=local_tile)
            tiles_to_be_clicked.remove(local_tile)
        draw()
    # print(pygame.mouse.get_pos())
    # print(pygame.mouse.get_pressed())

    pygame.display.update()
