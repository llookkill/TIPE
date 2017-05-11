from tkinter import *


def start(c):
    global pre
    toile.delete(ALL)
    toile.create_rectangle(400,3,600,6,width=1)
    if c == complex(110,110): c=complex(ac.get(),ab.get())
    print(c)
    toile.create_text(950,50,text="C = {} + {}i".format(c.real,c.imag))
    toile.update()
    pre=0
    for rea in range(-300,300,pre+1):
        for ima in range(-300,300,pre+1):
            z=complex(rea/150,ima/150)
            nb=julia(z,c)
            trace(z,nb)
            
def colorisation(nombre):
    coul=(min(54+nombre*20,254),0,min(abs(254-nombre*20),254))
    coul = str('#%02x%02x%02x' % coul)
    return coul
def trace(z,nb):
    z=z*149 # homothétie 
    z=complex(z.real,-z.imag)+complex(500,300) # complex(500,300) pour centrer la fractale
    if nb == -1 : couleur= "Black"
    else: couleur=colorisation(nb)
    toile.create_rectangle(round((z.real)+pre,0),round(z.imag + pre , 0),round(int(z.real)-pre,0),round(int(z.imag))-pre,fill=couleur,width=0)


def julia(z,c):
    Un = z
    for loop in range(100):
        Un = Un**2+c
        if abs(Un) > 2 :
            return loop
            break
    if abs(Un) <= 2 : return -1

fenetre = Tk()
fenetre.title("TIPE")
toile = Canvas(fenetre, width=1000, height=600, background='white')
ac=DoubleVar()
ab=DoubleVar()
c=complex(110,110)
Label(fenetre,text='parti réel de C').pack()
scaleac = Scale(fenetre,from_=-2, to=2,resolution=0.01,bg="brown",orient=HORIZONTAL,width=10,variable=ac).pack()
Label(fenetre,text='parti imaginaire de C').pack()
scaleab = Scale(fenetre,from_=-2, to=2,resolution=0.01,bg="brown",orient=HORIZONTAL,width=10,variable=ab).pack()
boutstart=Button(fenetre,text="Commencer",command=lambda: start(c)).pack(side=TOP)
#defiler=Button(fenetre,text="Commencer le défillement",command=lambda: defile()).pack(side=TOP)
bouton = Checkbutton(fenetre, text="Update continu ?")
bouton.pack()
toile.pack()
fenetre.mainloop()
