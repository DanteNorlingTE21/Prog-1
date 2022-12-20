def snake_sort(lista=list):
    if len(lista) < 2:
        return lista
    pop = lista.pop(-1)
    lista.insert(1, pop)
    return lista


def palindrom(sträng=str):
    if sträng == sträng[::-1]:
        return True
    return False


class Klass:
    objekt = 0

    def __init__(self, sak):
        self.sak = sak

    def själv_i_lista(self, lista):
        if self in lista:
            return True


for first in "ERTCBA":
    for second in "TCNIAM":
        for third in "NAURIE":
            for fourth in "SBLGMK":
                print(first + second + third + fourth, end=" ")
            print("\n")
