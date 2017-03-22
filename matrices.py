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

#Exercice n°5
def saisirMat(nbl,nbc):
    mat=initMatVide(nbl,nbc)
    for i in range(nbl):
        for j in range(nbc):
            mat[i][j]=eval(input("entrer la valeur de la case [{}][{}] : ".format(i,j)))
    return mat

#Exercice n°6
def transposeeMat(mat):
    nbc=len(mat)
    nbl=len(mat[0])
    tMat=initMatVide(nbl,nbc)
    for i in range(nbl):
        for j in range(nbc):
            tMat[i][j]=mat[j][i]
    return tMat

#Exercice n°7
def maximumMat(mat):
    nbl=len(mat)
    nbc=len(mat[0])
    maxi=mat[0][0]
    for i in range(nbl):
        for j in range(nbc):
            if maxi<mat[i][j]:
                maxi=mat[i][j]
    return maxi

#Exercice n°8
def valeurMinEtPosition(mat):
    nbl=len(mat)
    nbc=len(mat[0])
    mini=mat[0][0]
    posi=0
    posj=0
    for i in range(nbl):
        for j in range(nbc):
            if mini>mat[i][j]:
                mini=mat[i][j]
                posi=i
                posj=j
    print("la valeur minimal est ",mini," et elle a été trouvée en [",posi,"][",posj,"]")
    
#Exercice n°9
def presenceNombre(mat):
    nbl=len(mat)
    nbc=len(mat[0])
    test=False
    val=eval(input("entrez la valeur suposée présente : "))
    for i in range(nbl):
        for j in range(nbc):
            if mat[i][j]==val:
                test=True
    if test == True:
        print("la valeur",val,"est présente dans la matrice")
    else :print("la valeur",val,"n'est pas présente dans la matrice")
    
#Exercice n°10
def egaliteDeuxMatrices(mat):
    nbl=len(mat)
    nbc=len(mat[0])
    mat1=saisirMat(nbl,nbc)
    afficheMat(mat1)
    test=True
    for i in range(nbl):
        for j in range(nbc):
            if mat[i][j]!=mat1[i][j]:
                test=False
    if test ==True :print("les matrices sont identiques")
    else:print("les matrices sont différentes")

#Exercice n°11
def sommeMat(m1,m2):
    nbl1=len(mat1)
    nbc1=len(mat1[0])
    nbl2=len(mat2)
    nbc2=len(mat2[0])
    if nbl1 == nbl2 and nbc1 == nbc2 :
        mat3=initMatVide(nbl1,nbc1)
        for i in range(nbl1):
            for j in range(nbc1):
                mat3[i][j]=mat1[i][j]+mat2[i][j]
        return mat3


#Exercice n°12
def produitMat(mat1,mat2):
    nbl1=len(mat1)
    nbc1=len(mat1[0])
    nbl2=len(mat2)
    nbc2=len(mat2[0])
    if nbc1==nbl2:
        mat3=initMatVide(nbl1,nbc2)
        for i in range(nbl1):
            for j in range(nbc2):
                cij=0
                for k in range (nbc1):
                    cij=cij+mat1[i][k]*mat2[k][j]
                mat3[i][j]=cij
        return mat3
    else:
        print("erreur")
        return -1

nbl1=int(input("nombre de ligne de la 1er matrice : "))
nbc1=int(input("nombre de colonne de la 1er matrice : "))
nbl2=int(input("nombre de ligne de la 2eme matrice : "))
nbc2=int(input("nombre de colonne de la 2eme matrice : "))
matrice1=initMatAlea(nbl1,nbc1)
afficheMat(matrice1)
print("\n")
matrice2=initMatAlea(nbl2,nbc2)
afficheMat(matrice2)
print("\n")
matrice3=produitMat(matrice1,matrice2)
if matrice3 != -1 :
    afficheMat(matrice3)
else:print("-1")

    
