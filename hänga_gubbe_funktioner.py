import random


def ordlistan():
    ordlista = [
        "abba",
        "sill",
        "jazz",
        "pruttar",
        "ordningsregler",
        "cowboy",
        "jeans",
        "jorts",
    ]
    return  ordlista


def välj_ett_ord(lista=list):
    ordet = random.choice(lista)
    return ordet

def rita_ut_skärmen(försök, ord):


def kolla_bokstav_i_ord(bokstav=str, ord=str):

    if (len(bokstav) != 1) or (bokstav.isnumeric()):
        print("Skriv endast bokstäver")
        return False
    for index, tecken in enumerate(ord):
        if bokstav == tecken:
            return True, index
    return False


def hänga_gubbe_main():
    ordlista = ordlistan()
    nuvarande_ord = välj_ett_ord(ordlista)
    har_gissat_rätt = False
    rätt_gissningar= {}


    while not har_gissat_rätt:
        gissnig = input("Gissnig:")
        bokstav_i_ord, index =kolla_bokstav_i_ord(gissnig,nuvarande_ord)
        if bokstav_i_ord:
            rätt_gissningar{gissnig} = index
            
