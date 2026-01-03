import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

x = np.linspace(0, 2*np.pi, 400)
y = f(x)

points = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = sin(x)', color='black')

for a in points:
    y_tangent = f(a) + df(a) * (x - a)
    plt.plot(x, y_tangent, label=f'Tangente en x = {a:.2f}')
    plt.scatter(a, f(a))

plt.title('Rectas tangentes a f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
