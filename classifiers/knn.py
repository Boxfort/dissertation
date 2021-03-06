# Jack Anderson 2017
import numpy as np
import pandas as pd
from collections import OrderedDict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors

stochastic = False

def run(train_set, test_set):
    knn = KNeighborsClassifier(n_neighbors=3, algorithm='kd_tree')

    # Large set of data used to train the classifier.
    x_train = train_set.ix[:, 0:len(train_set.columns)-1] # All columns except Labels
    y_train = train_set['labels'] # Indices and labels

    # Smaller set of data used to test the trained classifier
    x_test = test_set.ix[:, 0:len(test_set.columns)-1] # All columns except Labels
    y_test = test_set['labels'] # Indices and labels

    print("Fitting Data...")

    # Fit the training set
    knn.fit(x_train, y_train)

    print("Predicting Test Data...")

    # Predict the testing set
    pred = knn.predict(x_test)

    return pred
