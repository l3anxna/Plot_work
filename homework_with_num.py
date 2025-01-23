import random
import numpy as np
import matplotlib.pyplot as plt
import time

def generate_centroids(num_points=4, x_range=(0, 100), y_range=(0, 100)):
    centroids = []
    for _ in range(num_points):
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        centroids.append((x, y))
    return centroids

def generate_points_around_centroids(centroids, num_points_per_centroid=300, spread=10):
    points = []
    for cx, cy in centroids:
        for _ in range(num_points_per_centroid):
            x = random.gauss(cx, spread)
            y = random.gauss(cy, spread)
            points.append((x, y))
    return np.array(points)

def plot_points_and_centroids(points, centroids, filename="centroids_plot.png"):
    plt.figure(figsize=(10, 6))
    plt.scatter(points[:, 0], points[:, 1], s=10, c='blue', alpha=0.5, label='Points')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='red', marker='x', label='Centroids')
    plt.title("Random Points Around Centroids")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

def k_means_vectorized(points, k=4, max_iterations=500):
    centroids = points[np.random.choice(points.shape[0], k, replace=False)]
    for iteration in range(max_iterations):
        distances = np.sqrt(((points[:, np.newaxis] - centroids) ** 2).sum(axis=2))
        closest_centroids = np.argmin(distances, axis=1)
        new_centroids = np.array([points[closest_centroids == i].mean(axis=0) for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, closest_centroids

if __name__ == "__main__":
    centroids = generate_centroids()
    points = generate_points_around_centroids(centroids)
    plot_points_and_centroids(points, np.array(centroids))

    start_time = time.time()
    found_centroids, closest_centroids = k_means_vectorized(points)
    end_time = time.time()

    print(f"Found centroids: {found_centroids}")
    print(f"Time taken for k-means: {end_time - start_time} seconds")

    plt.figure(figsize=(10, 6))
    colors = ['blue', 'green', 'cyan', 'magenta']
    for i in range(len(found_centroids)):
        cluster_points = points[closest_centroids == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], s=10, c=colors[i], alpha=0.5, label=f'Cluster {i+1}')
    for i, centroid in enumerate(found_centroids):
        plt.scatter(centroid[0], centroid[1], s=100, c=colors[i], marker='x', edgecolor='black', label=f'Centroid {i+1}')
    plt.title("K-Means Clustering")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.savefig("k_means_clusters.png")
    plt.show()