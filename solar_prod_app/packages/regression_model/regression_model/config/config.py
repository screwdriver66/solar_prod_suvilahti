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
TARGET = "Energy_kWh"
DATETIME_INDEX = "datetime_converted"
#variables
FEATURES = [
            'datetime_converted',
            'CloudAmount',
            'Pressure_msl_hpa',
            'RelativeHumidity_percent',
            'PrecipitationIntensity_mm_h',
            'SnowDepth_cm',
            'AirTemperature_degC',
            'DewPointTemperature_degC',
            'HorizontalVisibility_m',
            'WindDirection',
            'GustSpeed_m_s',
            'WindSpeed_m_s',
            'Energy_kWh',
            'GlobalRadiation_W_m2'
]

WIND_DISCRETE = 'WindDirection'

NUM_TO_BINARY = [
    'CloudAmount',
    'PrecipitationIntensity_mm_h'
]

BINARY_BOUNDARIES = {
    'CloudAmount': 5,
    'PrecipitationIntensity_mm_h': 0
}

TEMPORAL_HOUR = 'Hour'

TEMPORAL_DAY = 'DayofYear'

SOLAR_ANGLE = 'SolarElevationAngle_deg'

SUN_AZIMUTH = 'SunAzimuth_deg'

#variables that can be later dropped after used in calculation:
DROP_FEATURES = [
    'GustSpeed_m_s',
    'SnowDepth_cm',
    'HorizontalVisibility_m',
    'datetime_converted',
]

# think of more stuff here

PIPELINE_NAME  = "rf_pipeline"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

#for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
