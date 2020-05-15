# API reference

Some text here!

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
  |   GET  |         /health        |          Returns health status of the server          |
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
  2. Validates the input and uses it in the ML pipeline from solar_prod_suvilahti_ml_model package - rly??
  3. Predicts the values with make_prediction() method of the regression model package.
  4. Renders the predictions in the bar chart using the HTML page template.

  Example: [insert the link]()

### POST /v1/prediction/regression/

  Returns predictions, version and errors in JSON format.

  > { \
  > 'predictions': predictions, \
  >                'version': version, \
  >                    'errors': errors \
  >}
