h=input("entrez une valeur petite pour h :  ")
x0=input("entrez une valeur pour x0 :  ")
f=input("entrez la fonction :  ")
function y=f0(x)
    y=x^3-2*x-5
endfunction

function y=derivef(f,x0,h)
    y = (f(x0+h)-f(x0))/h
endfunction
function uk=newton1(x0,f,i)
    uk=x0
    for k = 1 : i
          uk = uk-f(uk)/derivef(f,uk,0.00001)
    end
endfunction
printf("la valeur aproché de f prime de (%f) est : %f",x0,derivef(f,x0,h))
n=input("Choisir la valeur de n pour la somme :  ")
for i = 1 : n
printf("La valeur de l_itération est %d et la valeur approchée pour cette itération est de %f\n",i,newton1(x0,f0,i))
end
