import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt("points.csv", delimiter=",", dtype=float)

distances = np.loadtxt("distances.csv", delimiter=",", dtype=float)

x = points[:, 0]
y = points[:, 1]

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=distances, cmap="viridis")
plt.colorbar(scatter, label="Distance")
plt.title("Scatter Plot of Points Colored by Distance")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.tight_layout()
plt.show()
