import turtle


def spirala(zelva, premik):
    '''Funkcija izriše spiralo glede na število
    podanih premikov pri kotu za 90 stopinj.'''
    dolzina = 10
    for _ in range(premik):
        zelva.left(90)
        zelva.fd(dolzina)
        dolzina += 10
    
spin = turtle.Turtle()
spirala(spin, 20)