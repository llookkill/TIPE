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

function z=phi4(x,y)
    z=y^2-x
endfunction

function z=phi5(x,y)
    z=sin(x*y)
endfunction

function z=phi6(x,y)
    z=exp(x*y)
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

function [x,y]=predictionCorrection(a,b,phi,y0,n)
    x=linspace(a,b,n+1)
    y=zeros(1,n+1)
    y(1)=y0
    pas = (b-a)/n
    for i=2:n+1
        ytmp=y(i-1)+pas*phi(x(i-1),y(i-1))
        
        y(i)=y(i-1)+0.5*pas*(phi(x(i-1),y(i-1))+phi(x(i),ytmp))
    end
    plot(x,y)
endfunction

function [x,y]=RungeKutta(a,b,phi,y0,n)
    x=linspace(a,b,n+1)
    y=zeros(1,n+1)
    y(1)=y0
    pas = (b-a)/n
    for i=2:n+1
        k1=phi(x(i-1),y(i-1))
        k2=phi(x(i-1)+0.5*pas,y(i-1)+0.5*pas*k1)
        k3=phi(x(i-1)+0.5*pas,y(i-1)+0.5*pas*k2)
        k4=phi(x(i-1)+pas,y(i-1)+pas*k3)
        y(i)=y(i-1)+pas*(k1+2*k2+2*k3+k4)/6
    end
    plot(x,y)
endfunction
