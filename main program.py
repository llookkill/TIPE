"""le programe suivant permet d'ouvrir un fenetre simple avec hello world"""
from tkinter import *
from time import *
from math import *
from random import *
fenetre = Tk()
label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()
