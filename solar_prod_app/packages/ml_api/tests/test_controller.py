from regression_model.config import config as model_config
from regression_model.processing.data_management import load_dataset
from regression_model import __version__ as _version

import json
import math

from api import __version__ as api_version

def test_health_enpoint_returns_200(flask_test_client):
    #when
    response = flask_test_client.get('/health')

    #then
    assert response.status_code == 200

def test_version_endpoint_returns_version(flask_test_client):
    #when
    response = flask_test_client.get('/version')

    #then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert resposne_json['model_version'] == _version
    assert reponse_json['api_version']  == api_version

def test_prediction_endpoint_returns_prediction(flask_test_client):
    # Given
    # Load the test data from the regression_model package
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
    post_json = test_data[0:1].to_json(orient='records')

    # when
    response = flask_test_client.post('/v1/predict/regression',
                                        json=json.loads(post_json))

    # then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    #add more
    assert response_version == _version
