
import numpy as np

class KMeans:
    """K-Means Class"""
    
    def __init__(self, data, num_clusters):
                self.data = data
        self.num_clusters = num_clusters

    def train(self, max_iterations):
        pass

    @staticmethod
        def centroids_init(data, num_clusters):
            

            # Get number of training examples.
            num_examples = data.shape[0]

            # Randomly reorder indices of training examples.
            random_ids = np.random.permutation(num_examples)

            # Take the first K examples as centroids.
            centroids = data[random_ids[:num_clusters], :]

            # Return generated centroids.
            return centroids

        @staticmethod
        def centroids_find_closest(data, centroids):
           

            # Get number of training examples.
            num_examples = data.shape[0]

            # Get number of centroids.
            num_centroids = centroids.shape[0]

            # We need to return the following variables correctly.
            closest_centroids_ids = np.zeros((num_examples, 1))

            for example_index in range(num_examples):
                distances = np.zeros((num_centroids, 1))
                for centroid_index in range(num_centroids):
                    distance_difference = data[example_index, :] - centroids[centroid_index, :]
                    distances[centroid_index] = np.sum(distance_difference ** 2)
                closest_centroids_ids[example_index] = np.argmin(distances)

            return closest_centroids_ids

        @staticmethod
        def centroids_compute(data, closest_centroids_ids, num_clusters):
           

            # Get number of features.
            num_features = data.shape[1]

            # We need to return the following variables correctly.
            centroids = np.zeros((num_clusters, num_features))


            for centroid_id in range(num_clusters):
                closest_ids = closest_centroids_ids == centroid_id
                centroids[centroid_id] = np.mean(data[closest_ids.flatten(), :], axis=0)

            return centroids
