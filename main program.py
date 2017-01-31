"""le programe suivant permet d'ouvrir un fenetre avec un toile, """
from tkinter import *
from time import *
from math import *
from random import *

def click(event):
    coord_du_click_en_x=event.x
    coord_du_click_en_y=event.y
    toile.create_oval(coord_du_click_en_x-10,coord_du_click_en_y-10,coord_du_click_en_x+10,coord_du_click_en_y+10,fill='green')

def trait_sous_click(event):
    coord_du_click_en_x=event.x
    coord_du_click_en_y=event.y
    toile.create_oval(coord_du_click_en_x-1,coord_du_click_en_y-1,coord_du_click_en_x+1,coord_du_click_en_y+1,fill='blue',width=0) 

def trait_continu(event):
    coord_du_click_en_x=event.x
    coord_du_click_en_y=event.y
    toile.create_oval(coord_du_click_en_x,coord_du_click_en_y,coord_du_click_en_x,coord_du_click_en_y,fill='red',width=0)
    
fenetre = Tk()
fenetre.title("je suis un titre")
toile = Canvas(fenetre, width=500, height=500, background='light grey')
toile.bind("<Button-1>",click)
toile.bind("<B1-Motion>",trait_sous_click)
toile.bind("<Motion>",trait_continu)
toile.pack()
fenetre.mainloop()
