#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kpp.py
import numpy as np
import math
import make_dataset
def getrand():
	res = 0
	while res == 0 or res == 1:
		res = np.random.random_sample()
	return res

def kmeans_pp(points, k):
	x = getrand()
	sampled_index = math.floor(x*len(points))
	centroids = []
	centroids.append(points[sampled_index]);
	minDistances = [np.inf for j in points]
	
	for i in range(1,k):
		#update distance to closest centroid for each input point
		for j in range(len(points)):
			x = math.dist(centroids[i-1],points[j])
			minDistances[j] = x if x < minDistances[j] else minDistances[j]
		
		#compute cum ulative distribution or squared distances
		cumulative = [minDistances[0] * minDistances[0]]
		
		for j in range(1,len(points)):
			cumulative.append(cumulative[j-1] + (minDistances[j] * minDistances[j]))
		
		#sample next centroid according to the distribution of squared distances
		x = getrand()
		x = x*cumulative[-1]
		
		#determine index of sampled point
		if x <= cumulative[0]:
			sampledIndex = 1;
		else:
			for j in range(1,len(points)):
				if x > cumulative[j-1] and x <= cumulative[j]:
					sampledIndex = j
		#add sampled point to set of centroids
		centroids.append(points[sampledIndex])
	return centroids
		
	
	
	

def main(args):
	print(kmeans_pp(make_dataset.blob(100),5))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
