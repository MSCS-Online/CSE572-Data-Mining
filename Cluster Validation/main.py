#!/usr/bin/env python3

"""
- Author: Jeremy Escobar
- Session: Spring session B
- Course: CSE 572, Cluster Validation Project
"""

import numpy as np  
from sklearn.cluster import DBSCAN, KMeans  
import pandas as pd  
import csv  


def load_insulin_glucose_datasets():
    """
    - DIRECTIONS: Load Insulin and Glucose data
    """
    """omitted"""


def perform_ground_truth():
    """
    - DISCRETIZE: the meal amount in bins of size 20.
    - In total, you should have n = (max-min)/20 bins.
    - Cluster Meal data based on the amount of carbohydrates in each meal
    """
    """omitted"""


def perform_clustering():
    """
    Evaluates clustering performance by computing SSE, Entropy, and Purity metrics.
    """
    """omitted"""


def perform_kmeans_clustering():
    """omitted"""


def perform_dbscan_clustering():
    """omitted"""
  

def main():
    """
    Main function to execute the clustering. 
    Expected Output: A Result.csv file which contains a 1 X 6 vector. 
    """
    """omitted"""


if __name__ == "__main__":
    main()
