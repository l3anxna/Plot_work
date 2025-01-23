import numpy as np
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


def plot_bar(values):
    value_counts = Counter(values)
    unique_values = list(value_counts.keys())
    counts = list(value_counts.values())
    plt.figure(figsize=(10, 6))
    bars = plt.bar(unique_values, counts, color="lightblue")
    plt.title("Frequency of Values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    for bar, count in zip(bars, counts):
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 0.05,
            int(count),
            ha="center",
            va="bottom",
        )
    plt.show()


def plot_histogram(histogram):
    plt.figure(figsize=(10, 6))
    plt.hist(histogram, bins=30, color="lightgreen", edgecolor="black")
    plt.title("Histogram of Values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
values = np.loadtxt("values_for_bars.csv", delimiter=",")
histogram = np.loadtxt("values_for_hist.csv", delimiter=",")

plot_surface_1(X, Y)
plot_surface_2(X, Y)
plot_surface_3(X, Y)
plot_bar(values)
plot_histogram(histogram)
