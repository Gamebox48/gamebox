#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Utilisateur
#
# Created:     07/02/2020
# Copyright:   (c) Utilisateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint
from likeprocessing.processing import *
class ChampDeMines(Dialog):
    def __init__(self,parent,x,y,nb_bombes=10,nb_rows=9,nb_cols=9):
        super().__init__(parent,(x, y, 300, 400))
        self.parent=parent
        self.nb_bombes=nb_bombes
        self.nb_cols=nb_cols
        self.nb_rows=nb_rows
        self.cases=[]
        self.tour=0
        self.case_a_deminer= self.nb_rows * self.nb_cols - self.nb_bombes
        self.champ = [0 for i in range(self.nb_rows * self.nb_cols)]
        self.zone =set()
        for i in range(self.nb_rows):
            for j in range(self.nb_cols):
                self.cases.append(Bouton(self,(j*30,i*30,30,30),"",command= lambda case=i*self.nb_cols+j: self.demine(case)))
                self.addObjet(self.cases[-1])
        # self.addObjet(Bouton(self,(0,0,60,30),'Nouvelle Partie',command=self.nouvellePartie))
        self.texte=Label(self,(0,(i+1)*30,120,30),"dqdqsd")
        self.addObjet(self.texte)
        # self.addObjet(self,Bouton(self, (0,0,60,30),'Quitter', command=self.quitter))


    def init(self,sauf):
        self.champ=[0 for i in range(self.nb_rows * self.nb_cols)]
        self.zone=set()
        b=0
        while b<self.nb_bombes:
            case=randint(0, self.nb_rows * self.nb_cols - 1)
            while case==sauf:
                case=randint(0, self.nb_rows * self.nb_cols - 1)

            if self.champ[case]!=9:
                self.champ[case]=9
                b+=1
        for case in range(len(self.champ)):
            if self.champ[case]==9:
                i=case//self.nb_cols
                j=case%self.nb_cols
                i_mini=max(i-1,0)
                i_maxi=min(i + 1, self.nb_rows - 1)
                j_mini=max(j-1,0)
                j_maxi=min(j + 1, self.nb_cols - 1)
                for i in range(i_mini,i_maxi+1):
                    for j in range(j_mini,j_maxi+1):
                        if i*self.nb_cols+j!=case and self.champ[i * self.nb_cols + j]!=9:
                            self.champ[i * self.nb_cols + j]+=1

    def nouvellePartie(self):
        self.texte.config(text="")
        self.tour=0
        self.config(text="Déminé : {}/{}".format(self.case_a_deminer, self.nb_cols * self.nb_rows))
        for c in self.cases:
            c.config(text="",bg="#d9d9d9")

    def demine(self,case):
        if self.tour==0:
            self.init(case)
            self.tour =1
        if self.champ[case]==9:
            self.texte.text("vous êtes mort")
            self.cases[case].fill = rgb_color("red")
            self.afficheMines()
        elif self.champ[case]==0:
            if self.cases[case].fill != rgb_color("green"):
                self.zone=set()
                self.demineZero(case)
                z=set(self.zone)
                for c in z:
                    for v in self.voisins(c):
                        if self.cases[v].fill == (255,255,255,255):
                            self.zone.add(v)
                for c in self.zone:
                    self.afficheMine(c)
                self.case_a_deminer-=len(self.zone)
            self.cases[case].fill = rgb_color("green")
        else:
            print(self.cases[case].text())
            if self.cases[case].text() ==[""] and self.champ[case]>0:
                self.cases[case].text(str(self.champ[case]))
                self.case_a_deminer-=1
        if self.case_a_deminer==0:
            self.texte.text("vous avez gagné")
            self.afficheMines()
        self.title("Démine : {}/{}".format(self.case_a_deminer, self.nb_cols * self.nb_rows))

    def afficheMines(self):
        for c in range(self.nb_cols * self.nb_rows):
            self.afficheMine(c)

    def afficheMine(self,c):
        if self.champ[c]==9:
            self.cases[c].fill='red'
        elif self.champ[c]==0:
            self.cases[c].fill='green'
        else:
            self.cases[c].text(self.champ[c])

    def afficheVoisins(self,case):
        for v in self.voisins(case):
            if self.champ[v]==0:
                self.cases[v].fill='green'
            else:
                self.cases[v].text(self.champ[v])

    def voisins(self,case):
        voisins=set()
        i=case//self.nb_cols
        j=case%self.nb_cols
        iMini=max(i-1,0)
        iMaxi=min(i + 1, self.nb_rows - 1)
        jMini=max(j-1,0)
        jMaxi=min(j + 1, self.nb_cols - 1)
        for i in range(iMini,iMaxi+1):
            for j in range(jMini,jMaxi+1):
                if i*self.nb_cols+j!=case:
                    voisins.add(i * self.nb_cols + j)
        return voisins

    def voisinsZero(self,case):
        voisins=self.voisins(case)
        vz=set()
        for v in voisins:
            if self.champ[v]==0:
                vz.add(v)
        return vz

    def demineZero(self,case):
        if self.champ[case]==0:
            self.zone.add(case)
            vz=self.voisinsZero(case)
            vz=vz-self.zone
            for v in vz:
                self.zone.add(v)
                self.demineZero(v)



    def __str__(self):
        s=""
        for i in range(self.nb_rows):
            for j in range(self.nb_cols):
                s+=" {}".format(self.champ[i * self.nb_cols + j])
            s+="\n"
        return s



if __name__ == '__main__':
    ihm = IhmScreen()
    def setup():
        createCanvas(800,600)
        background("grey")
        ihm.init()
        # ajout du jeu dans l'ihm
        ihm.addObjet(ChampDeMines(ihm,50,30))

    def compute():
        ihm.scan_events()

    def draw():
        ihm.draw()

    run(globals())
