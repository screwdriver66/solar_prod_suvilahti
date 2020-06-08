import pytest
from sklearn.model_selection import train_test_split

from regression_model.config import config
from regression_model.processing.data_management import load_dataset
from regression_model.processing.get_weather_forecast import get_forecast

@pytest.fixture(scope="session")
def pipeline_inputs():
    data = load_dataset(filename=config.TRAINING_DATA_FILE)

    #train test split
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=config.TEST_SIZE,
        random_state=config.RANDOM_STATE,
    )
    return X_train, X_test, y_train, y_test

# WHERE can i better utilize the above?

# @pytest.fixture()
# def raw_training_data():
#     return load_dataset(filename=config.TRAINING_DATA_FILE)

@pytest.fixture()
def sample_input_data():
    return load_dataset(filename=config.TESTING_DATA_FILE)

@pytest.fixture()
def forecast_input_data():
    return get_forecast(config.PREDICTION_PLACE)
