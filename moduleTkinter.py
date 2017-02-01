"""le programe suivant permet d'ouvrir un fenetre avec un toile, """

from tkinter import *
from time import *
from math import *
from random import *
"""
def click(event):
    coord_du_click_en_x=event.x
    coord_du_click_en_y=event.y
    toile.create_oval(coord_du_click_en_x-10,coord_du_click_en_y-10,coord_du_click_en_x+10,coord_du_click_en_y+10,fill='green')
"""
def trait_sous_click(event):
    coord_du_click_en_x=event.x
    coord_du_click_en_y=event.y
    toile.create_oval(coord_du_click_en_x-1,coord_du_click_en_y-1,coord_du_click_en_x+1,coord_du_click_en_y+1,fill='blue',width=0) 
"""
def trait_continu(event):
    coord_du_click_en_x=event.x
    coord_du_click_en_y=event.y
    toile.create_oval(coord_du_click_en_x,coord_du_click_en_y,coord_du_click_en_x,coord_du_click_en_y,fill='red',width=0)"""
def rectangle():
    toile.create_rectangle(50,50,100,150,fill='green',outline='yellow',width=3)
def cercle():
    toile.create_oval(100,100,250,250,fill='red',outline='yellow',width=3)
def cible():
    toile.create_oval(100-80,100-80,100+80,100+80,fill='blue',width=0)
    toile.create_oval(100-60,100-60,100+60,100+60,fill='yellow',width=0)
    toile.create_oval(100-40,100-40,100+40,100+40,fill='red',width=0)
    toile.create_oval(100-20,100-20,100+20,100+20,fill='green',width=0)
    toile.create_line(100,20,100,180)
    toile.create_line(20,100,180,100)
    toile.create_text(30,90,text=("10"),font="Arial 8",fill='red')
    toile.create_text(50,90,text=("20"),font="Arial 8",fill='blue')
    toile.create_text(70,90,text=("30"),font="Arial 8",fill='black')
    toile.create_text(93,90,text=("50"),font="Arial 8",fill='red')
    toile.create_text(107,110,text=("50"),font="Arial 8",fill='red')
    toile.create_text(130,110,text=("30"),font="Arial 8",fill='black')
    toile.create_text(150,110,text=("20"),font="Arial 8",fill='blue')
    toile.create_text(170,110,text=("10"),font="Arial 8",fill='red')

fenetre = Tk()
fenetre.title("rectangle et cercle")
toile = Canvas(fenetre, width=200, height=200, background='black')
boutrec=Button(fenetre,text="créer le rectangle",command=rectangle).pack()
boutcer=Button(fenetre,text="créer le cerle",command=cercle).pack()
boutcib=Button(fenetre,text="créer la cible",command=cible).pack()
#toile.bind("<Button-1>",click)
toile.bind("<B1-Motion>",trait_sous_click)
#toile.bind("<Motion>",trait_continu)
#toile.place(x=0,y=0)
#toile.place(bordermode=INSIDE,width=500,height=500)


toile.pack()
fenetre.mainloop()
