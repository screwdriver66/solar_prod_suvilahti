import pathlib

import regression_model

import pandas as pd

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10

PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

#data
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "Value (kWh)"

#variables
FEATURES = [

]

#variables that can be later dropped after used in calculation:
DROP_FEATURES = [

]

# think of more stuff here

PIPELINE_NAME  = "pipeline_name"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

#for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
