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
