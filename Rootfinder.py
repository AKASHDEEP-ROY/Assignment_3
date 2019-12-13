"""
AKASHDEEP ROY
DAA
NON-LINEAR EQUATIONS
"""
#import the libraries
from scipy.optimize import bisect
from scipy.optimize import newton
from numpy import *
#Defining Function
def f(x):
    return sin(cos(exp(x)))
#The starting bracket
a=float(input("Write the starting point of guessed interval "))
b=float(input("Write the ending point of guessed interval "))
#The bisection operation
m=bisect(f,a,b)
#printing the root of the function using bisection
print ("root of the function",m," (bisection method)")
print ("value of the function at",m,"is",f(m))

#The derivative of given function
def g(x):
    return -exp(x)*sin(exp(x))*cos(cos(exp(x)))
#Initial guess
s=float(input("Write the starting guess for Newton-Raphson "))
#Operation of Newton-Raphson method
n=newton(f,s,fprime=g)
#Printing the root found by Newton-Raphson method
print ("root of the function",n," (Newton-Raphson method)")
#Initial guess for Secant method
p=float(input("Write the starting guess for Secant method "))
#operation of Secant Method
secant=newton(f,p)
#printing the root found by Secant method
print ("root of the function",secant," (Secant's Method)")

"""
With the starting bracket (-1,1),root found by bisection method is ~ 0.45158
The corresponding value of function ~ -2.43133*10^-12
It is not exactly zero. I think it is mainly due to accuracy checking. After satisfying the accuracy condition, it shows the root.

Using -1 as initial guess, the result is ~ 9.17920.
Using -0.1 as initial guess, the result is ~ 0.45158.
The results differ in sufficient amount. It is because if we draw a tangent at x=-1,it crosses several roots before touching X-axis. But it is not the case for tangent at x=-0.1
"""