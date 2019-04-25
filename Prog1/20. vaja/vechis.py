import turtle
import math
import random
import pobarvanahisa

def vecHis(zelvak, st_his):
    '''Funkcija nariše več hiš različne velikosti
    in barve.'''
    barve = ['red', 'yellow', 'blue', 'pink', 'green', 'orange']
    for _ in range(st_his):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        dolzina = random.randint(20, 100)
        zelvak.penup()
        zelvak.goto(x, y)
        zelvak.pendown()
        barva1 = random.choice(barve)
        barva2 = random.choice(barve)
        pobarvanahisa.pobarvanahisa(zelvak, dolzina, barva1, barva2)
        
    
kuce = turtle.Turtle()
vecHis(kuce, 10)
