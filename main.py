# Jack Anderson 2017
import csv
import numpy as np
import pandas as pd
from collections import OrderedDict
from sklearn.neighbors import KNeighborsClassifier
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

# This is really good but im not sure if it's doing what I think it is... #TODO: Investigate this
def knn(dataset, input):
    print("Fitting Data.")
    knn = KNeighborsClassifier(n_neighbors=1)
    X = dataset.ix[:, 0:len(dataset.columns)-1] # All columns except Labels
    Y = dataset['labels'] # Labels column

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

    knn.fit(X_train, y_train)

    print(y_train)

    print("Predicting Row")
    pred = knn.predict(X_test)

    correct = 0
    incorrect = 0

    print(X_test.index.values)
    print(pred)

    count = 0

    for index in X_test.index.values:
        if dataset.loc[index].ix['labels'] == pred[count]:
            correct += 1
        else:
            incorrect += 1
        count += 1

    print("Correct : " + str(correct))
    print("Incorrect : " + str(incorrect))

# Main method
if __name__ == '__main__':
    # Load column names and attack types
    load_cols(NSL_KDD_FIELDS_PATH)
    load_attacks(NSL_KDD_ATTACKS_PATH)
    # Load dataset
    dataset = load_dataset(NSL_KDD_TRAINING20_PATH, dataset_cols)
    dataset_oh = one_hot_encoding(dataset, nominal_cols)

    knn(dataset_oh, 0)

    #print(list(dataset_oh.iloc[0]))
