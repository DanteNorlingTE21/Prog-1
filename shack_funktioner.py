from math import floor


class Pieces:
    def __init__(self, type="blank", white=True):

        self.type = type
        self.white = white
        if self.type == "blank":
            self.texture = "  "
        elif white:
            self.texture = "W" + type[0]
        else:
            self.texture = "B" + type[0]

    def position_on_board(self, local_board):
        for x_index, list in enumerate(local_board):
            for y_index, local_object in enumerate(list):
                if local_object == self:
                    coordinates = 10 * x_index + y_index
                    return coordinates
        else:
            print("Error in position_on_board")


class Rook(Pieces):
    def __init__(self, white=True):
        super().__init__("Rook", white)

    def allowed_to_move_there(self, local_board=list, move_coords=int):
        """move_coords in a two digit integer with the first being x and second being y"""
        if not isinstance(move_coords, int):
            return False

        self_coords = self.position_on_board(local_board)
        self_x = self_coords // 10
        self_y = self_coords - self_x * 10

        move_x = move_coords // 10
        move_y = move_coords - move_x * 10

        if self_coords == move_coords:
            return False

            # same x
        if self_x == move_x:
            return check_y_list_for_piece(local_board, self_x, self_y, move_y)
        if self_y == move_y:
            return check_x_list_for_piece(local_board, self_y, self_x, move_x)


class Pawn(Pieces):
    def __init__(self, white=True):
        super().__init__("Pawn", white)

    def allowed_to_move_there(self, local_board, move_coords):
        """move_coords in a two digit integer with the first being x and second being y"""

        self_coords = self.position_on_board(local_board)
        self_x = self_coords // 10
        self_y = self_coords - self_x * 10

        move_x = move_coords // 10
        move_y = move_coords - move_x * 10

        if move_y - self_y != 1:
            return False
        if self_x - move_x == 0 and local_board[move_x][move_y].type == "blank":
            return True
        if (self_x - move_x == 1 or self_x - move_x == -1) and local_board[move_x][
            move_y
        ].type != "blank":
            return True


class Queen(Pieces):
    def __init__(self, white=True):
        super().__init__("Queen", white)

    def allowed_to_move_there(self, local_board, move_coords):
        """move_coords in a two digit integer with the first being x and second being y"""
        pass


class King(Pieces):
    def __init__(self, white=True):
        super().__init__("King", white)

    def allowed_to_move_there(self, local_board, move_coords):
        """move_coords in a two digit integer with the first being x and second being y"""
        pass


class Bishop(Pieces):
    def __init__(self, white=True):
        super().__init__("Bishop", white)

    def allowed_to_move_there(self, local_board, move_coords):
        """move_coords in a two digit integer with the first being x and second being y"""
        pass


class Knight(Pieces):
    def __init__(self, white=True):
        super().__init__("Knight", white)

    def allowed_to_move_there(self, local_board, move_coords):
        """move_coords in a two digit integer with the first being x and second being y"""
        pass


def start_new_board():
    board = [[], [], [], [], [], [], [], []]

    for list in board:
        for i in range(8):
            list.append(i)

    # Board [x][y]

    board[0][0] = Rook()
    board[1][0] = Knight()
    board[2][0] = Bishop()
    board[3][0] = Queen()
    board[4][0] = King()
    board[5][0] = Bishop()
    board[6][0] = Knight()
    board[7][0] = Rook()

    for x in range(8):
        board[x][1] = Pawn()
    for y in range(2, 6):
        for x in range(8):
            board[x][y] = Pieces()
    for x in range(8):
        board[x][6] = Pawn(False)

    board[0][7] = Rook(False)
    board[1][7] = Knight(False)
    board[2][7] = Bishop(False)
    board[3][7] = Queen(False)
    board[4][7] = King(False)
    board[5][7] = Bishop(False)
    board[6][7] = Knight(False)
    board[7][7] = Rook(False)

    return board


def print_board(local_list=list):
    print("\n |---|---|---|---|---|---|---|---|")
    i = 8
    for y in range(-1, -9, -1):

        print(f"{i}| ", end="")
        for x in range(8):
            print(local_list[x][y].texture, end="| ")
        print("\n |---|---|---|---|---|---|---|---|")
        i -= 1
    print("   A   B   C   D   E   F   G   H  ")


def decifer_input(inputs=str):
    if not isinstance(inputs, str):
        return False
    current_pos, move_pos = inputs.split()
    # print(current_pos, move_pos)
    for index, letter in enumerate("ABCDEFGH"):
        if letter == current_pos[0].capitalize():
            current_coords = str(index) + str((int(current_pos[1]) - 1))
        if letter == move_pos[0].capitalize():
            move_coords = str(index) + str((int(move_pos[1]) - 1))
    try:
        print(current_coords, move_coords)
    except UnboundLocalError:
        return False
    return current_coords, move_coords


def set_texture(local_board, x, y, texture):
    local_board[x][y].texture = texture
    print_board(local_board)


def check_y_list_for_piece(board, x, y1, y2):
    local_list = board[x]
    if y1 < y2:
        for i in range(y1 + 1, y2):
            if local_list[i].type != "blank":
                return False
        else:

            return True
    else:
        y1, y2 = y2, y1
        for i in range(y1 + 1, y2):
            if local_list[i].type != "blank":
                return False
        else:

            return True


def check_x_list_for_piece(board, y, x1, x2):
    if x1 > x2:
        x1, x2 = x2, x1
    for i in range(x1 + 1, x2):
        if board[i][y].type != "blank":
            return False
    return True


def move(local_board, inputs):

    # Decifering inputs
    try:
        current_coords, move_coords = decifer_input(inputs)
        current_coords = int(current_coords)
        move_coords = int(move_coords)
    except ValueError:
        print("coordinates where not two xy pairs: ValueError")
        return False
    except TypeError:
        print(
            """decifer_input() did not return two strings. Input was wrong: TypeError"""
        )
        return False

    if current_coords > 77 or current_coords < 0 or move_coords > 77 or move_coords < 0:
        print("Faulty range of coordinates")
        return False

    current_x = int(current_coords) // 10
    current_y = int(current_coords) - 10 * current_x
    # print(current_x, current_y)
    move_x = int(move_coords) // 10
    move_y = int(move_coords) - 10 * move_x

    # local_board[current_x][current_y]         current piece
    # local_board[move_x][move_y]               square moved to

    # check for piece
    if local_board[current_x][current_y].type == "blank":
        print("can't move blank")
        return False

    # Capturing and moving

    print(
        "det är",
        local_board[current_x][current_y].allowed_to_move_there(
            local_board, move_coords
        ),
    )

    if local_board[move_x][move_y].type == "blank" and local_board[current_x][
        current_y
    ].allowed_to_move_there(local_board, move_coords):
        local_board[move_x][move_y], local_board[current_x][current_y] = (
            local_board[current_x][current_y],
            local_board[move_x][move_y],
        )
    elif (
        local_board[move_x][move_y].type != "blank"
        and local_board[move_x][move_y].white != local_board[current_x][current_y].white
        and local_board[current_x][current_y].allowed_to_move_there(
            local_board, move_coords
        )
    ):
        if isinstance(local_board[move_x][move_y], King):
            print("checkmate")
        local_board[move_x][move_y], local_board[current_x][current_y] = (
            local_board[current_x][current_y],
            Pieces(),
        )

    print(local_board[current_x][current_y].position_on_board(local_board))
