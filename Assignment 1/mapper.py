#!/usr/bin/env python
"""mapper.py"""

import sys
import numpy as np
from math import sqrt

# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
    '''
    Mapper function:
        load in coordinates, Centroid, 
        Calculate the distances from each sample to each centroid point
        output relabeled cluster ID as key, Coordinates as value.
    
    '''
    centroids = []
    with open(filepath, "r") as f:
        for line in f:
            temp=line.strip()
            temp=temp.split(",")
            centroids.append(list(map(float, temp)))

    return centroids

def euclidean_dis(point,random_centroid):
    point_array = np.array(point)
    random_centroid_array = np.array(random_centroid)
    return np.linalg.norm(point_array - random_centroid_array, axis=1)


# create clusters based on initial centroids
def createClusters(centroids):
    for line in sys.stdin:
        data_point= list(map(float, line.strip().split(",")))
        centroid_index= np.argmin(euclidean_dis(data_point,centroids))
        print(f"{centroid_index}\t{','.join(map(str, data_point))}")



if __name__ == "__main__":
    centroids_file = sys.argv[1]
    centroids = getCentroids(centroids_file)
    createClusters(centroids)