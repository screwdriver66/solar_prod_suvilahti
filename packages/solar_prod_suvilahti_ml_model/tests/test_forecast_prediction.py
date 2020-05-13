import math

from regression_model.config import config
from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset
from regression_model.processing.get_weather_forecast import get_forecast
import pandas as pd
import numpy as np

def test_get_forecast():
    df = get_forecast(config.PREDICTION_PLACE)

    assert type(df) == pd.core.frame.DataFrame

def test_get_single_prediction_with_forecast_data():
    #given
    data = get_forecast(config.PREDICTION_PLACE)
    single_test_json = data[0:1]

    #when
    subject = make_prediction(input_data=single_test_json)

    #then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float)

def test_get_multiple_predictions_with_forecast_data():
    data = get_forecast(config.PREDICTION_PLACE)
    original_data_length = len(data)
    multiple_test_json = data


    subject = make_prediction(input_data=multiple_test_json)

    assert subject is not None
    assert len(subject.get('predictions')) == original_data_length
