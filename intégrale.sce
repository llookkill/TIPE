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
