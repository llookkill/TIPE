printf("Résolution de l_équation du second degré ax^2+bx+c=0")
printf("Entrer dans une liste les coefficients a,b,c")
l=input("l")
a=l(1)
b=l(2)
c=l(3)
d=b^2-4*a*c
if d>0 then
    x1=(-b-sqrt(d))/2*a
    x2=(-b+sqrt(d)/2*a)
    printf("Le discriminant est positif et vaut %f \n",d)
    printf("L_équation admet deux racines distinctes: x1= %f et x2= %f",x1,x2)
elseif d==0 then x0=-b/2*a
    printf("Le discriminant est nul \n ")
    printf("L_équation admet une racine double: x0= %f",x0)   
else printf("L_équation n_admet pas de racines réelles")
end

function y=f2(x)
y=x^2-2
endfunction
function res=lagrange(x1,x2,f,n)
for i = 1 : n
xi=x1-((x2-x1)/(f(x2)-f(x1)))*f(x1)
if (f(xi)*f(x1))<0
x1=xi
else 
x2=xi
end
end
res=xi
endfunction


//Tracé de la focntion et Programme principal
clf() //Effaçage de la fenêtre graphique
plot([-1/0.1:10],f2) // répresentatin de la courbe entre -1 et 10 et pas de 0.1
f=input("Entrer la fonction a tester : ")
x1=input("Entrer la valeur minimale encadrant la solution : ")
x2=input("Entrer la valeur maximale encadrant la solution : ")
printf("La valeur approchée avec la méthode de Lagrange est de %f", lagrange(x1,x2,f,8))

//Programme principal demandant à l'utilisateur la valeur de départ/ max suite
//x0=input("Entrer une valeur de x0 :")
//h=input("Entrer une valeur très petite pour h :")
//n=input("Choisir la valeur de n pour la somme : ")
//printf("Le résultat de la dérivée est %f",derivef(f0,x0,h))
//for i = 1 : n
// printf("La valeur de l_itération est %d et la valeur approchée pour cette itération est de %f\n",i,newton1(x0,f2,i))
//end
