import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([], [], lw=4)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(t)
    y = np.sin(frame*t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 10), init_func=init, blit=True)

plt.show()