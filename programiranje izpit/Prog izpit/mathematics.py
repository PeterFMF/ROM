import io

file = io.open("mathematics.tab", mode = "r", encoding = "utf-8")
ind = False
seznam = dict()
for vrstica in file:
    vrstica = vrstica.split("\t")
    if ind == True:
        ime = vrstica[0] + " " + vrstica[1]
        id = vrstica[2]
        leto = vrstica[13]
        tocke = vrstica[22]
        if ime not in seznam:
            seznam[ime] = list()
        podatki = [id, leto, tocke]
        seznam[ime] += podatki
    ind = True

maks = 0
red = list()
for avtor in seznam.keys():
    podatki = seznam[avtor]
    nov_tocke = list()
    tocke = podatki[2::3]
    for tocka in tocke:
        if tocka != 'NA':
            nov_tocke.append(float(tocka))
    leta = list(map(int, podatki[1::3]))
    st_clankov = podatki.count(podatki[0])
    aktivnost = max(leta) - min(leta) + 1
    povp_tocke = sum(nov_tocke) / aktivnost
    povp_clanki = st_clankov / aktivnost
    red.append((avtor + '\t' + str(povp_clanki) + '\t' + str(povp_tocke), povp_tocke))
file.close()

file = io.open("scores.tab", "w", encoding = "utf-8")
red = sorted(red, key = lambda x: x[1])
for i in red[::-1]:
    file.write(i[0] + "\n")
file.close()
    
    
        





    


            

