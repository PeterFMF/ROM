import turtle

def sprehod(zelva, niz, dolzina):
    '''Funkcija glede na podani niz izriše lik.'''
    for crka in niz:
        if crka in 'udlr':
            if crka == 'u':
                zelva.left(90)
                zelva.fd(dolzina)
                zelva.right(90)
            elif crka == 'd':
                zelva.right(90)
                zelva.fd(dolzina)
                zelva.left(90)
            elif crka == 'l':
                zelva.bk(dolzina)
            else:
                zelva.fd(dolzina)
                
    
lik = turtle.Turtle()
sprehod(lik, 'ururullldldr', 40)