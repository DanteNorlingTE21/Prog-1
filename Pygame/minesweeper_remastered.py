import pygame
import random
from math import floor
import time


class Tiles:
    """The object class that the playing field is from"""

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
    """The object class of the surrounding buttons and empty space"""

    def __init__(self, texture="blank.gif", dx=0, dy=0, xcor=0, ycor=0, restart=False):
        self.texture = texture
        self.dx = dx
        self.dy = dy
        self.xcor = xcor
        self.ycor = ycor
        self.restart = restart

    def coord_tuple(self):
        """Same as the Tiles"""
        return (20 * self.xcor, 20 * self.ycor)

    def surface(self):
        """Returns a surface with the buttons texture"""
        local_tile = pygame.image.load(self.texture)
        return local_tile


def coord_round(x):
    """Used to find what tile or button is being pressed on.
    Since every tile's texture is 20x20 pixels and it's coordinates are 20 times it's position in the list_of_tiles[x][y],
    This function can be used to find the index of the tile clicked from mouse coordinates"""
    return floor(x / 20)


def startup(x=3, y=3, number_of_mines=int):
    """returns a list(x cord list) with y_lists that contain the tiles. Also makes some of them mines and adds the buttons at the bottom and right side"""

    x_list = []  # creates a local list
    for x_entry in range(x):  # loops x times
        y_list = []  # creates another local list
        for y_entry in range(y):  # loops y times
            local_tile = Tiles(xcor=x_entry, ycor=y_entry)  # creates a tile
            y_list.append(local_tile)  # adds it to the y_list
            # print(*y_list)
        x_list.append(y_list)  # adds the y_list to the x_list
        # print(*x_list)
    mine_counter = 0  # counts placed mines
    while (
        mine_counter < number_of_mines
    ):  # loops untill there is a sufficient number of mines
        local_tile = random.choice(
            random.choice(x_list)
        )  # the nested random chooses a random list and the outer one chooses from that list
        if not local_tile.mine:  # checks that the tile isn't a mine
            local_tile.mine = True  # makes it a mine
            mine_counter += 1  # tallys the mines

    for index, list in enumerate(x_list):  # Goes through the lists left to right
        blank = Button(xcor=index, ycor=y)  # creates a local Button
        if index == x - 2:  # checks if it should be a left arrow
            blank.texture = "minus_x.gif"
            blank.dx = -1
        elif index == x - 1:  # checks if it shoul be a left arrow
            blank.texture = "plus_x.gif"
            blank.dx = 1
        list.append(blank)  # adds the buttons at the bottom

    right_row = []  # creates a local list (the rightmost row)
    for i in range(y + 1):
        blank = Button(xcor=x, ycor=i)  # Creates local Buttons
        right_row.append(blank)  # Appends local buttons

    # puts on the right textures for the buttons
    right_row[-1].texture = "restart.gif"
    right_row[-1].restart = True
    right_row[-2].texture = "plus_y.gif"
    right_row[-2].dy = 1
    right_row[-3].texture = "minus_y.gif"
    right_row[-3].dy = -1
    x_list.append(right_row)  # adds the right row to the list

    return x_list  # returns the list


# cords[0] = x cords[1] = y


def restart():
    global list_of_tiles
    global dimensions
    global mines
    for i in list_of_tiles:
        list_of_tiles.remove(i)  # removes everything from list_of_tiles
    list_of_tiles = startup(
        int(dimensions[0]), int(dimensions[1]), mines
    )  # Reruns startup with dimensions and mines
    draw()


def left_click(cords=None, tile_to_be_clicked=None):
    """Cords is tuple, tile_to_be_clicked is Tiles
    Does left_click functionality"""
    # print(cords)
    global list_of_tiles
    if tile_to_be_clicked is not None:  # check if input is Tile
        cords = tile_to_be_clicked.coord_tuple()
    elif cords is None:  # check for cords input
        return 0
    mouse_x = cords[0]  # Makes local x and y for mouse coords
    mouse_y = cords[1]  # Makes local x and y for mouse coords
    global now  # Used for cooldown
    global MOUSE_COOLDOWN  # Set cooldown in ticks
    if (
        pygame.time.get_ticks() - now
    ) >= MOUSE_COOLDOWN:  # executes if enough ticks have passed
        local_tile = list_of_tiles[coord_round(mouse_x)][
            coord_round(mouse_y)
        ]  # uses coord_round to know index of tiles and avoid for-loop usage
        if isinstance(local_tile, Tiles):  # checks if it is a tile
            if not local_tile.clicked_on:  # Check if clicked on
                if not local_tile.flag:  # check if flagged
                    if local_tile.mine:  # check if mine
                        local_tile.texture = "mine.gif"
                        local_tile.clicked_on = True
                        for (
                            list
                        ) in (
                            list_of_tiles
                        ):  # Makes every Tile clicked preventing further play
                            for tile in list:
                                tile.clicked_on = True
                    else:
                        show_face(
                            local_tile
                        )  # runs show_face wich determines the face-value of a tile

        elif isinstance(local_tile, Button):  # checks if it's a button
            if local_tile.restart:  # checks if it's a restart button
                restart()  # restarts
            elif (local_tile.dx != 0) or (local_tile.dy != 0):
                if not (
                    local_tile.dx == -1 and len(list_of_tiles) == 6
                ):  # Checks if board is big enough to shrink
                    if not (
                        local_tile.dy == -1 and len(list_of_tiles[0]) == 6
                    ):  # Checks if board is big enough to shrink
                        resize(local_tile.dx, local_tile.dy)  # resizes board

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

MOUSE_COOLDOWN = 200

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
