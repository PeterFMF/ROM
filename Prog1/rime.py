def poisci_rime(besede, datoteka):
    '''Funkcija razporedi besede, ki se rimajo v posamezne
    tabele in jih zapiše v datoteko.'''
    slovar = dict()
    dat = open(datoteka, 'w')
    for beseda in besede:
        rima = ''
        samoglasnik = False
        for znak in beseda[::-1]:
            if znak in 'aeiou':
                rima = znak + rima
                samoglasnik = True
                break
            else:
                rima = znak + rima
        if samoglasnik:
            if rima in slovar:
                slovar[rima].append(beseda)
            elif rima != '':
                slovar[rima] = list()
                slovar[rima].append(beseda)
    for kljuc in slovar:
        dat.write(kljuc + ': ' + '[' + ", ".join(slovar[kljuc]) + ']' + '\n')
    dat.close()

if __name__ == '__main__':
    poisci_rime(["zob", "miš", "rob", "grob", "piš"], 'rime.txt')
    # navadni primer
    poisci_rime(["", "mik", "rik", "grb", "prb"], 'rime2.txt')
    # tabela, z praznim elementom
    poisci_rime([], 'rime3.txt')
    # prazna tabela
    poisci_rime(["zo3b", "miš1", "rob", "grob", "piš1"], 'rime4.txt')
    # elementi, ki ne vsebujejo le črke