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
IMPUTER_DF_FILE = "reference_df.csv"

#variables
FEATURES = [
            'Pressure (msl) (hPa)',
            'Relative humidity (%)',
            'Air temperature (degC)',
            'Dew-point temperature (degC)',
            'Gust speed (m/s)',
            'Wind speed (m/s)',
            'Global radiation (W/m2)'
            'Wind_direction'
            'Cloud_amount_binary',
            'Precipitation_binary',
            'hour_of_day',
            'day_of_year',
            'solar_elev_angle',
            'sun_azimuth'
]

NUMERICAL_VARS_WITH_NA = [
    'Air temperature (degC)',
    'Dew-point temperature (degC)'
]

WIND_DISCRETIZER_VAR = [
    'Wind direction (deg)'
]

NUM_TO_BINARY = [
    'Cloud amount (1/8)',
    'Precipitation intensity (mm/h)'
]

BINARY_BOUNDARIES = {
    'Cloud amount (1/8)': 5,
    'Precipitation intensity (mm/h)': 0
}

TEMPORAL_HOUR = [
    'hour_of_day'
]

TEMPORAL_DAY = [
    'day_of_year'
]

SOLAR_ANGLE_VAR = [
    'solar_elev_angle'
]

SUN_AZIMUTH_VAR = [
    'sun_azimuth'
]
#variables that can be later dropped after used in calculation:
# DROP_FEATURES =

# think of more stuff here

PIPELINE_NAME  = "rf_pipeline"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

#for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
