from tkinter import *

def defile():
    cc=complex(0,0)
    #texto=StringVar()
    #texto.set(" C = {} + {}i".format(cc.real,cc.imag))
    #affiche_reel_c = Label(fenetre,textvariable=texto).pack()
    for ca in range(int(ac.get()*100),int(ac.get()*100)+50,5):
        cc=complex(ca/100,ab.get())
        start(cc)
        toile.update()
        #texto.set(" C = {} + {}i".format(cc.real,cc.imag))
        #affiche_reel_c.configure(text=texto)
    for ca in range(int(ac.get()*100+50),int(ac.get()*100)-50,-5):
        cc=complex(ca/100,ab.get())
        start(cc)
        #texto.set(" C = {} + {}i".format(cc.real,cc.imag))
        #affiche_reel_c.configure(text=texto)
    for ca in range(int(ac.get()*100-50),int(ac.get()*100)+5,+5):
        cc=complex(ca/100,ab.get())
        start(cc)
        #texto.set(" C = {} + {}i".format(cc.real,cc.imag))
        #affiche_reel_c.configure(text=texto)
def start(c):
    toile.delete(ALL)
    if c == complex(110,110): c=complex(ac.get(),ab.get())
    print(c)
    for rea in range(-300,300,1):
        for ima in range(-300,300,1):
            z=complex(rea/150,ima/150)
            julia(z,c)
            
def julia(z,c):
    Un = z
    for loop in range(20):
        Un = Un**2+c
        if abs(Un)>2:break
        if abs(Un)<0.01:break
    z=z*149
    z=complex(z.real,-z.imag)+complex(300,300)
    if abs(Un)<1:
        toile.create_rectangle(round((z.real),0),round(int(z.imag)),round(int(z.real),0),round(int(z.imag)),fill='blue',width=0)
        toile.update()
#    if abs(Un)>3:toile.create_oval(int(z.real)-1,int(z.imag)-1,int(z.real)+1,int(z.imag)+1,fill='white',width=0)
        
fenetre = Tk()
fenetre.title("TIPE")
toile = Canvas(fenetre, width=600, height=600, background='white')
ac=DoubleVar()
ab=DoubleVar()
c=complex(110,110)
Label(fenetre,text='parti réel de C').pack()
scaleac = Scale(fenetre,from_=-2, to=2,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ac).pack()
Label(fenetre,text='parti imaginaire de C').pack()
scaleab = Scale(fenetre,from_=-2, to=2,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ab).pack()
boutstart=Button(fenetre,text="Commencer",command=lambda: start(c)).pack(side=TOP)
defiler=Button(fenetre,text="Commencer le défillement",command=lambda: defile()).pack(side=TOP)
toile.pack()
fenetre.mainloop()
