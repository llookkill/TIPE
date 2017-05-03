#Exercice 1
def affichechaîne(chaine):
    n=len(chaine)
    for i in range(n-1):
        print(chaine[i],end=",")
    print(chaine[n-1],end=".")


def affichechaîne2(chaine):
    n=len(chaine)
    for i in range(n-1):
        print(chaine[i],end=" ")
    print(chaine[n-1],end="")
    
def affichechaîne3(chaine):
    for caract in chaine:
        print(caract,end=" ")
        
lo="je suis un test"
affichechaîne(lo)
print("")
affichechaîne2(lo)
print("")
affichechaîne3(lo)
