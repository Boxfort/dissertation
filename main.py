# Jack Anderson 2017
import csv
import pandas as pd


NSL_KDD_TRAINING_PATH   = "Datasets/NSL-KDD/KDDTrain.csv"
NSL_KDD_TRAINING20_PATH = "Datasets/NSL-KDD/KDDTrain_20Percent.csv"
NSL_KDD_TESTING_PATH    = "Datasets/NSL-KDD/KDDTest.csv"
NSL_KDD_ATTACKS_PATH    = "Datasets/NSL-KDD/KDDAttackTypes.csv"
NSL_KDD_FIELDS_PATH     = "Datasets/NSL-KDD/KDDFieldNames.csv"

dataset_cols    = list() # [Field Name]
dataset_attacks = dict() # [Attack Name, Attack Type]

# Loads values from a two column .csv file and stores in a dictionary object.
def load_cols(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset_cols.append(row[0])

def load_attacks(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset_attacks[row[0]] = row[1]

# Loads a dataset and divides into 8 partitions.
def load_dataset(path, fields):
    return pd.read_csv(path, index_col=False, names=dataset_cols)

# Main method
if __name__ == '__main__':
    # Load column names and attack types
    load_cols(NSL_KDD_FIELDS_PATH)
    load_attacks(NSL_KDD_ATTACKS_PATH)
    # Load dataset
    dataset = load_dataset(NSL_KDD_TRAINING20_PATH, dataset_cols)
    print(dataset['labels'].to_string())
