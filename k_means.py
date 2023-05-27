
import numpy as np

class KMeans:
    """K-Means Class"""
    
    def __init__(self, data, num_clusters):
        """K-Means class constructor.

        :param data: training dataset.
        :param num_clusters: number of cluster into which we want to break the dataset.
        """
        self.data = data
        self.num_clusters = num_clusters

    def train(self, max_iterations):
        pass

    @staticmethod
    def centroids_compute(data, closest_centroids_ids, num_clusters):
        """Compute new centroids.

        Returns the new centroids by computing the means of the data points assigned to
        each centroid.

        :param data: training dataset.
        :param closest_centroids_ids: list of closest centroid ids per each training example.
        :param num_clusters: number of clusters.
        """

        # Get number of features.
        num_features = data.shape[1]

        # We need to return the following variables correctly.
        centroids = np.zeros((num_clusters, num_features))

        # Go over every centroid and compute mean of all points that belong to it. 
        #Concretely, the row vector centroids(i, :) should contain the mean of the data points assigned to centroid i.
        for centroid_id in range(num_clusters):
            closest_ids = closest_centroids_ids == centroid_id
            centroids[centroid_id] = np.mean(data[closest_ids.flatten(), :], axis=0)

        return centroids