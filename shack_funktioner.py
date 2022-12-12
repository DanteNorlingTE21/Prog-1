class Pieces:
    def __init__(self, position=tuple, type="blank", white=True):
        self.pos = position
        self.type = type
        self.white = white
        if self.type == "blank":
            self.texture = "  "
        elif white:
            self.texture = "W" + type[0]
        else:
            self.texture = "B" + type[0]

    def return_pos(self):
        print("X:", self.pos[0])
        print("Y", self.pos[1])
        return self.pos

    def return_coords(self):
        print("X:", self.pos[0])
        print("Y", self.pos[1])
        return self.pos[0], self.pos[1]


class Rook(Pieces):
    def __init__(self, position=tuple, white=True):
        super().__init__(position, "Rook", white)


class Pawn(Pieces):
    def __init__(self, position=tuple, white=True):
        super().__init__(position, "Pawn", white)


class Queen(Pieces):
    def __init__(self, position=tuple, white=True):
        super().__init__(position, "Queen", white)


class King(Pieces):
    def __init__(self, position=tuple, white=True):
        super().__init__(position, "King", white)


class Bishop(Pieces):
    def __init__(self, position=tuple, white=True):
        super().__init__(position, "Bishop", white)


class Knight(Pieces):
    def __init__(self, position=tuple, white=True):
        super().__init__(position, "Knight", white)


def start_new_board():
    board = [[], [], [], [], [], [], [], []]

    for list in board:
        for i in range(8):
            list.append(i)

    # Board [x][y]

    board[0][0] = Rook((0, 0))
    board[1][0] = Knight((1, 0))
    board[2][0] = Bishop((2, 0))
    board[3][0] = Queen((3, 0))
    board[4][0] = King((4, 0))
    board[5][0] = Bishop((5, 0))
    board[6][0] = Knight((6, 0))
    board[7][0] = Rook((7, 0))

    for x in range(8):
        board[x][1] = Pawn((x, 1))
    for y in range(2, 6):
        for x in range(8):
            board[x][y] = Pieces()
    for x in range(8):
        board[x][6] = Pawn((x, 6), False)

    board[0][7] = Rook((0, 7), False)
    board[1][7] = Knight((1, 7), False)
    board[2][7] = Bishop((2, 7), False)
    board[3][7] = Queen((3, 7), False)
    board[4][7] = King((4, 7), False)
    board[5][7] = Bishop((5, 7), False)
    board[6][7] = Knight((6, 7), False)
    board[7][7] = Rook((7, 7), False)

    return board


def print_board(local_list=list):
    print("\n|---|---|---|---|---|---|---|---|")
    for y in range(8):
        print("| ", end="")
        for x in range(8):
            print(local_list[x][y].texture, end="| ")
        print("\n|---|---|---|---|---|---|---|---|")
