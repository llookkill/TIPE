function y=f1(x)
    y=1/x
endfunction

function y=f2(x)
    y=1/(1+x^2)
endfunction

function y=rectg(f,a,b,n)
    y=0
    for i=0:n-1
        i=a+i*(b-a)/n
        y=y+f(i)
    end
    y=((b-a)/n)*y
endfunction

function y=rectd(f,a,b,n)
    y=0
    for i=1:n
        i=a+i*(b-a)/n
        y=y+f(i)
    end
    y=((b-a)/n)*y
endfunction

function aire=trapeze(f,a,b,n)
    pas=(b-a)/n
    somme=0
    xk=a
    for k=0:n-1
        somme=somme+((1/2)*(f(xk)+f(xk+pas))*pas)
        xk=xk+pas
    end
    aire=somme
endfunction

function aire=tangenteMilieu(f,a,b,n)
    pas=(b-a)/n
    somme=0
    xk=a+pas/2
    for k=0:n-1
        somme=somme+f(xk)*pas
        xk=xk+pas
    end
    aire=somme
endfunction

function afficheTableau1(f,a,b,valeur)
    n=10
    while n<=100000
        printf("%7d",n)
        printf("%10.6f",(rectangleGauche(f,a,b,n)))
        printf("%17.13f",(rectangleGauche(f,a,b,n))-valeur)
        printf("%14.10f",n*(rectangleGauche(f,a,b,n))-valeur)
        printf("%10.6f",(rectangleDroit(f,a,b,n)))
        printf("%17.13f",(rectangleDroit(f,a,b,n))-valeur)
        printf("%14.10f\n",n*(rectangleDroit(f,a,b,n))-valeur)
        n=n*10
    end
endfunction

function afficheTableau2(f,a,b,valeur)
    n=10
    while n<=100000
        printf("%7d",n)
        printf("%10.6f",(trapeze(f,a,b,n)))
        printf("%17.13f",(trapeze(f,a,b,n))-valeur)
        printf("%14.10f",n*(trapeze(f,a,b,n))-valeur)
        printf("%10.6f",(tangenteMilieu(f,a,b,n)))
        printf("%17.13f",(tangenteMilieu(f,a,b,n))-valeur)
        printf("%14.10f\n",n*(tangenteMilieu(f,a,b,n))-valeur)
        n=n*10
    end
endfunction
