import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

#Introducimos constantes
#Utilizamos la libreria numpy porque esta clase permite hacer 
#operaciones matematicas con arreglos de manera mas sencilla

mu_0 = 4 * np.pi * 1e-7                                             #Permeabilidad magnetica en el vacio
g = 1                                                               #Carga del monopolo magnetico

def campo_magnetico(x, y, z, g, mu_0):
    r = np.sqrt(x**2 + y**2 + z**2)
    r_hat = np.array([x, y, z]) / r
    B = (mu_0 * g) / (4 * np.pi * r**2) * r_hat
    return B, r

#Estos son los puntos de coordenadas en las tres dimensiones

x = np.linspace(-2,2,10)
y = np.linspace(-2,2,10)
z = np.linspace(-2,2,10)
X, Y, Z = np.meshgrid(x, y, z)

#El campo magnetico en cada punto tiene la siguiente forma
Bx, By, Bz = np.zeros(X.shape), np.zeros(Y.shape), np.zeros(Z.shape)
radii = np.zeros(X.shape)
for i in  range(X.shape[0]):
    for j in range(X.shape[1]):
        for k in range(X.shape[2]):
            B, r = campo_magnetico(X[i,j,k], Y[i,j,k], Z[i,j,k], g, mu_0) 
            Bx[i,j,k], By[i,j,k], Bz[i,j,k] = B
            radii[i, j, k] = r


#Graficamos ahora el campo magnetico con matplotlib
fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot( 111, projection = '3d')

#Definamos la longitud de las flechas para que sean mas grandes cerca del origen
magnitudes = np.sqrt(Bx**2 + By**2 + Bz**2)
longitudes = magnitudes*(radii**2) / np.max(radii**2)

#Dibujar las lineas de campo magnetico en cada punto
ax.quiver(X, Y, Z, Bx, By, Bz, length = 0.1, normalize = True, color = 'b')

#Configuramos los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Campo magnetico de un monopolo magnetico ')

plt.show()
