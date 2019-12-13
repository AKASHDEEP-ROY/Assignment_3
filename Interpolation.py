"""
AKASHDEEP ROY
DAA
INTERPOLATION
"""
#import of libraries
from scipy.interpolate import InterpolatedUnivariateSpline as pol
from scipy.interpolate import lagrange as lol
import numpy as np
import matplotlib.pyplot as plot

#given data set
x = np.array([0,1,2,3,4,5])
y = np.array([1.0,2.0,1.0,0.5,4.0,8.0])

#interpolation done...
f = pol(x,y,k=1) #linear spline
g = pol(x,y,k=2) #quadratic spline
h = pol(x,y,k=3) #cubic spline
c = lol(x,y)     #Lagrange Method

#title:
plot.xlabel("x")
plot.ylabel("y")
plot.title("Interpolation of given data set")

#plot of interpolated functions
p=np.arange(0,5,0.01)
plot.plot(p,f(p),label="linear spline")
plot.plot(p,g(p),label="quadratic spline")
plot.plot(p,h(p),label="cubic spline")
plot.plot(p,c(p),label="lagrange interpolation")

#plot of given data points
plot.plot(x,y,'ro',ms=5)
plot.legend()
plot.show()




