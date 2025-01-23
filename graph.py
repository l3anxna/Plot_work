import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f1(x):
    return x * np.sin(2*x)

def f2(x):
    return np.arctan(x)
x = np.linspace(-10, 10, 10)

y1 = f(x)
y2 = f1(x)
y3 = f2(x)

plt.plot(x, y1, label="f(x) = x^2", color="green", marker="o")
plt.plot(x, y2, label="f1(x) = x * sin(2x)", color="red", linestyle="--", marker="x")
plt.plot(x, y3, label="f2(x) = arctan(x)", color="cyan", linestyle=":", marker="s")

plt.title("Plot of x^2, arctan(x), and x * sin(2x)")
plt.xlabel("x")
plt.ylabel("f(x), f1(x), f2(x)")
plt.legend()

plt.grid(True)
plt.show()
