import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp 
import math
import scipy.integrate as integral
dist=np.arange(0,20,0.01)
def y_catenaria(x,x0,a):
    y=(a/2.0)*(np.exp((x-x0)/a)+np.exp((x0-x)/a))-a-7.5
    return y
def y_catenaria_pr(x,x0,a):
    y=(0.5)*(np.exp((x-x0)/a)-np.exp((x0-x)/a))
    return y

h=[]
for valor in dist:
    h.append(y_catenaria(valor,10,40))
A=np.arange(2,100,0.2)
y1=[]
n=0
while n < len(A):
    y1.append(y_catenaria(0,10,A[n]))
    n+=1
#plt.plot(dist,h)
#t.show()

error=1e-15
x1=2.0
X=[]
Y=[]
y2=10
while np.fabs(y2) > error:
    Y.append(y2)
    X.append(x1)
    delta=-y_catenaria(0.0,10.0,x1)/y_catenaria_pr(0.0,10.0,x1)
    x1=x1+delta
    y2=y_catenaria(0,10,x1)

plt.plot(X,Y)
plt.yscale('log')
plt.show()

def d_largo(x):
    y=np.sqrt(1+y_catenaria_pr(x,10,x1)**(2))
    return y
largo=integral.quad(d_largo,0,20)
print(largo)
print(x1)



    