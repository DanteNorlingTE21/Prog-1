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
