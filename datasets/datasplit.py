import sys
import os
import math
import csv
import numpy as np
import pandas as pd

DATASET = "NSL-KDD/KDDTrain.csv"
FIELDS = "NSL-KDD/KDDFieldNames.csv"

if __name__ == '__main__':
    #Open Dataset
    #Split into attacks / normal
    #Create 10 datasets where normal increases by 10% each time with all attacks in each
    dataset_cols = []
    with open("NSL-KDD/KDDFieldNames.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset_cols.append(row[0])
    dataset_total = pd.read_csv("NSL-KDD/KDDTest.csv", index_col=False, names=dataset_cols)
    allnormal = dataset_total[dataset_total['labels'] == 'normal']
    allattacks = dataset_total[dataset_total['labels'] != 'normal']

    folds = 10
    fold_size = len(allnormal.index) / folds

    for i in range(0, folds):
        filename = "newset/dataset_"+str(i+1)+"0pcnt_normal.csv"
        start = 0
        end = math.floor((i + 1) * fold_size)
        print(allnormal.index[start:end])
        new_dataset = allattacks.copy().append(allnormal.ix[allnormal.index[start:end]])
        new_dataset.to_csv(filename, encoding='utf-8', index=False, header=None)



