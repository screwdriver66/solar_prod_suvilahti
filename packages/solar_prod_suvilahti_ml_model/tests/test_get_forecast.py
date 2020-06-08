import math

from regression_model.config import config
from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset
from regression_model.processing.get_weather_forecast import get_forecast
import pandas as pd
import numpy as np

def test_get_forecast(forecast_input_data):
    assert type(forecast_input_data) == pd.core.frame.DataFrame
    assert forecast_input_data.columns.to_list() == config.FEATURES
    assert forecast_input_data[config.DATETIME_INDEX].dtype != np.number
