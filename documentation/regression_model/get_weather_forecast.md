# Get weather forecast [source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/packages/solar_prod_suvilahti_ml_model/regression_model/processing/get_weather_forecast.py)

This function is used to get weather forecast data from the FMI API through __fmi_weather__ python package. It prepares the dataframe with weather forecast values ready to enter the regression model pipeline, using the following steps:

1. Recieves forecast data from FMI API through __fmi_weather__ [source](https://github.com/kipe/fmi) python package __fmi.FMI.forecast()__ method in the form of a list of __observation__ objects (observations are in reality forecasts).
2. Iterates through the list of observation objects to create a pandas.DataFrame object
3. FMI forecast instead of Global Radiation values in W/m2 contains accumulation of global radiation in J/m2 for each of the hour. Thus, the function takes the difference between the consecutive hours and converts Joules to Watts. Due to taking a difference between the values the first hour of the dataframe will be missing. Thus, this application will yield predictions for [1 , 36] hours instead of [0 , 36]. That first row is dropped.
4. Dropping unnecessary columns.
5. Renaming the features according to the API data validation schema.

> get_forecast(place):

Function returns forecast data in a pandas.DataFrame object in the format ready for validation in the model and the API data validation schema.

    Parameters- place: str
                Name of the place (e.g. 'Kumpula' or 'Kaisaniemi')

    Outputs- pandas.DataFrame object
