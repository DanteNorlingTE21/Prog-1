import random


def packa_upp_sträng(sträng=str):
    lokal_lista = []
    for i in sträng:
        lokal_lista.append(i)
    return lokal_lista


def okänd_lista(sträng=str):
    lokal_lista = []
    for i in range(len(sträng)):
        lokal_lista.append("_")
    return lokal_lista


def skriv_ut(lista=list, försök=int, felgissningar=list):

    if försök == 0:
        print(
            """
         _____
         |   |
         |
         |
        /|\ 
        """
        )
    elif försök == 1:
        print(
            """
         _____
         |   |
         |  ( )
         |
        /|\ 
        """
        )
    elif försök == 2:
        print(
            """
         _____
         |   |
         |  ( )
         |   |-
        /|\ 
        """
        )
    elif försök == 3:
        print(
            """
         _____
         |   |
         |  ( )
         |  -|-
        /|\ 
        """
        )
    elif försök == 4:
        print(
            """
         _____
         |   |
         |  ( )
         |  -|-
        /|\ /
        """
        )
    elif försök == 5:
        print(
            """
         _____
         |   |
         |  ( )
         |  -|-
        /|\ / \ 
        """
        )
    print(*lista)
    print(*felgissningar)


def gissa():
    while True:
        lokal_gissning = input("Gissning:  ").lower()
        if (len(lokal_gissning) != 1) or lokal_gissning.isnumeric():
            print("Måste vara endast en BOKSTAV")
        else:
            return lokal_gissning


def kolla_vinst(lista=list):
    for i in lista:
        if i == "_":
            return False
    return True


def hänga_gubbe():
    while True:
        försök = 0
        ordlista = ["apa", "ariful", "sill", "jazz", "orangutang", "eldkastare"]
        nuvarande_ord = random.choice(ordlista)
        bokstäver_i_ordet = packa_upp_sträng(nuvarande_ord)
        okända_bokstäver = okänd_lista(nuvarande_ord)
        fel_gissningar = []
        rätt_gissningar = []

        while försök <= 5:
            skriv_ut(okända_bokstäver, försök, fel_gissningar)
            if kolla_vinst(okända_bokstäver):
                print("Du vann!")
                break
            gissning = gissa()
            if (not gissning in rätt_gissningar) and (not gissning in fel_gissningar):
                for index, bokstav in enumerate(bokstäver_i_ordet):
                    if gissning == bokstav:
                        okända_bokstäver[index] = bokstäver_i_ordet[index]
                if not gissning in bokstäver_i_ordet:
                    print("Fel")
                    fel_gissningar.append(gissning)
                    försök += 1
                else:
                    rätt_gissningar.append(gissning)
            else:
                print("Du har redan försökt denna bokstav")

        starta_om = input("Vill du spela igen? (Y/N)   ").capitalize()
        if starta_om == "N":
            break
