import turtle
import math


def pobarvanahisa(zelvak, dolzina, barva1, barva2):
    '''Funkcija s pomočjo turtle nariše
    hišo s podano dolžino in jo pobarva.'''
    zelvak.fillcolor(barva1)
    zelvak.begin_fill()
    for _ in range(4):
        zelvak.fd(dolzina)
        zelvak.left(90)
    zelvak.end_fill()
    zelvak.left(90)
    zelvak.penup()
    zelvak.fd(dolzina)
    zelvak.pendown()
    zelvak.fillcolor(barva2)
    zelvak.begin_fill()
    zelvak.right(45)
    zelvak.fd(math.sqrt(2 * dolzina ** 2) / 2)
    zelvak.right(90)
    zelvak.fd(math.sqrt(2 * dolzina ** 2) / 2)
    zelvak.end_fill()
    zelvak.penup()   
    zelvak.right(90)
    zelvak.fd(math.sqrt(2 * dolzina ** 2))
    zelvak.left(180 - 45)
    
    
if __name__ == '__main__':
    kuca = turtle.Turtle()
    pobarvanahisa(kuca, 100, 'yellow', 'red')
