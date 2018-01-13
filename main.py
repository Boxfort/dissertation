# Jack Anderson 2017
import csv
import numpy as np
import pandas as pd
from collections import OrderedDict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.cross_validation import train_test_split

NSL_KDD_TRAINING_PATH   = "Datasets/NSL-KDD/KDDTrain.csv"
NSL_KDD_TRAINING20_PATH = "Datasets/NSL-KDD/KDDTrain_20Percent.csv"
NSL_KDD_TESTING_PATH    = "Datasets/NSL-KDD/KDDTest.csv"
NSL_KDD_ATTACKS_PATH    = "Datasets/NSL-KDD/KDDAttackTypes.csv"
NSL_KDD_FIELDS_PATH     = "Datasets/NSL-KDD/KDDFieldNames.csv"

dataset_cols    = list() # [Field Name]
dataset_types   = list()
dataset_attacks = dict() # [Attack Name, Attack Type]

nominal_inx = [1, 2, 3]
binary_inx  = [6, 11, 13, 14, 20, 21]
numeric_inx = list(set(range(41)).difference(nominal_inx).difference(binary_inx))

nominal_cols = list()
binary_cols  = list()
numeric_cols = list()

# Loads values from a two column .csv file and stores in a dictionary object.
def load_cols(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset_cols.append(row[0])
            dataset_types.append(row[1])
    for i in nominal_inx:
        nominal_cols.append(dataset_cols[i])
    for i in binary_inx:
        binary_cols.append(dataset_cols[i])
    for i in numeric_inx:
        numeric_cols.append(dataset_cols[i])

def load_attacks(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset_attacks[row[0]] = row[1]

# Loads a dataset and divides into 8 partitions.
def load_dataset(path, fields):
    return pd.read_csv(path, index_col=False, names=fields)

# DOES NOT WORK !!!
def get_attribute_ratio(dataset):
    ratio_dict = dict()
    numeric_col_total = dataset[numeric_cols].mean().sum()
    for column in dataset:
        if column in numeric_cols:
            ratio_dict[column] = (dataset[column].max() / dataset[column].mean())# / numeric_col_total)
        elif column in binary_cols:
            ratio_dict[column] = np.sum(dataset[column] == 1) / np.sum(dataset[column] == 0)
    return OrderedDict(sorted(ratio_dict.items(), key=lambda v: -v[1]))

# Replaces Nominal Columns with several binary columns
def one_hot_encoding(dataset, nominalCols):
    dataset_oh = dataset
    to_concat = []
    for column in dataset:
        if column in nominalCols:
            df_oh = pd.get_dummies(dataset[column], prefix=column)
            to_concat.append(df_oh)
            dataset_oh = dataset_oh.drop(column, axis=1)
            for column_oh in df_oh:
                binary_cols.append(column_oh)

    to_concat = pd.concat(to_concat, axis=1)
    dataset_oh = pd.concat([to_concat, dataset_oh], axis=1)

    return dataset_oh

# Adds columns to the testing set which are missing based on its training set, removes errors relating to seperate OHE
def clean_testing_set(train_set, test_set):
    new_test_set = test_set
    for column in list(train_set.columns.values):
        if column not in list(test_set.columns.values):
            idx = train_set.columns.get_loc(column)
            new_test_set.insert(idx, column, 0)
    return new_test_set

# This is really good but im not sure if it's doing what I think it is...
# TODO: Investigate this
#     : Investigate different k-nn implementations in scikit
#     : Cry
def knn(train_set, test_set, k):
    knn = KNeighborsClassifier(n_neighbors=k, algorithm='kd_tree')

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

    # Init some variables
    correct = 0
    incorrectAttack = 0
    FP = 0
    FN = 0
    count = 0

    # Compare the prediction against the test set.
    for index in x_test.index.values:
        expected = test_set.loc[index].ix['labels']
        actual = pred[count]
        if expected == actual:
            correct += 1
        else:
            if expected == "normal":
                FP += 1
            elif expected != "normal" and actual != "normal":
                incorrectAttack += 1
            else:
                FN += 1
        count += 1

    print("Correct : " + str(correct))
    print("Correct Class - Wrong Attack : " + str(FN))
    print("FP : " + str(FP))
    print("FN : " + str(FN))

    return([k, correct, incorrectAttack, FP, FN])

def knn2(train_set, test_set):
    # Large set of data used to train the classifier.
    x_train = train_set.ix[:, 0:len(train_set.columns)-1] # All columns except Labels
    y_train = train_set['labels'] # Indices and labels

    # Smaller set of data used to test the trained classifier
    x_test = test_set.ix[:, 0:len(test_set.columns)-1] # All columns except Labels
    y_test = test_set['labels'] # Indices and labels


    knn = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(x_train)
    distances, indices = knn.kneighbors(x_test)
    print(distances)
    print(indices)

# Main method
if __name__ == '__main__':
    # Load column names and attack types
    load_cols(NSL_KDD_FIELDS_PATH)
    load_attacks(NSL_KDD_ATTACKS_PATH)
    # Load training set
    dataset_train = load_dataset(NSL_KDD_TRAINING_PATH, dataset_cols)
    dataset_train_oh = one_hot_encoding(dataset_train, nominal_cols)
    # Load testing set
    dataset_test = load_dataset(NSL_KDD_TESTING_PATH, dataset_cols)
    dataset_test_oh = one_hot_encoding(dataset_test, nominal_cols)

    dataset_test_oh = clean_testing_set(dataset_train_oh, dataset_test_oh)

    #print("***************TRAINING COLUMNS*****************")
    #print(dataset_train_oh)
    #print("***************TESTING COLUMNS*****************")
    #print(dataset_test_oh)

    #print("***************TRAINING COLUMNS*****************")
    #for column in list(dataset_train_oh.columns):
    #    print(column)
    #print("***************TESTING COLUMNS*****************")
    #for column in list(dataset_test_oh.columns):
    #    print(column)

    results = []

    for k in range(1, 110, 10):
        print("CALCULATING " + str(k))
        results.append(knn(dataset_train_oh, dataset_test_oh, k))

    print(results)

    #print(list(dataset_oh.iloc[0]))
