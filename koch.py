from turtle import *
def flocon(l,n) :
    if n==0 :
        fd(l)
    else :
        flocon(l/3,n-1)
        lt(60)
        flocon(l/3,n-1)
        right(120)
        flocon(l/3,n-1)
        lt(60)
        flocon(l/3,n-1)
 
#clearscreen()
#speed(0)
#tracer(5,0)
flocon(243,5)
update()
penup()
back(243)
pendown()
