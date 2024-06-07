import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z1 = X**2 + Y**2  # Пример функции среднеквадратичного отклонения
Z2 = np.log(Z1)  # Логарифмическая шкала для второго графика

# Построение первого графика
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')

# Построение второго графика с логарифмической шкалой на оси Z
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(MSE)')
ax2.set_yscale('log')  # Установка логарифмической шкалы на оси Z

plt.show()