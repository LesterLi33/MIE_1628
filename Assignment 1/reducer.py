#!/usr/bin/env python
"""reducer.py"""


import sys
from collections import defaultdict
import numpy as np

def calculateNewCentroids():
    '''
    Reducer function:
    Similar to combiner except it is for all machines
    load in what combiner gives
    Combines member, member centroid for each cluster from different machines
    together.
    Update Centroid for each cluster
    output exactly the same format of data as input file except centroid, cluster
    ID have been updated
    '''
    current_cluster = defaultdict(list)
 
    # input comes from STDIN
    for line in sys.stdin:

        # parse the input of mapper.py
        temp=line.strip()
        cluster_index, cord= temp.split("\t")       
        # convert x and y (currently a string) to float
        value=list(map(float,(cord.split(","))))
        key=int(cluster_index)
        current_cluster[key].append(value)
            # float was not a number, so silently
            # ignore/discard this line
         
    for key, points in current_cluster.items():
        new_centroid=np.mean(points,axis=0)
        print(f"{key}\t{','.join(map(str, new_centroid))}")
        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        
                # print the average of every cluster to get new centroids
             
            
    
    # print last cluster's centroids

if __name__ == "__main__":
    calculateNewCentroids()