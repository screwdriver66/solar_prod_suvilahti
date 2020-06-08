from regression_model import pipeline
from regression_model.config import config
from regression_model.processing.validation import validate_inputs

#Since we do not keep a training data file in the github, we will test
# validation of inputs in the pipeline by training the pipeline on the test set
 

def test_pipeline_predict_takes_validated_input(pipeline_inputs, sample_input_data):
    X_train, X_test, y_train, y_test = pipeline_inputs
    pipeline.energy_pipe.fit(X_train, y_train)

    validated_inputs = validate_inputs(input_data=sample_input_data)
    predictions = pipeline.energy_pipe.predict(validated_inputs[config.FEATURES])

    assert predictions is not None

def test_pipeline_predict_takes_validated_input_from_forecast(pipeline_inputs, forecast_input_data):
    X_train, X_test, y_train, y_test = pipeline_inputs
    pipeline.energy_pipe.fit(X_train, y_train)

    validated_inputs = validate_inputs(input_data=forecast_input_data)
    predictions = pipeline.energy_pipe.predict(validated_inputs[config.FEATURES])

    assert predictions is not None
