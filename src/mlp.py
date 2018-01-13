# Jack Anderson 2017
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

def run(train_set, test_set):

    mlp = MLPClassifier(hidden_layer_sizes=(100), solver='adam', learning_rate='invscaling')

    # Large set of data used to train the classifier.
    x_train = train_set.ix[:, 0:len(train_set.columns)-1] # All columns except Labels
    y_train = train_set['labels'] # Indices and labels

    # Smaller set of data used to test the trained classifier
    x_test = test_set.ix[:, 0:len(test_set.columns)-1] # All columns except Labels
    y_test = test_set['labels'] # Indices and labels

    #Fit the scaler to the training data
    scaler = StandardScaler()
    scaler.fit(x_train)

    # Apply Transformations to data
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    mlp.fit(x_train,y_train)
    predictions = mlp.predict(x_test)
    return predictions
