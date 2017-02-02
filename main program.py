from tkinter import *

""" def defile():
    for ca in range(-50,50,10):
        for cb in range(-50,50,10):
            cc=complex(ca/100,cb/100)
            fenetre.after(1,start(cc))
            toile.update_idletasks"""
def start(c):
    toile.delete(ALL)
    # if c != complex(0,0):
    c=complex(ac.get(),ab.get())
    print(c)
    for rea in range(-200,200,3):
        for ima in range(-200,200,3):
            z=complex(rea/100,ima/100)
            julia(z,c)
            
def julia(z,c):
    Un = z
    for loop in range(10):
        Un = Un**2+c
        if abs(Un)>3:break
    if abs(Un)<1:
        z=z*100+complex(500,500)
        toile.create_oval(int(z.real)-2,int(z.imag)-2,int(z.real)+2,int(z.imag)+2,fill='black')
        
fenetre = Tk()
fenetre.title("TIPE")
toile = Canvas(fenetre, width=1000, height=1000, background='white')
ac=DoubleVar()
ab=DoubleVar()
c=complex(0,0)
Label(fenetre,text='parti réel de C').pack()
scaleac = Scale(fenetre,from_=-1, to=1,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ac).pack()
Label(fenetre,text='parti imaginaire de C').pack()
scaleab = Scale(fenetre,from_=-1, to=1,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ab).pack()
boutstart=Button(fenetre,text="Commencer",command=lambda: start(c)).pack(side=TOP)
#defiler=Button(fenetre,text="Commencer le défillement",command=lambda: defile()).pack(side=TOP)
toile.pack()
fenetre.mainloop()
