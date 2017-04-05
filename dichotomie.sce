// dichotomie
function [x0,nbIter]=dichotomie(a,b,f)
for i=1:n
    
    //milieu de l'intervalle [a,b]
    m=(b+a)/(a*f(b)-b*f(a))/((f(b)-f(a))
    //Détermination du sous-intervalle contenant le zéro
    if f(m)*f(a)<0 then 
        b=m
    else
        a=m
    end
end
//renvoi des résultats 
x0=m


endfunction

function y=fe(x)
    y=x^2-2*x-10
endfunction

