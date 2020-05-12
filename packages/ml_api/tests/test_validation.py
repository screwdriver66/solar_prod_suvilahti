import json
from api import config
from api.data_management import load_dataset

def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    # Load the test data from the regression_model package.
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(filename=config.TESTING_DATA_FILE)
    post_json = test_data.to_json(orient='records')

    #when
    response = flask_test_client.post('/v1/predict/regression',
                                        json=json.loads(post_json))

    #then
    assert response.status_code == 200
    response_json = json.loads(response.data)
