from tkinter import *
from turtle import *

coeff=2/3
angle=60

def tronc(taille):
    width(7)
    color("brown")
    up()
    goto(0,-250)
    speed("fastest")
    title("Erable")
    shape("turtle")
    left(90)
    down()
    forward(taille*2)
    


def erable(taille,rep):
    width(5)
    (x,y)=pos()
    color("green")
    if rep==0 :
        up()
        goto(x,y)
        down()
    else:
        forward((2/3)*taille)
        right(45)
        erable(taille*coeff,rep-1)
        left(45)
        
        forward((1/3)*taille)
        left(45)
        erable(taille*coeff,rep-1)
        right(45)

        right(7)
        erable(taille*coeff,rep-1)
        left(7)
        forward(-1/3*taille)
        forward(-2/3*taille)
        
        (x,y)=pos()

tronc(100)
erable(100,6)
