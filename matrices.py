from random import *
#Exercice n°1
def afficheMat(mat):
    nbl=len(mat)
    nbc=len(mat[0])
    for i in range(nbl):
        print("(",end="")
        for j in range(nbc):
            print(" {:4} ".format(mat[i][j]),end="")
        print(")")
        
#Exercice n°2
def initMatVide(nbl,nbc):
    m=[None]*nbl
    for i in range (nbl):
        m[i]=[None]*nbc
    return m

#Exercice n°3
def initMatVal(nbl,nbc,val):
    m=[val]*nbl
    for i in range (nbl):
        m[i]=[val]*nbc
    return m

#Exercice n°4
def initMatAlea(nbl,nbc):
    mat=initMatVide(nbl,nbc)
    for i in range(nbl):
        for j in range(nbc):
            mat[i][j]=randint(0,20)
    return mat
