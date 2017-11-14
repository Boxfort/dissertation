# Jack Anderson 2017
import csv
import pyspark
from pyspark.sql import SQLContext, Row

NSL_KDD_TRAINING_PATH   = "Datasets/NSL-KDD/KDDTrain.csv"
NSL_KDD_TRAINING20_PATH = "Datasets/NSL-KDD/KDDTrain_20Percent.csv"
NSL_KDD_TESTING_PATH    = "Datasets/NSL-KDD/KDDTest.csv"
NSL_KDD_ATTACKS_PATH    = "Datasets/NSL-KDD/KDDAttackTypes.csv"
NSL_KDD_FIELDS_PATH     = "Datasets/NSL-KDD/KDDFieldNames.csv"

dataset_cols = [] # [Field Name, Data Type]

sc = pyspark.SparkContext(master='local[8]')
sc.setLogLevel('INFO')
sqlContext = SQLContext(sc)

def load_columns():
    with open(NSL_KDD_FIELDS_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset_cols[row[0]] = row[1]

def load_dataset(path):


# Main method
if __name__ == '__main__':
    return 0
