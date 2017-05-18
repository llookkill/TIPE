from tkinter import * #importation du module graphique

def start(c): #définition de la fonction qui va initialisé 
    global precision #on définit la variable precision qui va définir la précision de la fractale
    toile.delete(ALL) #on supprime la fractale d'avant
    c=complex(ac.get(),ab.get())# on va chercher la variable c  
    toile.create_text(950,50,text="C = {} + {}i".format(c.real,c.imag)) #on ajoute un texte en haut a droite pour afficher la valeur de c
    toile.update()#on rafraichit le canvas pour afficher le texte
    precision=preci.get()# on va chercher la variable precision
    pourcentage=0
    
    #içi l'on va chercher chaque pixel dans la toile , ils correspondent a un nombre complexe (ordonnée = partie imaginaire ,abscisse = partie réel)  
    for rea in range(-300,300,precision+1): # pour chaque abscisse  
        for ima in range(-300,300,precision+1): #pour chaque ordonnée 
            z=complex(rea/150,ima/150) #on va associé un nombre complexe
            nb=julia(z,c) #grâce à la fonction julia, on voit si ce nombre complexe est dans l'ensemble de julia ou sinon l'on renvoie sous forme d'un nombre réel sa tendance a divergé, c'est a dire sa tendance a s'éloigné de l'ensemble de julia
            trace(z,nb) #on colorie le pixel en fonctiondu nombre renvoyé
            if enable.get(): # si on veut le rafraichissement en continu 
                toile.update() # on rafraichit la toile
        if rea % 60 == 0: #on écrit le pourcentage effectué pour avoir un suivit
            print(int((rea+300)/600)+pourcentage,"%")
            pourcentage+=10
    toile.update()# à la fin quand tout les pixel sont près a être affiché, on rafraichit la toile
    print("100 %")
def julia(z,c): #la fonction julia qui va définir si le complexe est dans l'ensemble ou non
    Un = z #on initialise la suite Un 
    for loop in range(301): # on va procédé à 301 itérations
        Un = Un**2+c # on va au terme suivant de la suite Un
        if abs(Un) > 2 : # si Un a une valeur absolue trop élévé (s'il sort d'un périmêtre de sécurité définit par 2) alors la série somme de Un^2 +c diverge et donc n'est pas dans l'ensemble de julia
            return loop # on retourne a quel ittération il sort de ce " périmètre de sécurité "
            break # on sort de la boucle
    if abs(Un) <= 2 : return -1 # si à la fin des 301 itérations la valeur absolue de Un est toujours inférieur a 2 alors l'on considère que le complexe est dans l'ensemble de julia (on renvoie -1 comme nombre)

def colorisation(nombre): # la fonction qui va associé une couleur au nombre s'il n'est pas dans l'ensemble de julia
    coul=(min(54+nombre*20,254),0,min(abs(254-nombre*20),254)) # on définit sa couleur en code RGB 
    coul = str('#%02x%02x%02x' % coul) # que l'on convertit en code Hexa pour le module graphique
    return coul # on retourne la couleur

def trace(z,nb): # la fonction qui va appliqué la couleur du pixel en fonction du complexe 
    z=z*149 # homothétie (içi on multiplie par 149 et non par 150 comme l'on l'avont fait l'or de la ligne 14 ( "z=complex(rea/150,ima/150)" ) car l'ors que l'on fait les calculs ont arrondit pour redonner des entier pour les pixels ( on ne peut pas dire au pixel 5,6 met toi en vert ) du coup il faut rétrécire à peine l'homothétie pour que chaque pixel ai une couleur  
    z=complex(z.real,-z.imag)+complex(500,300) # on ajoute le complex(500,300) (qui correspond au milleu de la toile) pour centrer la fractale
    if nb == -1 : couleur= "Black" # si le complexe est dans l'ensemble de julia on le colorie en noir
    else: couleur=colorisation(nb) # sinon on utilise la fonction colorisation 
    toile.create_rectangle(round((z.real)+precision,0),round(z.imag +precision,0),round(int(z.real)-precision,0),round(int(z.imag))-precision,fill=couleur,width=0) # on applique enfin la couleur au pixel correspondant 
    


fenetre = Tk() #création de la fenêtre
fenetre.title("TIPE Ensemble de Julia") #nom de la fenêtre
toile = Canvas(fenetre, width=1000, height=600, background='white') # on crée le canvas 
ac=DoubleVar() #on définit les variables qui vont aller dans les scale ( curseur )
ab=DoubleVar()
preci=IntVar()
enable = IntVar()
c=complex(0,0)# de base c = 0+0i

#definition des boutons etc..
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=TOP)
Frame2 = Frame(Frame1, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT)
Frame3 = Frame(Frame1, borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT)
Frame4 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame4.pack()

Label(Frame2,text='parti réel de C').pack(side=TOP)
scaleac = Scale(Frame2,from_=-2, to=2,resolution=0.01,bg="brown",orient=HORIZONTAL,width=10,variable=ac).pack()

Label(Frame3,text='parti imaginaire de C').pack(side=TOP)
scaleab = Scale(Frame3,from_=-2, to=2,resolution=0.01,bg="brown",orient=HORIZONTAL,width=10,variable=ab).pack(side=RIGHT)

Label(Frame4,text='précision').pack(side=TOP)
scalepre = Scale(Frame4,from_=0, to=5,resolution=1,bg="gold",orient=HORIZONTAL,width=3,variable=preci).pack()

boutstart=Button(fenetre,text="Commencer",bg="green",command=lambda: start(c)).pack(side=TOP)
bouton = Checkbutton(fenetre,variable=enable, text=" Rafraichissement en continu ")
bouton.pack()
toile.pack()
fenetre.mainloop()
