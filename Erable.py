from tkinter import *
from turtle import *

"""

def erable(angle,taille,rep):
    color("black")
    up()
    goto(0,-250)
    speed("fast")
    title("Erable")
    shape("turtle")
    left(90)
    down()
    forward(taille*2)
    width(7)
    coef=1
    i=0
    j=0
    x=[None]*rep
    y=rep*[None]
    while i<rep:
        left(angle)
        forward(taille*coef)
        coef=coef*2/3
        if i==rep-1-j :
            x[j],y[j]=pos()
        print(x[j],",",y[j])
        i+=1
        j+=1
    goto(x[j-2],y[j-2])
    right(2*angle)
    forward(taille*(2/3)**i)
        """
_________________________________________________________

theo


def erable(angle,taille,rep):
    color("black")
    up()
    goto(0,-250)
    speed("fast")
    title("Erable")
    shape("turtle")
    left(90)
    down()
    forward(taille*2)
    width(7)
    coef=1
    i=1
    j=1
    liste=[None]*rep
    for k in range (rep):
        for i in range (2^(rep)):
            if( i%2 == 0):
                right(angle)
                forward(taille*coef)
                coef = coef*(2/3)
                liste[x][y]= pos() 
                i=i+1
                j=j+1
                
                
            else :
                left(angle)
                forward(taille*coef)
                coef = coef*(2/3)
                liste[x][y]= pos()
                i=i+1
                j=j+1
                
                
______________________________________________________
def erable(angle,taille,rep):
    color("black")
    up()
    goto(0,-250)
    speed("fast")
    title("Erable")
    shape("turtle")
    left(90)
    down()
    forward(taille*2)
    width(7)
    coef=1
    i=0
    j=0
    x=[None]*rep
    y=rep*[None]
def erable(angle,taille,rep):
    if rep==0:
        color("brown")
        up()
        goto(0,-250)
        width(10)
        speed("fast")
        title("Erable")
        shape("turtle")
        left(90)
        down()
        forward(taille*2)
        rep=rep+1
    else:
        color("green")
        width(7)
        x,y=pos()
        left(angle)
        erable(angle,taille*2/3,rep-1)
        goto(x,y)
        right(angle*2)
        erable(angle,taille*2/3,rep-1)

def erable(taille,rep):
    color("black")
    up()
    goto(0,-250)
    speed("fast")
    title("Erable")
    shape("turtle")
    left(90)
    down()
    forward(taille*2)
    width(7)
    if rep==0 :
        fd(taille)
    else:
        erable(2/3,rep-1)
        left(45)
        erable(2/3,rep-1)
    update()
    penup()
    back(taille)
    pendown()
