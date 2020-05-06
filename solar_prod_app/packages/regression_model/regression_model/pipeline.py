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
        ("numerical_imputer", pp.NumericalImputer(variables=config.NUMERICAL_VARS_WITH_NA,reference_df=config.IMPUTER_DF_FILE),),
        ("wind_discretizer", pp.WindDiscretizer(variables=config.WIND_DISCRETIZER_VAR),),
        ("discretizer_into_binary", pp.DiscretizerNumericalIntoBinary(variables=config.NUM_TO_BINARY,boundaries=config.BINARY_BOUNDARIES),),
        ("temporal_estimator_hour", pp.TemporalVariableEstimatorHour(variables=config.TEMPORAL_HOUR),),
        ("temporal_estimator_day", pp.TemporalVariableEstimatorDay(variables=config.TEMPORAL_DAY),),
        ("solar_angle_estimator", pp.SolarAngleEstimator(variables=config.SOLAR_ANGLE_VAR),),
        ("solar_azimuth_estimator", pp.SolarAzimuthEstimator(variables=config.SUN_AZIMUTH_VAR),),
        ("scaler", StandardScaler()),
        ("random_forest", RandomForestRegressor(n_estimators=5000, max_depth=10, random_state=42))
    ]
)
