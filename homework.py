import random

def generate_centroids(num_points=4, x_range=(0, 100), y_range=(0, 100)):
    centroids = []
    for _ in range(num_points):
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        centroids.append((x, y))
    return centroids

if __name__ == "__main__":
    centroids = generate_centroids()
    for i, centroid in enumerate(centroids):
        print(f"Centroid {i+1}: {centroid}")