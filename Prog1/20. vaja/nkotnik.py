import turtle
import math


def nkotnik(zelva, kraki, dolzina, barva):
    '''Funkcija izriše n-kotnik in mu dodeli barvo.'''
    kot = 360 / 12
    zelva.fillcolor(barva)
    zelva.begin_fill()
    for _ in range(kraki):
        zelva.fd(dolzina)
        zelva.left(kot)
    zelva.end_fill()

lik = turtle.Turtle()
nkotnik(lik, 12, 40, 'red')