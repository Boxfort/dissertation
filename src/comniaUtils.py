# Jack Anderson 2017
import csv
import numpy as np
import pandas as pd
from collections import OrderedDict

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
    with open(path, 'rU') as file:
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

def flatten_attacks(dataset):
    dataset_flat = dataset
    mask = dataset_flat['labels'] != 'normal'
    column_name = 'labels'
    dataset_flat.loc[mask, column_name] = 'attack'
    return dataset_flat

