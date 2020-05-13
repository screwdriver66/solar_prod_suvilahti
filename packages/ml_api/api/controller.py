from flask import Blueprint, request, jsonify, render_template
from regression_model.predict import make_prediction
from regression_model import __version__ as _version
from regression_model.processing.get_weather_forecast import get_forecast
from regression_model.config import config as reg_config


from api.config import get_logger
from api.validation import validate_inputs
from api import __version__ as api_version

import numpy as np
import pandas as pd

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'

@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})

@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data)

        # Step 3: Model prediction
        result = make_prediction(input_data=input_data)

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})


@prediction_app.route('/bar_chart')
def bar_chart():
    # html = "<h1> Solar Power Production ML App for Suvilahti PV Plant operated by Helen.</h1>"
    legend = 'Energy production [kWh]'
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    forecast = get_forecast(place=reg_config.PREDICTION_PLACE)
    result = make_prediction(input_data=forecast)
    predictions = result.get('predictions').tolist()
    values = np.around(predictions,2)
    # TIME IS IN UTC
    labels = pd.DatetimeIndex(pd.to_datetime(forecast[reg_config.DATETIME_INDEX])).time

    return render_template('bar_chart.html', values=values, labels=labels, legend=legend)
