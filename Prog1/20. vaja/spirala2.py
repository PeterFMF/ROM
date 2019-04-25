import turtle
import math

def spirala2(zelva, n, kraki):
    '''Funkcija izriše n-krakov glede na n števila
    zavite spirale.'''
    kot = 360 / kraki
    x, y = turtle.screensize()
    dolzina = x / n
    zelva.penup()
    zelva.goto(x, y/2)
    zelva.pendown()
    zelva.left(180 + kot/2)
    for _ in range(n):
        for i in range(1, kraki + 1):
            zelva.fd(dolzina)
            zelva.right(kot)
            if i % 2 = 0:
                dolzina -= n * kraki
        
        
    
lik = turtle.Turtle()
spirala2(lik, 3, 4)