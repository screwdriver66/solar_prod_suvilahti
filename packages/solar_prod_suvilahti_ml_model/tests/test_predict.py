import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset
from regression_model.config import config

def test_make_single_prediction(sample_input_data):
    single_test_json = sample_input_data[0:1]

    subject = make_prediction(input_data=single_test_json)

    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float)

def test_make_multiple_predictions(sample_input_data):
    original_data_length = len(sample_input_data)

    subject = make_prediction(input_data=sample_input_data)

    assert subject is not None
    assert len(subject.get('predictions')) == original_data_length

# DO WE EVEN NEED THESE ABOVE? # CHECK FEATURES COLUMNS IN ABOVE


def test_get_single_prediction_with_forecast_data(forecast_input_data):
    single_test_json = forecast_input_data[0:1]
    subject = make_prediction(input_data=single_test_json)

    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float)

def test_get_multiple_predictions_with_forecast_data(forecast_input_data):
    subject = make_prediction(input_data=forecast_input_data)

    assert subject is not None
    assert len(subject.get('predictions')) == len(forecast_input_data)

def test_prediction_quality_against_benchmark(sample_input_data):
    training_input = sample_input_data.drop(config.TARGET, axis=1)
    training_output = sample_input_data[config.TARGET]

    #selecting benchmarking values
    benchmark_flexibility = 151
    # this is the boundary that test data passes the test with all its outliers
    # basically at the moment this boundary is tailored for the test to pass
    # I still believe that the model architecture could be a bit more sophisticated,
    # it would be useful to compare to a situation when we have more space available
    # and train the model with a bit more elaborated forest.

    #Outliers in prediction should be studied separately, have to also check the slices
    # of similar data and model performance on those. Clearly, several values get mispridicted.
    # perhaps if this is not the issue from the business stand point of view, there should be
    # a certain % of allowed values like that.

    benchmark_lower_boundary = round(training_output, ndigits=0) - benchmark_flexibility
    benchmark_upper_boundary = round(training_output, ndigits=0) + benchmark_flexibility

    subject = make_prediction(input_data=training_input)

    assert subject is not None
    prediction = subject.get('predictions')
    assert isinstance(prediction[0], float)
    for i in range(len(prediction)):
        assert prediction[i] > benchmark_lower_boundary[i]
        assert prediction[i] < benchmark_upper_boundary[i]

def test_prediction_quality_against_another_model():
    # this will be added when we have another model. At the moment, 60 MB PyPi upload limit seriously limits
    # us in the mamount of models we can share in the same package. Unless I create a separate PyPi package,
    # which probably is a good idea, there won't be such a test.
    # Another option is to train a separate pipeline and save that model, protect it in .gitignore from uploading
    # and so on. However, I feel it is better to make a separate package.
    # basic principle is to get two predictions and asser current_mse < alternative_mse
    pass
