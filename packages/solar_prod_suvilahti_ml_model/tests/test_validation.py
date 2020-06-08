from regression_model.processing.validation import validate_inputs

def test_validate_inputs_test_data(sample_input_data):
    validated_inputs = validate_inputs(input_data=sample_input_data)
    assert validated_inputs.isnull().any().any() == False

def test_validate_inputs_forecast_data(forecast_input_data):
    validated_inputs = validate_inputs(input_data=forecast_input_data)
    assert validated_inputs.isnull().any().any() == False
