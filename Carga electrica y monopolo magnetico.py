import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Definir la trayectoria de la carga electrica alrededor del monopolo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Límites de los ejes
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

# Datos iniciales (un solo punto)
xdata, ydata, zdata = [], [], []
line, = ax.plot(xdata, ydata, zdata, 'b-', lw=2, label='Trayectoria de la carga eléctrica')

# Esto define el monopolo magn\'etico que crea la trayectoria de la carga
ax.scatter(0, 0, -1, color='red', label='Monopolo Magnético')
ax.legend()

# Función para actualizar la trayectoria
def animate(i):
    # Ángulo máximo para cada frame
    angle = 2 * np.pi * i / 100
    # Generar puntos de la trayectoria
    theta = np.linspace(0, angle, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros(100)
    line.set_data(x, y)
    line.set_3d_properties(z)
    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=100, interval=20)

# Agregar una etiqueta general
ax.set_title("Movimiento de una carga eléctrica alrededor de un monopolo magnético")

plt.show()