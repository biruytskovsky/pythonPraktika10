#import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

degrees = range(1, 8)
fig, a = plt.subplots()
for degree in degrees:
    x = np.linspace(-1, 1, 1000)
    y = legendre(degree)(x)
    a.plot(x, y, label=f'n = {degree}')

a.set_title('Полиномы Лежандра')
a.legend()
plt.show()