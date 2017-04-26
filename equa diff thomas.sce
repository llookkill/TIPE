function [x,y]=Euler1(a,b,y0,n)
    x=linspace(a,b,n+1)
    y=zeros(1,n+1)
    y(1)=y0
    pas = (b-a)/n
    for i=2:n+1
        y(i)=y(i-1)+pas*y(i-1)
    end
    plot(x,y)
endfunction

function z=phi1(x,y)
    z=1/(1+x^2)
endfunction

function z=phi2(x,y)
    z=-y
endfunction

function z=phi3(x,y)
    z=y^2
endfunction



function [x,y]=Euler2(a,b,phi,y0,n)
    x=linspace(a,b,n+1)
    y=zeros(1,n+1)
    y(1)=y0
    pas = (b-a)/n
    for i=2:n+1
        y(i)=y(i-1)+pas*phi(x(i-1),y(i-1))
    end
    plot(x,y)
endfunction
