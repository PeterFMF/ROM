def crkujNATO(niz):
    '''Funkcija podani niz pretvori v NATO
    abecedo.'''
    slovar = { 'a': 'alfa', 'b': 'bravo',
               'c': 'charlie', 'd': 'delta',
               'e': 'echo', 'f': 'foxtrot',
               'g': 'golf', 'h': 'hotel',
               'i': 'india', 'j': 'juliett',
               'k': 'kilo', 'l': 'lime',
               'm': 'mike', 'n': 'november',
               'o': 'oscar', 'p': 'papa',
               'q': 'quebec', 'r': 'romeo',
               's': 'sierra', 't': 'tango',
               'u': 'uniform', 'v': 'victory',
               'w': 'whiskey', 'x': 'x-ray',
               'y': 'yankee', 'z': 'zulu'
        }
    NATO_niz = ""
    for crka in niz.lower():
        if crka in slovar:
            NATO_niz += slovar[crka] + ' '
        elif crka == ' ':
            NATO_niz += '   '
    return NATO_niz[:-1]

def razberiNATO(niz):
    '''Funkcija iz podanega niza odšifrira
    NATO besedilo v navadno besedilo.'''
    slovar = { 'a': 'alfa', 'b': 'bravo',
               'c': 'charlie', 'd': 'delta',
               'e': 'echo', 'f': 'foxtrot',
               'g': 'golf', 'h': 'hotel',
               'i': 'india', 'j': 'juliett',
               'k': 'kilo', 'l': 'lime',
               'm': 'mike', 'n': 'november',
               'o': 'oscar', 'p': 'papa',
               'q': 'quebec', 'r': 'romeo',
               's': 'sierra', 't': 'tango',
               'u': 'uniform', 'v': 'victory',
               'w': 'whiskey', 'x': 'x-ray',
               'y': 'yankee', 'z': 'zulu'
        }
    novi_niz = ''
    besedilo = niz.split()
    for beseda in besedilo:
        beseda = beseda.lower()
        if beseda in slovar.values():
            for kljuc, podatek in slovar.items():
                if podatek == beseda:
                    novi_niz += kljuc
        else:
            novi_niz += beseda
    return novi_niz
            

if __name__ == '__main__':
    print(crkujNATO('zaspan sem.'))
    # preverim z običajnim besedilom
    print(crkujNATO('zASpaN sEm'))
    # preverjanje z velikimi tiskanimi črkami
    print(crkujNATO(''))
    # preverjanje brez niza
    print(crkujNATO('z%&pan/se1 '))
    # ---
    print(razberiNATO('zulu alfa sierra papa alfa november - sierra echo mike'))
    # preverimo z običajnim besedilom
    print(razberiNATO('zuluu alfa sie$rra papa alfa november   sierra echo mik2e'))
    # preverimo z besedilom, ki vsebuje različne besede abecede
    print(razberiNATO(' '))
    # preverimo z nizom, ki vsebuje le presledek
    print(razberiNATO('kilo alfa juliett - sierra echo - delta oscar golf alfa juliett alfa '))
    # preverimo z praznim besedilom
    print(razberiNATO('Zulu alfa siErra papa alfa novemb22er - sierra ecCo mike'))
    # preverimo z velikimi črkami