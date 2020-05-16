# API reference

Get the prediction values from the regression model either in a POST request or use the GET method to view predictions
in a rendered HTML page visualized in the bar chart.

<!-- 2. Endpoints and methods

  The endpoints indicate how you access the resource, while the method indicates the allowed interactions (such as GET, POST, or DELETE) with the resource.

3. Parameters

  Parameters are options you can pass with the endpoint (such as specifying the response format or the amount returned) to influence the response.

4. Request example

  The request example includes a sample request using the endpoint, showing some parameters configured.

5. Response example and schema

  The response example shows a sample response from the request example; the response schema defines all possible elements in the response. -->

### API endpoints

  | Method |        Endpoint        |                      Description                      |
  |:------:|:----------------------:|:-----------------------------------------------------:|
  |   GET  |        /version        |        Returns regression model and API version       |
  |   GET  |       /bar_chart       | Returns an HTML page the latest predictions  |
  |  POST  | /v1/predict/regression |        Returns predictions, version and errors        |

### GET /version
  Returns the regression model and the API versions in the following JSON format.

  > { \
  > 'model_version': _version, \
  >  'api_version': api_version \
  > }

### GET /bar_chart

  Returns the HTML rendered template with the latest predictions of produced energy in kWh for the next 36 hours.

  1. Fetches the forecast data from the FMI API through [fmi_weather](https://github.com/kipe/fmi) python package.
  2. Validates the input and uses it in the ML pipeline from solar_prod_suvilahti_ml_model package
  3. Predicts the values with make_prediction() method of the regression model package.
  4. Renders the predictions in the bar chart using the HTML page template.

  Example: [insert the link]()

### POST /v1/prediction/regression/

  Returns predictions, version and errors in JSON format.

  > { \
  > 'predictions': python list of floats, \
  >                'version': version, \
  >                    'errors': errors \
  >}

Example request:

> import requests \
> import json \
> response = requests.post('http://127.0.0.1:5000/v1/predict/regression',json=json.loads(data))

Example response:
> { \
> 'predictions': [196.40, 211.97, 6.17, ..., 133.08], \
>                'version': 0.1.1, \
>                    'errors': None \
>}

### Schema

|           Variable          |  Type |
|:---------------------------:|:-----:|
|      datetime_converted     |  str  |
|         CloudAmount         |  int  |
|       Pressure_msl_hpa      | float |
|   RelativeHumidity_percent  | float |
| PrecipitationIntensity_mm_h | float |
|     AirTemperature_degC     | float |
|   DewPointTemperature_degC  | float |
|        WindDirection        |  int  |
|        GustSpeed_m_s        | float |
|        WindSpeed_m_s        | float |
|          Energy_kWh         | float |
|     GlobalRadiation_W_m2    | float (allow_none=True) |
