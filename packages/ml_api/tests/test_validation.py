import json
from api import config
from regression_model.config import config as reg_config
from regression_model.processing.data_management import load_dataset
from regression_model.processing.get_weather_forecast import get_forecast

def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    # Load the test data from the regression_model package.
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(filename=reg_config.TESTING_DATA_FILE)
    post_json = test_data.to_json(orient='records')

    #when
    response = flask_test_client.post('/v1/predict/regression',
                                        json=json.loads(post_json))

    #then
    assert response.status_code == 200
    response_json = json.loads(response.data)

def test_prediction_endpoint_validation_200_forecast_data(flask_test_client):
    # Given
    test_data = get_forecast(place=reg_config.PREDICTION_PLACE)
    post_json = test_data.to_json(orient='records')

    #when
    response = flask_test_client.post('/v1/predict/regression',
                                        json=json.loads(post_json))

    #then
    assert response.status_code == 200
    response_json = json.loads(response.data)
