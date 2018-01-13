# Jack Anderson 2017
from comniaUtils import *
from sklearn.metrics import classification_report

NSL_KDD_TRAINING_PATH   = "Datasets/NSL-KDD/KDDTrain.csv"
NSL_KDD_TRAINING20_PATH = "Datasets/NSL-KDD/KDDTrain_20Percent.csv"
NSL_KDD_TESTING_PATH    = "Datasets/NSL-KDD/KDDTest.csv"
NSL_KDD_ATTACKS_PATH    = "Datasets/NSL-KDD/KDDAttackTypes.csv"
NSL_KDD_FIELDS_PATH     = "Datasets/NSL-KDD/KDDFieldNames.csv"

# Main method
if __name__ == '__main__':

    #import mlp as algorithm
    import knn as algorithm

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

    # Flatten Attacks
    dataset_train_oh = flatten_attacks(dataset_train_oh)
    dataset_test_oh = flatten_attacks(dataset_test_oh)

    print("Running algorithm...")

    #print(dataset_test_oh['labels'] != 'normal')
    #predictions = algorithm.run(dataset_train_oh, dataset_test_oh)
    predictions = algorithm.run(dataset_train_oh, dataset_test_oh)

    print(classification_report(dataset_test_oh['labels'],predictions))

