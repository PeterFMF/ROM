import sys

def wordspin(niz):
    '''Funkcija v najkrašjem času prvi niz pretvori
    v drugi podani niz, s pomočjo svojih pod nizov.
    Torej, ustvarimo tabelo razmikov, katera ima pozitivne ali negativne vrednosti,
    katere bi radi spravili na 0.'''
    beseda1, beseda2 = niz.split()
    indeks = [0] * len(beseda1) # pove ali je razmak pozitiven ali negativen (torej, če je znak v beseda1 večji ali manjši od znaka v beseda2)
    razmaki = [0] * len(beseda1) # pove razdaljo, katera je lahko pozitivna ali negativna
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
    prvotni_razmaki = list(razmaki) # ustvarimo kopijo prvotne tabele
    for i in range(1, len(indeks)):
        if indeks[i] != indeks[i - 1] and indeks[i - 1] != 0: # če je v indeksu[i - 1] 0, se ne vrednost premika ne spremeni
            premiki += abs(razmaki[i - 1])
            razmaki[i - 1] = 0
        elif indeks[i - 1] != 0: # izognemo ne produktivnega delovanja kot v predhodnem if-u
            predznak = indeks[i] # -1 ali 1
            if razmaki[i - 1] != 0:
                predhodni_razmik = abs(razmaki[i - 1])
                trenutni_razmik = abs(razmaki[i])    
                if predhodni_razmik <= trenutni_razmik:
                    premiki += predhodni_razmik
                    razmaki[i - 1] -= predhodni_razmik * predznak
                    razmaki[i] -= predhodni_razmik * predznak
                else:
                    premiki += trenutni_razmik
                    razmaki[i - 1] -= trenutni_razmik * predznak
                    razmaki[i] -= trenutni_razmik * predznak
            else:
                if abs(prvotni_razmaki[i - 1]) >= abs(razmaki[i]):
                    razmaki[i] = 0
                else:
                    razmaki[i] -= abs(prvotni_razmaki[i -1]) * predznak
    #print(premiki, razmaki)
    return(premiki + sum(map(abs, razmaki))) # izpiše seštevek vseh premikov in vrednosti, ki so ostale v tabeli
    # vrednosti, katere se ostali v tabeli razmaki, so največje oziroma najmanjše vrednosti, katere imajo sosede vrednost 0. Ni pa nujno.

niz='ggggg bdefa'
print(wordspin(niz))