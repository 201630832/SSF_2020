#Runge-Kutta 4 aplicado a la ecuación de Duffing sin rozamiento
# x'' + ax + bx**3 = Fcos(wt)
# con sistema de ecuaciones diferenciales de primer orden
import numpy as np
import matplotlib.pyplot as plt 
import math as m

def f(t,x):
	F =  120 #intensidad de la fuerza (N)
	a =  -4 # constante
	b =  -4 # constante
	w = 2*m.pi #periodo de la fuerza F
	return (F*m.cos(w*t))-(a*x)-(b*x**3)

def g(y):
	return y

A =  0 #Punto incial
B = 50 #punto final
h = 1 #Tamaño de paso
y0 =  0.15 #condicion inicial para x(0), posicion en t=0
d0 = 0 #condicion inicial para g, y= x'(0)=0

d = np.arange(A,B+h,h)
n = len(d)
z = np.zeros(n) #vector para guardar las velocidades y=x'
z[0]= d0

x = np.arange(A,B+h,h)
y = np.zeros(n)
y[0] = y0 #vector que guarda las soluciones para las posiciones x

t = np.arange(A,B+h,h)
t[0]=0 #vector del tiempo

for i in range (0,n-1): #implementaion del metodo RK 4
 k1 = h*g(x[i])
 l1 = h*f(t[i],d[i])

 k2 = h*g(x[i] + l1/2)
 l2 = h*f(t[i] + h/2, d[i] + k1/2)	

 k3 = h*g(x[i] + l2/2)
 l3 = h*f(t[i] + h/2, d[i] + k2/2)

 k4 = h*g(x[i] + l3)
 l4 = h*f(t[i] + h, d[i] + k3)

 y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
 z[i + 1] = z[i] + (l1 + 2*l2 + 2*l3 + l4)/6 


plt.plot(x,y,"rv")
plt.xlabel("t")
plt.ylabel("x")
plt.title("Solución Encontrada con RK-4")
plt.show()
