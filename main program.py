from tkinter import *

def defile():
    for ca in range(int(ac.get()*100),int(ac.get()*100)+50,5):
        cc=complex(ca/100,ab.get())
        start(cc)
        toile.update()
    for ca in range(int(ac.get()*100+50),int(ac.get()*100)-50,-5):
        cc=complex(ca/100,ab.get())
        start(cc)
        toile.update()
    for ca in range(int(ac.get()*100-50),int(ac.get()*100)+5,+5):
        cc=complex(ca/100,ab.get())
        start(cc)
        toile.update()
def start(c):
    toile.delete(ALL)
    if c == complex(110,110): c=complex(ac.get(),ab.get())
    print(c)
    for rea in range(-200,200,1):
        for ima in range(-200,200,1):
            z=complex(rea/100,ima/100)
            julia(z,c)
            
def julia(z,c):
    Un = z
    for loop in range(10):
        Un = Un**2+c
        if abs(Un)>3:break
    z=z*150+complex(250,250)
    if abs(Un)<1:
        toile.create_rectangle(round((z.real),0),round(int(z.imag)),int(z.real)+1,int(z.imag)+1,fill='black',width=1)
#    if abs(Un)>3:toile.create_oval(int(z.real)-1,int(z.imag)-1,int(z.real)+1,int(z.imag)+1,fill='white',width=0)
        
fenetre = Tk()
fenetre.title("TIPE")
toile = Canvas(fenetre, width=500, height=500, background='white')
ac=DoubleVar()
ab=DoubleVar()
c=complex(110,110)
Label(fenetre,text='parti réel de C').pack()
scaleac = Scale(fenetre,from_=-1, to=1,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ac).pack()
Label(fenetre,text='parti imaginaire de C').pack()
scaleab = Scale(fenetre,from_=-1, to=1,resolution=0.01,bg="indian red",orient=HORIZONTAL,width=10,variable=ab).pack()
boutstart=Button(fenetre,text="Commencer",command=lambda: start(c)).pack(side=TOP)
defiler=Button(fenetre,text="Commencer le défillement",command=lambda: defile()).pack(side=TOP)
toile.pack()
fenetre.mainloop()
