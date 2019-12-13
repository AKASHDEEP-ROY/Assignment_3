"""
AKASHDEEP ROY
DAA
INTEGRATION
"""
#import libraries
from numpy import * 
from scipy.integrate import simps
from scipy.integrate import romberg
from scipy.integrate import fixed_quad
#Input section
a=float(input("lower limit "))
b=float(input("upper limit "))
c=float(input("elementary segment length "))
#Trapezoidal
x=arange(a,b+c,c)
y=exp(x)
t=trapz(y,x)
print ("integration result",t,"(Trapezoidal)")
#Simpson
x=arange(a,b+c,c)
q=simps(y,x)
print("integration result",q,"(Simpson)")
#Defining function
def f(x):
    return exp(x)
#Romberg
w=romberg(f,a,b)
print("integration result",w,"(Romberg)")
#Gauss Quadrature
u=fixed_quad(f,a,b)
print("integration result",u,"(Gauss quadrature)")