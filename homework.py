import random
import matplotlib.pyplot as plt
import time

def generate_centroids(num_points=4, x_range=(0, 100), y_range=(0, 100)):
    """
    Generate a list of random centroids within the given range.
    """
    centroids = []
    for _ in range(num_points):
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        centroids.append((x, y))
    return centroids

def generate_points_around_centroids(centroids, num_points_per_centroid=300, spread=10):
    """
    Generate random points around each centroid with a higher probability of being close to the centroid.
    """
    points = []
    for cx, cy in centroids:
        for _ in range(num_points_per_centroid):
            x = random.gauss(cx, spread)
            y = random.gauss(cy, spread)
            points.append((x, y))
    return points

def plot_points_and_centroids(points, centroids, filename="centroids_plot.png"):
    """
    Plot the points and centroids and save the image.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter([p[0] for p in points], [p[1] for p in points], s=10, c='blue', alpha=0.5, label='Points')
    plt.scatter([c[0] for c in centroids], [c[1] for c in centroids], s=100, c='red', marker='x', label='Centroids')
    plt.title("Random Points Around Centroids")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

def k_means(points, k=4, max_iterations=500):
    """
    Implement the k-means algorithm to find clusters and centroids.
    """
    # Initialize centroids randomly from the points
    centroids = random.sample(points, k)
    for iteration in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for point in points:
            distances = [((point[0] - cx)**2 + (point[1] - cy)**2)**0.5 for cx, cy in centroids]
            closest_centroid = distances.index(min(distances))
            clusters[closest_centroid].append(point)
        new_centroids = []
        for cluster in clusters:
            if cluster:
                avg_x = sum([p[0] for p in cluster]) / len(cluster)
                avg_y = sum([p[1] for p in cluster]) / len(cluster)
                new_centroids.append((avg_x, avg_y))
            else:
                new_centroids.append(random.choice(points))
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return centroids, clusters

if __name__ == "__main__":
    centroids = generate_centroids()
    points = generate_points_around_centroids(centroids)
    plot_points_and_centroids(points, centroids)

    start_time = time.time()
    found_centroids, clusters = k_means(points)
    end_time = time.time()

    print(f"Found centroids: {found_centroids}")
    print(f"Time taken for k-means: {end_time - start_time} seconds")

    # Plot the final clusters and centroids
    plt.figure(figsize=(10, 6))
    colors = ['blue', 'green', 'cyan', 'magenta']
    for i, cluster in enumerate(clusters):
        plt.scatter([p[0] for p in cluster], [p[1] for p in cluster], s=10, c=colors[i], alpha=0.5, label=f'Cluster {i+1}')
    for i, centroid in enumerate(found_centroids):
        plt.scatter(centroid[0], centroid[1], s=100, c=colors[i], marker='x', edgecolor='black', label=f'Centroid {i+1}')
    plt.title("K-Means Clustering")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.savefig("k_means_clusters.png")
    plt.show()