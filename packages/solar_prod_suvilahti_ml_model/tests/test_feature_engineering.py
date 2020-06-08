import math
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
# unit testing feature engineering logic
from regression_model.processing import data_management as dm
from regression_model.processing import preprocessors as pp
from regression_model.config import config

def test_WindDiscretizer(sample_input_data):
    ct = pp.WindDiscretizer(variables=config.WIND_DISCRETE)
    data_t = ct.transform(sample_input_data)

    assert len(data_t[config.WIND_DISCRETE].unique())==16
    assert data_t[config.WIND_DISCRETE].min()==1
    assert data_t[config.WIND_DISCRETE].max()==16
    assert len(data_t) == len(sample_input_data)
    assert type(data_t) == pd.core.frame.DataFrame
    assert data_t[config.WIND_DISCRETE] is not None

#   2.1 for var 1
#   2.2 for var 2
def test_DiscretizerNumericalIntoBinary(sample_input_data):
    ct = pp.DiscretizerNumericalIntoBinary(boundaries=config.BINARY_BOUNDARIES, variables=config.NUM_TO_BINARY)
    data_t = ct.transform(sample_input_data)

    for var in config.NUM_TO_BINARY:
        assert len(data_t[var].unique()) == 2
        assert data_t[var].min() == 0
        assert data_t[var].max() == 1
        assert type(data_t) == pd.core.frame.DataFrame

def test_TemporalHour(sample_input_data):
    ct = pp.TemporalHour(variable=config.TEMPORAL_HOUR, ref_feature=config.DATETIME_INDEX)
    data_t = ct.transform(sample_input_data)
    var = config.TEMPORAL_HOUR

    assert len(data_t[var].unique()) == 24
    assert data_t[var].min() == 0
    assert data_t[var].max() == 23
    assert type(data_t) == pd.core.frame.DataFrame

def test_TemporalDayofYear(sample_input_data):
    ct = pp.TemporalDayofYear(variable=config.TEMPORAL_DAY, ref_feature=config.DATETIME_INDEX)
    data_t = ct.transform(sample_input_data)
    var = config.TEMPORAL_DAY

    assert len(data_t[var].unique()) == 366
    assert data_t[var].min() == 1
    assert data_t[var].max() == 366
    assert type(data_t) == pd.core.frame.DataFrame

def test_SolarElevAngle(sample_input_data):
    ct0 = pp.TemporalHour(variable=config.TEMPORAL_HOUR, ref_feature=config.DATETIME_INDEX)
    ct1 = pp.TemporalDayofYear(variable=config.TEMPORAL_DAY, ref_feature=config.DATETIME_INDEX)
    ct2 = pp.SolarElevAngle(var_name=config.SOLAR_ANGLE, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    data_t = ct0.transform(sample_input_data)
    data_t = ct1.transform(data_t)
    data_t = ct2.transform(data_t)
    var = config.SOLAR_ANGLE

    assert data_t[var] is not None
    #in summer it doesn't go over 53 degrees
    #in winter doesn't drop below -53 degrees
    assert (data_t[var].max()  > 50) & (data_t[var].max()  < 55)
    assert (data_t[var].min()  < -50) & (data_t[var].min()  > -55)
    assert type(data_t) == pd.core.frame.DataFrame

def test_SunAzimuth(sample_input_data):
    ct0 = pp.TemporalHour(variable=config.TEMPORAL_HOUR, ref_feature=config.DATETIME_INDEX)
    ct1 = pp.TemporalDayofYear(variable=config.TEMPORAL_DAY, ref_feature=config.DATETIME_INDEX)
    ct2 = pp.SolarElevAngle(var_name=config.SOLAR_ANGLE, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    ct3 = pp.SunAzimuth(var_name=config.SUN_AZIMUTH, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    data_t = ct0.transform(sample_input_data)
    data_t = ct1.transform(data_t)
    data_t = ct2.transform(data_t)
    data_t = ct3.transform(data_t)
    var = config.SUN_AZIMUTH

    assert data_t[var] is not None
    assert data_t[var].max()  <= 180
    assert data_t[var].min() >= -180
    assert type(data_t) == pd.core.frame.DataFrame

def test_TheoreticalIrradiance(sample_input_data):
    ct0 = pp.TemporalHour(variable=config.TEMPORAL_HOUR, ref_feature=config.DATETIME_INDEX)
    ct1 = pp.TemporalDayofYear(variable=config.TEMPORAL_DAY, ref_feature=config.DATETIME_INDEX)
    ct2 = pp.SolarElevAngle(var_name=config.SOLAR_ANGLE, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    ct3 = pp.SunAzimuth(var_name=config.SUN_AZIMUTH, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    ct4 = pp.TheoreticalRadiation(var_name=config.THEOR_SRAD, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    data_t = ct0.transform(sample_input_data)
    data_t = ct1.transform(data_t)
    data_t = ct2.transform(data_t)
    data_t = ct3.transform(data_t)
    data_t = ct4.transform(data_t)
    var = config.THEOR_SRAD

    assert data_t[var] is not None
    assert len(sample_input_data) == len(data_t[var])
    assert type(data_t) == pd.core.frame.DataFrame

def test_DropFeatures(sample_input_data):
    ct0 = pp.TemporalHour(variable=config.TEMPORAL_HOUR, ref_feature=config.DATETIME_INDEX)
    ct1 = pp.TemporalDayofYear(variable=config.TEMPORAL_DAY, ref_feature=config.DATETIME_INDEX)
    ct2 = pp.SolarElevAngle(var_name=config.SOLAR_ANGLE, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    ct3 = pp.SunAzimuth(var_name=config.SUN_AZIMUTH, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    ct4 = pp.TheoreticalRadiation(var_name=config.THEOR_SRAD, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)
    ct5 = pp.DropUnnecessaryFeatures(variables_to_drop=config.DROP_FEATURES)
    data_t = ct0.transform(sample_input_data)
    data_t = ct1.transform(data_t)
    data_t = ct2.transform(data_t)
    data_t = ct3.transform(data_t)
    data_t = ct4.transform(data_t)
    data_t = ct5.transform(data_t)
    assert config.DROP_FEATURES not in data_t.columns.to_list()
    assert type(data_t) == pd.core.frame.DataFrame
