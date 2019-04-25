import turtle
import math


def hisa(zelvak, dolzina):
    '''Funkcija s pomočjo turtle nariše
    hišo s podano dolžino.'''
    zelvak.fd(dolzina)
    zelvak.left(90)
    zelvak.fd(dolzina)
    zelvak.left(90)
    zelvak.fd(dolzina)
    zelvak.left(90)
    zelvak.fd(dolzina)
    zelvak.left(180)
    zelvak.penup()
    zelvak.fd(dolzina)
    zelvak.pendown()
    zelvak.right(45)
    zelvak.fd(math.sqrt(2 * 100 ** 2) / 2)
    zelvak.right(90)
    zelvak.fd(math.sqrt(2 * 100 ** 2) / 2)
    zelvak.penup()   
    zelvak.right(90)
    zelvak.fd(math.sqrt(2 * 100 ** 2))
    zelvak.left(180 - 45)
    
    

kuca = turtle.Turtle()
hisa(kuca, 100)