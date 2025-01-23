import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2


def f1(x):
    return x * np.sin(2 * x)


def f2(x):
    return np.arctan(x)


x = np.linspace(-10, 10, 400)

y1 = f(x)
y2 = f1(x)
y3 = f2(x)

plt.plot(x, y1, label="f(x) = x^2")
plt.plot(x, y2, label="f1(x) = x * sin(2x)")
plt.plot(x, y3, label="f2(x) = arctan(x)")

plt.grid(True)
plt.show()
