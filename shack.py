from shack_funktioner import *

bräde = start_new_board()
print_board(bräde)
set_texture(bräde, 0, 0, "ÄÄ")
# move = decifer_input(input())
while True:
    move(bräde, input())
    print_board(bräde)
