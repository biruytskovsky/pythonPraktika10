import numpy as np
import matplotlib.pyplot as plt

def Lissajous_figure(a, b):
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(a*t)
    y = np.sin(b*t)

    plt.figure()
    plt.plot(x, y)
    plt.title(f"Фигура Лиссажу ({a}:{b})")
    plt.axis('equal')
    plt.show()

frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]
for freq in frequencies:
    Lissajous_figure(freq[0], freq[1])