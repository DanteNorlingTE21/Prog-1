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


class objekt:
    def __init__(self, sak):
        self.sak = sak

    def själv_i_lista(self, lista):
        if self in lista:
            return True


per = objekt(1)
sture = objekt(2)
sven = objekt(3)
lista = []
lista.append(per)
lista.append(sture)
lista.append(sven)

print(per.själv_i_lista(lista))


for i in range(1, 6):
    print(i)
