from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import MinMaxScaler #select  one of the two

from regression_model.processing import preprocessors as pp
from regression_model.config import config
# from regression_model.processing import features

import logging

_logger = logging.getLogger(__name__)

energy_pipe = Pipeline(
    [
        ('wind_disc', pp.WindDiscretizer(variables=config.WIND_DISCRETE)),
        ('num_to_binary', pp.DiscretizerNumericalIntoBinary(boundaries=config.BINARY_BOUNDARIES, variables=config.NUM_TO_BINARY)),
        # ('cloud_binary', pp.DiscretizerNumericalIntoBinary(boundaries=5, variables=['Cloud amount (1/8)'])),
        ('temporal_hour', pp.TemporalHour(variables=config.TEMPORAL_HOUR)),
        ('temporal_dayofyear', pp.TemporalDayofYear(variables=config.TEMPORAL_DAY)),
        ('solar_angle', pp.SolarElevAngle(var_name=config.SOLAR_ANGLE, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)),
        ('sun_azimuth', pp.SunAzimuth(var_name=config.SUN_AZIMUTH, day=config.TEMPORAL_DAY, hour=config.TEMPORAL_HOUR)),
        ('drop_features', pp.DropUnnecessaryFeatures(variables_to_drop=config.DROP_FEATURES)),
        ("scaler", StandardScaler()),
        ("random_forest", RandomForestRegressor(n_estimators=2, max_depth=2, random_state=42))
    ]
)
