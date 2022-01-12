#!/usr/bin/env python
# -*- coding: utf-8 -*-

# seed the pseudorandom number generator
from random import seed
from random import randint
import math

#skikit
from sklearn.datasets import make_blobs

import numpy as np

import pickle
import time


#step 1:
#create nodes
#this makes blobs using the scilearn library and adds them in the graph G
def blob(samples):
	X,Y = make_blobs(n_samples = samples, n_features = 2, centers = 3)
	G = []
	for x in X:
		G.append((x[0],x[1]))
	return G
