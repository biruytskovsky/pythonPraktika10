import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Создание фигуры и осей
fig, ax = plt.subplots(3, 1, figsize=(8, 6))

# Задание начальных параметров для волн
t = np.linspace(0, 2*np.pi, 1000)
a1_0 = 1.0
f1_0 = 1.0
a2_0 = 1.0
f2_0 = 1.0

# Вычисление волн
s1 = a1_0 * np.sin(2 * np.pi * f1_0 * t)
s2 = a2_0 * np.sin(2 * np.pi * f2_0 * t)
s_sum = s1 + s2

# Построение графиков для исходных волн и их суммы
l1, = ax[0].plot(t, s1, lw=2, color='r')
l2, = ax[1].plot(t, s2, lw=2, color='g')
l_sum, = ax[2].plot(t, s_sum, lw=2, color='b')

# Настройка параметров графиков
ax[0].set_title('Волна 1')
ax[1].set_title('Волна 2')
ax[2].set_title('Сумма волн')

# Создание слайдеров для регулировки амплитуды и частоты волн
axcolor = 'lightgoldenrodyellow'
ax_A1 = plt.axes([0.15, 0.02, 0.7, 0.02], facecolor=axcolor)
ax_f1 = plt.axes([0.15, 0.05, 0.7, 0.02], facecolor=axcolor)
ax_A2 = plt.axes([0.15, 0.08, 0.7, 0.02], facecolor=axcolor)
ax_f2 = plt.axes([0.15, 0.11, 0.7, 0.02], facecolor=axcolor)

s_A1 = Slider(ax_A1, 'Амплитуда 1', 0.1, 5.0, valinit=a1_0)
s_f1 = Slider(ax_f1, 'Частота 1', 0.5, 5.0, valinit=f1_0)
s_A2 = Slider(ax_A2, 'Амплитуда 2', 0.1, 5.0, valinit=a2_0)
s_f2 = Slider(ax_f2, 'Частота 2', 0.5, 5.0, valinit=f2_0)

# Функция обновления графика при изменении параметров
def update(val):
    a1 = s_A1.val
    f1 = s_f1.val
    a2 = s_A2.val
    f2 = s_f2.val
    l1.set_ydata(a1 * np.sin(2 * np.pi * f1 * t))
    l2.set_ydata(a2 * np.sin(2 * np.pi * f2 * t))
    l_sum.set_ydata((a1 * np.sin(2 * np.pi * f1 * t)) + (a2 * np.sin(2 * np.pi * f2 * t)))
    fig.canvas.draw_idle()

s_A1.on_changed(update)
s_f1.on_changed(update)
s_A2.on_changed(update)
s_f2.on_changed(update)

plt.show()