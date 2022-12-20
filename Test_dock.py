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
per = objekt(1)
sture = objekt(2)
sven = objekt(3)
lista = []
lista.append(per)
lista.append(sture)
lista.append(sven)

print(per.själv_i_lista(lista))


class Test:
    klass_variabler = 0

    def __init__(self, variabler):
        self.värde = variabler


print(Test.klass_variabler)
Test.klass_variabler += 1
print(Test.klass_variabler)
test_objekt = Test(1)
print(test_objekt.klass_variabler)
Test.klass_variabler += 1
print(test_objekt.klass_variabler)
print(Test.klass_variabler)
Test.klass_variabler += 1

test_objekt.klass_variabler += (
    1  # Verkar som att om man manipulerar variabeln i ett objekt så blir det separat.
)


print(test_objekt.klass_variabler)
print(Test.klass_variabler)
