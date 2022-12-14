from shack_funktioner import *

vits_tur = True
bräde = start_new_board()
print_board(bräde, vits_tur)
set_texture(bräde, 0, 0, "ÄÄ")
# move = decifer_input(input())

while True:
    shack_matt, vits_tur = move(bräde, input(), vits_tur)
    print_board(bräde, vits_tur)
    if shack_matt:
        break
