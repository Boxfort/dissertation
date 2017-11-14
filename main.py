# Jack Anderson 2017
import csv
import pyspark
from pyspark.sql import SQLContext, Row

NSL_KDD_TRAINING_PATH   = "Datasets/NSL-KDD/KDDTrain.csv"
NSL_KDD_TRAINING20_PATH = "Datasets/NSL-KDD/KDDTrain_20Percent.csv"
NSL_KDD_TESTING_PATH    = "Datasets/NSL-KDD/KDDTest.csv"
NSL_KDD_ATTACKS_PATH    = "Datasets/NSL-KDD/KDDAttackTypes.csv"
NSL_KDD_FIELDS_PATH     = "Datasets/NSL-KDD/KDDFieldNames.csv"

dataset_cols    = [] # [Field Name, Data Type]
symbolic_cols   = [] # Columns which consist of a string
continuous_cols = [] # Columns which consist of some numeric value
boolean_cols    = [] # Columns which consist of a boolean value i.e 0 or 1
dataset_attacks = [] # [Attack Name, Attack Type]

sc = pyspark.SparkContext(master='local[8]')
sc.setLogLevel('INFO')
sqlContext = SQLContext(sc)

# Loads values from a two column .csv file and stores in a dictionary object.
def csv_to_dict(path, dictionary):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dictionary[row[0]] = row[1]

def load_dataset():


# Main method
if __name__ == '__main__':
    #Load column names and attack types
    csv_to_dict(NSL_KDD_FIELDS_PATH, dataset_cols)
    csv_to_dict(NSL_KDD_ATTACKS_PATH, dataset_cols)

    return 0
