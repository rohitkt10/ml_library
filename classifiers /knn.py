#!/usr/bin/env python

"""
Class definition for a KNN classifier.

"""

class knn:
    def __init__(self, X, Y):
        """
        X ->  features matrix
        
        Y -> Labels
        
        dtype X:: numpy.ndarray
        dtype Y:: numpy.ndarray
        """
        
        self.X = X
        self.Y = Y
    
    
    def classify(X):
        """
        X -> Examples to classify.
        Shape : N \times D
        
        where, N -> number of examples.
               D -> number of features per example. 
         """
        
        n = X.shape[0]
        
        
        
        
    