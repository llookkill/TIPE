from turtle import *

def koch(n,longueur):
 speed(0)
 if n==0:
  forward(longueur)
 else:
 koch_n(n-1,longueur/3)
 left(60)
 koch_n(n-1,longueur/3)
 right(120)
 koch_n(n-1,longueur/3)
 left(60)
 koch_n(n-1,longueur/3)
decale_vers_la_gauche(300)
decale_vers_le_haut(-200)
koch_n(4,300)

def decale_vers_la_gauche(largeur):
  left(180)
  penup()
  forward(180)
  pendown()
  left(180)
  
 def decale_vers_le_haut(hauteur):
  left(90)
  penup()
  forward(hauteur)
  pendown()
  right(90)
  
def sierpinski(n,longueur):
speed(0)
if n==0:
  for i in range(0,3):
   forward(longueur)
   left(120)
if n>0:
 sierpinski(n-1,longueur/2)
 forward(longueur/2)
 sierpinski(n-1,longueur/2)
 backward(longueur/2)
 left(60)
 forward(longueur/2)
 right(60)
 sierpinski(n-1,longueur/2)
 left(60)
 backward(longueur/2)
 right(60)
decale_vers_la_gauche(300)
decale_vers_le_haut(-200)
sierpinski(4,600)
