import sys

def wordspin(niz):
    '''Funkcija v najkrašjem času prvi niz pretvori
    v drugi podani niz, kjer uporablja pod nize niza.'''
    beseda1, beseda2 = niz.split()
    # ustvarimo dve tabeli, v kateri imamo sprevljene razdalje znakov in ali se rabimo premikati gor ali dol po abecedi
    indeks = [0] * len(beseda1)
    razmaki = [0] * len(beseda1)
    premiki = 0
    for i in range(len(beseda1)):
        crka1 = ord(beseda1[i])
        crka2 = ord(beseda2[i])
        razmik = crka2 - crka1
        razmaki[i] += razmik
        if razmik < 0:
            indeks[i] = -1
        elif razmik > 0:
            indeks[i] = 1
    prvotni_razmaki = list(razmaki) # ustvarimo prvotno tabelo
    for i in range(1, len(indeks)):
        if indeks[i] != indeks[i - 1]:
            premiki += abs(razmaki[i - 1])
            razmaki[i - 1] = 0
        else:
            if razmaki[i - 1] != 0: # izognemo dodatnemu delu
                predhodni_razmik = abs(razmaki[i - 1])
                trenutni_razmik = abs(razmaki[i])
                if indeks[i] == -1:
                    predznak = -1
                else:
                    predznak = 1
                if predhodni_razmik <= trenutni_razmik:
                    premiki += predhodni_razmik
                    razmaki[i - 1] -= predhodni_razmik * predznak
                    razmaki[i] -= predhodni_razmik * predznak
                else:
                    premiki += trenutni_razmik
                    razmaki[i - 1] -= trenutni_razmik * predznak
                    razmaki[i] -= trenutni_razmik * predznak
            else:
                razmaki[i] -= prvotni_razmaki[i - 1]
    return(premiki + sum(map(abs, razmaki)))

niz='bdefa ggggg'
print(wordspin(niz))
                    
                
            

    

                