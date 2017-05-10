function [x0,nbIter]=lagrange(a,b,f,eps)
n=0
while (b-a >=2*eps)
    n=n+1
    //milieu de l'intervalle [a,b]
    m=(a*f(b)-b*f(a))/(f(b)-f(a))
    //Détermination du sous-intervalle contenant le zéro
    if f(m)*f(a)<0 then 
        b=m
    else
        a=m
    end
end
//renvoi des résultats 
x0=m
nbIter=n

endfunction

function y=fe(x)
    y=x^2-2*x-10
endfunction