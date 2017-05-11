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


#Exercice 2
def prefixe(chaine):
    suffixe="ack"
    for initiale in chaine:
        print(initiale+suffixe,end=" ")

chaine="JKLMNOP"

#Exercice 3
def ordreAlpha(mot1,mot2):
    if mot1<mot2:
        print("Le ",mot1," précède le ",mot2,".")
    elif mot1>mot2:
        print("Le ",mot1," suit le ",mot2,".")
    else:
        print("Les deux mots sont identiques")
        
#Exercice 4
def minMaj(string):
    for i in range(len(string)):
        if 97<=ord(string[i])<=122:
            print (string[i]," est une minuscule")
        elif 65<=ord(string[i])<=90:
                   print (string[i]," est une majuscule")
        else:
            print(string[i]," n'est pas une lettre")

def voyCons(chaine):
    for i in range(len(string)):
        if ord(string[i])==(65 or 69 or 73 or 79 or 85 or 89 or 97 or 101 or 105 or 111 or 117 or 121):
            print (string[i]," est une voyelle")
        else:
            print(string[i]," est une consonne ou un autre caractère)    
