from shack_funktioner import *

vits_tur = True
bräde = start_new_board()
print_board(bräde, vits_tur)

while True:
    shack_matt, vits_tur = move(bräde, input(), vits_tur)
    print_board(bräde, vits_tur)
    if shack_matt:
        break
