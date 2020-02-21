#Juan Ochoa 000340107 Modelamiento Matemático.
import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint

import math
def masa_resorte( X , t ):
    m1 = 6 #Masa del cuerpo 1
    m2 = 4 #Masa del cuerpo 2
    lo = 10 #Elongación del resorte
    b = 2.4 #Coeficiente de fricción
    kr = 110 #Constante elástica del resorte 1
    kr2 = 100#Constante elástica del resorte 2
    cos = b * math.cos(t*4)#Función COSENO
    x1, vx1, x2, vx2 = X
    d1 = np.abs(x1 - cos)#Distancia del punto rojo a la masa 1
    d2 = np.abs(x2 - x1)#Distancia del punto 1 al punto 2
    dx1dt = vx1#Masa 1: Derivada con respecto al tiempo de la posición(Velocidad)
    dvx1dt = -b*(vx1/m1) - ((1/m1) * (kr * (d1 - lo) * (cos - x1)/d1)) + (1/m1)*(kr2*(d2-lo)*(d2))#Masa 1: Derivada de la velocidad con respecto al tiempo(Aceleración)
    dx2dt = vx2#Masa 2: Derivada con respecto al tiempo de la posición(Velocidad)
    dvx2dt = -b*(vx2/m2) + ((1/m2) * (kr2 * (d2 - lo) * ((x1-x2)/d2)))#Masa 2: Derivada de la velocidad con respecto al tiempo(Aceleración)
    
    return [dx1dt, dvx1dt, dx2dt, dvx2dt]#Retorno las variables calculadas
t = np.linspace(0,13,500)#Tiempo
y = odeint(masa_resorte, [0,0,10,0], t)#Recibe la función y los valores de esta.
#Datos en la gráfica.
plt.plot(t,y[:,0])
plt.plot(t,y[:,2])
plt.xlabel('Time')
plt.ylabel('Acceleration')
plt.legend(['Car 1', 'Car 2'])



 
