import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import sys
fig=plt.figure()
ax1=fig.gca(projection='3d')
delta=.25
x=np.arange(-3,3,delta)
y=np.arange(-3,3,delta)
X, Y=np.meshgrid(x,y)
Z1=(X**4)+(Y**4)-15
Z2=(X**3)*(Y)-X*(Y**3)-Y/2-1.728
Z=Z1-Z2
Z3=Z1-Z1+Z2-Z2
#surface=ax1.plot_wireframe(X,Y,Z1)
#surface=ax1.plot_surface(X,Y,Z2,cmap='binary',vmin=-100,vmax=100)
#surface=ax1.plot_wireframe(X,Y,Z3,)
#ax1.set_zlim(-50,50)
#ax1.zaxis.set_major_locator(LinearLocator(0))
#ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#fig.colorbar(surface,shrink=0.5,aspect=5)
#plt.show()
def func(y):
    Resultado=((15-y**4)**(3/4.0))*y-((15-y**4)**(1/4.0))*y**3-y/2.0-1.728
    return Resultado
#buscando el entre 0.5 y 1,5
def cero_biseccion(f,a,b,error):
    c=(a+b)/2.0
    while np.fabs(f(c))>error:
        if f(c)*f(a)<0:
            b=c
        elif f(c)*f(b)<0:
            a=c
        else:
            break
        c=(a+b)/2.0
    return c
print(cero_biseccion(func,0.5,1.5,1e-5))
print(cero_biseccion(func,-0.5,-1.8,1e-5))
