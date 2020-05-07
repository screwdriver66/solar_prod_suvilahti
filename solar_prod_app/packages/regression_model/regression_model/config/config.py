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
DATETIME_INDEX = "datetime_converted"
#variables
FEATURES = [
            'datetime_converted',
            'Cloud amount (1/8)',
            'Pressure (msl) (hPa)',
            'Relative humidity (%)',
            'Precipitation intensity (mm/h)',
            'Snow depth (cm)',
            'Air temperature (degC)',
            'Dew-point temperature (degC)',
            'Horizontal visibility (m)',
            'Wind direction (deg)',
            'Gust speed (m/s)',
            'Wind speed (m/s)',
            'Global radiation (W/m2)'
]

WIND_DISCRETE = ['Wind direction (deg)']

NUM_TO_BINARY = [
    'Cloud amount (1/8)',
    'Precipitation intensity (mm/h)'
]

BINARY_BOUNDARIES = {
    'Cloud amount (1/8)': 5,
    'Precipitation intensity (mm/h)': 0
}

TEMPORAL_HOUR = 'hour'

TEMPORAL_DAY = 'dayofyear'

SOLAR_ANGLE = 'solar_elev_angle'

SUN_AZIMUTH = 'sun_azimuth'

#variables that can be later dropped after used in calculation:
DROP_FEATURES = [
    'Gust speed (m/s)',
    'Snow depth (cm)',
    'Horizontal visibility (m)',
    'datetime_converted',
]

# think of more stuff here

PIPELINE_NAME  = "rf_pipeline"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

#for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
