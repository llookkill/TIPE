from tkinter import *
import random
from math import *
import time
dir(random)
class Meca(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Mécanique des foules")
        self.can1 = Canvas(self,bg='white',cursor="crosshair",height=600,width=900)
        self.can1.pack(side=LEFT)
        self.can1.create_rectangle(250,50,850,550,width=1,fill="black")
        self.can1.create_rectangle(252,52,848,548,width=1,fill="white")
        self.COULEURS = ['medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10','gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37','gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47','gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56','gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65','gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74','gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83','gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92','gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
        self.bou2 = Button(self,text='commencer',font="Arial 24 italic",bg="green",cursor="star",relief=RAISED,command=self.testdep)
        self.bou3 = Button(self,text='créer un rectangle "obstacle"',font="Arial 12 italic",cursor="dotbox",bg="grey",relief=RAISED,command=self.creer_car)
        self.bou6 = Button(self,text='créer un cercle "obstacle"',font="Arial 12 italic",cursor="circle",bg="grey",relief=RAISED,command=self.creer_obser)
        self.bou4 = Button(self,text='créer une "personne" ',font="Arial 12 italic",cursor="circle",bg="indian red",relief=RAISED,command=self.creer_cerr)
        self.bout44 = Button(self,text='créer une porte ronde ',font="Arial 12 italic",relief=RAISED,cursor="circle",bg='light blue',command=self.creer_porte_ronde)
        self.bout55 = Button(self,text='créer une porte rectangulaire ',font="Arial 12 italic",cursor="dotbox",bg='light blue',relief=RAISED,command=self.creer_porte_rec)
        self.bou5 = Button(self,text='TOUT RESET ',font="Arial 14 italic",bg='red',cursor="X_cursor",relief=RAISED,command=self.reset_tout)
        self.mvp = 0
        self.valeurr = IntVar()
        self.accealea= IntVar()
        self.aléavit = IntVar()
        self.tout = LabelFrame(self, text="Options suplémentaires")
        self.l = LabelFrame(self.tout, text="Présélection :")
        self.l2 = LabelFrame(self.tout, text="insertion aléatoire")
        self.l3 = LabelFrame(self.tout,text="vitesse aléatoire")
        self.l4 = LabelFrame(self.tout,text="accélération aléatoire")
        self.labelletlabète =Label(self.l4,text="accélaration aléatoire max  (en %) :",font="Arial 8 italic").pack(side=TOP)
        self.labelle =Label(self.l2,text="Nombre de personnes:",font="Arial 8 italic")
        self.labelabeille =Label(self.l3,text=" vitesse aléatoire max  (en %) :",font="Arial 8 italic")
        self.leboutontrèsbon = Scale(self.l3,from_=0, to=100,bg="indian red",orient=HORIZONTAL,width=15,variable=self.aléavit)
        self.lejambon = Scale(self.l4,from_=0, to=100,bg="indian red",orient=HORIZONTAL,width=15,variable=self.accealea).pack(side=TOP)
        self.rozone = Button(self.l2,text="zone d'apparition",font="Arial 10 italic",bg='gold',cursor="pencil",relief=RAISED,command=self.ozone)
        self.gen = Button(self.l2,text="générer les personnes",font="Arial 10 italic",bg='indian red',relief=RAISED,command=self.générer)
        self.valeurrr =0
        self.presel = 0
        self.couleurcer=[]
        self.bouton1 = Button(self.l, text='présélection "Vide"',command=self.defpresel0)
        self.bouton2 = Button(self.l, text="présélection n°1",command=self.defpresel1)
        self.bouton3 = Button(self.l, text="présélection quai de métro",command=self.defpresel2)
        self.boutonledaron = Button(self.l, text="activer les trajectoires",bg='pink',command=self.active_trajet)
        self.boutonledaronne = Button(self.l, text="désactiver les trajectoires",bg='pink',command=self.desa_trajet)
        self.quezak = Button(self.l,text='quadrillage',font="Arial 10 italic",bg="grey",relief=RAISED,command=self.quadrillage)
        self.labelle.pack(side=TOP)
        self.bouton1.pack(side=TOP)
        self.bouton2.pack(side=TOP)

        self.boutonledaron.pack(side=TOP)
        self.boutonledaronne.pack(side=TOP)
        self.quezak.pack(side=TOP)
        self.tout.pack(fill="both", expand="yes",side=RIGHT)
        self.l.pack(fill="both", expand="yes",side=TOP)
        self.l2.pack(fill="both", expand="yes",side=TOP)
        self.l3.pack(fill="both", expand="yes",side=TOP)
        self.l4.pack(fill="both", expand="yes",side=TOP)
        self.scale = Scale(self.l2,from_=1, to=200,bg="indian red",orient=HORIZONTAL,width=30,variable=self.valeurr)
        self.scale.pack(side=TOP)
        self.labelabeille.pack(side=TOP)
        self.leboutontrèsbon.pack(side=TOP)
        self.bou2.pack(pady=3,side=TOP)
        self.bou3.pack(pady=3,side=TOP)
        self.bou6.pack(pady=3,side=TOP)
        self.bou4.pack(pady=3,side=TOP)
        self.bout44.pack(pady=3,side=TOP)
        self.bout55.pack(pady=3,side=TOP)
        self.gen.pack(side=TOP)
        self.rozone.pack(side=TOP)
        self.bou5.pack(pady=3,side=BOTTOM)
        self.labtaille=Label(self, text="Taille des personnes en pixel",bg="white").pack(pady=6,side=TOP)
        self.value=IntVar()
        self.entree = Entry(self, textvariable=self.value, width=10)
        self.entree.pack()
        self.taille=6
        self.bou55 = Button(self,text='Valider',font="Arial 12 italic",relief=RAISED,bg="green",cursor="pencil",command=self.valide).pack(pady=3,side=TOP)
        self.x=[]
        self.ycercle2 = 0
        self.y=[]
        self.cercle=[]
        self.e=0
        self.tre=[]
        self.vitxact=[]
        self.vityact=[]
        self.toutou = False
        self.Vitymax=[]
        self.Vitxmax=[]
        self.compteurre = 0
        self.trajetx=0
        self.testariv=[]
        self.trajety=0
        self.obje=0
        self.aleax=0
        self.aleay=0
        self.xobjectif = []
        self.yobjectif= []
        self.xnewob = 0
        self.departtest = 0
        self.ynewob = 0
        self.intense=6
        self.car = 0
        self.testt=1
        self.depart=[]
        self.xcarre1=[]
        self.ycarre1=[]
        self.xcarre2=[]
        self.ycarre2=[]
        self.xcercle1=[]
        self.ycercle1=[]
        self.accelerate = []
        self.compt2=0
        self.compt = 0
        self.coefdir = 0
        self.halo=0
        self.creer_cer = 1
        self.dist = []
        self.xcarmin=0
        self.xcarmax=0
        self.ycarmin=0
        self.ycarmax=0
        self.end=0
        self.debut=0
        self.copp=0
        self.total = 0
        self.fin = 0
        self.prout = 0
        self.temps = 0
        self.timereal=0
        self.rt=0
        self.first=0
        self.xcercle2 = 0
        self.testt2=1
        self.xor = 0
        self.objectifportex1= 0
        self.objectifportey1= 0
        self.hoodor = 0
        self.objectifportex2=0
        self.objectifportey2=0
        self.can1.bind("<Button-1>",self.creer_cercle)
        self.objectifxmax= 0
        self.objectifxmin = 0
        self.objectifymax = 0
        self.objectifymin = 0
        self.xavant =[]
        self.yavant=[]
        self.quadri=0
        self.quadro=0
        self.ob = 0
        self.see = 0
        self.compt3 = 0
        self.testo = 0
    def reset_tout(self):
        self.depart=[]
        self.can1.delete(ALL)
        self.can1.create_rectangle(250,50,850,550,width=1,fill="black")
        self.can1.create_rectangle(252,52,848,548,width=1,fill="white")
        self.xcercle1=[]
        self.ycercle1=[]
        self.compt2=0
        self.compt3 = 0
        self.couleurcer=[]
        self.x=[]
        self.vitxact=[]
        self.vityact=[]
        self.ycercle2 = 0
        self.halo=0
        self.y=[]
        self.cercle=[]
        self.e=0
        self.bou2.config(bg="green",cursor="star")
        self.trajetx=0
        self.trajety=0
        self.Vitymax=[]
        self.Vitxmax=[]
        self.obje=0
        self.xobjectif = []
        self.yobjectif=[]
        self.car = 0
        self.testt=1
        self.total = 0
        self.xcarre1=[]
        self.ycarre1=[]
        self.xcarre2=[]
        self.ycarre2=[]
        self.testariv=[]
        self.dist = []
        self.tre = []
        self.compt = 0
        self.coefdir = 0
        self.creer_cer = 1
        self.prout = 0
        self.xcarmin=0
        self.xcarmax=0
        self.ycarmin=0
        self.ycarmax=0
        self.debut=0
        self.departtest = 0
        self.end=0
        self.toutou = False
        self.copp=0
        self.fin = 0
        self.temps = 0
        self.timereal=0
        self.rt=0
        self.xor = 0
        self.objectifportex1= 0
        self.objectifportey1= 0
        self.hoodor = 0
        self.objectifportex2=0
        self.objectifportey2=0
        self.objectifxmax= 0
        self.objectifxmin = 0
        self.objectifymax = 0
        self.objectifymin = 0
        self.accelerate = []
        if self.see == 1 :
            self.mvp=1
            self.defpresel1()
        if self.see == 2 :
            self.mvp=1
            self.defpresel2()
    def quadrillage(self):
        self.txtkt = self.can1.create_text(550, 42, text="60 cm", font="Arial 16 italic", fill="blue")
        self.txtkt2 = self.can1.create_text(242, 300, text="50 cm", font="Arial 16 italic", fill="blue",width=2)
        self.txtkt3 = self.can1.create_text(862, 300, text="4,5 cm", font="Arial 10 italic", fill="blue")
        self.quadri = 70
        self.quadro = 70
        for i in range(14):
            self.can1.create_line(self.quadri,50,self.quadro,550,dash=(2, 1, 2, 1))
            self.quadri += 60
            self.quadro += 60
        self.quadri = 50
        self.quadro = 50
        for i in range(11):
            self.can1.create_line(70,self.quadri,850,self.quadro,dash=(2, 1, 2, 1))
            self.quadri += 50
            self.quadro += 50
    def active_trajet(self):
        self.testo = 1
    def desa_trajet(self):
        self.testo = 0
    def defpresel0(self):
        self.see = 0
        self.reset_tout()
    def defpresel2(self):
        self.defpresel1()
        self.see = 2
        self.xcarre1.append(200)
        self.ycarre1.append(100)
        self.xcarre2.append(210)
        self.ycarre2.append(-200)
        self.xcarre1.append(200)
        self.ycarre1.append(500)
        self.xcarre2.append(210)
        self.ycarre2.append(2200)
        self.xcarre1.append(200)
        self.ycarre1.append(200)
        self.xcarre2.append(210)
        self.ycarre2.append(260)
        self.xcarre1.append(200)
        self.ycarre1.append(340)
        self.xcarre2.append(210)
        self.ycarre2.append(400)
        self.can1.create_rectangle(self.xcarre1[5], self.ycarre1[5],self.xcarre2[5], self.ycarre2[5], fill="grey")
        self.can1.create_rectangle(self.xcarre1[4], self.ycarre1[4],self.xcarre2[4], self.ycarre2[4], fill="grey")
        self.can1.create_rectangle(self.xcarre1[2], self.ycarre1[2],self.xcarre2[2], self.ycarre2[2], fill="grey")
        self.can1.create_rectangle(self.xcarre1[3], self.ycarre1[3],self.xcarre2[3], self.ycarre2[3], fill="grey")

    def defpresel1(self):
        self.see = 1
        if self.mvp == 0:self.reset_tout()
        else:
            self.mvp = 0
            self.xcarre1.append(850)
            self.ycarre1.append(278)
            self.xcarre2.append(1000)
            self.ycarre2.append(-2000)
            self.xcarre1.append(850)
            self.ycarre1.append(323)
            self.xcarre2.append(1000)
            self.ycarre2.append(2000)
            self.can1.create_rectangle(self.xcarre1[0], self.ycarre1[0],self.xcarre2[0], self.ycarre2[0], fill="grey")
            self.can1.create_rectangle(self.xcarre1[1], self.ycarre1[1],self.xcarre2[1], self.ycarre2[1], fill="grey")
            self.obje = 2
            self.xnewob= 880
            self.ynewob = 300
            self.objectifxmin,self.objectifxmax,self.objectifymin,self.objectifymax=880,900,278,323
            self.can1.create_rectangle(880,278,900,323, fill="blue")
    def creer_carre(self):

        if self.creer_cer == 0 :
            if self.testt==1 :
                self.xcarre1.append(self.xx)
                self.ycarre1.append(self.yy)
                self.testt= 0
            else:
                self.xcarre2.append(self.xx)
                self.ycarre2.append(self.yy)
                self.testt= 1
            self.compt = self.compt +1
            if int((self.compt)/2)-self.compt/2 == 0 and self.compt != 0:
                for loop in range (0,len(self.xcarre1)):
                    self.can1.create_rectangle(self.xcarre1[loop], self.ycarre1[loop],self.xcarre2[loop], self.ycarre2[loop], fill="grey")
        if self.creer_cer == 2:
            if self.testt2==1 :
                self.xcercle1.append(self.xx)
                self.ycercle1.append(self.yy)
                self.testt2= 0
            else:
                self.xcercle2=self.xx
                self.ycercle2=self.yy
                self.testt2= 1
            self.compt2 = self.compt2+1
            if int((self.compt2)/2)-self.compt2/2 == 0 and self.compt2 != 0:
                    self.dist.append(int(((self.xcercle1[self.xor]-self.xcercle2)**2+(self.ycercle1[self.xor]-self.ycercle2)**2)**0.5))
                    self.can1.create_oval(self.xcercle1[self.xor]-self.dist[self.xor], self.ycercle1[self.xor]-self.dist[self.xor],self.xcercle1[self.xor]+self.dist[self.xor], self.ycercle1[self.xor]+self.dist[self.xor], fill="grey")
                    self.xor= self.xor+1
        if self.creer_cer == 25 and self.compt3<2:
            if self.testt==1 :
                self.zonex1=self.xx
                self.zoney1=self.yy
                self.testt= 0
            else:
                self.zonex2=self.xx
                self.zoney2=self.yy
                self.testt= 1
            self.compt3 = self.compt3 +1
            if self.compt3 ==2:
                self.can1.create_rectangle(self.zonex1,self.zoney1,self.zonex2,self.zoney2, outline="gold",width = 3)

    def ozone(self):
        self.creer_cer=25
    def valide(self):
        self.taille=int(self.entree.get())
        for loop in range(len(self.x)):
            self.can1.coords(self.cercle[loop],self.x[loop]-self.taille, self.y[loop]-self.taille,self.x[loop]+self.taille, self.y[loop]+self.taille)
        self.can1.coords(self.ob,self.xnewob-self.taille,self.ynewob-self.taille,self.xnewob+self.taille,self.ynewob+self.taille)
    def testdep(self):
        if self.halo==0:
            for loop in range(len(self.x)):
                self.xobjectif.append(self.xnewob)
                self.yobjectif.append(self.ynewob)
                self.halo=1
        for loop in range(len(self.x)):
            self.bou2.config(bg="red",cursor="X_cursor")
            self.Vitxmax=self.Vitymax
            if self.debut == 0:
                self.debut = time.time()


            self.xavant[loop]=self.x[loop]
            self.yavant[loop]=self.y[loop]
            if not(self.x[loop] <= 0 and self.y[loop] <=21):
                if self.testo == 1:
                    self.can1.create_oval(self.x[loop],self.y[loop],self.x[loop]+1,self.y[loop]+1,fill=self.COULEURS[loop])
                for nop in range (0,len(self.x)):
                    if not(self.x[loop] == self.x[nop] or self.y[loop] == self.y[nop]) and self.x[nop]!=-2 :    #condition de départ
                        if self.xnewob>self.x[loop]:                                                            #si l'objectif est situé a droite
                            if (((self.x[loop]-self.x[nop])**2+(self.y[loop]-self.y[nop])**2)**0.5<=6*self.taille ):    #si la distance entre les 2 personnes est inférieure a 6 fois le rayon
                                 if (self.x[nop]>self.x[loop]):                                                 #si la personne est bien devant l'objectif
                                    if (self.y[loop]>self.y[nop]-self.taille and self.y[loop]<self.y[nop]+self.taille):    #si la personne est bien en face de nous
                                        self.departtest = 1                                                             #alors il ne peut pas avancer

                        if self.xnewob<=self.x[loop]:                                                                   #si l'objectif est situé a droite
                            if (((self.x[loop]-self.x[nop])**2+(self.y[loop]-self.y[nop])**2)**0.5<=6*self.taille ):
                                 if (self.x[nop]<self.x[loop]):
                                    if (self.y[loop]>self.y[nop]-self.taille and self.y[loop]<self.y[nop]+self.taille):
                                        self.departtest = 1


                if self.departtest == 0:    #si on peut démarer alors:
                    self.depart[loop]=1     #alors on dit on démare
                    self.can1.itemconfigure(self.cercle[loop], fill="red") #on change a la couleur de orange a rouge
                self.departtest=0                               #et on reset le test pour la prochaine personne

        self.move()

    def move(self):
        for loop in range(len(self.x)):
            for nop in range (0,len(self.x)):
                if (((self.x[loop]-self.x[nop])**2+(self.y[loop]-self.y[nop])**2)**0.5<=2*self.taille+1 ) and self.x[loop]>0 and self.x[nop]>0:   #si les personnes sont colés / les une dans les autres

                    if not(self.x[loop] == self.x[nop] or self.y[loop] == self.y[nop]) and self.x[nop]>0 :
                        self.rejetx = round(((abs(self.x[loop]-self.x[nop])/(abs(self.y[loop]-self.y[nop])+abs(self.x[loop]-self.x[nop])))*self.intense),0)
                        self.rejety = round(((abs(self.y[loop]-self.y[nop])/(abs(self.y[loop]-self.y[nop])+abs(self.x[loop]-self.x[nop])))*self.intense),0)
                        if self.x[loop]>self.x[nop]:self.rejetx = abs(self.rejetx)
                        else:self.rejetx=abs(self.rejetx)*-1
                        if self.y[loop]>self.y[nop]:self.rejety = abs(self.rejety)
                        else:self.rejety=abs(self.rejety)*-1
                        self.can1.coords(self.cercle[loop],self.x[loop]-self.taille+self.rejetx,self.y[loop]-self.taille+self.rejety,self.x[loop]+self.taille+self.rejetx,self.y[loop]+self.taille+self.rejety)
                        self.y[loop] =self.y[loop]+ self.rejety
                        self.x[loop] =self.x[loop]+ self.rejetx
                        self.rejetx = self.rejetx*-0.5
                        self.rejety = self.rejety*-0.5
                        self.can1.coords(self.cercle[nop],self.x[nop]-self.taille+self.rejetx,self.y[nop]-self.taille+self.rejety,self.x[nop]+self.taille+self.rejetx,self.y[nop]+self.taille+self.rejety)
                        self.x[nop]= self.x[nop]+ self.rejetx
                        self.x[nop] =self.x[nop]+ self.rejetx
                        self.depart[nop]=1
                        self.can1.itemconfigure(self.cercle[nop], fill="dark orchid")
                        self.can1.itemconfigure(self.cercle[loop], fill="dark orchid")
        if self.prout == 0:self.move2()

    def move2(self):

        for loop in range(len(self.x)):
            if self.x[loop]>0:
                for zen in range (0,len(self.xcarre2)):         #analyse trajectoire avec les rectangles :

                    if (((self.x[loop]-((self.xcarre1[zen] + self.xcarre2[zen])/2))**2+(self.y[loop]-((self.ycarre1[zen]+self.ycarre2[zen])/2))**2)**0.5)<=(((((self.xcarre1[zen] + self.xcarre2[zen])/2)-self.xcarre1[zen])**2+(((self.ycarre1[zen] + self.ycarre2[zen])/2)-self.ycarre1[zen])**2)**0.5+85):
                        if (self.xobjectif[loop]-(self.xcarre1[zen] + self.xcarre2[zen])/2) == 0 :
                            self.xobjectif[loop] = self.xobjectif[loop] +1
                        self.coefdir = float((self.yobjectif[loop]-((self.ycarre1[zen]+self.ycarre2[zen])/2))/(self.xobjectif[loop]-(self.xcarre1[zen] + self.xcarre2[zen])/2))
                        self.b = (int(self.coefdir*self.xobjectif[loop])-self.yobjectif[loop])*-1
                        if self.xcarre1[zen]>self.xcarre2[zen]:self.xcarmax,self.xcarmin = self.xcarre1[zen],self.xcarre2[zen]
                        else:self.xcarmax,self.xcarmin = self.xcarre2[zen],self.xcarre1[zen]
                        if self.ycarre1[zen]>self.ycarre2[zen]:self.ycarmax,self.ycarmin = self.ycarre1[zen],self.ycarre2[zen]
                        else:self.ycarmax,self.ycarmin = self.ycarre2[zen],self.ycarre1[zen]


                        if self.xnewob> self.xcarmax:# si objectif a droite de obstacle
                            if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.x[loop]<min(self.xcarre1[zen] , self.xcarre2[zen]) and self.y[loop]<self.ycarmax+self.taille+5 and self.y[loop]>self.ycarmin-self.taille-5:
                                self.xobjectif[loop] = min(self.xcarre1[zen] , self.xcarre2[zen])
                                self.yobjectif[loop]=min(self.ycarre1[zen],self.ycarre2[zen])-self.taille-10
                            elif self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.x[loop]<min(self.xcarre1[zen] , self.xcarre2[zen])and self.y[loop]<self.ycarmax+self.taille+5 and self.y[loop]>self.ycarmin-self.taille+5:
                                self.xobjectif[loop] = min(self.xcarre1[zen], self.xcarre2[zen])
                                self.yobjectif[loop]=max(self.ycarre1[zen],self.ycarre2[zen])+self.taille+10
                            if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.x[loop]<max(self.xcarre1[zen] , self.xcarre2[zen]) and self.x[loop]>min(self.xcarre1[zen] , self.xcarre2[zen]) and self.y[loop]<self.ycarmax+self.taille+5 and self.y[loop]>self.ycarmin-self.taille-5:
                                self.xobjectif[loop] = max(self.xcarre1[zen] , self.xcarre2[zen])
                                self.yobjectif[loop]=min(self.ycarre1[zen],self.ycarre2[zen])-self.taille-10
                            elif self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.x[loop]<max(self.xcarre1[zen] , self.xcarre2[zen])and self.x[loop]>min(self.xcarre1[zen] , self.xcarre2[zen]) and self.y[loop]<self.ycarmax+self.taille+5 and self.y[loop]>self.ycarmin-self.taille+5:
                                self.xobjectif[loop] = max(self.xcarre1[zen], self.xcarre2[zen])
                                self.yobjectif[loop]=max(self.ycarre1[zen],self.ycarre2[zen])+self.taille+10
                        if self.xnewob < self.xcarmin:# si objectif a gauche de obstacle

                            if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.x[loop]>max(self.xcarre1[zen] , self.xcarre2[zen])and self.y[loop]<self.ycarmax+self.taille+5 and self.y[loop]>self.ycarmin-self.taille-5:
                                self.xobjectif[loop] = max(self.xcarre1[zen] , self.xcarre2[zen])
                                self.yobjectif[loop]=min(self.ycarre1[zen],self.ycarre2[zen])-self.taille-10
                            elif self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.x[loop]>max(self.xcarre1[zen] , self.xcarre2[zen])and self.y[loop]<self.ycarmax+self.taille+5 and self.y[loop]>self.ycarmin-self.taille+5:
                                self.xobjectif[loop] = max(self.xcarre1[zen] , self.xcarre2[zen])
                                self.yobjectif[loop]=max(self.ycarre1[zen],self.ycarre2[zen])+self.taille+10

                        if self.xnewob >= self.xcarmin and self.xnewob <= self.xcarmax :
                            if self.ynewob > self.ycarmax: #si objectif en bas de obstacle

                                if self.xnewob>(self.xcarre1[zen] + self.xcarre2[zen])/2:
                                    if self.y[loop]> self.x[loop]*self.coefdir+self.b and self.y[loop]<((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille-5:

                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  min(self.xcarre2[zen],self.xcarre1[zen]) -self.taille-10
                                    elif self.y[loop]<= self.x[loop]*self.coefdir+self.b and self.y[loop]<((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille+5:

                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  max(self.xcarre2[zen],self.xcarre1[zen]) +self.taille+10
                                else:
                                    if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.y[loop]<((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille-5:
                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  min(self.xcarre2[zen],self.xcarre1[zen]) -self.taille-10
                                    elif self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.y[loop]<((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille+5:
                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  max(self.xcarre2[zen],self.xcarre1[zen]) +self.taille+10

                            if self.ynewob < self.ycarmin: # si objectif en haut de obstacle
                                if self.xnewob >= ((self.xcarre1[zen] + self.xcarre2[zen])/2):

                                    if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.y[loop]>((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille-5:
                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  min(self.xcarre2[zen],self.xcarre1[zen]) -self.taille-10
                                    elif self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.y[loop]>((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille+5:
                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  max(self.xcarre2[zen],self.xcarre1[zen]) +self.taille+10
                                else :

                                    if self.y[loop]> self.x[loop]*self.coefdir+self.b and self.y[loop]>((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille-5:
                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  min(self.xcarre2[zen],self.xcarre1[zen]) -self.taille-10
                                    elif self.y[loop]<= self.x[loop]*self.coefdir+self.b and self.y[loop]>((self.ycarre1[zen] + self.ycarre2[zen])/2)and self.x[loop]<self.xcarmax+self.taille+5 and self.x[loop]>self.xcarmin-self.taille+5:
                                        self.yobjectif[loop] = ((self.ycarre1[zen] + self.ycarre2[zen])/2)
                                        self.xobjectif[loop]=  max(self.xcarre2[zen],self.xcarre1[zen]) +self.taille+10

                for mix in range (0,len(self.dist)):        #analyse trajectoire avec le cercle
                    if (((self.x[loop]-self.xcercle1[mix])**2+(self.y[loop]-self.ycercle1[mix])**2)**0.5)<=(self.dist[mix]+100):
                        self.coefdir = round(((self.ynewob-self.ycercle1[mix])/(self.xnewob-self.xcercle1[mix])),3)
                        self.b = (int(self.coefdir*self.xobjectif[loop])-self.yobjectif[loop])*-1
                        if self.xnewob> self.xcercle1[mix]:
                            if self.y[loop]<(self.x[loop]*self.coefdir+self.b) and self.x[loop]<self.xcercle1[mix] and self.y[loop]<self.ycercle1[mix]+self.dist[mix]+self.taille+5 and self.y[loop]>self.ycercle1[mix]-self.dist[mix]-self.taille-5:
                                self.xobjectif[loop] = self.xcercle1[mix]
                                self.yobjectif[loop]=  self.ycercle1[mix] -self.dist[mix] -self.taille-10
                            if self.y[loop]>=(self.x[loop]*self.coefdir+self.b) and self.x[loop]<self.xcercle1[mix] and self.y[loop]<self.ycercle1[mix]+self.dist[mix]+self.taille+5 and self.y[loop]>self.ycercle1[mix]-self.dist[mix]-self.taille+5:
                                self.xobjectif[loop] = self.xcercle1[mix]
                                self.yobjectif[loop]=  self.ycercle1[mix] +self.dist[mix] +self.taille+10
                        if self.xnewob< self.xcercle1[mix]:
                            if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.x[loop]>self.xcercle1[mix] and self.y[loop]<self.ycercle1[mix]+self.dist[mix]+self.taille+5 and self.y[loop]>self.ycercle1[mix]-self.dist[mix]-self.taille-5:
                                self.xobjectif[loop] = self.xcercle1[mix]
                                self.yobjectif[loop]=  self.ycercle1[mix] -self.dist[mix] -self.taille-10
                            if self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.x[loop]>self.xcercle1[mix] and self.y[loop]<self.ycercle1[mix]+self.dist[mix]+self.taille+5 and self.y[loop]>self.ycercle1[mix]-self.dist[mix]-self.taille+5:
                                self.xobjectif[loop] = self.xcercle1[mix]
                                self.yobjectif[loop]=  self.ycercle1[mix] +self.dist[mix] +self.taille+10
                        if self.xnewob >= self.xcercle1[mix]-self.dist[mix] and self.xnewob <= self.xcercle1[mix]+self.dist[mix] :
                            if self.ynewob > self.ycercle1[mix]+self.dist[mix]:
                                if self.xnewob>self.xcercle1[mix]:
                                    if self.y[loop]> self.x[loop]*self.coefdir+self.b and self.y[loop]<self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille-5:
                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]-self.dist[mix] -self.taille-10

                                    elif self.y[loop]<= self.x[loop]*self.coefdir+self.b and self.y[loop]<self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille+5:

                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]+self.dist[mix] +self.taille+10
                                else:
                                    if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.y[loop]<self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille-5:
                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]-self.dist[mix] -self.taille-10

                                    elif self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.y[loop]<self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille+5:

                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]+self.dist[mix] +self.taille+10
                            if  self.ynewob <= self.ycercle1[mix]-self.dist[mix]:
                                if self.xnewob>self.xcercle1[mix]:
                                    if self.y[loop]< self.x[loop]*self.coefdir+self.b and self.y[loop]>self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille-5:
                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]-self.dist[mix] -self.taille-10

                                    elif self.y[loop]>= self.x[loop]*self.coefdir+self.b and self.y[loop]>self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille+5:

                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]+self.dist[mix] +self.taille+10
                                else:
                                    if self.y[loop]> self.x[loop]*self.coefdir+self.b and self.y[loop]>self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille-5:
                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]-self.dist[mix] -self.taille-10

                                    elif self.y[loop]<= self.x[loop]*self.coefdir+self.b and self.y[loop]>self.ycercle1[mix] and self.x[loop]<self.xcercle1[mix]+self.dist[mix]+self.taille+5 and self.x[loop]>self.xcercle1[mix]-self.dist[mix]-self.taille+5:

                                        self.yobjectif[loop] = self.ycercle1[mix]
                                        self.xobjectif[loop]=  self.xcercle1[mix]+self.dist[mix] +self.taille+10
        if self.prout == 0:self.collision()
    def collision(self):
        for loop in range(len(self.x)):
            if self.x[loop]>0:
                for zen in range (0,len(self.xcarre2)):
                    if self.xcarre1[zen]>self.xcarre2[zen]:self.xcarmax,self.xcarmin = self.xcarre1[zen],self.xcarre2[zen]
                    else:self.xcarmax,self.xcarmin = self.xcarre2[zen],self.xcarre1[zen]
                    if self.ycarre1[zen]>self.ycarre2[zen]:self.ycarmax,self.ycarmin = self.ycarre1[zen],self.ycarre2[zen]
                    else:self.ycarmax,self.ycarmin = self.ycarre2[zen],self.ycarre1[zen]
                    self.compteurre = 0 #si la personne est dans le rectangle alors :
                    while self.x[loop]>=(self.xcarmin-self.taille) and self.x[loop] <= (self.xcarmax +self.taille)and self.y[loop] >= self.ycarmin-self.taille and self.y[loop] <= self.ycarmax+self.taille and self.compteurre<= self.taille:
                        if self.x[loop]>=(self.xcarmin-self.taille) and self.x[loop]<= ((self.xcarre1[zen] + self.xcarre2[zen])/2):
                            self.can1.coords(self.cercle[loop],self.x[loop]-self.taille-self.vitxact[loop],self.y[loop]-self.taille,self.x[loop]+self.taille-self.vitxact[loop],self.y[loop]+self.taille)
                            self.x[loop]=self.x[loop]-abs(self.vitxact[loop])


                        if self.x[loop]<=(self.xcarmax+self.taille) and self.x[loop]>= ((self.xcarre1[zen] + self.xcarre2[zen])/2):
                            self.can1.coords(self.cercle[loop],self.x[loop]-self.taille+self.vitxact[loop],self.y[loop]-self.taille,self.x[loop]+self.taille+self.vitxact[loop],self.y[loop]+self.taille)
                            self.x[loop]=self.x[loop]+abs(self.vitxact[loop])


                        if self.y[loop]<=(self.ycarmax+self.taille) and self.y[loop]>= ((self.ycarre1[zen] + self.ycarre2[zen])/2):
                            self.can1.coords(self.cercle[loop],self.x[loop]-self.taille,self.y[loop]-self.taille+self.vityact[loop],self.x[loop]+self.taille,self.y[loop]+self.taille+self.vityact[loop])
                            self.y[loop]=self.y[loop]+abs(self.vityact[loop])


                        if self.y[loop]>=(self.ycarmin-self.taille) and self.y[loop]<= ((self.ycarre1[zen] + self.ycarre2[zen])/2):
                            self.can1.coords(self.cercle[loop],self.x[loop]-self.taille,self.y[loop]-self.taille-self.vityact[loop],self.x[loop]+self.taille,self.y[loop]+self.taille-self.vityact[loop])
                            self.y[loop]=self.y[loop]-abs(self.vityact[loop])
                        self.compteurre = self.compteurre +1


                self.compteurre = 0
                for mix in range (0,len(self.dist)):
                    #analyse collisions avec le cercle
                    while (((self.x[loop]-self.xcercle1[mix])**2+(self.y[loop]-self.ycercle1[mix])**2)**0.5)<=(self.dist[mix]+self.taille) and self.compteurre < self.taille:
                        self.rejetx = int((abs(self.x[loop]-self.xcercle1[mix])/(abs(self.y[loop]-self.ycercle1[mix])+abs(self.x[loop]-self.xcercle1[mix])))*self.intense)
                        self.rejety = int((abs(self.y[loop]-self.ycercle1[mix])/(abs(self.y[loop]-self.ycercle1[mix])+abs(self.x[loop]-self.xcercle1[mix])))*self.intense)
                        if self.x[loop]>self.xcercle1[mix]:self.rejetx = abs(self.rejetx)
                        else:self.rejetx=abs(self.rejetx)*-1
                        if self.y[loop]>self.ycercle1[mix]:self.rejety = abs(self.rejety)
                        else:self.rejety=abs(self.rejety)*-1

                        self.can1.coords(self.cercle[loop],self.x[loop]-self.taille+self.rejetx,self.y[loop]-self.taille+self.rejety,self.x[loop]+self.taille+self.rejetx,self.y[loop]+self.taille+self.rejety)
                        self.y[loop] =self.y[loop]+ self.rejety
                        self.x[loop] =self.x[loop]+ self.rejetx
                        self.compteurre = self.compteurre +1
        if self.prout == 0:self.trajet()
    def trajet(self):
        for loop in range(len(self.x)):
            self.can1.create_oval(self.xobjectif[loop]-1,self.yobjectif[loop]-1,self.xobjectif[loop]+1,self.yobjectif[loop]+1,fill="green")
            if self.depart[loop]==1:    #si la personnes peut démarer alors :
                if not(self.x[loop] <= 0 and self.y[loop] <=1):
                    if self.x[loop] == self.xobjectif[loop] and self.y[loop] == self.yobjectif[loop] :
                        self.xobjectif[loop] = self.xobjectif[loop] + 1
                    self.trajetx =round(((abs(self.x[loop]-self.xobjectif[loop])/(abs(self.y[loop]-self.yobjectif[loop])+abs(self.x[loop]-self.xobjectif[loop])))*self.vitxact[loop]),0)
                    self.trajety =round(((abs(self.y[loop]-self.yobjectif[loop])/(abs(self.y[loop]-self.yobjectif[loop])+abs(self.x[loop]-self.xobjectif[loop])))*self.vityact[loop]),0)
                    if self.x[loop]>self.xobjectif[loop]:self.trajetx = abs(self.trajetx)*-1
                    else:self.trajetx=abs(self.trajetx)
                    if self.y[loop]>self.yobjectif[loop]:self.trajety = abs(self.trajety)*-1
                    else:self.trajety=abs(self.trajety)
                    self.can1.coords(self.cercle[loop],self.x[loop]-self.taille+self.trajetx,self.y[loop]-self.taille+self.trajety,self.x[loop]+self.taille+self.trajetx,self.y[loop]+self.taille+self.trajety)
                    self.y[loop] =self.y[loop]+ self.trajety
                    self.x[loop] =self.x[loop]+ self.trajetx
                    self.can1.itemconfigure(self.cercle[loop], fill="red")
                    if self.testo == 1:
                        self.can1.create_line(self.x[loop],self.y[loop],self.xavant[loop],self.yavant[loop],fill=self.COULEURS[self.couleurcer[loop]],width=2)





            if self.obje == 1:
                if  (((self.x[loop]-self.xnewob)**2+(self.y[loop]-self.ynewob)**2)**0.5 <= 2*self.taille ):
                    self.can1.coords(self.cercle[loop],-20,-20,-20,-20)
                    self.x[loop]=-20
                    self.y[loop]=-20
            else :
                if (self.x[loop]<self.objectifxmax+self.taille and self.x[loop]>self.objectifxmin-self.taille and self.y[loop]<self.objectifymax+self.taille and self.y[loop] > self.objectifymin-self.taille):
                    self.can1.coords(self.cercle[loop],-20,-20,-20,-20)
                    self.x[loop]=-20
                    self.y[loop]=-20
            if self.vitxact[loop]<self.Vitxmax[loop]:self.vitxact[loop]=self.vitxact[loop]+round(self.accelerate[loop],0)
            if self.vityact[loop]<self.Vitymax[loop]:self.vityact[loop]=self.vityact[loop]+round(self.accelerate[loop],0)
        for loop in range(len(self.x)):
            self.xobjectif[loop] = self.xnewob
            self.yobjectif[loop] = self.ynewob
        self.traji()
    def traji(self):
        self.prout = 1
        for loop in range(floor(log(int(len(self.x)-int((len(self.can1.find('enclosed', -30, -30, -10, -10)))-3))))):
            self.move()
            self.collision()
        self.prout = 0
        self.endi()
    def endi(self):

        for hi in range (0,len(self.x)):    #test si toute les personnes sont arrivé
            self.copp = self.copp + self.x[hi]
        if self.copp == len(self.x)*-20:
            self.rt=round(self.timereal/1000,4)
            self.fin = 1
            self.end = time.time()
            self.temps = round((self.end-self.debut),4)
            if self.first == 0 :
                self.first = self.first+ 1
                self.Frame1 = Frame(self, borderwidth=2, relief=GROOVE)
                self.Frame1.pack(side=TOP, padx=1, pady=1)
                self.Frame3 = Frame(self.Frame1, bg="light grey", borderwidth=2, relief=GROOVE)
                self.Frame3.pack(side=RIGHT, padx=1, pady=1)
                self.label=Label(self.Frame1, text="TEMPS :").pack()
                self.label2=Label(self.Frame3, text=self.temps,bg="white").pack()
                self.Frame11 = Frame(self, borderwidth=2, relief=GROOVE)
                self.Frame11.pack(side=TOP, padx=1, pady=1)
                self.Frame33 = Frame(self.Frame11, bg="light grey", borderwidth=2, relief=GROOVE)
                self.Frame33.pack(side=RIGHT, padx=1, pady=1)
                self.label1=Label(self.Frame11, text="TEMPS REEL :").pack()
                self.label22=Label(self.Frame33, text=self.rt,bg="white").pack()
                self.Frame111 = Frame(self, borderwidth=2, relief=GROOVE)
                self.Frame111.pack(side=TOP, padx=1, pady=1)
                self.Frame333 = Frame(self.Frame11, bg="light grey", borderwidth=2, relief=GROOVE)
                self.Frame333.pack(side=RIGHT, padx=1, pady=1)
                self.label1=Label(self.Frame11, text="Nombre de personnes :").pack()
                self.label22=Label(self.Frame33, text=len(self.x),bg="white").pack()
            else:
                self.Frame1.destroy()
                self.Frame111.destroy()
                self.Frame333.destroy()
                self.Frame11.destroy()
                self.Frame3.destroy()
                self.Frame33.destroy()
                self.Frame1 = Frame(self, borderwidth=2, relief=GROOVE)
                self.Frame1.pack(side=TOP, padx=1, pady=1)
                self.Frame3 = Frame(self.Frame1, bg="light grey", borderwidth=2, relief=GROOVE)
                self.Frame3.pack(side=RIGHT, padx=1, pady=1)
                self.label=Label(self.Frame1, text="TEMPS :").pack()
                self.label2=Label(self.Frame3, text=self.temps,bg="white").pack()
                self.Frame11 = Frame(self, borderwidth=2, relief=GROOVE)
                self.Frame11.pack(side=TOP, padx=1, pady=1)
                self.Frame33 = Frame(self.Frame11, bg="light grey", borderwidth=2, relief=GROOVE)
                self.Frame33.pack(side=RIGHT, padx=1, pady=1)
                self.label1=Label(self.Frame11, text="TEMPS REEL :").pack()
                self.label22=Label(self.Frame33, text=self.rt,bg="white").pack()
                self.Frame111 = Frame(self, borderwidth=2, relief=GROOVE)
                self.Frame111.pack(side=TOP, padx=1, pady=1)
                self.Frame333 = Frame(self.Frame11, bg="light grey", borderwidth=2, relief=GROOVE)
                self.Frame333.pack(side=RIGHT, padx=1, pady=1)
                self.label1=Label(self.Frame11, text="Nombre de personnes :").pack()
                self.label22=Label(self.Frame33, text=len(self.x),bg="white").pack()
        if self.fin==0:
            self.after(1,self.testdep)
            self.timereal=self.timereal+1
        self.copp = 0
    def creer_obser(self):
        self.creer_cer = 2
    def creer_car(self):
        self.creer_cer = 0
    def creer_cerr(self):
        self.creer_cer = 1
    def creer_porte_rec(self):
        self.creer_cer = 12
    def creer_porte_ronde(self):
        self.creer_cer = 10
    def générer(self):
        self.valeurrr=int(self.valeurr.get())
        self.compt55 = 0
        while len(self.x)<int(self.valeurrr) and self.compt55<2000:
            self.aleax=random.randrange(min(self.zonex1,self.zonex2)+self.taille,max(self.zonex1,self.zonex2)-self.taille,1)
            self.aleay=random.randrange(min(self.zoney1,self.zoney2)+self.taille,max(self.zoney1,self.zoney2)-self.taille,1)
            for loop in range(len(self.y)):
                    if (((self.x[loop]-self.aleax)**2+(self.y[loop]-self.aleay)**2)**0.5<=2*self.taille+5):
                        self.e = 1
                        break
            if self.e != 1 :
                self.couleurcer.append(random.randrange(0,len(self.COULEURS)))
                self.x.append(self.aleax)
                self.y.append(self.aleay)
                self.tre.append(0)
                self.xobjectif.append(self.xnewob)
                self.yobjectif.append(self.ynewob)
                self.xavant.append(0)
                self.testariv.append(0)
                self.yavant.append(0)
                if self.aléavit.get()!=0:self.Vitymax.append(round(4+0.05*(random.randrange(0,self.aléavit.get())),0))
                else:self.Vitymax.append(4)
                if self.accealea.get()!=0:self.accelerate.append(round(1+0.01*(random.randrange(0,self.accealea.get())),2))
                else:self.accelerate.append(1)
                self.vitxact.append(0)
                self.vityact.append(0)
                self.depart.append(0)
                self.procura = self.can1.create_oval(self.aleax-self.taille, self.aleay-self.taille,self.aleax+self.taille,self.aleay+self.taille, fill="orange")
                self.cercle.append(self.procura)
            self.e = 0
            self.compt55 = self.compt55 +1
    def creer_cercle(self, event):
        global xx,yy
        self.xx=event.x
        self.yy=event.y
        if self.creer_cer ==1:
            xx=event.x
            yy=event.y
            for loop in range (0,len(self.x)):
                if (((self.x[loop]-xx)**2+(self.y[loop]-yy)**2)**0.5<=2*self.taille+10 ) or xx <= 42 or xx >= 958 or yy <=42 or yy >= 558 :
                    self.e = 1
                    break
            if self.e != 1 :
                self.couleurcer.append(random.randrange(0,len(self.COULEURS)))
                self.x.append(xx)
                self.y.append(yy)
                self.testariv.append(0)
                self.tre.append(0)
                if self.aléavit.get()!=0:self.Vitymax.append(round(5+0.05*(random.randrange(0,self.aléavit.get())),0))
                else:self.Vitymax.append(5)
                if self.accealea.get()!=0:self.accelerate.append(round(1+0.01*(random.randrange(0,self.accealea.get())),2))
                else:self.accelerate.append(1)
                self.vitxact.append(0)
                self.xavant.append(0)
                self.xobjectif.append(self.xnewob)
                self.yobjectif.append(self.ynewob)
                self.yavant.append(0)
                self.vityact.append(0)
                self.depart.append(0)
                self.procura = self.can1.create_oval(self.xx-self.taille, self.yy-self.taille,self.xx+self.taille, self.yy+self.taille, fill="orange")
                self.cercle.append(self.procura)
            self.e = 0
        if self.creer_cer == 10 and self.obje ==0 :
            self.xnewob = self.xx
            self.ynewob = self.yy
            self.ob = self.can1.create_oval(self.xx-5, self.yy-5, self.xx+5, self.yy+5, fill="blue")
            self.obje = 1
        if self.creer_cer == 12 and self.obje==0:
            if self.hoodor == 0 :
                self.objectifportex1= self.xx
                self.objectifportey1= self.yy
                self.hoodor = 1
            else:
                self.objectifportex2=self.xx
                self.objectifportey2=self.yy
                self.hoodor =0
                self.obje=2
                if self.objectifportex1>self.objectifportex2:self.objectifxmax,self.objectifxmin =self.objectifportex1,self.objectifportex2
                else:self.objectifxmax,self.objectifxmin =self.objectifportex2,self.objectifportex1
                if self.objectifportey1>self.objectifportey2:self.objectifymax,self.objectifymin =self.objectifportey1,self.objectifyporte2
                else:self.objectifymax,self.objectifymin =self.objectifportey2,self.objectifportey1
                self.xnewob=(self.objectifportex1+self.objectifportex2)/2
                self.ynewob=(self.objectifportey1+self.objectifportey2)/2
                self.can1.create_rectangle(self.objectifportex1, self.objectifportey1,self.objectifportex2, self.objectifportey2, fill="blue")
        else:
            self.creer_carre()

if __name__ == "__main__":
    fen1 = Meca()
    fen1.resizable(width=False, height=False)

    fen1.mainloop()
