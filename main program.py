from tkinter import *


def defile():
    cc=complex(0,0)
    for ca in range(int(ac.get()*100),int(ac.get()*100)+50,1):
        cc=complex(ca/100,ab.get())

        start(cc)
    for ca in range(int(ac.get()*100+50),int(ac.get()*100)-50,-1):
        cc=complex(ca/100,ab.get())
        start(cc)
    for ca in range(int(ac.get()*100-50),int(ac.get()*100)+5,+1
                    ):
        cc=complex(ca/100,ab.get())
        start(cc)


def start(c):
    toile.delete(ALL)
    if c == complex(110,110): c=complex(ac.get(),ab.get())
    print(c)
    toile.create_text(950,50,text="C = {} + {}i".format(c.real,c.imag))
    toile.update()

    for rea in range(-300,300,1):
        for ima in range(-300,300,1):
            z=complex(rea/150,ima/150)
            julia(z,c)

def julia(z,c):
    Un = z
    for loop in range(6):
        Un = Un**2+c
        if abs(Un)>8:break
        if abs(Un)<0.01:break
    z=z*149
    z=complex(z.real,-z.imag)+complex(500,300)
    for dist in range (100,801):
        if abs(Un)<dist/100:
            if dist > 100:coul = '#%02x%02x%02x' % (int(dist/801*256),int(dist/801*256),int(dist/801*256))
            if dist <=100:coul = "#0054A8"
            toile.create_rectangle(round((z.real),0),round(int(z.imag)),round(int(z.real),0),round(int(z.imag)),fill=coul,width=0)
            toile.update()
            break


fenetre = Tk()
fenetre.title("TIPE")
toile = Canvas(fenetre, width=1000, height=600, background='white')
ac=DoubleVar()
ab=DoubleVar()
c=complex(110,110)
Label(fenetre,text='parti réel de C').pack()
scaleac = Scale(fenetre,from_=-2, to=2,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ac).pack()
Label(fenetre,text='parti imaginaire de C').pack()
scaleab = Scale(fenetre,from_=-2, to=2,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ab).pack()
boutstart=Button(fenetre,text="Commencer",command=lambda: start(c)).pack(side=TOP)
defiler=Button(fenetre,text="Commencer le défillement",command=lambda: defile()).pack(side=TOP)
bouton = Checkbutton(fenetre, text="Update continu ?")
bouton.pack()
toile.pack()
fenetre.mainloop()
