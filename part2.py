import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from collections import Counter


def plot_surface_1(X, Y):
    Z1 = X * Y
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z1, cmap="winter")
    ax.set_title("f(x,y) = x*y")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


def plot_surface_2(X, Y):
    Z2 = X**2 + Y**2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z2, cmap="summer")
    ax.set_title("f(x,y) = x^2 + y^2")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


def plot_surface_3(X, Y):
    Z3 = np.sin(3 * X) * Y
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z3, cmap="viridis")
    ax.set_title("f(x,y) = sin(3*x)*y")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

plot_surface_1(X, Y)
plot_surface_2(X, Y)
plot_surface_3(X, Y)
