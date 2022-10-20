def skottår(år):
    if år % 4 == 0:
        if år % 100 == 0 and not år % 400 ==0:
            return False
        else:
            return True
    else:
        return False

def pyramid(nummer):
    for i in range(nummer+1):
        for n in range(i):
            print(n+1,"", end='')
        print('\n')

a = int(input('Hur stor pyramid vill du ha?'))
pyramid(a)